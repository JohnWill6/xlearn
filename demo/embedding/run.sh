#!/bin/bash

num_fields=40
train_data="train.txt"
valid_data="valid.txt"

# feature interaction white list
python gen_map.py ${num_fields} > fea.init  # 默认任意交叉

# 1. train model -> train.txt.model
./xlearn_train ${train_data} -v ${valid_data} -s 2 -k 4 -e 50

# 2. feature transform -> valid.txt.out
./xlearn_embedding ${train_data} ${train_data}.model

# 3. feature select
./train -s 6 -c 0.02 ${valid_data}.out lr.txt
python gen_fea.py ${num_fields} lr.txt fea.init
