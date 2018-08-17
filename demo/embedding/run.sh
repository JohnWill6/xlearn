#!/bin/bash

num_fields=40
train_data="train.txt"
valid_data="valid.txt"

# 1. train model -> train.txt.model
./xlearn_train ${train_data} -v ${valid_data} -s 2 -k 4 -e 50

# 2. feature transform -> valid.txt.out
./xlearn_embedding ${train_data} ${train_data}.model

# 3. feature select
# 3.1 reindex field
cat ${valid_data}.out | python reindex.py ${num_fields} > ${valid_data}.emb
rm ${valid_data}.out

# 3.2 L1-LR(liblinear)
./train -s 6 -c 0.02 ${valid_data} lr.txt
python gen_fea.py ${num_fields} lr.txt
