#!/usr/bin/env sh
set -e

echo $1

/home/diego/frameworks/caffe/build/tools/caffe train --solver=/home/diego/Experimentos/Tests/fold$1/models/solver.prototxt