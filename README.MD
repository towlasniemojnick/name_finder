# Name finder

This is a small app, that collects names from dane.gov.pl, and allows user to search for name of their choice.
It proposes up to 10 random names and indicates which are trending.

The tool downloads the data from years 2025 and 2020.

## Key features

- Normalizes the data, as there is a decline in birth rates.
- Finds out which names are trending.
- Takes user preferences into account Lenght of name and Popularity.

## Architecture
* `src/processor.py`: Handles CSV merging (Inner Join (so only names that appeared both years)) and data calculations.
* `src/main.py`: The user interface. Manages user input, mapping, and result sampling.
* `src/downloader.py`: Access the dane.gov.pl files and places them in data directory
* `data/`: Directory for source government CSV files.


## Methodology
A name is flagged as **Trending (🔥)** if its share increased by more than **25%** over 5 years:

$$Trend = \frac{Share_{2025}}{Share_{2020}} > 1.25$$

Name is considered **Unique**, when Count in 2025 is less than 50

$$Unique = Count 2025 < 50 $$

Name is considered **Popular**, if it reaches the top 30 names in 2025.

Otherwise, name is considered **Common**

## How to run
1. **Environment**
    ```bash
   pip install -r requirements.txt 

2. **Grab the data**: run `src/processor.py`.

3. **Have fun with finder**: `run src/main.py`.