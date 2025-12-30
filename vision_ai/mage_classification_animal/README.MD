
-------------------Project Explanation

“I built an Animal Image Classification system using Vision AI.
The goal of the project is to automatically identify animals such as cat, dog, monkey, and elephant from images.”

“I used Python and TensorFlow with a pre-trained MobileNetV2 model.
Instead of training a model from scratch, I applied transfer learning to reuse visual features learned from ImageNet.”

“The dataset was organized into training and testing folders, where each animal had its own directory.
I used Keras’ ImageDataGenerator for image loading, resizing, normalization, and data augmentation.”

“I froze the pretrained layers and added custom dense layers on top to classify my specific animal classes.
The model was trained using categorical cross-entropy loss and the Adam optimizer.”

“After training, I evaluated the model on test images, visualized accuracy, saved the trained model, and implemented a function to predict a single image.”

----------------------------------------Technology Stack Used:


| Component        | Used Tool          |
| ---------------- | ------------------ |
| Language         | Python 3.11        |
| Deep Learning    | TensorFlow / Keras |
| Vision Model     | MobileNetV2        |
| Data Handling    | NumPy              |
| Visualization    | Matplotlib         |
| Image Processing | Pillow             |
| Training Method  | Transfer Learning  |

--------------------------------------

Model Architecture

“I used MobileNetV2 as the base model with ImageNet weights and removed its top classification layer.”
Custom layers added:

GlobalAveragePooling2D

Dense layer (ReLU activation)

Output Dense layer (Softmax)

👉 Softmax converts outputs into class probabilities.

-------------------------------
Training Strategy

“I froze the pretrained layers so the model could retain generic visual features and trained only the custom layers.”

--------------------------------------------
Training details:

Optimizer: Adam

Loss Function: Categorical Cross-Entropy

Metric: Accuracy

Epochs: 5 (small dataset)

------------------------------
Prediction System
    “I implemented a prediction function that accepts an image path, preprocesses the image, and returns the predicted animal class.”

Model Saving
    “The trained model is saved using the native Keras .keras format, which is recommended for long-term compatibility.”

--------------------------------Questions and Answers
Why MobileNetV2?
    “It is lightweight, fast, and performs well on small datasets, making it ideal for beginners and real-time applications.”

Why not train from scratch?
    “Training from scratch requires large datasets and computational resources. Transfer learning is more efficient and practical.”





