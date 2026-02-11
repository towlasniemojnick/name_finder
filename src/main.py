from processor import NameProcessor

def main():
    print('Hello, welcome to the name finder.')
    print('If you have no good idea for a Polish name, that is understandable.')
    print('We are here to give you some inspiration.')

    print("========================================")

    def get_user_choice(prompt, options):
        while True:
            choice = input(prompt).strip().upper()
            if choice in options:
                return choice
            else:
                print(f'Please enter a valid option: {options}')
    #let's get your preferences
    gender = get_user_choice('A boy(M) or a girl (F)? ', ['M', 'F'])
    length = get_user_choice('Name should be Short (S) or Long (L)? ', ['S', 'L'])
    popularity = get_user_choice('Do you prefer Unique (U), Popular (P) or Common (C)? ', ['U', 'P', 'C'])

    proc = NameProcessor()
    df = proc.process_names(gender=gender)

    gender_map = {'F': 'Girl', 'M': 'Boy'}
    length_map = {'S': 'Short', 'L': 'Long'}
    popularity_map = {'P': 'Popular', 'U': 'Unique', 'C': 'Common'}

    mask = (df['Name_Length'] == length_map[length]) & (df['Popularity'] == popularity_map[popularity])
    results = df[mask].copy()

    if results.empty:
        print('No results found.')

    else:
        results['Display_Name'] = results.apply(
            lambda row: f"{row['Name']} 🔥" if row['Is_Trendy'] else row['Name'],
            axis=1)
        num = min(len(results), 10)

        result_list = results.sample(num)

        print(f"--- {num} random proposals: {gender_map[gender]}, {length_map[length]}, {popularity_map[popularity]} ---")
        print("(🔥 are trendy names!)")

        print(result_list[['Display_Name', 'Count25', 'Trend']].to_string(index=False,
                                                                         header=['Name', 'Count (2025)', 'Trend']))

if __name__ == '__main__':
    main()
    
