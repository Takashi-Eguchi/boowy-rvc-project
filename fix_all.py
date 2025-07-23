import os
import unicodedata
import json

folder = "logs/boowy_himuro"
filelist_path = os.path.join(folder, "filelist_fixed.txt")
config_path = os.path.join(folder, "config.json")

# 1. ファイル名の不可視文字除去＆正規化してリネーム＆リスト作成
fixed_files = []
for filename in sorted(os.listdir(folder)):
    if filename.endswith(".wav"):
        safe_name = "".join(c for c in filename if c.isprintable())
        safe_name = unicodedata.normalize("NFKC", safe_name)
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, safe_name)
        if old_path != new_path:
            os.rename(old_path, new_path)
        fixed_files.append(safe_name)

# 2. filelist_fixed.txt を作成
with open(filelist_path, "w", encoding="utf-8") as f:
    for name in fixed_files:
        path = os.path.join(folder, name)
        f.write(f"{path}\taa\tboowy\n")  # テキストは適当に "aa" にしてあります

print(f"filelist_fixed.txtを作成しました：{filelist_path}")

# 3. config.json の training_files を書き換え
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

config["training_files"] = filelist_path

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print(f"config.jsonのtraining_filesを更新しました：{config_path}")
