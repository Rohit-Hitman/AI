# ============================================================
# Animal Image Classification using Vision AI (TensorFlow)
# Python 3.11.3 compatible
# ============================================================

# ----------------------------
# STEP 1: Import Libraries
# ----------------------------
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image


# ----------------------------
# STEP 2: Configuration
# ----------------------------
IMAGE_SIZE = (224, 224)
# BATCH_SIZE = 4        # small batch (you have few images)
BATCH_SIZE = 16        # small batch (you have few images)
EPOCHS = 5            # small epochs to avoid overfitting

TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"


# ----------------------------
# STEP 3: Data Augmentation
# ----------------------------
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=30,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale=1.0 / 255
)


# ----------------------------
# STEP 4: Load Dataset
# ----------------------------
train_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

test_data = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

print("\nClass Indices:", train_data.class_indices)


# ----------------------------
# STEP 5: Load Pretrained Model
# ----------------------------
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False


# ----------------------------
# STEP 6: Build Final Model
# ----------------------------
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
output = Dense(train_data.num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)


# ----------------------------
# STEP 7: Compile Model
# ----------------------------
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ----------------------------
# STEP 8: Train Model
# ----------------------------
history = model.fit(
    train_data,
    validation_data=test_data,
    epochs=EPOCHS
)


# ----------------------------
# STEP 9: Plot Accuracy
# ----------------------------
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


# ----------------------------
# STEP 10: Evaluate Model
# ----------------------------
loss, accuracy = model.evaluate(test_data)
print(f"\nTest Accuracy: {accuracy * 100:.2f}%")


# ----------------------------
# STEP 11: Save Model
# ----------------------------
model.save("animal_image_classifier.h5")
print("\nModel saved as animal_image_classifier.h5")


# ----------------------------
# STEP 12: Predict Single Image
# ----------------------------
def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)

    class_labels = list(train_data.class_indices.keys())
    return class_labels[predicted_index]


# Example usage
# Replace with your image path
# sample_image_path = "sample.jpg"
# sample_image_path = "sample_1.jpg"
sample_image_path = "sample2_1.jpg"
# sample_image_path = "sample3.jpg"
# sample_image_path = "snake.jpg"

try:
    result = predict_image(sample_image_path)
    print("Predicted Animal:", result)
except:
    print("Please provide a valid image path for prediction.")
