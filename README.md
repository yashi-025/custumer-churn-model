# *Face Detection using Haar Cascade Classifier*

Haar Cascade is a machine learning object detection algorithm used to identify objects in images or videos. It uses Haar-like features and a cascade of increasingly complex classifiers to detect objects quickly and efficiently.

# 🔍 Key Parameters:
**1) scaleFactor:**
> - Determines how much the image size is reduced at each image scale.
> - Smaller values (e.g., 1.05) mean the algorithm will be more thorough and slower; larger values (e.g., 1.4) make it faster but may miss faces.
> - Recommended Range: 1.05 – 1.3

**2) minNeighbors:**
> Specifies how many neighbors each rectangle candidate should have to retain it.
> Higher values reduce false positives but may miss some faces.
> Recommended Range: 3 – 6

Example:
> scaleFactor=1.1 implies image is scaled down by 10% at each step.
> minNeighbors=5 means region must have at least 5 neighbors to be considered a face.
