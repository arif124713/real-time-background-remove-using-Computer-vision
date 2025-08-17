


# Real-Time Background Removal using Computer Vision

This project demonstrates **background removal** from both **static images** and **real-time video streams (webcam)** using **YOLOv8-segmentation** (`yolo11n-seg.pt`) and OpenCV. It leverages **instance segmentation** to detect objects and isolate them with transparency while removing the background.

## Features
- Remove background from images
- Real-time video background removal using webcam
- Produces transparent PNGs (RGBA)
- Works with YOLO segmentation masks
- Lightweight & fast (`yolo11n-seg.pt`)

## Project Structure


.
├── image\_background\_remove.py   # Background removal from static images
├── video\_background\_remove.py   # Real-time background removal (webcam)
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation


## Installation
1. Clone the repository:
bash
git clone https://github.com/arif124713/real-time-background-remove-using-Computer-vision.git
cd real-time-background-remove-using-Computer-vision


2. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download YOLO segmentation weights:

```python
from ultralytics import YOLO
model = YOLO("yolo11n-seg.pt")
```

## Usage

### For Image Background Removal

```bash
python image_background_remove.py --input your_image.jpg --output output.png
```

* Input: Any JPG/PNG image
* Output: PNG with transparent background

### For Real-Time Video Background Removal

```bash
python video_background_remove.py
```

* Uses your **webcam feed**
* Press `q` to exit the window

## Use Cases

* **Virtual Try-On (E-commerce & Fashion)**: Remove clothing product backgrounds for online stores, virtual trial rooms
* **Video Conferencing**: Replace/blur background in real time (like Zoom, Google Meet)
* **Content Creation**: Remove video/image backgrounds for YouTube, TikTok, Reels
* **Augmented Reality (AR) Applications**: Place real-world objects into digital environments
* **Photo Editing & Media**: Create transparent images (product catalogs, posters)

## How It Works

1. YOLOv8 segmentation detects objects/person in the frame
2. A segmentation mask is generated for detected objects
3. The mask is applied on the original image/video
4. Background pixels are replaced with transparency (alpha channel)

## Requirements

* Python 3.8+
* OpenCV
* NumPy
* Ultralytics (YOLO)

Install via:

```bash
pip install opencv-python numpy ultralytics
```

## Author

**Arif Hussain**
🔗 [GitHub](https://github.com/arif124713)

## Contribute

Feel free to fork, improve, or create pull requests! Contributions are welcome.

```

I can also **write a ready-to-use `requirements.txt`** for your repo so anyone can install everything with a single command. Do you want me to do that?
```
