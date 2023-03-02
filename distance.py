import csv
import datetime

from distance_data_list import distance_data_2dlist


# create list to hold address data
address_list = []

# read csv file with locations names and address of the locations

with open('name_and_address_data.csv') as csvfile02:
    location_data = csv.reader(csvfile02, delimiter=',')

    for row in location_data:
        address = row[2]

        address_list.append(address)


# Function to get distance between two addresses

def get_distance(address1, address2):
    row1 = address_list.index(address1)
    column1 = address_list.index(address2)

    distance_between = distance_data_2dlist[row1][column1]

    return distance_between
