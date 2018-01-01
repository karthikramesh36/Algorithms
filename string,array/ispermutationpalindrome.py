import unittest,string

def ispp(arr):
    toggle = dict.fromkeys(string.ascii_lowercase,False)

    for char in arr:
        count = 0
        if(ord(char) > 96 and ord(char) <123):
            toggle[char] = not toggle[char]
    for i in toggle:
        if toggle[i] == True:
            count+=1
            if count > 1:
                return False
    return True

class test(unittest.TestCase):

    def test_ispp(self):
        self.assertTrue(ispp("abcdfeedcba"))
        self.assertTrue(ispp("abcddcba"))

if __name__ == '__main__':
    unittest.main(exit=False)
