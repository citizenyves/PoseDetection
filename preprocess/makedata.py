import os, sys
import pathlib

imgtrainpath = "/Users/taeyeon/recherche/yolopose/images/train2017"
imgvalpath = "/Users/taeyeon/recherche/yolopose/images/val2017"
imgtestepath = "/Users/taeyeon/recherche/yolopose/images/test2017"

lbtrainpath = "/Users/taeyeon/recherche/yolopose/labels/train2017"
lbvalpath = "/Users/taeyeon/recherche/yolopose/labels/val2017"
lbtestepath = "/Users/taeyeon/recherche/yolopose/labels/test2017"

# select task
path = lbvalpath

# read all in list type
imgs = os.listdir(path)

# modification of filenames
newname = []
for img in imgs:
    split = list(img)
    zerochecker = True
    for idx, letter in enumerate(split):
        if letter != '0':
            zerochecker = False
        if zerochecker is False:
            newname.append(''.join(split[idx:]))
            break
for old, new in zip(imgs, newname):
    # images
    # os.rename(f"/Users/taeyeon/recherche/yolopose/images/val2017/{old}", f"/Users/taeyeon/recherche/yolopose/images/val2017/{new}")

    # labels
    os.rename(f"/Users/taeyeon/recherche/yolopose/labels/val2017/{old}", f"/Users/taeyeon/recherche/yolopose/labels/val2017/{new}")


# # read all in list type
# imgs = os.listdir(path)
#
# # write all in a txt file
# f = open("/Users/taeyeon/recherche/yolopose/datasets/val2017.txt", 'w')
# for img in imgs:
#     f.write(f"{path}/{img}\n")
#
# print(f"{len(imgs)} images are written.")