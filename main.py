# Shwetha Mettakadapa 009620095
from ReadCSVPackageData import hash_Instance

from truck import findmin_and_deliver, total_distance_trucklist

# First truck gets first priority based on time(10:30AM) and rules for delivering packages
# All trucks start from the hub which is the first address of the address list
# Truck 1 leaves the hub at 8.00 am
# Truck 1 can carry max 16 packages
#  14, 15, 16, 19, 20 must be delivered together

truck1 = [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 35, 37, 40]

#  packages in truck 2
truck2 = [3, 6, 10, 17, 18, 25, 28, 32, 33, 36, 38, 39, 2, 5, 26]

# packages in truck3
truck3 = [4, 9, 8, 7, 11, 12, 21, 22, 23, 24]

# Calling the delivery function which contains the greedy algorithm for all trucks
# 9.2 converts to 9:11 am after the packages arrive at the hub at 9:05 am to be loaded onto truck 2
findmin_and_deliver(truck1, 8.0)
findmin_and_deliver(truck2, 9.2)
findmin_and_deliver(truck3, 11.00)

# Calculating the total distance of all the distances in the lists
total_distance_all_trucks = sum(total_distance_trucklist)

# UI to interact with users Package ID: 1, Address: 195 W Oakland Ave, ….Delivered at 08:46:20 Provide an interface
# for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage
# traveled by all trucks.

user_input = int(input("PRESS 1 to Print All Package Status and Total Mileage"
                       " or PRESS 2 to see a specific package status with ID: "
                       ))

# To print info about all packages and their status along with total distance traveled by the trucks
if user_input == 1:
    input_hour = int(input("Please enter a time in hours (MILITARY TIME FORMAT) : "))
    input_minutes = int(input("Please enter a time in minutes: "))
    total_time = input_hour + input_minutes / 60.0
    print("Packages STATUS AT : {} : {} ".format(input_hour, input_minutes))

    for i in range(1, 41):
        package1 = hash_Instance.get_value(i)

        print("Package ID: {} at Address : {}, with deadline: {}, in Salt Lake City with zipcode: {}, weight: {}"
              .format(i, package1.address, package1.delivery_deadline, package1.zip_code, package1.weight))
        if float(package1.raw_delivered_timestamp) < total_time:
            print("Delivered at " + package1.delivered_timestamp + " STATUS CHECK AT : {} : {} "
                  .format(input_hour, input_minutes))
        elif package1.outfordelivery_time > total_time:
            print("AT HUB" + " Status check at : {} : {} "
                  .format(input_hour, input_minutes))
        else:
            print("EN ROUTE" + " Status check at : {} : {} "
                  .format(input_hour, input_minutes))

# print status of 1 package and total distance traveled by trucks
if user_input == 2:
    input_packageID = int(input("Please enter a package ID you want to find status of packages 1-40: "))

    if input_packageID >= 1 or input_packageID <= 40:
        input_hour = int(input("Please enter a time in hours (MILITARY FORMAT) : "))
        input_minutes = int(input("Please enter a time in minutes: "))
        total_time = input_hour + input_minutes / 60.0

        package2 = hash_Instance.get_value(input_packageID)

        print("Package ID: {} at Address : {}, with deadline: {}, in Salt Lake City with zipcode: {}, weight: {}"
              .format(input_packageID, package2.address, package2.delivery_deadline, package2.zip_code, package2.weight))

        if float(package2.raw_delivered_timestamp) < total_time:
            print("Delivered at " + package2.delivered_timestamp)
        elif package2.outfordelivery_time > total_time:
            print("at hub")
        else:
            print("En route")
print("Total Distance in miles to deliver all 40 packages in miles : {} ".format(total_distance_all_trucks))
