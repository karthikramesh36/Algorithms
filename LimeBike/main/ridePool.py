
import os
import sys

from settings import input_file
import ride
import itemCounter

# function to validate the directory and file existence
def validate_file(file):
        directory_check = os.path.exists(input_file)
        file_check = os.path.isfile(input_file)
        file_size = os.path.getsize(input_file)
        if not directory_check and not file_check:
            print("Check the directory and file for input file")
        else:
            if(int(file_size) <= 0):
                print("input file is empty")
            else:
                return True

class RidePool:

    def __init__(self):
#        Constructor
        self.list_of_rides = []

    def populate_rides(self):
        # check for directory and file
        file_check = validate_file(input_file)
        if file_check:
            with open(input_file) as f:
                lines = [line.strip() for line in f]
                for line in lines:
            #        print(line)
                    newride = ride.Ride()
                    newride.load_from_string(line)
                    self.list_of_rides.append(newride)

    def process_all_rides(self):
        item_counter = itemCounter.itemCounter()
        for item in self.list_of_rides:
            item_counter.process_ride(item)
        return item_counter

    def remove_empty_rides(self):
        for item in self.list_of_rides:
            if ((item.start_time == None) or (item.end_time == None) or (item.basket_items == None) ):
                self.list_of_rides.remove(item)
