import json
from typing import List, Dict

from file_utils import get_images_in_nested_directories
from image_model import get_similar_images, load_model
from paths import get_images_directory, DUPLICATES_RESULT_PATH
from mean_colors_preparer import get_mean_colors_map, similar_mean_color


class ImagesGrouper:
    def __init__(self, model, paths: List[str], mean_colors_map: Dict[str, List[int]]):
        self.model = model
        self.paths = paths
        self.mean_colors_map = mean_colors_map

    def get_duplicates(self):
        duplicates = {}
        for path in self.paths:
            similar_images = self.get_duplicates_for_path(path)
            if similar_images:
                duplicates[path] = similar_images
        return duplicates

    def get_duplicates_for_path(self, path: str) -> List[str]:
        return list(
            get_similar_images(
                model=self.model,
                img_path=path,
                img_paths_list=self.get_paths_to_check(path),
            )
        )

    def get_paths_to_check(self, path: str):
        for _path in self.paths:
            if path == _path:
                continue
            color_1 = self.mean_colors_map[path]
            color_2 = self.mean_colors_map[_path]
            if similar_mean_color(color_1, color_2):
                yield _path


if __name__ == "__main__":
    try:
        mean_colors_map = get_mean_colors_map()
    except FileNotFoundError:
        raise FileNotFoundError(
            "mean_colors.json not found. Please run mean_colors_preparer.py first."
        )

    images_path = get_images_directory()

    model = load_model()
    images = list(get_images_in_nested_directories(images_path))

    grouper = ImagesGrouper(model=model, paths=images, mean_colors_map=mean_colors_map)
    duplicates = grouper.get_duplicates()

    with open(DUPLICATES_RESULT_PATH, "w") as file:
        json.dump(duplicates, file, indent=4)
