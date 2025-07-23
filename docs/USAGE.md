# 📘 USAGE - BOØWY RVC CLI Project

## 🎯 プロジェクト概要

Retrieval-based Voice Conversion (RVC) を使って、1987年のBOØWY氷室京介の歌声を学習し、CLIのみで1982年の楽曲を再現。完全オフライン環境・Mac対応・WebUI非使用。

---

## 💻 推論（音声変換）

```bash
bash infer_scripts/infer_generic.sh 入力ファイル.wav 出力ファイル.wav
```

例：
```bash
bash infer_scripts/infer_generic.sh \
  /Users/user/Desktop/DAKARA/DAKARA-monovocals.wav \
  output/DAKARA_himuro.wav
```

---

## 🛠️ 学習（モデル再学習）

```bash
bash train_scripts/train_highquality.sh
```

---

## 📁 フォルダ構成（抜粋）

- `train_scripts/`：学習スクリプト
- `infer_scripts/`：推論スクリプト
- `configs/`：推論設定
- `docs/USAGE.md`：この使い方マニュアル

---

## 🔒 注意事項

- `.gitignore` により音声・モデルファイルは含まれていません
- 本プロジェクトは非商用・研究目的です
