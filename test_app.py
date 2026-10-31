"""
Plant Disease Detection - Comprehensive Test Suite
---------------------------------------------------
Verifies all backend validation, image processing, model inference,
and HTTP response contracts.
"""

import unittest
import io
import json
from app import app
from classifier import classifier_instance


class PlantDiseaseAppTests(unittest.TestCase):

    def setUp(self):
        # Configure Flask test client
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_01_home_page_renders_successfully(self):
        """Verify the home page loads with 200 OK and expected HTML tags."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("Plant Disease Detection", html)
        self.assertIn("AI-Powered Leaf Diagnostic Tool", html)
        self.assertIn("AI Model: Active", html)

    def test_02_api_status_endpoint(self):
        """Verify the /api/status endpoint returns model metadata."""
        response = self.client.get("/api/status")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "online")
        self.assertTrue(data["model_available"])
        self.assertEqual(data["classes_count"], 38)
        self.assertIn("Apple", data["supported_plants"])

    def test_03_api_samples_endpoint(self):
        """Verify bundled sample leaf images are returned."""
        response = self.client.get("/api/samples")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("samples", data)
        self.assertGreaterEqual(len(data["samples"]), 3)

    def test_04_predict_missing_file_payload(self):
        """Verify 400 Bad Request when no file is provided."""
        response = self.client.post("/api/predict", data={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data["success"])
        self.assertIn("No image file provided", data["error"])

    def test_05_predict_empty_filename(self):
        """Verify 400 Bad Request when filename is empty."""
        data = {"image": (io.BytesIO(b""), "")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertFalse(json_data["success"])
        self.assertIn("No file selected", json_data["error"])

    def test_06_predict_unsupported_file_extension(self):
        """Verify 415 Unsupported Media Type for non-image files (.txt)."""
        data = {"image": (io.BytesIO(b"Hello world text"), "malicious.txt")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 415)
        json_data = response.get_json()
        self.assertFalse(json_data["success"])
        self.assertIn("Unsupported file format", json_data["error"])

    def test_07_predict_corrupted_image_content(self):
        """Verify Pillow rejects corrupted/fake images with a valid extension."""
        fake_jpeg = b"This is not a real JPEG image stream at all!"
        data = {"image": (io.BytesIO(fake_jpeg), "fake.jpg")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertFalse(json_data["success"])
        self.assertIn("Invalid or corrupted image", json_data["error"])

    def test_08_predict_oversized_file(self):
        """Verify 413 Payload Too Large when file exceeds 5MB."""
        oversized_data = b"X" * (5 * 1024 * 1024 + 1024)
        data = {"image": (io.BytesIO(oversized_data), "huge_image.jpg")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 413)
        json_data = response.get_json()
        self.assertFalse(json_data["success"])
        self.assertIn("exceeds the maximum allowed size of 5 MB", json_data["error"])

    def test_09_predict_real_apple_scab_image(self):
        """Verify real AI classification on sample Apple Scab image."""
        with open("static/samples/apple_scab.jpg", "rb") as f:
            image_bytes = f.read()

        data = {"image": (io.BytesIO(image_bytes), "apple_scab.jpg")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 200)
        res = response.get_json()

        self.assertTrue(res["success"])
        self.assertTrue(res["model_available"])
        self.assertEqual(res["prediction"]["disease_name"], "Apple Scab")
        self.assertGreater(res["prediction"]["confidence"], 0.90)
        self.assertFalse(res["prediction"]["is_healthy"])
        self.assertEqual(res["prediction"]["plant_type"], "Apple")
        self.assertIn("recommendations", res)
        self.assertIn("immediate_actions", res["recommendations"])
        self.assertIn("prevention", res["recommendations"])

    def test_10_predict_real_healthy_apple_image(self):
        """Verify real AI classification on sample Healthy Apple image."""
        with open("static/samples/apple_healthy.jpg", "rb") as f:
            image_bytes = f.read()

        data = {"image": (io.BytesIO(image_bytes), "apple_healthy.jpg")}
        response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 200)
        res = response.get_json()

        self.assertTrue(res["success"])
        self.assertTrue(res["model_available"])
        self.assertEqual(res["prediction"]["disease_name"], "Healthy Apple")
        self.assertTrue(res["prediction"]["is_healthy"])

    def test_11_model_unavailable_fallback_behavior(self):
        """
        Verify that if the model is absent or unconfigured, the system
        does NOT fabricate results, but instead returns model_available=False
        with Pillow-verified image metadata and setup instructions.
        """
        # Temporarily detach session
        saved_session = classifier_instance.session
        classifier_instance.session = None

        try:
            with open("static/samples/apple_scab.jpg", "rb") as f:
                image_bytes = f.read()

            data = {"image": (io.BytesIO(image_bytes), "test_leaf.jpg")}
            response = self.client.post("/api/predict", data=data, content_type="multipart/form-data")
            self.assertEqual(response.status_code, 200)
            res = response.get_json()

            self.assertTrue(res["success"])
            self.assertFalse(res["model_available"])
            self.assertIsNone(res["prediction"])
            self.assertIn("AI prediction is currently unavailable", res["message"])
            self.assertIn("image_meta", res)
            self.assertEqual(res["image_meta"]["format"], "JPEG")
        finally:
            # Restore session
            classifier_instance.session = saved_session


if __name__ == "__main__":
    unittest.main()
