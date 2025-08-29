import pandas as pd
import sys
import os

def convert(csv_file='data.csv', excel_file='data.xlsx'):
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(csv_file, encoding='cp1251')  # fallback
    df.to_excel(excel_file, index=False)
    print(f'Сохранено в {excel_file}')

if __name__ == '__main__':
    convert()