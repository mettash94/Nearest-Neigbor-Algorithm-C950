import csv
from typing import List

from hashTable import HashMap
from package_model import Package

# Create object of hashmap class
hash_Instance = HashMap();

# Read the data from csv files

with open('package_data2.csv') as csvfile:
    CSV_data = csv.reader(csvfile, delimiter=',')

    # SpaceTimeComplexity for loop- O(N)

    for row in CSV_data:
        package_ID = int(row[0])
        address_value = row[1]
        city_value = row[2]
        state_value = row[3]
        zip_value = row[4]
        delivery_deadline_value = row[5]
        weight_value = row[6]
        note_value = row[7]
        delivery_status = 'At hub'
        outfordelivery_value = 8.0
        raw_delivered_timestamp = 0.0
        delivered_timestamp = 0.0

        # Create all package objects
        packageInstance = Package(package_ID, address_value, city_value, state_value, zip_value,
                                  delivery_deadline_value,
                                  weight_value, note_value, delivery_status, outfordelivery_value, raw_delivered_timestamp, delivered_timestamp)

        # Insert packages into hashmap with package id as the key

        hash_Instance.insert(package_ID, packageInstance)
