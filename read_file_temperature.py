import csv
import numpy as np

with open("temperatures.csv", encoding="utf-8-sig", newline="") as file:
    read_file = csv.reader(file, delimiter=",", quotechar='"')
    header_file = next(read_file)

    data_from_file = ["U10", "f4", "f4"]
    all_together = list(zip(header_file, data_from_file))

    data_temp = np.array(
            [tuple(row) for row in read_file],
            dtype=all_together
    )

print(data_temp.dtype.names)
print(data_temp)