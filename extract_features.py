import os
import numpy as np
import librosa

audio_dir = './1987_full_wav'
feature_dir = './features'

if not os.path.exists(feature_dir):
    os.makedirs(feature_dir)

# 拡張子を.wavと.mp3の両方に対応させる
wav_files = [f for f in os.listdir(audio_dir) if f.lower().endswith(('.wav', '.mp3'))]

for wav_file in wav_files:
    wav_path = os.path.join(audio_dir, wav_file)
    y, sr = librosa.load(wav_path, sr=None)  # mp3も読み込み可能
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    feature_path = os.path.join(feature_dir, wav_file + '.npy')
    np.save(feature_path, mfcc)
    print(f"特徴量保存: {feature_path}")

print("全ファイルの特徴量抽出が完了しました。")
