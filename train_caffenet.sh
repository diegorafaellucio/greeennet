#!/usr/bin/env sh
set -e

echo $1

/home/diego/caffe/build/tools/caffe train  --gpu=4 --solver=/home/diego/Experimentos/Tests/fold$1/models/solver.prototxt
