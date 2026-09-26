# ROS 2 Projects: Robotics Tasks & Package Simulations

> **Note:** This repository is my personal fork of a collaborative project developed alongside my team for our ROS 2 system design coursework. 

Welcome to the repository containing the source code, custom nodes, and launch configurations for our automated ROS 2 workflows and package simulations.

## 👥 The Team
This project was collaboratively designed and implemented by:
* **Rowan Tamer** 
* **Nada Mahmoud**  
* **Abd El-Rhman Saad**
* **Marina Said**
* **Razan Ramzy**
* **Tasneem El-Shandidi**
* **Mariam Mamdouh**
* **Asmaa Galal**

## 🎥 Task Explanation Videos
For a visual breakdown and detailed explanation of how each task operates, you can watch our project demonstration videos here:
👉 [ROS 2 Projects Video Explanations](https://drive.google.com/drive/folders/14aFGvR1XqMG_KZoHEpeqvxyVF2EOvVvs)

## 🚀 Project Overview & Key Tasks
As a team, we collaboratively engineered the following core functionalities:

### 1. Robot Control & Trajectory Planning
* **Kinematics & Motion:** Co-developed nodes to handle coordinate transforms and configure motor trajectory profiles.
* **Safety Protocols:** Programmed safety thresholds to prevent actuator saturation during high-acceleration movements.

### 2. Multi-Node Communication & Custom Interfaces
* **Data Pipelines:** Designed and implemented customized publishers and subscribers using custom `.msg` and `.srv` interfaces to communicate robot joint states effectively.
* **Orchestration:** Configured and optimized launch files to orchestrate the simultaneous execution of multiple life-cycle nodes.

## 🛠️ Prerequisites & Setup
To run these packages locally, ensure you have a working installation of **Ubuntu Linux** and **ROS 2**.

### Workspace Installation
Follow these sequential steps to clone, build, and source the workspace:

1. Create a clean colcon workspace directory structure on your system.
2. Clone this repository directly into your workspace's `src` folder.
3. Run `rosdep install` from the root of your workspace to automatically fetch missing dependencies.
4. Build the packages using `colcon build --symlink-install` to allow quick updates to script modifications.
5. Source the overlay by running `source install/setup.bash` in your current terminal session.
