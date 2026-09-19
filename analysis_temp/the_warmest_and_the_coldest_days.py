import numpy as np

from read_file_temperature import read_file

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
where_file = BASE_DIR / "temperatures.csv"

array_temp = read_file(where_file)

warmest_day = np.argmax(array_temp['temperature_day_c'])

coldest_day = np.argmin(array_temp['temperature_night_c'])

date_warmest_day = array_temp["date"][warmest_day]
temp_warmest_day = array_temp['temperature_day_c'][warmest_day]

date_coldest_day = array_temp["date"][coldest_day]
temp_coldest_day = array_temp['temperature_night_c'][coldest_day]

if __name__ == "__main__":
    print("Warmest day index:", warmest_day)
    print("Coldest day index:", coldest_day)
    print("Warmest day temp:", temp_warmest_day, "Date:", date_warmest_day)
    print("Coldest day temp:", temp_coldest_day, "Date:", date_coldest_day)
