import unittest
def longest_palindrome_substring(string):
    maxlength=1 #keeps tab of length of current found max substring
    start=0
    length=len(string)

    low=0
    high=0
    #considering every element as a center of palindrome
    for i in range(1,length):
        #finding max even substring
        low=i-1
        high=i
        while low>=0 and high<length and string[low] == string[high]:
            if high-low+1 > maxlength:
                start=low
                maxlength=high-low+1
            low-=1
            high+=1
        #finding odd max substring
        low=i-1
        high=i+1
        while low>=0 and high<length and string[low] == string[high]:
            if high-low+1 > maxlength:
                start=low
                maxlength=high-low+1
            low-=1
            high+=1
    print("the longest palindrome substring is")
    print(string[start:start+maxlength])
    print(maxlength)
    return int(maxlength)

class test(unittest.TestCase):
    def test_longest_palindrome_substring(self):
        string="csdfwerjijrewpo"
        self.assertEqual(9,longest_palindrome_substring(string))


if __name__ == '__main__':
    unittest.main()
