import csv
import numpy as np


def read_file(file_for_read: str) -> np.ndarray:
    with open(file_for_read, encoding="utf-8-sig", newline="") as file:
        read_file = csv.reader(file, delimiter=",", quotechar='"')
        header_file = next(read_file)

        data_from_file = ["U10", "f4", "f4"]
        all_together = list(zip(header_file, data_from_file))

        data_temp = np.array(
            [tuple(row) for row in read_file],
            dtype=all_together
        )
    return data_temp


if __name__ == "__main__":
    read_f = read_file(r"temperatures.csv")
    print(read_f.dtype.names)
    print(read_f)
