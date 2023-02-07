import os
import json

path = "/Users/taeyeon/recherche/yolopose/labels/annotations/person_keypoints_val2017.json"
txtpath = "/Users/taeyeon/recherche/yolopose/labels/val2017"

with open(path, "r", encoding="utf8") as f:
    data = f.read() # string 타입
    dict = json.loads(data)

annos = dict['annotations']
ids = list(set([anno['image_id'] for anno in annos]))

annobyid = {id:[] for id in ids}
for anno in annos:
    id = anno['image_id']
    kpt = anno['keypoints']
    annobyid[id].append(kpt)

# make txt files
for id, kpts in annobyid.items():
    f = open(f"{txtpath}/{id}.txt", 'w')
    for kpt in kpts:
        f.write("0 ")
        for point in kpt:
            f.write(f"{point} ")
        f.write("\n")
    f.close()


# # (!) after removing the .Ds store file
# # remove null annotations
# for file in os.listdir(txtpath):
#     with open(f"/Users/taeyeon/recherche/yolopose/labels/val2017/{file}", 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     with open(f"/Users/taeyeon/recherche/yolopose/labels/val2017/{file}", 'w') as f:
#         for line in lines:
#             if line != '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n':
#                 f.write(line)


