import argparse
import glob
import os
import sys
from socket import socket

import joblib
import numpy as np

from aggregate.predict import pre
from cal_module.generate_dataset_svm import get_WD_from_plane

from cal_module.model.GLCM import get_mask, getGlcm, feature_computer

print(sys.path)
sys.path.append("C:\\Users\\perlicue\\.m2\\repository\\org\\python\\jython-standalone\\2.7.1\\Lib\\site-packages")



def normalize(x):
    if np.max(x) - np.min(x) == 0:
        return x
    return (x - np.min(x)) / (np.max(x) - np.min(x))


def generate_feature(nii_dir):
    old_data_file = glob.glob(nii_dir + os.sep + '*.nii.gz')[0]
    data_file = nii_dir + os.sep + 'lymphoma_001_0000.nii.gz'
    label_file = nii_dir + os.sep + 'lymphoma_001.nii.gz'
    if not os.path.exists(data_file):
        os.rename(old_data_file, data_file)
    pre(nii_dir, nii_dir)

    feature = normalize(get_WD_from_plane(label_file))

    data = get_mask(data_file, label_file)
    if data.shape == np.zeros(1).shape:
        return [0, 0, 0, 0]
    glcm = np.zeros((16, 16), dtype=int)
    for i in range(data.shape[2]):
        glcm = glcm + getGlcm(data[:, :, i].astype(int), 1, 0)
    asm, con, eng, idm = feature_computer(glcm)
    result = np.append(feature[:7], [asm, con, eng, idm])
    # print(np.asarray([result]))
    xgboost_model = r'C:\Users\perlicue\PycharmProjects\MHM-Model\aggregate\classifier\XGB_modelglcmAndwd_134_A.pkl'
    clf = joblib.load(xgboost_model)
    out = clf.predict(np.asarray([result]))
    print(out[0])
    return out[0]


if __name__ == '__main__':
    dir = r"C:\Users\perlicue\Desktop\master_lecture\aggregate_engineering\2"
    generate_feature(dir)

