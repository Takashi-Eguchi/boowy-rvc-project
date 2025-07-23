#!/bin/bash
# Generic CLI inference script for any input/output

INPUT=$1
OUTPUT=$2

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: $0 <input_wav> <output_wav>"
  exit 1
fi

PYTHONPATH=. python3 infer_offline.py \
  --model_path weights/boowy_himuro.pth \
  --config_path configs/boowy_himuro.json \
  --input_path "$INPUT" \
  --output_path "$OUTPUT"
