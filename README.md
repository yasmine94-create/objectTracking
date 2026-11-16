# Object Tracking

A lightweight OpenCV + Streamlit project for tracking moving objects in uploaded videos.

## Overview

This repository contains a simple web app that lets you:

- Upload a video file (`.mp4`, `.avi`, or `.mov`)
- Run background subtraction to isolate moving objects
- Draw bounding boxes around detected objects in real time
- View the processed frames in the browser with Streamlit

The app uses OpenCV's `BackgroundSubtractorMOG2` to detect motion and highlights each moving region with a rectangle.

## Features

- Video upload from local machine
- Motion detection using background subtraction
- Object contour filtering based on area threshold
- Bounding boxes around detected objects
- Simple and interactive UI via Streamlit

## Project Structure

- `app.py` — Streamlit application entry point
- `requirements.txt` — Python dependencies
- `Data/` — sample media files and test assets
- `cv2_videos.ipynb` and `openCV.ipynb` — exploratory notebooks for OpenCV experiments

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Demo

Live demo: https://objecttracking-rxqg8gtwc82apkavhudvlt.streamlit.app/

## Run

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

## Usage

1. Upload a video from the sidebar.
2. Click the `start tracking` button.
3. The app processes frames and displays moving objects with green bounding boxes.

## Notes

- Detection works best when the camera or background remains mostly stable.
- The app uses a minimum contour area filter (`> 500`) to avoid small noise detections.
- Sample videos and images are included in the `Data/` folder for testing.

## Dependencies

- Python
- OpenCV (`opencv-python`)
- NumPy
- Streamlit
