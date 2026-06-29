'''
first = [1,2,3,4,5,6]
second = []
n = len(first)
num = 3
middle = (n)//2
#print(first[middle])
for i in range(n):
    if first[middle]<= num:
        second.append(middle+1)
        middle = (n)//2
    elif first[middle]>= num:
        second.append(middle-1)
        middle = (n)//2

    else:
        print(middle)
# fibo

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(5))'''

'''
-----------THE TWO SUM PROBLEM------
'''
array = [5,4,7,6,9,7,2]
target = int(input("enter the target value"))

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] + array[j] == target:
            print(str(array[i]) + " " + str(array[j]))
