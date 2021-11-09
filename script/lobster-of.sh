#!/usr/bin/bash

echo hello-world

python ./projection_to_sino.py \
    -f ./lobster-projection/lobster-diff-norm-1024to2048-uint16_512x512x512.raw \
    -o ./lobster-sinogram/lobster-diff-norm-1024to2048-uint16

python ./projection_to_sino.py \
    -f ./lobster-projection/lobster-horn-shunck-1024to2048-uint16_512x512x512.raw \
    -o ./lobster-sinogram/lobster-horn-shunck-1024to2048-uint16