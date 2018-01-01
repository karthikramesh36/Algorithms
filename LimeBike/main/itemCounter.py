import collections
import datetime
import re

def timevalue(string):
    value = datetime.datetime.strptime(string,'%H:%M').time()
    #print(value)
    return value


# funtion to update the current common dictionary item values from the previous sum
def update_cumulative_values(current_start,cumulative_item_values):

    temp_current_start = {}
    temp_current_start = current_start[1]
    if cumulative_item_values is None:
        cumulative_item_values = temp_current_start
    else:
        for key , value in temp_current_start.items():
            if key not in cumulative_item_values.keys():
                cumulative_item_values[key] = int(value)
            else:
                cumulative_item_values[key] += int(value)

    return cumulative_item_values

class itemCounter:

    def __init__(self):

        #Constructor
        self.start_times = {}
        self.end_times = {}
        self.intervals = []

    def process_ride(self,ride):
        #check if start and end time dictionary already have the ride.object.time
        # as its key , if it does then we have to update the basket values
        # else it will get replaced and lost.
        if ride.start_time in self.start_times:
            temp = self.start_times[ride.start_time]
            for key,value in ride.basket_items.items():
                if key not in temp.keys():
                    temp[key] = ride.basket_items[key]
                else:
                    temp[key] =int(temp[key])+int( ride.basket_items[key])
            self.start_times[ride.start_time] = temp
        else:
            self.start_times[ride.start_time] = ride.basket_items
        if ride.end_time in self.end_times:
            temp = self.end_times[ride.end_time]
            for key,value in ride.basket_items.items():
                if key not in temp.keys():
                    temp[key] = ride.basket_items[key]
                else:
                    temp[key] = int(temp[key]) - int(ride.basket_items[key])
            self.end_times[ride.end_time] = temp
        else: # logic to save the basket values in negative in self.end_times
            neg_basket_items = {}
            for items in ride.basket_items:
                neg_basket_items[items] = min(int(ride.basket_items[items]),-int(ride.basket_items[items]))
            self.end_times[ride.end_time] = neg_basket_items


    def print_items_per_interval(self):
        #how do we create intervals ? find union of start times and end times whilst updating coressponding dict values
        #creating reversed sorted dictionary
        sorted_start_time = collections.OrderedDict(sorted(self.start_times.items(),reverse = True))
        sorted_end_time = collections.OrderedDict(sorted(self.end_times.items(), reverse = True))
    #    print(sorted_start_time,"printing all end times")
    #    print(sorted_end_time,"printing all end times")

        #create a common dict for items in ride per intervals
        common_dict = collections.OrderedDict()
        loop_length = int(len(sorted_start_time) + len(sorted_end_time))
        count =0
        cumulative_item_values={}
        #loop goes until either of the two sorted dictionaries is empty
        #done by calculating length of two dictionaries
        while count < loop_length:
            #pop last item from each dictionary and compare for smallest time.
            #insert into commom dict in a sorted manner.
            # At the same time we calculate cumulative of items present until the previous
            #time interval
            # this done by adding the cumulative previous basket items up untill current key

            #failproof break condition
            if len(sorted_start_time) == 0 or len(sorted_end_time) == 0 :
                break
            current_start = sorted_start_time.popitem()
            current_end = sorted_end_time.popitem()
            if timevalue(current_start[0]) < timevalue(current_end[0]):
                print("start time is smaller , adding",current_start[0],"to common_dict and update cumulative")
                cumulative_item_values = update_cumulative_values(current_start,cumulative_item_values)
                common_dict[current_start[0]] = str(cumulative_item_values)
                count+=1
                sorted_end_time[current_end[0]] = current_end[1]
            elif timevalue(current_start[0]) == timevalue(current_end[0]):
                print(" time is equal , adding",current_start[0],"to common_dict and update cumulative twice")
                cumulative_item_values = update_cumulative_values(current_start,cumulative_item_values)
                cumulative_item_values = update_cumulative_values(current_end,cumulative_item_values)
                common_dict[current_start[0]] = str(cumulative_item_values)
                count+=2
            else:
                print("end time is smaller , adding",current_end[0],"to common_dict and update cumulative")
                cumulative_item_values = update_cumulative_values(current_end,cumulative_item_values)
                common_dict[current_end[0]] = str(cumulative_item_values)
                count+=1
                sorted_start_time[current_start[0]] = current_start[1]

#       adding the remaining items from start and end times to common dict
        remaining_start = int(len(sorted_start_time))
        remaining_end = int(len(sorted_end_time))
        print(remaining_start,remaining_end,"remainig start_times to be put in common_dict")
        remaining_count=0

        if remaining_start > 0:
            while remaining_count < remaining_start:
                current_start = sorted_start_time.popitem()
                cumulative_item_values = update_cumulative_values(current_start,cumulative_item_values)
                remaining_count+=1
                common_dict[current_start[0]] = str(cumulative_item_values)

        if remaining_end > 0:
            while remaining_count < remaining_end:
                current_end = sorted_end_time.popitem()
                cumulative_item_values = update_cumulative_values(current_end,cumulative_item_values)
                remaining_count+=1
                common_dict[current_end[0]] = str(cumulative_item_values)
        print("OUTPUT AS REQUIRED")
        pretty_print_items_per_interval(common_dict)

def pretty_print_items_per_interval(common_dict):
        count=0
        correct_start_time,correct_basket_items,zero_value_flag = None,None,False
        lastvalue=[]
        # iterate through each item in dictionary and print it out
        for start_time,basket_items in common_dict.items():
            # eliminating intervals with zero items
            total = 0
            values=re.findall(r'\d+', basket_items)
            for value in values:
                total = total + int(value)
            basket_items = str(basket_items)
            basket_items = basket_items.replace("{","")
            basket_items = basket_items.replace("}","")
            basket_items = basket_items.replace("'","")
            if total != 0: # eliminating intervals with zero items
            #  final touch for proper output format
                output = [correct_start_time,"-",start_time,"->",correct_basket_items]
                if zero_value_flag:
                    output = [zero_value_time,"-",start_time,"->",correct_basket_items]
                    zero_value_flag = False
                correct_start_time = start_time
                correct_basket_items = basket_items
                if count > 0:
                    print(''.join(output))
                count+=1
            else:
                zero_value_time = start_time
                zero_value_flag = True
            lastvalue=[correct_start_time,"-",start_time,"->",correct_basket_items]
        print(''.join(lastvalue))
