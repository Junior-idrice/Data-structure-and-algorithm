# this is a binary search algorithm

first = [4,5,7,1,23]
second = []
n = len(first)
num = 1
middle = (n)//2
print(first[middle])
for i in range(n):
    if first[middle]< num:
        second.append[middle+1]
        middle = (n)//2
    elif first[middle]> num:
        second.append[middle-1]
        middle = (n)//2

    else:
        print(second[middle])

