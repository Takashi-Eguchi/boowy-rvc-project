import numpy as np
import librosa
import joblib
import sys

# コマンドライン引数で判定したいファイルパスを受け取る
if len(sys.argv) != 2:
    print("使い方: python predict_vocal.py 判定したい音声ファイル.wav")
    sys.exit(1)

audio_path = sys.argv[1]

# モデル読み込み
model = joblib.load('svm_model.pkl')

# 音声読み込み
y, sr = librosa.load(audio_path, sr=None)

# MFCC抽出（13次元）
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# MFCC平均ベクトルに変換
mfcc_mean = np.mean(mfcc, axis=1)

# 予測（1:ボーカル, 0:ボーカル以外）
pred = model.predict([mfcc_mean])[0]

if pred == 1:
    print(f"{audio_path} はボーカル音声と判定されました。")
else:
    print(f"{audio_path} はボーカル音声ではないと判定されました。")
