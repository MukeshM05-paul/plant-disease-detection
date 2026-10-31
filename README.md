# 🍃 Plant Disease Detection Web Application

An end-to-end, beginner-friendly web application that detects plant diseases from leaf photographs using **Python Flask**, **Pillow (PIL)**, and a real pretrained **MobileNetV2 ONNX neural network** fine-tuned on the PlantVillage benchmark dataset.

Built with clean architecture and robust error handling for software engineering technical interviews.

---

## 🌟 Key Features

1. **Responsive Home Page**: Modern, responsive user interface explaining the diagnostic tool, supported crops, and detection pipeline.
2. **File Picker & Drag-and-Drop Upload**: Clean dropzone supporting JPG, JPEG, PNG, and WEBP formats with a 5 MB maximum size limit.
3. **Instant Previews**: Client-side image preview with metadata display (file name, file size, natural dimensions).
4. **Backend Security & Format Validation**: Multi-layer validation checking MIME types, file extensions, payload size limits, and Pillow `Image.verify()` to detect corrupted or fake images.
5. **Real Pretrained AI Model (Zero Fabricated Results)**: Runs a 9.2 MB MobileNetV2 ONNX model over 38 agricultural classes, outputting genuine softmax probabilities and confidence scores.
6. **Graceful Fallback Mode**: If model weights are ever unconfigured, image upload and preview succeed normally while clearly informing the user that AI prediction is offline until configured (no random guesses or faked predictions).
7. **Comprehensive Agricultural Recommendations**: Displays pathogen cause (fungal, bacterial, viral, pest), symptoms checklist, immediate corrective treatments, and long-term prevention strategies for every supported plant condition.
8. **One-Click Quick Test Samples**: Three bundled sample leaves (`apple_scab.jpg`, `apple_healthy.jpg`, `tomato_early_blight.jpg`) enabling instant testing during technical demos.
9. **User-Friendly Error Handling**: Informative alerts for invalid file types, oversized files (> 5MB), corrupted files, and connection errors.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla ES6) | Responsive UI, drag-and-drop, instant image preview, asynchronous `fetch()` API |
| **Backend** | Python Flask 3.1 | RESTful routing, request parsing, upload validation, error handling |
| **Image Processing** | Pillow (PIL 13.0) | Stream validation, corruption verification, aspect-ratio resizing, center-cropping |
| **Machine Learning** | ONNX Runtime 1.31 | High-performance CPU inference on pretrained MobileNetV2 graph |
| **Dataset & Model** | MobileNetV2 (PlantVillage Fine-Tuned) | 38 crop disease & healthy classes across 14 plant families |

---

## 📋 System Requirements

- **Operating System:** Windows 10 / 11 (also compatible with macOS and Linux)
- **Python Version:** Python 3.10, 3.11, 3.12, 3.13, or 3.14
- **Internet Connection:** Only needed during initial setup to download dependencies and model weights. Once downloaded, the application runs **100% locally and offline**.

---

## 🚀 Windows Installation & Run Instructions

Follow these step-by-step commands in **Windows PowerShell** or **Command Prompt**:

### Step 1: Open the Project Directory
```powershell
cd c:\Users\mukes\OneDrive\Desktop\plat_disease_detection
```

### Step 2: (Optional but Recommended) Create a Virtual Environment
```powershell
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Or on Windows Command Prompt (cmd.exe):
.\venv\Scripts\activate.bat
```

### Step 3: Install Required Dependencies
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Verify or Download Model Weights
The repository includes a helper script that downloads the official 9.2 MB MobileNetV2 model and configuration from Hugging Face if they are not already present:
```powershell
python download_model.py
```
*(If the model files already exist in the `model/` folder, this script simply confirms they are present and verified.)*

### Step 5: Run the Automated Test Suite
Ensure all backend validations, error handlers, and prediction endpoints are functioning correctly:
```powershell
python test_app.py
```
*Expected output: `Ran 11 tests in ... OK`*

### Step 6: Start the Flask Application
```powershell
python app.py
```

### Step 7: Open the Application in Your Browser
Open your favorite web browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📁 Project Directory Structure & File Explanations

```
plat_disease_detection/
├── app.py                   # Main Flask backend server and API endpoints
├── classifier.py            # Pillow preprocessing & ONNX Runtime inference engine
├── recommendations.py       # Curated agricultural plant care knowledge base
├── download_model.py        # Automated model weights & config download utility
├── test_app.py              # Automated unit and integration test suite (11 test cases)
├── requirements.txt         # Pinned Python package dependencies
├── README.md                # Documentation and interview guide
├── model/
│   ├── model.onnx           # 9.2 MB MobileNetV2 neural network weights (ONNX format)
│   └── config.json          # Dictionary mapping class indices (0-37) to disease names
├── static/
│   ├── css/
│   │   └── style.css        # Responsive styling with modern color scheme and cards
│   ├── js/
│   │   └── main.js          # Pure vanilla JS: preview, validation, and fetch upload
│   ├── samples/             # Bundled leaf photos for quick interview demonstrations
│   │   ├── apple_scab.jpg
│   │   ├── apple_healthy.jpg
│   │   └── tomato_early_blight.jpg
│   └── favicon.svg          # Custom leaf SVG browser favicon
└── templates/
    └── index.html           # Semantic HTML5 home page and diagnostic layout
```

### Detailed Breakdown of Every Important File

1. **`app.py`**:
   - Initializes Flask and configures `MAX_CONTENT_LENGTH = 5 * 1024 * 1024` (5 MB upload limit).
   - Implements `GET /` to render `index.html`.
   - Implements `POST /api/predict` to receive leaf image uploads, validate filename and extensions, enforce file size limits, verify image integrity with Pillow, invoke `classifier.predict()`, and return JSON.
   - Implements `GET /api/status` for application health checks and supported disease counts.
   - Registers error handlers for HTTP 400 (Bad Request), 413 (Payload Too Large), 415 (Unsupported Media Type), and 500 (Internal Server Error).

2. **`classifier.py`**:
   - Manages the `PlantClassifier` class using `onnxruntime` and `Pillow`.
   - Checks whether model weights are available (`is_available()`).
   - Implements `preprocess_image()`: converts image to RGB, scales shortest edge to 256px, takes a 224&times;224 center-crop, normalizes pixel values with mean=[0.5, 0.5, 0.5] and std=[0.5, 0.5, 0.5], and shapes into a `(1, 3, 224, 224)` float32 tensor.
   - Computes mathematical softmax over raw logits:
     $$\text{softmax}(z_i) = \frac{e^{z_i - \max(z)}}{\sum_j e^{z_j - \max(z)}}$$
   - Returns top prediction, confidence score, and top-3 alternatives.
   - **Honesty Guarantee**: If model files are absent, does NOT fake or randomize results; returns `model_available: false` with Pillow image metadata and setup instructions.

3. **`recommendations.py`**:
   - Contains a comprehensive agricultural knowledge base for all 38 classes.
   - Maps disease names to plant family, biological cause (Fungal, Bacterial, Viral, Pest, None), severity rating, symptoms to inspect, immediate chemical/organic treatments, and long-term cultural prevention techniques.

4. **`download_model.py`**:
   - A standalone script that safely downloads `config.json` and `model.onnx` directly from the Hugging Face repository using standard Python `urllib` with progress indicators.

5. **`templates/index.html`**:
   - Semantic HTML5 structure including sticky navbar, hero section, 2-column analyzer workspace, interactive "How It Works" pipeline, supported crops catalog, and technical architecture interview reference.

6. **`static/css/style.css`**:
   - Modern, responsive styling with clean variables, flexbox, CSS grid, accessible contrast ratios, drag-and-drop hover animations, and card layouts.

7. **`static/js/main.js`**:
   - Handles file input change and drag-and-drop events.
   - Performs client-side validation (file size < 5MB and image extension).
   - Generates instantaneous image previews via `URL.createObjectURL(file)`.
   - Dispatches multipart form data to `POST /api/predict`.
   - Renders results, confidence bars, top-3 tables, and agricultural advice cards.

---

## 🔄 End-to-End Walkthrough: How Image Uploads Reach the Backend

Here is the exact step-by-step lifecycle of an image from user interaction to diagnostic report:

```
[User Selects Image]
        │
        ▼
[Client-side (main.js)]
   ├── 1. Validates file extension (JPG, PNG, WEBP)
   ├── 2. Validates file size (< 5 MB)
   ├── 3. Renders immediate preview via URL.createObjectURL()
   └── 4. Builds FormData({ image: file }) and calls fetch('/api/predict', { method: 'POST' })
        │
        ▼ (HTTP POST multipart/form-data)
[Flask Backend (app.py)]
   ├── 1. Enforces MAX_CONTENT_LENGTH = 5MB (returns 413 if exceeded)
   ├── 2. Validates 'image' key in request.files
   ├── 3. Checks secure_filename() and validates extension against whitelist (returns 415 if invalid)
   └── 4. Passes image bytes to classifier_instance.predict(image_bytes)
        │
        ▼
[Image Preprocessor (classifier.py & Pillow)]
   ├── 1. Calls Image.open(BytesIO) and pil_image.verify() to detect corrupted bytes (returns 400 if bad)
   ├── 2. Converts image to RGB colorspace
   ├── 3. Scales shortest edge to 256px and extracts a 224x224 center crop
   └── 4. Normalizes to float32 tensor of shape (1, 3, 224, 224)
        │
        ▼
[ONNX Runtime Neural Graph]
   ├── 1. Executes MobileNetV2 graph: input 'pixel_values' -> output 'logits' (38 float values)
   ├── 2. Applies numerically stable Softmax: exp(logits - max(logits)) / sum(...)
   ├── 3. Identifies top-1 winning class index and formats confidence score
   └── 4. Collects top-3 alternative predictions for full transparency
        │
        ▼
[Recommendation Engine (recommendations.py)]
   └── Matches predicted disease label to symptoms, causes, immediate actions, and prevention tips
        │
        ▼ (HTTP 200 JSON Response)
[Client-side UI (main.js)]
   └── Transitions from loading spinner to diagnostic report, updating confidence bar and advice cards
```

---

## 🌿 Supported Plant Families & Disease Classes (38 Total)

| Plant Family | Conditions Covered |
| :--- | :--- |
| **Apple** | Apple Scab, Black Rot, Cedar Apple Rust, Healthy Apple |
| **Blueberry** | Healthy Blueberry Plant |
| **Cherry** | Powdery Mildew, Healthy Cherry Plant |
| **Corn (Maize)** | Cercospora / Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy Corn |
| **Grape** | Black Rot, Esca (Black Measles), Isariopsis Leaf Spot, Healthy Grape Plant |
| **Orange / Citrus** | Citrus Greening (Huanglongbing / HLB) |
| **Peach** | Bacterial Spot, Healthy Peach Plant |
| **Bell Pepper** | Bacterial Spot, Healthy Bell Pepper Plant |
| **Potato** | Early Blight, Late Blight, Healthy Potato Plant |
| **Raspberry** | Healthy Raspberry Plant |
| **Soybean** | Healthy Soybean Plant |
| **Squash** | Powdery Mildew |
| **Strawberry** | Leaf Scorch, Healthy Strawberry Plant |
| **Tomato** | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus (TYLCV), Mosaic Virus (ToMV), Healthy Tomato |

---

## 🎯 Technical Interview Discussion Points

When discussing this application in your interview, highlight these intentional engineering choices:

1. **Why ONNX Runtime instead of full PyTorch or TensorFlow?**
   - *Answer:* In production web inference, bundling full PyTorch or TensorFlow adds 1.5 GB to 3.0 GB of dependencies, slow cold-start times, and heavy memory usage. ONNX Runtime is a lightweight C++ engine with Python bindings (under 20 MB) that executes optimized computation graphs on standard CPUs with single-digit millisecond latency.
2. **How is input security handled?**
   - *Answer:* Attackers often upload executable scripts renamed to `.jpg`. We validate on three distinct layers:
     - Extension whitelist (`.jpg`, `.jpeg`, `.png`, `.webp`).
     - HTTP payload limit (`MAX_CONTENT_LENGTH = 5MB`).
     - Image stream header and structure parsing via Pillow's `Image.verify()`. If non-image bytes are masked as a JPEG, Pillow raises an exception and the server returns a friendly 400 error.
3. **Why center-crop and shortest-edge resize instead of direct squishing?**
   - *Answer:* Direct squishing distorts the aspect ratio of leaf veins and lesions, altering the morphological features the neural network was trained to recognize. By resizing the shortest edge to 256px and cropping the central 224x224 area, natural biological proportions are maintained.
4. **How are predictions kept genuine without fabricating scores?**
   - *Answer:* The model outputs unnormalized log-odds (logits) across 38 classes. We apply the standard mathematical softmax function to obtain true probability distributions that sum to 1.0. We display both the top prediction and top-3 alternatives for transparent evaluation.
5. **How does the system handle an unconfigured model?**
   - *Answer:* Rather than crashing or returning fake dummy predictions, `classifier.py` checks for model availability. If absent, the upload and preview flow completes successfully and returns a clean `model_available: false` response instructing the user how to configure the model.

---

## 🧪 Testing Summary

The project includes an automated test suite in `test_app.py`:
- `test_01_home_page_renders_successfully`: Validates 200 status code and template elements.
- `test_02_api_status_endpoint`: Tests `/api/status` JSON contract and class count.
- `test_03_api_samples_endpoint`: Tests sample leaf catalog availability.
- `test_04_predict_missing_file_payload`: Tests 400 error when no file is passed.
- `test_05_predict_empty_filename`: Tests 400 error for empty filename selection.
- `test_06_predict_unsupported_file_extension`: Tests 415 error for `.txt` or non-image files.
- `test_07_predict_corrupted_image_content`: Tests Pillow verification catching corrupted byte streams.
- `test_08_predict_oversized_file`: Tests 413 error when upload exceeds 5 MB.
- `test_09_predict_real_apple_scab_image`: Tests real inference on Apple Scab (>99% confidence).
- `test_10_predict_real_healthy_apple_image`: Tests real inference on Healthy Apple.
- `test_11_model_unavailable_fallback_behavior`: Tests graceful fallback when model is detached.

Run all tests anytime with:
```powershell
python test_app.py
```
