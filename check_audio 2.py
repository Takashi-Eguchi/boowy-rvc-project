import pandas as pd

# 予測結果ファイル
pred_file = './batch_results.csv'
# 正解ラベルファイル
label_file = './labels.csv'

def main():
    # 予測結果読み込み
    df_pred = pd.read_csv(pred_file)
    # 正解ラベル読み込み
    df_label = pd.read_csv(label_file)
    
    # 正解ラベルが0のファイルを抽出
    label0_files = df_label[df_label['label'] == 0]['filename'].tolist()
    
    # 予測結果からラベル0のファイルの行を抽出
    df_label0_pred = df_pred[df_pred['filename'].isin(label0_files)]
    
    # ラベル0のファイルのpredictionとconfidenceを表示
    if df_label0_pred.empty:
        print("ラベル0のファイルは予測結果に存在しません。ファイル名の不一致等を確認してください。")
    else:
        print("ラベル0のファイルの予測結果一覧:")
        print(df_label0_pred[['filename', 'prediction', 'confidence']])
    
if __name__ == '__main__':
    main()
