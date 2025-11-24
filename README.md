# 🎯 ColorTrackFusion  
### Hybrid Object Detection & Tracking Using HSV, Optical Flow, MeanShift/CamShift

## 🚀 Overview

This project implements a **robust real-time object tracking system** that fuses:

- HSV-based color segmentation  
- Lucas–Kanade Optical Flow  
- MeanShift & CamShift tracking  
- Multi-tracker fusion with periodic re-detection  

This hybrid approach offers:

✔ Stable and smooth tracking  
✔ Resistance to noise and drift  
✔ Recovery when the object is lost  
✔ Real-time performance

---

## 🔥 Features

- 🎨 HSV-based object detection  
- 🧠 Sparse optical flow tracking (Lucas–Kanade)  
- 📦 MeanShift & CamShift region tracking  
- ⚒️ Tracker fusion for robustness  
- ♻️ Automatic tracking drift correction  
- 🧩 Modular and clean pipeline  
- 🎥 Works with both video input and webcam  

---

## 📁 Project Structure

ColorTrackFusion/
│
├── src/
│   ├── detection/
│   │   ├── hsv_detector.py
│   │   └── color_ranges.py
│   │
│   ├── tracking/
│   │   ├── optical_flow_tracker.py
│   │   ├── meanshift_tracker.py
│   │   ├── camshift_tracker.py
│   │   └── fusion.py
│   │
│   ├── pipeline/
│   │   └── pipeline.py
│   │
│   ├── utils/
│   │   ├── visualization.py
│   │   ├── video_io.py
│   │   ├── common.py
│   │   └── metrics.py
│   │
│   └── main.py
│
├── configs/
│   ├── colors.yaml
│   ├── tracker.yaml
│   └── camera.yaml
│
├── notebooks/
│   ├── demo.ipynb
│   ├── experiments.ipynb
│   └── color-calibration.ipynb
│
├── examples/
│   ├── example_video.mp4
│   └── screenshots/
│       └── demo.png
│
├── tests/
│   ├── test_hsv.py
│   ├── test_optical_flow.py
│   ├── test_camshift.py
│   └── test_pipeline.py
│
├── docs/
│   ├── README_images/
│   ├── installation.md
│   ├── pipeline.md
│   └── api_reference.md
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md


For implementation details, see the `src/` directory

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/color-object-tracker.git
cd color-object-tracker
pip install -r requirements.txt
```

## ▶️ Usage

Run the main script:
`python src/main.py --video examples/example_video.mp4`

or webcam mode:
`python src/main.py --webcam`

## ⚙️ Configuration

All thresholds and parameters are stored in:
- `configs/colors.yaml`
- `configs/tracker.yaml`
You can easily tune HSV color ranges here

## 📊 Pipeline

- HSV object detection
- Initialize optical flow + CamShift
- Track both
- Fuse results
- Re-detect periodically
- Output final bounding box

## 📓 Notebooks

- `notebooks/demo.ipynb` – quick overview and visualization
- `notebooks/experiments.ipynb` – tuning & tracking benchmarks
- `notebooks/color-calibration.ipynb` – adjusting HSV values

## 🖼 Examples

See the examples/ folder for sample videos and screenshots

## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues or discussion threads

## 📄 License

This project is licensed under the MIT License