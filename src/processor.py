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

        df['Is_Trendy'] = df['Trend'] > 1.25

        df['Name_Length'] = df['Name'].apply(lambda x: 'Short' if len(x) <= 5 else 'Long')

        top30_threshold = df['Count25'].nlargest(30).min()

        def categorize(row):
            if row['Count25'] >= top30_threshold:
                return 'Popular'
            elif row['Count25'] < 50:
                return 'Unique'
            else:
                return 'Common'

        df['Popularity'] = df.apply(categorize, axis=1)

        return df

if __name__ == '__main__':
    processor = NameProcessor()
    women = processor.process_names('F')

    print(women)


