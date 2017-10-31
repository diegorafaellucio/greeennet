#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/diego/Experimentos/Tests/fold$1/data
DATA=/home/diego/Experimentos/Tests/fold$1
TOOLS=/home/diego/frameworks/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
