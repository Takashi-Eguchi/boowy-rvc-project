#!/bin/bash
# BOØWY RVC - Generic CLI Inference with Logging

INPUT=$1
OUTPUT=$2

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: $0 <input_wav> <output_wav>"
  exit 1
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOGFILE="logs/infer_$TIMESTAMP.log"

echo "🔁 Starting inference..." | tee "$LOGFILE"
echo "Input : $INPUT" | tee -a "$LOGFILE"
echo "Output: $OUTPUT" | tee -a "$LOGFILE"

PYTHONPATH=. python3 Retrieval-based-Voice-Conversion-WebUI/infer_offline.py \
  --model_path weights/boowy_himuro.pth \
  --config_path configs/boowy_himuro.json \
  --input_path "$INPUT" \
  --output_path "$OUTPUT" 2>&1 | tee -a "$LOGFILE"

echo "✅ Inference completed. Log saved to $LOGFILE"
