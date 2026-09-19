from pathlib import Path

import numpy as np

from read_file_temperature import read_file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
where_file = BASE_DIR / "temperatures.csv"

array_temp = read_file(where_file)

days_30_or_more = array_temp[array_temp['temperature_day_c'] >= 30]
count_30_or_more = np.sum(array_temp['temperature_day_c'] >= 30)

night_less_3 = array_temp[array_temp['temperature_night_c'] < -3]
count_night_less_3 = np.sum(array_temp['temperature_night_c'] < -3)

days_25_or_more = array_temp[array_temp['temperature_day_c'] >= 25]
count_25_or_more = np.sum(array_temp['temperature_day_c'] >= 25)

night_from_negative_1_to_1 = array_temp[
    (array_temp['temperature_night_c'] >= -1) & (array_temp['temperature_night_c'] <= 1)]
count_night_from_negative_1_to_1 = np.sum(
    (array_temp['temperature_night_c'] >= -1) & (array_temp['temperature_night_c'] <= 1))

if __name__ == "__main__":
    print("Count 30 or more:", count_30_or_more)
    print(days_30_or_more)
    print("Count 25 or more:", count_25_or_more)
    print(days_25_or_more)
    print("Night temp between -1 and 1:", count_night_from_negative_1_to_1)
    print(night_from_negative_1_to_1)
