#!/bin/bash
# BOØWY RVC - Offline Inference for DAKARA
PYTHONPATH=. python3 infer_offline.py \
  --model_path weights/boowy_himuro.pth \
  --config_path configs/boowy_himuro.json \
  --input_path /Users/user/Desktop/DAKARA/DAKARA-monovocals.wav \
  --output_path output/DAKARA_himuro.wav
