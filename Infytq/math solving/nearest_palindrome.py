def getNextPalindrome(num):
    while True:
        s = str(num)
        if(s == s[::-1]):
            return num
        num+=1
def getPrevPalindrome(num):
    while (num>0):
        s = str(num)
        if(s == s[::-1]):
            return num
        num-=1
    return -1
number = int(input())
nextnum = getNextPalindrome(number)
prevnum = getPrevPalindrome(number)
if(prevnum == -1):
    nearestnum = nextnum
elif((nextnum - number) > (number-prevnum)):
    nearestnum = prevnum
else:
    nearestnum = nextnum
print(nearestnum)