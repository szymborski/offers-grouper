import os

from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from scipy.spatial.distance import cosine

from paths import IMAGE_FEATURES_PATH


def extract_features(img_path, model):
    # Load an image file, resizing it to 224x224 pixels (required by ResNet50 model input)
    img = image.load_img(img_path, target_size=(224, 224))
    # Convert the image to a numpy array and add a dimension to fit the model input
    img_array = image.img_to_array(img)
    img_array_expanded = np.expand_dims(img_array, axis=0)
    # Preprocess the image for the model
    img_array_preprocessed = preprocess_input(img_array_expanded)
    # Extract features
    features = model.predict(img_array_preprocessed)
    # Flatten the features to a 1D array
    flattened_features = features.flatten()
    # Normalize the features
    normalized_features = flattened_features / np.linalg.norm(flattened_features)
    return normalized_features


def feature_storage_path(img_path):
    img_path = img_path.replace("/", "_")
    feature_file_path = os.path.join(IMAGE_FEATURES_PATH, img_path + ".npy")
    return feature_file_path


def load_or_extract_features(img_path, model, extract=True):
    feature_path = feature_storage_path(img_path)
    features = None
    if os.path.exists(feature_path):
        # Load features from file
        features = np.load(feature_path)
    elif extract:
        # Extract features and save to file
        features = extract_features(img_path, model)
        np.save(feature_path, features)
    return features


def features_are_similar(image_1_features, image_2_features, threshold=0.8):
    if image_1_features is None or image_2_features is None:
        return False

    sim = 1 - cosine(image_1_features, image_2_features)

    return sim >= threshold
