import os
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

feature_dir = './features'
feature_files = os.listdir(feature_dir)

X = []
y = []

TARGET_MFCC_DIM = 13  # 目標のMFCC次元数に統一

for f in feature_files:
    feature_path = os.path.join(feature_dir, f)
    mfcc = np.load(feature_path)
    print(f"{f}: shape={mfcc.shape}")
    
    # MFCC次元をTARGET_MFCC_DIMに変換（切り出しまたはパディング）
    if mfcc.shape[0] > TARGET_MFCC_DIM:
        mfcc = mfcc[:TARGET_MFCC_DIM, :]
    elif mfcc.shape[0] < TARGET_MFCC_DIM:
        # 不足分はゼロパディング
        pad_width = TARGET_MFCC_DIM - mfcc.shape[0]
        mfcc = np.pad(mfcc, ((0, pad_width), (0, 0)), mode='constant')

    mfcc_mean = np.mean(mfcc, axis=1)
    print(f"mfcc_mean shape: {mfcc_mean.shape}")
    X.append(mfcc_mean)
    
    if 'vocals' in f.lower():
        y.append(1)
    else:
        y.append(0)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

joblib.dump(clf, 'svm_model.pkl')
print("モデルを'svm_model.pkl'に保存しました。")
