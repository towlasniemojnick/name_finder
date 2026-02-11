import requests
from pathlib import Path

def download_csv(filename, url):
    current_dir = Path(__file__).resolve().parent

    data_dir = current_dir.parent / 'data'
    data_dir.mkdir(exist_ok=True)

#define the target path

    if not filename.endswith('.csv'):
        filename += '.csv'

    target_path = data_dir / filename

    try:
        print(f'Downloading {filename}')
#try to connect
        response = requests.get(url)
        response.raise_for_status()

#save the file in target location
        with open(target_path, 'wb') as f:
            f.write(response.content)

        print('Download complete')
        return target_path

#exception handling
    except requests.exceptions.HTTPError as errh:

        error_response = errh.response
        status_code = error_response.status_code
        reason = error_response.reason

        print(f"Error: {status_code} - {reason}")

    except requests.exceptions.RequestException as err:

        print(f"Error: Could not fetch data for {url}.")


if __name__ == '__main__':

    file_download_dict = {'M_2025': 'https://api.dane.gov.pl/resources/1159536,imiona-meskie-nadane-dzieciom-w-polsce-w-2025-r-imie-pierwsze/csv',
                          'M_2020': 'https://api.dane.gov.pl/resources/28020,imiona-meskie-nadane-dzieciom-w-polsce-w-2020-r-imie-pierwsze/csv',
                          'F_2025': 'https://api.dane.gov.pl/resources/1159538,imiona-zenskie-nadane-dzieciom-w-polsce-w-2025-r-imie-pierwsze/csv',
                          'F_2020': 'https://api.dane.gov.pl/resources/28021,imiona-zenskie-nadane-dzieciom-w-polsce-w-2020-r-imie-pierwsze/csv'}


    for filename, url in file_download_dict.items():
        download_csv(filename, url)