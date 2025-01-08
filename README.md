## Spatial-Texture Hybrid MRI Model &mdash; Official PyTorch Implementation

![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg?style=plastic) ![PyTorch 2.5.1](https://img.shields.io/badge/pytorch-2.5.1-green.svg?style=plastic) ![License MIT](https://img.shields.io/github/license/zhangzjn/APB2Face)

Official pytorch implementation of the paper "Spatial-Texture Hybrid MRI Model for Orbital Lymphoma Typing".
## What is STHM-Model
The project aims to develop a hybrid model leveraging MRI scans to discern between MALT and non-MALT types of orbital lymphomas. 
Unlike other regions of the human body, the anatomical structure and positional information of tissues around the eye are highly distinct. The occupation of the tumor alters the relative positions of structures in the tissue surrounding the eye, hence for the first time, we extracted the relative spatial positional features between different structures and the tumor (representing global-scale features), complemented by the texture characteristics of the tumor area (representing local-scale features), to perform modeling.
## Using the Code

### Requirements

This code has been developed under `Python3.10`, `PyTorch 2.5.1` and `CUDA 11.8` on `Windows/Ubantu`. 


```shell
# Install python3 packages
pip3 install -r requirements.txt
```

### Datasets in the paper
- Only feature data extracted from segmentation is available in directory [calculation/data]


### Segmentation Model
1. Experiment planning and preprocessing.

   ```shell
   nnUNet_plan_and_preprocess -D DATASET_ID --verify_dataset_integrity
   ```
2. Train `3D Unet` model.
   ```shell
   nnUNet_train 3d_fullres nnUNetTrainerV2 FOLD --val --npz
   ```

2. Test prediction model.

   ```shell
   nnUNet_predict -i INPUT_FOLDER -o OUTPUT_FOLDER -d DATASET_NAME_OR_ID -c CONFIGURATION --save_probabilities
   ```

### Classification model
1. Train and test XGBoost model.

   ```shell
   python3 classifier1.py
   ```

2. Train and test SVM model.

   ```shell
   python3 classifier2.py
   ```




### Acknowledgements

We thank for the source code from the great work [nnUNet](https://github.com/MIC-DKFZ/nnUNet).
