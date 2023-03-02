# Class for packages
class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, note, status,
                 outfordelivery_time, raw_delivered_timestamp,delivered_timestamp):
        self.package_ID = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.note = note
        self.status = status
        self.outfordelivery_time = outfordelivery_time
        self.raw_delivered_timestamp = raw_delivered_timestamp
        self.delivered_timestamp = delivered_timestamp


