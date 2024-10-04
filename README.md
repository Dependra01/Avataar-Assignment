# Avataar-Assignment

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Task 1: Segmenting Objects](#task-1-segmenting-objects)
  - [Task 2: Changing Object Positions](#task-2-changing-object-positions)
- [Results](#results)
- [References](#references)

## Introduction
This repository contains code for a scene composition assignment that leverages the Segment Anything Model (SAM) to segment objects in images and allows for repositioning those objects based on user-defined parameters. The project aims to develop a user-friendly method for editing product photographs for e-commerce applications.

## Problem Statement
With the advancement of generative AI, there is a growing need for efficient post-production editing workflows. This project focuses on two main tasks:
1. **Segmenting an object** in a given scene based on a user-defined class prompt.
2. **Changing the position** of the segmented object within the same scene.

## Installation
To run this project, make sure you have Python installed along with the necessary packages. Follow these steps to set up the environment:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install required packages:
   ```bash
   pip install torch torchvision torchaudio
   pip install opencv-python
   pip install numpy
   
4. Download the SAM model checkpoint and place it in the root directory:
   https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

## Usage

To run the segmentation and repositioning scripts, use the following commands:
### Task 1: Segmenting Objects
Description: The script identifies and segments a specified object class within an image, applying a red mask to highlight the object.

    python task1.py --image ./path/to/your/image.jpg --object_class <class_name> --output ./path/to/output/image.png
  
Replace <class_name> with one of the supported classes (e.g., curtains, window, armchair, etc.).

### Task 2: Changing Object Positions
Description: After segmentation, the object can be repositioned within the image based on user-defined pixel shifts.
      
    python task2.py --image ./path/to/your/image.jpg --object_class <class_name> --x <x_shift> --y <y_shift> --output ./path/to/output/image.png
      
Here, <x_shift> and <y_shift> specify the number of pixels to move the object in the horizontal and vertical directions, respectively.

## Results
### Example Input: 
![bagpack](https://github.com/user-attachments/assets/ba54e928-1294-47c3-b0b6-bf50624a57e4)

### Segmented Output: 
![segmented_image](https://github.com/user-attachments/assets/f7a2b753-73e5-4510-ba00-960d605c82c7)

### Shifted Output: 
![shifted_image](https://github.com/user-attachments/assets/56419a93-d2aa-4b9e-ab55-2b2579d53055)

## References
Segment Anything Model (SAM) [SAM](https://segment-anything.com/)
PyTorch Documentation
OpenCV Documentation
Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks


