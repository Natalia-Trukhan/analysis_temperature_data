
import numpy as np

from analysis_temp.analysis_warm_and_cold_days import (
    total_days_in_day_30_and_more,
    total_days_temp_less_zero_in_night,
)
from analysis_temp.total_statistic import (
    average_temp_day,
    average_temp_night,
    max_temp_day,
    min_temp_night,
    sum_temp_day,
    sum_temp_night,
    total_amount_days,
)

array_data = [
    ("min_night_temperature", min_temp_night),
    ("max_day_temperature", max_temp_day),
    ("mean_day_temperature", round(average_temp_day, 2)),
    ("mean_night_temperature", round(average_temp_night, 2)),
    ("sum_day_temperature", sum_temp_day),
    ("sum_night_temperature", sum_temp_night),
    ("days_count", total_amount_days),
    ("below_zero_nights", total_days_temp_less_zero_in_night),
    ("at_or_above_30_days", total_days_in_day_30_and_more),
]

data_temp = np.array(array_data, dtype=[("metric", "U30"), ("Value", "U30")])

tsv_filename = "temperature_metrics.tsv"

np.savetxt(
    tsv_filename,
    data_temp,
    comments="",
    fmt="%s\t%s",
    delimiter="\t",
    header="metric\tvalue",
)

print(f"File {tsv_filename} created successfully!")