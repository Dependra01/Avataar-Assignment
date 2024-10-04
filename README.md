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
- [Future Improvements](#future-improvements)
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
Task 1: Segmenting Objects
  ```bash
   python task1.py --image ./path/to/your/image.jpg --object_class <class_name> --output ./path/to/output/image.png
