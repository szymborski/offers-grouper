import json

import cv2
import numpy as np

from file_utils import get_images_in_nested_directories
from paths import get_images_directory, MEAN_COLORS_PATH


def get_mean_color_for_image(image_path):
    img = cv2.imread(image_path)
    mean_color = cv2.mean(img)

    return mean_color


def similar_mean_color(mean_color1, mean_color2, threshold=10):
    color_distance = np.linalg.norm(np.array(mean_color1) - np.array(mean_color2))

    return color_distance < threshold


def prepare_mean_colors_file(images_path: str):
    path_to_color = {}
    for img_path in get_images_in_nested_directories(images_path):
        mean_color = get_mean_color_for_image(img_path)
        path_to_color[img_path] = mean_color
    with open(MEAN_COLORS_PATH, "w") as file:
        json.dump(path_to_color, file, indent=4)


def get_mean_colors_map():
    with open(MEAN_COLORS_PATH) as file:
        return json.load(file)


if __name__ == "__main__":
    images_path = get_images_directory()
    prepare_mean_colors_file(images_path)
