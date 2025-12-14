# 🚗 Car Damage Detection SaaS (MVP)

## 🔍 Overview
This project is an end-to-end AI solution designed to automate the vehicle inspection process. By leveraging Computer Vision (YOLOv8), the application detects and classifies vehicle damages (e.g., scratches, dents, glass shatter) from images or video streams.

The goal was to build a SaaS MVP (Minimum Viable Product) that can help insurance companies and car rental agencies reduce manual inspection time and ensure consistent damage reporting.

## 🚀 Key Features
* Automated Detection: Instantly identifies various types of car damage with high accuracy.

* User-Friendly Dashboard: A web-based interface built with Flask for easy image uploading and result visualization.

* Cloud-Ready Architecture: Designed and initially deployed on AWS for scalability.

* Custom Dataset: Trained on a curated dataset labeled via Roboflow to ensure model robustness.

## 📸 Screenshots & Demo
(Since the AWS instance is currently paused for cost optimization, here are snapshots from the working prototype.)

## Detection Result
<img src="https://github.com/user-attachments/assets/4dcc7126-3bb6-47a9-b77c-51027a18e103" width="300">

## 🛠️ Tech Stack & Pipeline
This project follows a complete MLOps pipeline from data collection to deployment:

1.**Data Curation**: Images were collected and labeled using Roboflow. 

2. **Model Training**: Fine-tuned YOLOv8 (You Only Look Once) model for object detection.

3. **Backend**: Developed a RESTful API using Flask to serve the model.
   
4. **Frontend**: HTML/CSS/JS interface for user interaction.
   
5. **Deployment**: Containerized and deployed on AWS (EC2).

## 🗺️ Roadmap (Future Improvements)
As a product-focused engineer, I have planned the following iterations:
* [ ] [ ] Cost Estimation: Integrate an algorithm to estimate repair costs based on detected damage size.
* [ ] [ ] Mobile Integration: Develop a mobile-first version for on-site inspections.
* [ ] [ ] Report Generation: Auto-generate PDF reports for insurance claims.

## 📬 Contact
Şeyda Öksüzoğlu

LinkedIn: www.linkedin.com/in/şeyda-öksüzoğlu-666b90302

Email: seydaoksuzoglu01@gmail.com
