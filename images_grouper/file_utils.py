import os


def get_images_in_nested_directories(directory, extensions=("jpg", "jpeg", "webp")):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                yield os.path.join(root, file)
