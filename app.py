"""
Plant Disease Detection - Flask Application Backend
----------------------------------------------------
This is the main entry point for the Plant Disease Detection web application.
It provides:
1. Static and template routing for the web interface.
2. File upload reception and backend validation (file size, format, image integrity).
3. AI classification through the PlantClassifier (using Pillow & ONNX Runtime).
4. Agricultural care recommendation dispatch.
5. Robust, user-friendly error handlers.

Author: Technical Interview Project Candidate
"""

import os
from typing import Dict, Any, Tuple
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from classifier import classifier_instance
from recommendations import RECOMMENDATIONS_DATABASE

# Initialize the Flask application
app = Flask(__name__)

# ==========================================
# CONFIGURATION & CONSTANTS
# ==========================================
# Maximum allowed upload size: 5 Megabytes
# Flask automatically rejects requests exceeding this threshold with a 413 status code.
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Allowed image file extensions
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

# Ensure secure secret key for session handling if needed
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "plant-disease-detection-interview-secret-key")


def is_allowed_file(filename: str) -> bool:
    """
    Validates whether the uploaded file has a safe and permitted image extension.
    Example: 'leaf.jpg' -> True, 'script.sh' -> False
    """
    if not filename or "." not in filename:
        return False
    extension = filename.rsplit(".", 1)[1].lower()
    return extension in ALLOWED_EXTENSIONS


# ==========================================
# APPLICATION ROUTES
# ==========================================

@app.route("/")
def index():
    """
    Renders the responsive home page for the application.
    Passes the current model availability status to the template.
    """
    model_ready, status_message = classifier_instance.is_available()
    return render_template(
        "index.html",
        model_ready=model_ready,
        status_message=status_message,
        classes_count=len(classifier_instance.id2label)
    )


@app.route("/api/status", methods=["GET"])
def api_status():
    """
    Returns application health and model configuration status as JSON.
    Used by the frontend to dynamically display system readiness.
    """
    model_ready, status_message = classifier_instance.is_available()

    # Group classes by plant type for display
    plants_summary = {}
    for class_id, label in classifier_instance.id2label.items():
        # Look up plant type from recommendations database
        rec = RECOMMENDATIONS_DATABASE.get(label, {})
        plant_type = rec.get("plant", "Other")
        plants_summary.setdefault(plant_type, []).append(label)

    return jsonify({
        "status": "online",
        "app_name": "Plant Disease Detection",
        "model_available": model_ready,
        "model_name": "MobileNetV2 (PlantVillage Fine-Tuned ONNX)",
        "message": status_message,
        "classes_count": len(classifier_instance.id2label),
        "supported_plants": plants_summary
    })


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Receives an uploaded leaf image via HTTP POST multipart/form-data.

    Processing Steps:
    1. Checks if a file was submitted under the 'image' field.
    2. Validates that the filename is present and not empty.
    3. Validates that the file extension is an allowed image type (.jpg, .jpeg, .png, .webp).
    4. Reads raw bytes into memory (avoids unnecessary disk I/O and leaks).
    5. Validates file size (< 5MB).
    6. Verifies image integrity and dimensions using Pillow inside PlantClassifier.
    7. Runs real ONNX model inference (if configured) or gracefully returns preview data.
    8. Returns a clean JSON payload with prediction and care recommendations.
    """
    # Step 1: Check if the file part is present in the request
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image file provided in the upload request. Please select a leaf photo."
        }), 400

    file = request.files["image"]

    # Step 2: Validate non-empty filename
    if not file or file.filename.strip() == "":
        return jsonify({
            "success": False,
            "error": "No file selected. Please choose a valid image to analyze."
        }), 400

    filename = secure_filename(file.filename)

    # Step 3: Validate file extension
    if not is_allowed_file(filename):
        return jsonify({
            "success": False,
            "error": (
                f"Unsupported file format '{filename.rsplit('.', 1)[-1] if '.' in filename else 'unknown'}'. "
                f"Please upload an image in JPG, JPEG, PNG, or WEBP format."
            )
        }), 415

    # Step 4 & 5: Read bytes and validate file size (< 5MB)
    image_bytes = file.read()
    if len(image_bytes) == 0:
        return jsonify({
            "success": False,
            "error": "The uploaded file is empty (0 bytes). Please upload a valid image."
        }), 400

    if len(image_bytes) > app.config["MAX_CONTENT_LENGTH"]:
        return jsonify({
            "success": False,
            "error": "File size exceeds the 5 MB limit. Please compress or resize the image before uploading."
        }), 413

    # Step 6 & 7: Hand off to classifier for Pillow validation and ONNX inference
    result = classifier_instance.predict(image_bytes)

    # If Pillow rejected the file as invalid or corrupted
    if not result.get("success"):
        return jsonify({
            "success": False,
            "error": result.get("error", "The uploaded file could not be parsed as a valid image.")
        }), 400

    # Add sanitized filename to response metadata
    result["filename"] = filename

    return jsonify(result), 200


@app.route("/api/samples", methods=["GET"])
def api_samples():
    """
    Returns a list of bundled sample leaf images for quick interview testing.
    """
    samples = [
        {
            "id": "apple_scab",
            "name": "Apple Scab Leaf",
            "expected": "Apple Scab (Disease)",
            "url": "/static/samples/apple_scab.jpg"
        },
        {
            "id": "apple_healthy",
            "name": "Healthy Apple Leaf",
            "expected": "Healthy Apple (Optimal Health)",
            "url": "/static/samples/apple_healthy.jpg"
        },
        {
            "id": "tomato_early_blight",
            "name": "Tomato Early Blight Leaf",
            "expected": "Tomato with Early Blight (Disease)",
            "url": "/static/samples/tomato_early_blight.jpg"
        }
    ]
    return jsonify({"samples": samples})


# ==========================================
# ERROR HANDLERS (Friendly error responses)
# ==========================================

@app.errorhandler(413)
def handle_file_too_large(e):
    """Handles requests where the payload exceeds MAX_CONTENT_LENGTH (5MB)."""
    return jsonify({
        "success": False,
        "error": "The uploaded file exceeds the maximum allowed size of 5 MB. Please select a smaller photo."
    }), 413


@app.errorhandler(415)
def handle_unsupported_media(e):
    """Handles unsupported media types."""
    return jsonify({
        "success": False,
        "error": "Unsupported file format. Please upload a JPG, JPEG, PNG, or WEBP image."
    }), 415


@app.errorhandler(404)
def handle_not_found(e):
    """Handles 404 Not Found."""
    if request.path.startswith("/api/"):
        return jsonify({"success": False, "error": "Requested API endpoint not found."}), 404
    return render_template("index.html", error_message="Page not found. Redirected to home."), 404


@app.errorhandler(500)
def handle_internal_server_error(e):
    """Handles unexpected server errors."""
    return jsonify({
        "success": False,
        "error": "An internal server error occurred while processing your request. Please try again."
    }), 500


# ==========================================
# MAIN EXECUTION ENTRYPOINT
# ==========================================
if __name__ == "__main__":
    # In development mode, listen on 127.0.0.1:5000
    print("[+] Starting Plant Disease Detection web application...")
    print("[+] Server URL: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
