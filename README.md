# ROS 2 Robotics Control & Simulation Packages

## 🚀 Overview
Welcome to the repository containing the source code, custom nodes, and launch configurations for our automated ROS 2 workflows and package simulations.

This project was a highly collaborative, full-stack team effort developed for our ROS 2 system design coursework. All team members participated in the complete development lifecycle—from writing node logic and defining custom interfaces to testing and simulation.

## 🛠️ Technical Stack & Core Skills
* **Framework:** ROS 2 (Robot Operating System)
* **Languages:** C++ / Python
* **Build System:** Colcon
* **Environment:** Ubuntu Linux
* **Key Concepts:** Node Lifecycle Management, Topics (Publishers/Subscribers), Custom Interfaces (`.msg`, `.srv`), Trajectory Planning, Kinematics.

## ⚙️ Key System Features
As a team, we collaboratively engineered the following core functionalities:

### 1. Robot Control & Trajectory Planning
* **Kinematics & Motion:** Co-developed transform nodes to handle complex coordinate kinematics and configure motor trajectory profiles.
* **Safety Protocols:** Programmed dynamic safety thresholds and constraints to effectively prevent actuator saturation during high-acceleration motion profiles.

### 2. Multi-Node Communication & Integration
* **Data Pipelines:** Designed and deployed customized publishers and subscribers utilizing user-defined `.msg` and `.srv` interfaces for real-time robot joint state communication.
* **Orchestration:** Configured and optimized complex `launch` files to orchestrate the simultaneous execution of multiple life-cycle nodes seamlessly.

## 🎥 Project Demonstration
For a visual breakdown and detailed explanation of the system's operation and node interactions, please refer to our demonstration videos:
👉 [ROS 2 Projects Video Explanations](https://drive.google.com/drive/folders/14aFGvR1XqMG_KZoHEpeqvxyVF2EOvVvs)

## 💻 Prerequisites & Workspace Setup
To run these packages locally, ensure you have a working installation of **Ubuntu Linux** and **ROS 2**.

Follow these sequential steps to clone, build, and source the workspace:

1. Create a clean `colcon` workspace directory structure on your system.
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
* **Tasneem El-Shandidi**
* **Asmaa Galal**
