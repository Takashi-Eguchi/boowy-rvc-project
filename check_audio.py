import os
import librosa
import matplotlib.pyplot as plt

# 1987年ボーカル抽出済みWAVが入ったディレクトリパスを設定
audio_dir = './1987_vocal_wav'

# ファイルリスト取得（wavファイルのみ）
wav_files = [f for f in os.listdir(audio_dir) if f.lower().endswith('.wav')]

if not wav_files:
    print("WAVファイルが見つかりません。audio_dirのパスとファイルを確認してください。")
    exit()

print(f"{len(wav_files)}個のWAVファイルを検出。最初のファイルを読み込みます。")

# 最初のファイル読み込み
wav_path = os.path.join(audio_dir, wav_files[0])
y, sr = librosa.load(wav_path, sr=None, mono=True)  # sr=Noneで元のサンプリングレート保持

print(f"ファイル名: {wav_files[0]}")
print(f"サンプルレート: {sr}")
print(f"オーディオ長さ: {len(y)/sr:.2f}秒")

# 波形プロット
plt.figure(figsize=(14, 5))
plt.title(f"Waveform of {wav_files[0]}")
plt.plot(y)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
import os
import librosa
import matplotlib.pyplot as plt

# 1987年ボーカル抽出済みWAVが入ったディレクトリパスを設定
audio_dir = './1987_vocal_wav'

# ファイルリスト取得（wavファイルのみ）
wav_files = [f for f in os.listdir(audio_dir) if f.lower().endswith('.wav')]

if not wav_files:
    print("WAVファイルが見つかりません。audio_dirのパスとファイルを確認してください。")
    exit()

print(f"{len(wav_files)}個のWAVファイルを検出。最初のファイルを読み込みます。")

# 最初のファイル読み込み
wav_path = os.path.join(audio_dir, wav_files[0])
y, sr = librosa.load(wav_path, sr=None, mono=True)  # sr=Noneで元のサンプリングレート保持

print(f"ファイル名: {wav_files[0]}")
print(f"サンプルレート: {sr}")
print(f"オーディオ長さ: {len(y)/sr:.2f}秒")

# 波形プロット
plt.figure(figsize=(14, 5))
plt.title(f"Waveform of {wav_files[0]}")
plt.plot(y)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
import os
import librosa
import matplotlib.pyplot as plt

# 1987年ボーカル抽出済みWAVが入ったディレクトリパスを設定
audio_dir = './1987_vocal_wav'

# ファイルリスト取得（wavファイルのみ）
wav_files = [f for f in os.listdir(audio_dir) if f.lower().endswith('.wav')]

if not wav_files:
    print("WAVファイルが見つかりません。audio_dirのパスとファイルを確認してください。")
    exit()

print(f"{len(wav_files)}個のWAVファイルを検出。最初のファイルを読み込みます。")

# 最初のファイル読み込み
wav_path = os.path.join(audio_dir, wav_files[0])
y, sr = librosa.load(wav_path, sr=None, mono=True)  # sr=Noneで元のサンプリングレート保持

print(f"ファイル名: {wav_files[0]}")
print(f"サンプルレート: {sr}")
print(f"オーディオ長さ: {len(y)/sr:.2f}秒")

# 波形プロット
plt.figure(figsize=(14, 5))
plt.title(f"Waveform of {wav_files[0]}")
plt.plot(y)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()

