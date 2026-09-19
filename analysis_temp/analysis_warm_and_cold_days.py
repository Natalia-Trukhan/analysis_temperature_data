import numpy as np

from read_file_temperature import read_file

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
where_file = BASE_DIR / "temperatures.csv"

array_temp = read_file(where_file)
total_days_temp_less_zero_in_night = np.sum(array_temp['temperature_night_c'] < 0)

conditions = (array_temp['temperature_day_c'] > 0) & (array_temp['temperature_day_c'] <= 9)
total_days_in_day_from_0_to_9 = np.sum(conditions)

conditions_2 = (array_temp['temperature_day_c'] > 10) & (array_temp['temperature_day_c'] <= 19)
total_days_in_day_from_10_to_19 = np.sum(conditions_2)

conditions_3 = (array_temp['temperature_day_c'] > 20) & (array_temp['temperature_day_c'] <= 29)
total_days_in_day_from_20_to_29 = np.sum(conditions_3)

total_days_in_day_30_and_more = np.sum(array_temp['temperature_day_c'] >= 30)

if __name__ == "__main__":
    print("Night temp below 0:", total_days_temp_less_zero_in_night)
    print("Day temp 0 to 9:", total_days_in_day_from_0_to_9)
    print("Day temp 10 to 19:", total_days_in_day_from_10_to_19)
    print("Day temp 20 to 29:", total_days_in_day_from_20_to_29)
    print("Day temp 30 and above:", total_days_in_day_30_and_more)
