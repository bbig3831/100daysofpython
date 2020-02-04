import os
import csv
from collections import namedtuple

data = []

Record = namedtuple(
    'Record',
'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,'
'average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,'
'record_max_temp_year,actual_precipitation,average_precipitation,'
'record_precipitation'
)

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)

def parse_row(row):
    int_cols = ['actual_mean_temp','actual_min_temp','actual_max_temp','average_min_temp',
                'average_max_temp','record_min_temp','record_max_temp','record_min_temp_year',
                'record_max_temp_year']
    float_cols = ['actual_precipitation','average_precipitation','record_precipitation']
    for col in int_cols:
        row[col] = int(row[col])

    for col in float_cols:
        row[col] = float(row[col])

    record = Record(**row)
    return record

def hot_days():
    return sorted(data, key=lambda r: r.actual_max_temp, reverse=True)

def cold_days():
    return sorted(data, key=lambda r: r.actual_max_temp)

def wet_days():
    return sorted(data, key=lambda r: r.actual_precipitation, reverse=True)