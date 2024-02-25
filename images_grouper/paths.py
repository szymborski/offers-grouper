import sys

DUPLICATES_PATH = "duplicates"
IMAGE_FEATURES_PATH = "_features"
MEAN_COLORS_PATH = "_mean_colors.json"
DUPLICATES_RESULT_PATH = "duplicates_result.json"


def get_images_directory():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <images_directory>")
        sys.exit(1)  # Exit the script and indicate error
    return sys.argv[1]
