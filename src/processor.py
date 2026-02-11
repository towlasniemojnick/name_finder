import pandas as pd
from pathlib import Path

class NameProcessor:
    def __init__(self):
        #find the path
        self.base_dir = Path(__file__).resolve().parent.parent
        self.data_dir = self.base_dir / 'data'

    def process_names(self, gender = 'F'):
        file_2020 = self.data_dir / f'{gender}_2020.csv'
        file_2025 = self.data_dir / f'{gender}_2025.csv'

        df_2020 = pd.read_csv(file_2020, sep=',')
        df_2025 = pd.read_csv(file_2025, sep=',')

        df_2020.columns = ['Name', 'Gender', 'Count20']
        df_2025.columns = ['Name', 'Gender', 'Count25']

        df = df_2020.merge(df_2025[['Name','Count25']], how='inner', on='Name')

        total_2020 = df['Count20'].sum()
        total_2025 = df['Count25'].sum()

        df['Share20'] = df['Count20'] / total_2020
        df['Share25'] = df['Count25'] / total_2025

        df['Trend'] = df['Share25'] / df['Share20']

        print(df.head(50))


if __name__ == '__main__':
    processor = NameProcessor()
    processor.process_names()


