#!/usr/bin/env sh
set -e

/home/diego/caffe/build/tools/caffe train \
    --solver=/home/diego/caffe/build/tools/caffemodels/bvlc_reference_caffenet/solver.prototxt \
    --snapshot=/home/diego/caffe/build/tools/caffemodels/bvlc_reference_caffenet/caffenet_train_10000.solverstate.h5 \
$@
