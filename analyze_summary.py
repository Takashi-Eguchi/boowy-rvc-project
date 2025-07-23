import pandas as pd

def main():
    df = pd.read_csv('./batch_results.csv', encoding='utf-8-sig')

    total_files = len(df)
    vocal_count = df[df['prediction'] == 1].shape[0]
    nonvocal_count = total_files - vocal_count
    avg_confidence = df['confidence'].mean()

    print(f"全ファイル数: {total_files}")
    print(f"ボーカル判定ファイル数: {vocal_count}")
    print(f"非ボーカル判定ファイル数: {nonvocal_count}")
    print(f"信頼度（confidence）平均値: {avg_confidence:.3f}")

    summary = pd.DataFrame({
        '項目': ['全ファイル数', 'ボーカル判定数', '非ボーカル判定数', '平均信頼度'],
        '値': [total_files, vocal_count, nonvocal_count, avg_confidence]
    })
    summary.to_csv('./summary_report.csv', index=False, encoding='utf-8-sig')
    print("集計結果をsummary_report.csvに保存しました。")

if __name__ == "__main__":
    main()
