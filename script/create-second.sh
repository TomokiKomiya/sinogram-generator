#!/usr/bin/bash

echo hello-world-second

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-26624_27648-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-26624_27648-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-27648_28672-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-27648_28672-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-28672_29696-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-28672_29696-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-29696_30720-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-29696_30720-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-30720_31744-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-30720_31744-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-31744_32768-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-31744_32768-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-32768_33792-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-32768_33792-uint16

python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-33792_34816-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-33792_34816-uint16