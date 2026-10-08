# ROS 2 Distributed Vision & Coordination Systems

## 📖 Overview
Source code of **five multi-node ROS 2 systems** written in Python (`rclpy`): **four computer-vision pipelines** (camera → detection → depth/analysis → decision) and **one multi-vehicle coordination system**. Each system is split into independent nodes that communicate over ROS 2 topics and services.

> **Scope:** this repository contains the **node scripts**. The custom interface packages used by the nodes (`multi_view_interfaces`, `fleet_interfaces`, `navigation_msgs`) and the Depth Anything V2 model code/weights are **not bundled here** and must be available in your workspace (see *Dependencies*). Actuation and physical motor control are not part of this repository.

## 🛠️ Tech Stack
* **Framework:** ROS 2, `rclpy`, `cv_bridge`, `message_filters`
* **Language:** Python
* **Vision & AI:** OpenCV, NumPy, PyTorch, YOLO (Ultralytics), Depth Anything V2
* **Environment:** Ubuntu Linux

## 🚀 Included Systems

| System | Nodes |
| :--- | :--- |
| **Smart Exam Proctoring** | camera stream · face detection · object detection · depth estimation · behavior analysis · rule evaluation · alert action · system monitor |
| **Smart Security Surveillance** | camera stream · object detection · depth estimation · scene analysis · event manager · event logger · security response · system monitor |
| **Visual Navigation Hint** | camera stream · object detection · depth estimation · feature extraction · motion tracking · visual odometry · navigation · action execution |
| **Multi-View Geometry Reasoning** | camera stream · keypoint detection · descriptor extraction · feature matching · match filtering · geometric consistency · motion estimation · reliability decision |
| **Grid Fleet Coordination** | task manager · traffic controller · vehicle node · monitor node |

## 🏗️ Architecture
* **Modular pipelines:** each stage is a separate node, e.g. `Camera → Detection → Depth → Decision / Monitoring`.
* **Topics and services** carry images, detections and decisions between nodes; custom `.msg` / `.srv` interfaces are used for structured data (interface packages listed above).

## 🎥 Demonstration
Demo videos and node-interaction explanations: [ROS 2 Projects Video Explanations](https://drive.google.com/drive/folders/14aFGvR1XqMG_KZoHEpeqvxyVF2EOvVvs)

## 📦 Dependencies
Python packages imported by the nodes: `rclpy`, `cv_bridge`, `opencv-python`, `numpy`, `torch`, `ultralytics`, plus the Depth Anything V2 code (`depth_anything_v2`) and its model weights.
Interface packages (not included): `multi_view_interfaces`, `fleet_interfaces`, `navigation_msgs`.

## 💻 Setup
1. Create a ROS 2 workspace and clone this repository into `src`:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   git clone https://github.com/Abd-El-Rhman-Saad/ROS2-Projects-.git
   ```
2. Install the Python dependencies above and add the interface packages and Depth Anything V2 to your workspace.
3. Build and source the workspace:
   ```bash
   cd ~/ros2_ws
   colcon build --symlink-install
   source install/setup.bash
   ```
4. Run the nodes of the system you want (each system folder has a `nodes/` directory).

## 👥 The Development Team
This complete system design was successfully delivered through the joint efforts of:
* **Abd El-Rhman Saad**
* **Tasneem El-Shandidi**
* **Mariam Mamdouh**
* **Rowan Tamer** 
* **Nada Mahmoud**  
* **Marina Said**
* **Razan Ramzy**
* **Asmaa Galal**
