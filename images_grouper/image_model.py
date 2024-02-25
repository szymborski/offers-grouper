from image_features import load_or_extract_features, features_are_similar


def load_model():
    from tensorflow.keras.applications.resnet50 import ResNet50
    from tensorflow.keras.models import Model

    # Load the ResNet50 model pre-trained on ImageNet data, excluding the top fully connected layers
    model = ResNet50(weights="imagenet", include_top=False)
    # Add global average pooling to summarize features in a vector per image
    model = Model(inputs=model.inputs, outputs=model.output)
    return model


def get_similar_images(model, img_path, img_paths_list):
    image_1_features = load_or_extract_features(img_path, model, extract=True)

    for img_path in img_paths_list:
        # Extract features for each image to compare
        image_2_features = load_or_extract_features(img_path, model, extract=False)
        if features_are_similar(image_1_features, image_2_features):
            yield img_path
