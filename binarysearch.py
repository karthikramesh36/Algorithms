import unittest

def bin_search(arr,ele):

    # Base Case!
    if len(arr) == 0:
        return False

    # Recursive Case
    else:

        mid = len(arr)/2

        # If match found
        if arr[mid]==ele:
            return True

        else:

            # Call again on second half
            if ele<arr[mid]:
                return bin_search(arr[:mid],ele)

            # Or call on first half
            else:
                return bin_search(arr[mid+1:],ele)

class test(unittest.TestCase):

    def test_bsearch(self):
        arr=[1,2,3,4,5,6,7,8]
        self.assertTrue(bin_search(arr,4))



if __name__ == '__main__':
    unittest.main()
