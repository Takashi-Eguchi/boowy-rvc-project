# 🎙️ BOØWY RVC Project — CLI-Only Voice Conversion (Kyosuke Himuro 1987)

このプロジェクトは、1987年のBOØWY氷室京介の歌声を学習させて、1982年の曲を氷室の声で再現する「完全CLI・完全オフライン」のRVCプロジェクトです。

## 🔧 環境
- MacBook Air M2（macOS 15.5）
- Python 3.10（仮想環境：rvc_py310）
- WebUI一切使用せず、ターミナルのみ

## 📁 プロジェクト構成
\`\`\`
boowy_project/
├── Retrieval-based-Voice-Conversion-WebUI/     # RVC本体
├── rvc_model/dataset/                          # 音声WAV（非公開）
├── logs/boowy_himuro/                          # 学習ログ（非公開）
├── weights/boowy_himuro.pth                    # 学習済みモデル（非公開）
├── configs/boowy_himuro.json                   # 推論設定ファイル
└── infer_offline.py                            # 推論用スクリプト
\`\`\`

## 🎤 推論コマンド例（完全オフライン）
\`\`\`bash
PYTHONPATH=. python3 infer_offline.py \
  --model_path weights/boowy_himuro.pth \
  --config_path configs/boowy_himuro.json \
  --input_path /Users/user/Desktop/DAKARA/DAKARA-monovocals.wav \
  --output_path output/DAKARA_himuro.wav
\`\`\`

## 🛡️ 注意
- 音声データやモデルファイルはすべて `.gitignore` で除外済み
- 非商用・研究目的で使用中
