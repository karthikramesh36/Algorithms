

def is_palindrome(string):
    i = 0
    j = len(string)-1
    for x in range(len(string)//2):
        if string[i] != string[j]:
            return False
        i+= 1
        j-= 1
        x+= 1
    print("done")
    return True

string = "nitin"
print(is_palindrome(string))
