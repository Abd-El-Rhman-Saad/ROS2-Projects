# ROS 2 Robotics Control & Simulation Packages

## 📖 Overview
This repository contains the source code for five distributed, multi-node vision and perception systems built using **ROS 2 (Robot Operating System)**. The primary focus of these packages is real-time computer vision, object detection, and depth estimation, acting as the perception layer for robotic applications. 

*(Note: This repository focuses on the vision/perception nodes and custom communication interfaces. Actuation and physical motor control nodes are handled separately and are not included here).*

## 🛠️ Technical Stack & Core Skills
* **Framework:** ROS 2 (Humble / Foxy)
* **Languages:** C++, Python
* **Computer Vision & AI:** OpenCV, YOLO, Depth Anything V2
* **Build System:** Colcon
* **Environment:** Ubuntu Linux
* **Key Concepts:** Topics (Publishers/Subscribers), Custom Interfaces (`.msg`, `.srv`).

## 🚀 Included Systems
1. **Exam Proctoring System**
2. **Security Surveillance**
3. **Visual Navigation**
4. **Multi-View Geometry**
5. **Fleet Coordination**

## 🏗️ Architecture & Communication
* **Modular Node Pipeline:** `Camera Node` → `Detection Node` → `Depth Node` → `Decision/Monitoring Node`.
* Features custom `.msg` and `.srv` interfaces to ensure lightweight, structured data transfer between distributed nodes across the network.
  
## 🎥 Project Demonstration
For a visual breakdown and detailed explanation of the system's operation and node interactions, please refer to our demonstration videos:
👉 [ROS 2 Projects Video Explanations](https://drive.google.com/drive/folders/14aFGvR1XqMG_KZoHEpeqvxyVF2EOvVvs)

## 💻 Prerequisites & Workspace Setup
To run these packages locally, ensure you have a working installation of **Ubuntu Linux** and **ROS 2**.

Follow these sequential steps to clone, build, and source the workspace:

1. Create a clean `colcon` workspace directory structure on your system:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
2. Clone this repository directly into your workspace's `src` folder.
3. Run `rosdep install` from the root of your workspace to automatically fetch missing dependencies.
4. Build the packages using the symlink option to allow quick updates to script modifications:
   ```bash
   colcon build --symlink-install
   ```
5. Source the overlay in your current terminal session:
   ```bash
   source install/setup.bash
   ```

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
