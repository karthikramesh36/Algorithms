'''
Created on Nov 17, 2017

@author: karthik
'''
import sys,os
sys.path.append('/Users/karthik/Documents/Python/LimeBike')

import unittest
import main.ridePool as r
import main.itemCounter as i

class Test(unittest.TestCase):


    def test_file_read(self):
        ride_pool = r.RidePool()
        ride_pool.populate_rides()
        ride_pool.remove_empty_rides()
        item_counter=ride_pool.process_all_rides()
    #    for ride in ride_pool.list_of_rides:
    #        item_counter.process_ride(ride)
        item_counter.print_items_per_interval()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_file_read']
    unittest.main()
