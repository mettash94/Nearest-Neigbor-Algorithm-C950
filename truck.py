from distance import get_distance
from ReadCSVPackageData import hash_Instance


# Take raw time and convert to string O(1)
def convert_time(raw_time):
    hours = int(raw_time)
    mins = int((raw_time - float(hours)) * 60)
    time_string = str(hours).zfill(2) + ":" + str(mins).zfill(2)
    return time_string


# Empty list to which each sums of each trucks distances are appended from the while loop O(1)
total_distance_trucklist = []


# Space Time Complexity- O(N)^2
# Function to find min distance
def findmin_and_deliver(truck_list, truck_start_time):
    truck_address = '4001 South 700 East'
    # truck_start_time = truck_start_time
    timestamp_to_deliver = truck_start_time

    speed = 18
    round_trip_list = []
    total_distance = None

    # while loop till all packages are delivered and removed
    while len(truck_list) > 0:
        min_distance = 20
        min_package_id = None
        # loops through truck list and finds the package with min distance
        # Space Time Complexity- O(N)

        for n in truck_list:
            package1 = hash_Instance.get_value(n)

            # Set all packages in truck 1 to leave at their specific start time by looping thought hash object first

            package1.outfordelivery_time = truck_start_time

            distance = get_distance(truck_address, package1.address)

            if distance < min_distance:
                min_distance = distance
                min_package_id = n

        # Time it to took to deliver and timestamp

        time_to_deliver = min_distance / speed
        timestamp_to_deliver = timestamp_to_deliver + time_to_deliver
        hash_Instance.get_value(min_package_id).raw_delivered_timestamp = timestamp_to_deliver

        # Get the package object from hashtable and change delivery status of package that has been delivered
        hash_Instance.get_value(min_package_id).status = 'delivered'

        hash_Instance.get_value(min_package_id).delivered_timestamp = convert_time(timestamp_to_deliver)

        # Once the package has been delivered remove it from truck list
        truck_list.remove(min_package_id)

        # add distances for each package to a list
        round_trip_list.append(min_distance)
        total_distance = sum(round_trip_list)

        # once it's been delivered to a location change from address to address of package its just been delivered tp
        truck_address = hash_Instance.get_value(min_package_id).address
    total_distance_trucklist.append(total_distance)
