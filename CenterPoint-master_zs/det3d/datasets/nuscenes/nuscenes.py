import sys
import pickle
import json
import random
import operator
import numpy as np
import os

from functools import reduce
from pathlib import Path
from copy import deepcopy

from torch.utils.data import Dataset
from det3d.datasets.pipelines import Compose
from det3d.datasets.registry import DATASETS

@DATASETS.register_module
class NuScenesDataset(Dataset):
    NumPointFeatures = 5  # x, y, z, intensity, ring_index

    def __init__(
        self,
        root_path,
        nsweeps=0, # here set to zero to catch unset nsweep
        cfg=None,
        pipeline=None,
        class_names=None,
        test_mode=False,
        version="v1.0-trainval",
        **kwargs,
    ):
        self.test_mode = test_mode
        self.pipeline = Compose(pipeline)
        self.nsweeps = nsweeps
        assert self.nsweeps > 0, "At least input one sweep please!"
        print(self.nsweeps)

        self.root_path = root_path
        self.lidar_path = os.path.join(self.root_path,'lidar')
        self.annotation_path = os.path.join(self.root_path,'label')
        self._class_names = class_names

        self._num_point_features = NuScenesDataset.NumPointFeatures
        self.version = version

        self.virtual = kwargs.get('virtual', False)
        if self.virtual:
            self._num_point_features = 16 

        self.single_lidar_path = []
        self.single_annotation_path = []
        self._nusc_infos = []
        #计算训练数据长度
        filelists = os.listdir(self.lidar_path)
        count = 0
        for filename in filelists:
            file_absolute_path = os.path.join(self.lidar_path,filename)
            if not os.path.isdir(file_absolute_path):
                count+=1
                self.single_lidar_path.append(file_absolute_path)
                annotation_absolute_path = os.path.join(self.annotation_path, filename.split('.')[0] + ".json")
                self.single_annotation_path.append(annotation_absolute_path)
                self._nusc_infos.append({'lidar_path': file_absolute_path,'annotation_path':annotation_absolute_path})
        self.data_count = count

    def __len__(self):
        return self.data_count


    def get_sensor_data(self, idx):

        info = self._nusc_infos[idx]

        res = {
            "lidar": {
                "type": "lidar",
                "points": None,
                "nsweeps": self.nsweeps,
                # "ground_plane": -gp[-1] if with_gp else None,
                "annotations": None,
            },
            "metadata": {
                "image_prefix": self.root_path,
                "num_point_features": self._num_point_features,
            },
            "calib": None,
            "cam": {},
            "mode": "val" if self.test_mode else "train",
            "virtual": self.virtual 
        }
        data, _ = self.pipeline(res, info)
        return data

    def __getitem__(self, idx):
        return self.get_sensor_data(idx)
