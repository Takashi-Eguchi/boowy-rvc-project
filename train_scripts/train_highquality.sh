#!/bin/bash
# BOØWY RVC - High Quality Training Script
PYTHONPATH=. python3 infer/modules/train/train_nsf_sim_cache_sid_load_pretrain.py \
  -e boowy_himuro \
  -sr 44100 \
  -bs 4 \
  -lr 1e-4 \
  --cache_all_data \
  --save_every_epoch 50 \
  --epochs 1000 > train_highquality.log 2>&1 &
