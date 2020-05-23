#HashMaps with Open Addressing Collision system
class HashMap:

    #while defining a hashmap No.1 thing is the size of the array.

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collision = 0):
        key_bytes = key.encode() #converting the string into CS bytes
        hash_code = sum(key_bytes) #suming up the bytes into an integer
        return hash_code + count_collision

    def compress(self, hash_code): #hash_code in compress() and hash_code in hash() are different variable for arguments
        return hash_code % self.array_size # returing the remainder of the hash_code
        #Note - hash() already exists in python
        #Note - Since we are returning the remainder of hash_code
        #with the array_size so no matter how big the collision is the index will be
        #range(array_size)
        #so using hash_map.compress(hash("")) is using python's hashing function
        #and hash_map.compress(hash_map.hash("hi")) is our function

    #Now, lets put [key, value pairs inside the array

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        current_index_value = self.array[array_index]

        if current_index_value is None or current_index_value[0] == key: #we are storing an array inside an array
            self.array[array_index] = [key, value]
            return

        #Incase of collisions

        collision_counts = 1

        while(current_index_value[0] != key):
            new_array_index = self.compress(self.hash(key, collision_counts))
            current_index_value = self.array[new_array_index] #assigning new value to the existing variable

            if current_index_value is None or current_index_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            collision_counts += 1 #so that the next time any collsion happens it will show a +plus 1 index value

    # retireving th data related to the key

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        possible_value = self.array[array_index] #Same as the assign function

        if possible_value is None:
            return None #if there is nothing in the array with the given key we return None

        elif possible_value[0] == key:
            return possible_value[1] #it means that the key is found thus, we return the associated value

        #Now, in case of a key, which created a collsion while assigning it so even though the index is same
        #we will have to increment the index to find the value

        collision_counts = 1

        while(possible_value[0] != key):
            new_array_index = self.compress(self.hash(key, collision_counts))
            new_possible_value = self.array[new_array_index]

            if new_possible_value is None:
                return None

            elif new_possible_value[0] == key:
                return new_possible_value[1]

            collision_counts += 1

        return  # Same as the function in self.assign()
