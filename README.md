# CHL7001
This is the project I build for CHL7001, the topic is Covid Detection from X-rays.

# Quick Start

Build from local
```
pip3 install -r requirements.txt
```

Start Docker Image
```
```

# Scripts

There are different scripts that are responsible for different topics. Here is the summary over all:
1. boxing_label.ipynb
    * Responsible for generating the boxing locations after resizing the images.
1. transfer_to_rgb.ipynb
    * Perform image enhancement. Could transfer image to RGB, or perform UM, CLAHE and HEF those common image enhancement techniques. However, those images have been cached.
1. Xray_PreData_Compare.ipynb
    * Compare different image enhancement techniques, the optimum solution we had is **CLAHE**
1. Dense121_transfer_learning.ipynb
    * Compare the transfer_learning on CheXNet with Naive Dense 121 model for classification tasks.
1. EffNet_train.ipynb 
    * Train the efficient net for image classification tasks.
    * (To be transferred from cloud to github)
1. FRCNN_train.ipynb
    * Train the Faster RCNN for object detection tasks.
    * (To be transferred from cloud to github)
1. YOLO_train_scripts.ipynb
    * Train the YOLOv5 model for object detection tasks.
1. prediction.ipynb
    * generate the predictions based on cached models. Used for Kaggle competition submissions
    * (To be transferred from cloud to github)
1. Cloud_Deployment.ipynb
    * Deploy the optimum YOLOv5 model with AWS SageMaker for real time predictions. I haven't yet build the APIs, so you need to upload the image locally.
    * (To be Done)

# Future Work

There are couple data engineering works that I want to finish in the future.

* Build a full RESTapi so users could upload images for object detection through web applications.
* Build a data pipeline that can handle large amount of image classification tasks.
