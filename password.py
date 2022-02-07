import string
import random
def gen(length):
    random.seed()
    letters = list(string.letters)
    numbers = [1,2,3,4,5,6,7,8,9,0]
    a = 0
    newpass =[]
    while a < length:
        ranchars =[]
        randle = random.choice(letters)
        rannum = random.choice(numbers)
        ranchars.append(randle)
        ranchars.append(str(rannum))
        ranchar = random.choice(ranchars)
        newpass.append(ranchar)
        a+=1
    return string.join(newpass)
print()
