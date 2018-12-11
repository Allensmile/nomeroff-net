import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

class NNNET:
    def __init__(self, config):
        self.MASK_RCNN_DIR = os.path.abspath(config["MASK_RCNN"]["DIR"])
        self.ROOT = os.path.abspath(config["LIB"]["ROOT"])
        self.LOG_DIR = os.path.join(self.ROOT, config["NN"]["LOG_DIR"])
        self.MODEL_PATH = os.path.join(self.ROOT, config["NN"]["MODEL_PATH"])

        self.CLASS_NAMES = config["NN"]["CLASS_NAMES"]
        self.NN_MASK_RCNN_CONFIG = config["NN_MASK_RCNN_CONFIG"]

    def loadModel(self):
        sys.path.append(self.MASK_RCNN_DIR)
        sys.path.append(self.ROOT)

        import mrcnn.model as modellib
        from lib.NN_Mask_RCNN import InferenceConfig

        config = InferenceConfig(self.NN_MASK_RCNN_CONFIG)
        self.MODEL = modellib.MaskRCNN(mode="inference", model_dir=self.LOG_DIR, config=config)
        self.MODEL.load_weights(self.MODEL_PATH, by_name=True)

    def detect(self, image_paths, verbose = 0):
        images = [skimage.io.imread(image_path) for image_path in image_paths]
        return self.MODEL.detect(images, verbose=verbose)