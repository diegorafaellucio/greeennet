#!/usr/bin/env sh

for i in 1 2 3 4 5 6 7 8 9 10
do
  echo "create imagenet to fold$i"
  ./create_imagenet.sh $i
  ./make_imagenet_mean.sh $i
  ./train_caffenet.sh $i
done