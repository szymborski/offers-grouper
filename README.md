# Images Association Tool

## Overview
This project aims to identify duplicate images using Python, OpenCV and scikit-image. 
The main goal is to group similar images from different sources, such as different websites or databases, to avoid showing the same offer to the user more than once and to associate a new offer with the old one.

For example, different housing portals use different watermarks in their images, so the same image can be treated as different. This tool can help to group them together.

## Features
- Duplicate detection using feature matching.
- Efficient processing for large image datasets thanks to color-comparison heuristics.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher

## Quickstart


```bash
git clone https://github.com/szymborski/offers-grouper.git
cd offers-grouper
pip install -r requirements.txt
cd images_grouper
python mean_colors_preparer.py images
python main.py images
cat duplicates_results.json
```

First run is the slowest one, because algorithm needs to prepare image features for further use.
