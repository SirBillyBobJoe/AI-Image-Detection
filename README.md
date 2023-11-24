# Machine-Learning Image Detection

## Overview
Machine-Learning Image Detection is a Python-based application utilizing machine learning models to identify objects in images. This project leverages the CIFAR-10 and CIFAR-100 datasets for image classification.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have a `Windows`, `Linux` or `Mac` machine.
* You have installed the latest version of `Python`.

## Installation

### Python and pip Installation

#### Windows
1. Download Python from [Python's official website](https://www.python.org/downloads/windows/).
2. Run the installer. Ensure to check “Add Python to PATH” before installation.
3. Verify the installation by opening Command Prompt and typing `python --version`.

#### Linux (Debian/Ubuntu)
1. Open Terminal and update the package list: `sudo apt update`.
2. Install Python: `sudo apt install python3`.
3. Install pip: `sudo apt install python3-pip`.
4. Verify Python and pip installation: `python3 --version` and `pip3 --version`.

#### MacOS
1. Install [Homebrew](https://brew.sh/), a package manager for macOS.
2. Open Terminal and install Python: `brew install python`.
3. This will install both Python and pip.
4. Verify the installation: `python3 --version` and `pip3 --version`.

### Dependency Installation For Windows

Run the following commands to install necessary libraries:

```bash
pip install numpy
pip install matplotlib
pip install tensorflow
pip install opencv-python
```

### Dependency Installation For MacOS & Linux

Run the following commands to install necessary libraries:

```bash
pip3 install numpy
pip3 install matplotlib
pip3 install tensorflow
pip3 install opencv-python
```
## Running the Application

To start the application, navigate to the project directory in your Python environment and execute the `run.py` script. Ensure that all the necessary libraries are installed before attempting to run the application.

## Models and Accuracy

The AI Image Detection application supports two distinct machine learning models:

### CIFAR-10 Model
- **Accuracy**: Approximately 70%
- **Classes Detected**: This model is capable of identifying the following objects:
  - Plane
  - Car
  - Bird
  - Cat
  - Deer
  - Dog
  - Frog
  - Horse
  - Ship
  - Truck

### CIFAR-100 Model
- **Accuracy**: Approximately 30%
- **Classes Detected**: This model can detect a broader range of objects, including:
  - apple, aquarium_fish, baby, bear, beaver, bed, bee, beetle
  - bicycle, bottle, bowl, boy, bridge, bus, butterfly, camel
  - can, castle, caterpillar, cattle, chair, chimpanzee, clock, cloud
  - cockroach, couch, crab, crocodile, cup, dinosaur, dolphin, elephant
  - flatfish, forest, fox, girl, hamster, house, kangaroo, keyboard
  - lamp, lawn_mower, leopard, lion, lizard, lobster, man, maple_tree
  - motorcycle, mountain, mouse, mushroom, oak_tree, orange, orchid, otter
  - palm_tree, pear, pickup_truck, pine_tree, plain, plate, poppy, porcupine
  - possum, rabbit, raccoon, ray, road, rocket, rose, sea
  - seal, shark, shrew, skunk, skyscraper, snail, snake, spider
  - squirrel, streetcar, sunflower, sweet_pepper, table, tank, telephone, television
  - tiger, tractor, train, trout, tulip, turtle, wardrobe, whale
  - willow_tree, wolf, woman, worm
