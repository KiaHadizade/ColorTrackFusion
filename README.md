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

ColorTrackFusion/<br>
│<br>
├── src/<br>
│   ├── detection/<br>
│   │   ├── hsv_detector.py<br>
│   │   └── color_ranges.py<br>
│   │<br>
│   ├── tracking/<br>
│   │   ├── optical_flow_tracker.py<br>
│   │   ├── meanshift_tracker.py<br>
│   │   ├── camshift_tracker.py<br>
│   │   └── fusion.py<br>
│   │<br>
│   ├── pipeline/<br>
│   │   └── pipeline.py<br>
│   │<br>
│   ├── utils/<br>
│   │   ├── visualization.py<br>
│   │   ├── video_io.py<br>
│   │   ├── common.py<br>
│   │   └── metrics.py<br>
│   │<br>
│   └── main.py<br>
│<br>
├── configs/<br>
│   ├── colors.yaml<br>
│   ├── tracker.yaml<br>
│   └── camera.yaml<br>
│<br>
├── notebooks/<br>
│   ├── demo.ipynb<br>
│   ├── experiments.ipynb<br>
│   └── color-calibration.ipynb<br>
│<br>
├── examples/<br>
│   ├── example_video.mp4<br>
│   └── screenshots/<br>
│       └── demo.png<br>
│<br>
├── tests/<br>
│   ├── test_hsv.py<br>
│   ├── test_optical_flow.py<br>
│   ├── test_camshift.py<br>
│   └── test_pipeline.py<br>
│<br>
├── docs/<br>
│   ├── README_images/<br>
│   ├── installation.md<br>
│   ├── pipeline.md<br>
│   └── api_reference.md<br>
│<br>
├── .gitignore<br>
├── requirements.txt<br>
├── LICENSE<br>
└── README.md<br>


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