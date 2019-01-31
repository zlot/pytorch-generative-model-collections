#!/usr/bin/bash

pip install imageio
pip install scipy
pip install numpy
pip install matplotlib

mkdir -p /storage/${MY_DRIVE}/models/gan/
mkdir -p /storage/${MY_DRIVE}/datasets/fashion-mnist/
mkdir -p /storage/${MY_DRIVE}/results/gan/

# train
python main.py --gan_type BEGAN --dataset fashion-mnist --epoch 50 --batch_size 64 --result_dir /storage/${MY_DRIVE}/results/gan/
