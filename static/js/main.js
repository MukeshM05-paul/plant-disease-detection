/**
 * Plant Disease Detection - Frontend Application Logic
 * ----------------------------------------------------
 * Beginner-friendly vanilla JavaScript implementation.
 *
 * This script manages:
 * 1. File picker and drag-and-drop file ingestion.
 * 2. Instant client-side validation (file size limit: 5MB, supported MIME types).
 * 3. Client-side image preview and metadata extraction (dimensions, filesize).
 * 4. Sample image loading for fast interview testing.
 * 5. Asynchronous multipart/form-data upload via fetch() to Flask backend.
 * 6. UI state transitions: Idle -> Loading -> Results / Graceful Fallback / Friendly Error.
 */

// Run when the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // =========================================================================
  // DOM ELEMENT REFERENCES
  // =========================================================================
  const dropZone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');
  const previewContainer = document.getElementById('previewContainer');
  const previewImage = document.getElementById('previewImage');
  const previewMeta = document.getElementById('previewMeta');
  const metaFilename = document.getElementById('metaFilename');
  const metaFilesize = document.getElementById('metaFilesize');
  const metaDimensions = document.getElementById('metaDimensions');
  const clearBtn = document.getElementById('clearBtn');
  const analyzeBtn = document.getElementById('analyzeBtn');
  const uploadFeedback = document.getElementById('uploadFeedback');
  const toastContainer = document.getElementById('toastContainer');

  // Results State Containers
  const stateIdle = document.getElementById('stateIdle');
  const stateLoading = document.getElementById('stateLoading');
  const stateModelUnavailable = document.getElementById('stateModelUnavailable');
  const stateResults = document.getElementById('stateResults');
  const resultsTimestamp = document.getElementById('resultsTimestamp');

  // Diagnostic Detail Elements
  const healthBadge = document.getElementById('healthBadge');
  const latencyBadge = document.getElementById('latencyBadge');
  const diseaseTitle = document.getElementById('diseaseTitle');
  const plantName = document.getElementById('plantName');
  const confidenceValue = document.getElementById('confidenceValue');
  const confidenceBar = document.getElementById('confidenceBar');
  const top3List = document.getElementById('top3List');
  const recCause = document.getElementById('recCause');
  const recSeverity = document.getElementById('recSeverity');
  const symptomsList = document.getElementById('symptomsList');
  const actionsList = document.getElementById('actionsList');
  const preventionList = document.getElementById('preventionList');
  const modelUnavailableMsg = document.getElementById('modelUnavailableMsg');

  // Sample Buttons
  const sampleButtons = document.querySelectorAll('.sample-btn');

  // =========================================================================
  // APPLICATION STATE
  // =========================================================================
  let currentFile = null;
  const MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024; // 5 Megabytes
  const ALLOWED_MIME_TYPES = ['image/jpeg', 'image/png', 'image/webp'];

  // =========================================================================
  // HELPER UTILITIES
  // =========================================================================

  /**
   * Converts byte size into a friendly human-readable string (e.g., "350 KB", "2.1 MB")
   */
  function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  }

  /**
   * Displays non-blocking, accessible toast notifications
   */
  function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    const icon = type === 'error' ? '❌' : type === 'warning' ? '⚠️' : '✅';
    toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;

    toastContainer.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(16px)';
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }

  /**
   * Displays or clears feedback banner inside the upload card
   */
  function showFeedback(message, type = 'error') {
    if (!message) {
      uploadFeedback.className = 'feedback-banner hidden';
      uploadFeedback.textContent = '';
      return;
    }
    uploadFeedback.className = `feedback-banner ${type}`;
    uploadFeedback.textContent = message;
  }

  /**
   * Switches the active state in the results card
   * States: 'idle', 'loading', 'warning', 'results'
   */
  function setResultsState(state) {
    stateIdle.classList.add('hidden');
    stateLoading.classList.add('hidden');
    stateModelUnavailable.classList.add('hidden');
    stateResults.classList.add('hidden');

    if (state === 'idle') {
      stateIdle.classList.remove('hidden');
      resultsTimestamp.textContent = 'Ready for analysis';
    } else if (state === 'loading') {
      stateLoading.classList.remove('hidden');
      resultsTimestamp.textContent = 'Processing request...';
    } else if (state === 'warning') {
      stateModelUnavailable.classList.remove('hidden');
      resultsTimestamp.textContent = 'Model Offline';
    } else if (state === 'results') {
      stateResults.classList.remove('hidden');
      const now = new Date();
      resultsTimestamp.textContent = `Completed at ${now.toLocaleTimeString()}`;
    }
  }

  // =========================================================================
  // FILE VALIDATION & PREVIEW
  // =========================================================================

  /**
   * Validates selected file and generates immediate visual preview
   */
  function handleSelectedFile(file) {
    showFeedback(''); // Clear any previous error

    if (!file) return;

    // 1. Validate File Size (< 5MB)
    if (file.size > MAX_FILE_SIZE_BYTES) {
      showToast(`Selected file (${formatBytes(file.size)}) exceeds the 5 MB limit.`, 'error');
      showFeedback('File too large: Please choose an image smaller than 5 MB.', 'error');
      resetUpload();
      return;
    }

    // 2. Validate File Type (JPG, PNG, WEBP)
    const validExtension = /\.(jpe?g|png|webp)$/i.test(file.name);
    if (!ALLOWED_MIME_TYPES.includes(file.type) && !validExtension) {
      showToast('Unsupported format. Please select a JPG, PNG, or WEBP image.', 'error');
      showFeedback('Invalid format: Only JPG, JPEG, PNG, or WEBP photos are supported.', 'error');
      resetUpload();
      return;
    }

    currentFile = file;

    // 3. Render Instant Preview via Object URL
    const objectUrl = URL.createObjectURL(file);
    previewImage.src = objectUrl;

    // Extract natural dimensions using HTML Image object
    const tempImg = new Image();
    tempImg.onload = () => {
      metaDimensions.textContent = `${tempImg.naturalWidth} × ${tempImg.naturalHeight}`;
    };
    tempImg.src = objectUrl;

    // Populate preview metadata tags
    metaFilename.textContent = file.name;
    metaFilesize.textContent = formatBytes(file.size);

    // Show preview container and enable analyze button
    previewContainer.classList.remove('hidden');
    dropZone.classList.add('hidden');

    // Reset results column to idle prompt
    setResultsState('idle');
  }

  /**
   * Clears the current image selection and returns upload area to starting state
   */
  function resetUpload() {
    currentFile = null;
    fileInput.value = '';
    previewImage.src = '';
    previewContainer.classList.add('hidden');
    dropZone.classList.remove('hidden');
    showFeedback('');
    setResultsState('idle');
  }

  // =========================================================================
  // EVENT LISTENERS: DRAG & DROP AND FILE PICKER
  // =========================================================================

  // File Picker Change Event
  fileInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files[0]) {
      handleSelectedFile(e.target.files[0]);
    }
  });

  // Drag and Drop Visual Feedback
  ['dragenter', 'dragover'].forEach((eventName) => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach((eventName) => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.remove('dragover');
    });
  });

  // Drop File Handling
  dropZone.addEventListener('drop', (e) => {
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleSelectedFile(e.dataTransfer.files[0]);
    }
  });

  // Clear / Remove Button
  clearBtn.addEventListener('click', resetUpload);

  // =========================================================================
  // SAMPLE IMAGES LOADER (FOR FAST INTERVIEW DEMO)
  // =========================================================================
  sampleButtons.forEach((btn) => {
    btn.addEventListener('click', async () => {
      const sampleId = btn.dataset.sample;
      const sampleUrl = `/static/samples/${sampleId}.jpg`;

      try {
        btn.disabled = true;
        btn.style.opacity = '0.6';

        // Fetch sample file as a binary blob
        const response = await fetch(sampleUrl);
        if (!response.ok) {
          throw new Error(`Failed to load sample image (HTTP ${response.status})`);
        }

        const blob = await response.blob();
        const filename = `${sampleId}.jpg`;
        const file = new File([blob], filename, { type: 'image/jpeg' });

        // Load into preview
        handleSelectedFile(file);
        showToast(`Loaded sample: ${filename}`, 'info');

        // Automatically trigger analysis for seamless demo
        setTimeout(() => {
          analyzeLeaf();
        }, 200);

      } catch (err) {
        showToast(`Could not load sample: ${err.message}`, 'error');
      } finally {
        btn.disabled = false;
        btn.style.opacity = '1';
      }
    });
  });

  // =========================================================================
  // ASYNC PREDICTION HANDLER (FETCH API TO FLASK BACKEND)
  // =========================================================================
  analyzeBtn.addEventListener('click', analyzeLeaf);

  async function analyzeLeaf() {
    if (!currentFile) {
      showToast('Please select or drop a leaf image first.', 'warning');
      return;
    }

    // 1. Transition UI to Loading State
    setResultsState('loading');
    analyzeBtn.disabled = true;

    // 2. Build FormData payload
    // The backend route (/api/predict) expects the file under key 'image'
    const formData = new FormData();
    formData.append('image', currentFile);

    try {
      // 3. Dispatch POST request to Flask
      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();

      // 4. Handle Server / Validation Errors
      if (!response.ok || !data.success) {
        const errorMsg = data.error || `Server returned error status ${response.status}`;
        showToast(errorMsg, 'error');
        showFeedback(errorMsg, 'error');
        setResultsState('idle');
        return;
      }

      // 5. Check if the model is available or marked offline
      if (data.model_available === false) {
        // Model is not configured; display graceful fallback
        modelUnavailableMsg.textContent = data.message || 'Model is not configured.';
        setResultsState('warning');
        showToast('Image verified by Pillow! Note: AI model is currently offline.', 'warning');
        return;
      }

      // 6. Display Genuine AI Classification & Agricultural Care Advice
      renderResults(data);
      setResultsState('results');
      showToast('Leaf analysis completed successfully!', 'info');

    } catch (err) {
      console.error('Prediction request error:', err);
      showToast(`Network or server error: ${err.message}`, 'error');
      showFeedback(`Connection failed: ${err.message}`, 'error');
      setResultsState('idle');
    } finally {
      analyzeBtn.disabled = false;
    }
  }

  // =========================================================================
  // RENDER DIAGNOSTIC RESULTS
  // =========================================================================
  function renderResults(data) {
    const pred = data.prediction;
    const recs = data.recommendations;

    // 1. Primary Disease / Health Info
    diseaseTitle.textContent = pred.disease_name;
    plantName.textContent = pred.plant_type;
    latencyBadge.textContent = `${data.inference_time_ms} ms`;

    if (pred.is_healthy) {
      healthBadge.className = 'health-badge healthy';
      healthBadge.textContent = '🌱 Healthy Plant Specimen';
    } else {
      healthBadge.className = 'health-badge disease';
      healthBadge.textContent = '⚠️ Disease Detected';
    }

    // 2. Confidence Metric & Bar
    const confScore = (pred.confidence * 100).toFixed(2);
    confidenceValue.textContent = `${confScore}%`;
    confidenceBar.style.width = `${Math.min(confScore, 100)}%`;

    // Visual color shift if confidence is low/moderate
    if (pred.confidence < 0.6) {
      confidenceBar.style.background = '#d97706'; // Amber for lower certainty
    } else {
      confidenceBar.style.background = 'linear-gradient(90deg, #10b981 0%, #059669 100%)';
    }

    // 3. Top 3 Predictions Breakdown
    top3List.innerHTML = '';
    if (pred.top_3 && pred.top_3.length > 0) {
      pred.top_3.forEach((item) => {
        const row = document.createElement('div');
        row.className = 'top3-item';
        row.innerHTML = `
          <div class="top3-left">
            <span class="top3-rank">#${item.rank}</span>
            <span class="top3-name">${item.label}</span>
          </div>
          <span class="top3-conf">${item.confidence_percent}</span>
        `;
        top3List.appendChild(row);
      });
    }

    // 4. Agricultural Recommendations
    if (recs) {
      recCause.textContent = recs.cause || 'Not specified';
      recSeverity.textContent = recs.severity || 'Moderate';

      // Symptoms
      symptomsList.innerHTML = '';
      (recs.symptoms || []).forEach((symptom) => {
        const li = document.createElement('li');
        li.textContent = symptom;
        symptomsList.appendChild(li);
      });

      // Immediate Actions
      actionsList.innerHTML = '';
      (recs.immediate_actions || []).forEach((action) => {
        const li = document.createElement('li');
        li.textContent = action;
        actionsList.appendChild(li);
      });

      // Prevention
      preventionList.innerHTML = '';
      (recs.prevention || []).forEach((prev) => {
        const li = document.createElement('li');
        li.textContent = prev;
        preventionList.appendChild(li);
      });
    }
  }

});
