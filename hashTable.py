class HashMap:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # SpaceTimeComplexity - O(N)

    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.

        self.hash_table = []
        for i in range(initial_capacity):
            self.hash_table.append([])

    # Insert a package into the hashtable
    # Space Time Complexity: O(1)

    def insert(self, key, package):
        # Get the index from the key
        # using hash function
        bucket = hash(key) % len(self.hash_table)

        key_value_pair = [key, package]

        self.hash_table[bucket].append(key_value_pair)

    # Search for a package given packageID which is the key
    # Space Time Complexity O(N)

    def search_key(self, key):
        # Get the bucket list where this key/ID should be found
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # search for the corresponding key inside the list
        for package in bucket_list:
            if package[0] == key:
                return package[0]
            else:
                return None

    # Given key return the value
    # Space Time Complexity O(N)

    def get_value(self, key):
        bucket = key % len(self.hash_table)
        package_list = self.hash_table[bucket]

        for package in package_list:
            if package[0] == key:
                return package[1]
            else:
                return None

        # Delete a package with the input key which is the package id
        # O(N)

    def delete_package(self, key):

        bucket = hash(key) % len(self.hash_table)

        package_list = self.hash_table[bucket]

        # Look inside the bucket and remove package for the matching key/ID, if found.
        for package in package_list:
            if package[0] == key:
                package_list.remove(key)
