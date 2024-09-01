import pandas as pd

# エクセルファイルからデータを読み込み（ファイルパスを指定してください）
file_path = 'your_excel_file.xlsx'  # エクセルファイルのパスに置き換えてください
df = pd.read_excel(file_path)

# 列をアルファベット順に並べ替え
sorted_columns_df = df.reindex(sorted(df.columns), axis=1)

# 並べ替えたデータフレームを表示
print(sorted_columns_df)

# 並べ替えた結果を別のエクセルファイルに保存したい場合
sorted_columns_df.to_excel('sorted_excel_file.xlsx', index=False)
