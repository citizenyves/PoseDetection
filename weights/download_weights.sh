#!/bin/bash
# Download latest models from https://github.com/ultralytics/yolov5/releases
# Usage:
#    $ bash weights/download_weights.sh

python - <<EOF
import sys
file_path = "/Users/taeyeon/recherche/yolopose/edgeai-yolov5-yolo-pose/utils"
sys.path.append(file_path)

from google_utils import attempt_download
#from ./utils.google_utils import attempt_download

for x in ['s', 'm', 'l', 'x', 's6']:
    attempt_download(f'yolov5{x}.pt')

EOF
