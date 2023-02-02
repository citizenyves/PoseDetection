# Le projet de l'initiation de la recherche (Université Sorbonne Paris Nord)

## Pose Detection en utilisant YOLO-pose

### 1. Téléchargement du 'Pre-trained weight files'
- Placez-vous dans le répertoire `./posedetection`</br>
- Exécutez la commande cd-dessous
```
sh download_weights.sh
```
- Vous pouvez dès à présent voir 5 fichiers de weight `yolov5s`, `yolov5m`, `yolov5l`, `yolov5x`, `yolov5s6`

### 2. Test model
```
python test.py --data coco_kpts.yaml --img 640 --conf 0.001 --iou 0.65 --weights "path to the pre-trained ckpt" --kpt-label
```

### 3. Téléchargement des données et ses labels
https://drive.google.com/file/d/18PjeP5896uulWB5d2ySTitqPm_U7O60V/view?usp=share_link

