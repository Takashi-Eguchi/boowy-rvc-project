import os
import sys
import numpy as np
import librosa
import soundfile as sf

def trim_silence(y, top_db=30):
    """無音区間を除去"""
    yt, _ = librosa.effects.trim(y, top_db=top_db)
    return yt

def extract_mfcc_mean(filepath, sr=44100, n_mfcc=13):
    y, sr = librosa.load(filepath, sr=sr)
    y = trim_silence(y)  # 無音除去を追加
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean

def main(input_dir):
    output_dir = input_dir.rstrip("/").replace("_wav", "_wav_npy")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(input_dir, filename)
            try:
                mfcc_mean = extract_mfcc_mean(filepath)
                out_path = os.path.join(output_dir, filename + ".npy")
                np.save(out_path, mfcc_mean)
                print(f"保存しました: {out_path}")
            except Exception as e:
                print(f"スキップ: {filename} エラー: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python create_npy_from_wav.py <wavフォルダパス>")
    else:
        main(sys.argv[1])
