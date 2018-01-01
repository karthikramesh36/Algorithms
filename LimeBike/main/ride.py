
import string
import re

class Ride:


    def __init__(self):
#        Constructor
        self.start_time = None
        self.end_time = None
        self.basket_items = {}

    def load_from_string(self,string):
        string_upper=string.upper()
        if re.match("^([01]\d|2[0-3]):?([0-5]\d)", string_upper):
            # parse duration and items
            ride_data=string_upper.split('->')
            duration = ride_data[0].strip()
            items = ride_data[1].strip()
            #parse start and end time from duration
            duration = duration.split('-')
            start_time = duration[0].strip()
            end_time = duration[1].strip()

            #check for corrupt input
            time_pattern = "^([01]\d|2[0-3]):?([0-5]\d)$"
            start_match = bool(re.match(time_pattern, start_time))
            end_match = bool(re.match(time_pattern, end_time))
            correct_time = False # flag to continue checking items

            #add time values from string to ride object
            if start_match and end_match:
                    self.start_time = start_time
                    self.end_time = end_time
                    correct_time = True
            else:
                print("corrupt input")

            if correct_time:
                total_items = items.split(',')
                d={}    # temp dict to store ride items
                for item in total_items:
                    #check for valid item input from string
                    stripped_item = item.strip()
                    item_list = stripped_item.split(' ')
                    dictionary_key = item_list[1].strip()
                    dictionary_value = item_list[0].strip()
                    key_match = re.match("^[A-Z]+$",dictionary_key)
                    value_match = re.match("^([-+]?\d)+$", dictionary_value)
                    #print(key_match,value_match)
                    if key_match and value_match:
                        d[dictionary_key] = dictionary_value
                    else:
                        pass
                #update ride objects items only if time input not corrupt
                self.basket_items = d
