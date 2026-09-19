import numpy as np

from read_file_temperature import read_file

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
where_file = BASE_DIR / "temperatures.csv"

array_temp = read_file(where_file)
# print(array_temp.dtype.names)
# print(array_temp)
total_amount_days = array_temp.size

max_temp_day = np.max(array_temp['temperature_day_c'])

min_temp_night = np.min(array_temp['temperature_night_c'])

average_temp_day = np.mean(array_temp['temperature_day_c'])

average_temp_night = np.mean(array_temp['temperature_night_c'])

median_temp_day = np.median(array_temp['temperature_day_c'])

median_temp_night = np.median(array_temp['temperature_night_c'])

sum_temp_day = np.sum(array_temp['temperature_day_c'])

sum_temp_night = np.sum(array_temp['temperature_night_c'])

if __name__ == "__main__":
    print(f"Total amount days: {total_amount_days}")
    print(f"Max day temperature: {max_temp_day}")
    print(f"Min night temperature: {min_temp_night}")
    print(f"Average days temperature: {average_temp_day:.2f}")
    print(f"Average nights temperature: {average_temp_night:.2f}")
    print(f"Median day temperature: {median_temp_day}")
    print(f"Median night temperature: {median_temp_night}")
    print(f"Sum day temperature: {sum_temp_day}")
    print(f"Sum night temperature: {sum_temp_night}")
