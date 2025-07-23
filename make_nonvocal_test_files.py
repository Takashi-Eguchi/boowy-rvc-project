import numpy as np
import soundfile as sf
import os

out_dir = './nonvocals'
os.makedirs(out_dir, exist_ok=True)

sr = 44100
duration = 5  # 秒

# 無音
silence = np.zeros(int(sr * duration))
sf.write(os.path.join(out_dir, 'silence_test.wav'), silence, sr)

# ホワイトノイズ（小さめ振幅）
noise = (np.random.randn(int(sr * duration)) * 0.02).astype(np.float32)
sf.write(os.path.join(out_dir, 'noise_test.wav'), noise, sr)

print("非ボーカルテストファイル生成: silence_test.wav, noise_test.wav")
