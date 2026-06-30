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
first method time complexity of n^2
we can go nlogn using binary search 
and then use map to make it for efficient even
'''
'''
array = [5,4,7,6,9,7,2]
target = int(input("enter the target value"))

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] + array[j] == target:
            print(str(array[i]) + " " + str(array[j]))'''




# ------ two sum using mapping ------------
'''
def two_sum(array, target):
    there = {}
    for i,elt in enumerate(array):
        complement = target - elt

        if complement in there:
            return [there[complement], i]
        there[elt] = i

nums = [7,8,9,6,3]
target = 9

print(two_sum(nums, target))'''


#------------------  letcode 217 --------------------#
#see if there are any duplicate elements in an array

#--- if use a brute force approach the time complexity will be O(n^2)

#this is the first approach of the day
''''array = [1,5,18,7,118]
array.sort()
for i in range(len(array)):
    if array[i] == array[i-1]:
      print(True)
      break
    else:
       print(False)
       break'''

'''
we will solve this using hashsets
'''

'''def leetcode(array):
    elt = set()
    for i in range(len(array)):
        if array[i] in elt:
            return True
        elt.add(array[i])
    
    return False

print(leetcode([4,5]))'''



#--- Given an integer array nums and an integer k, return 
#true if there are two distinct indives i and j in the array such 
#such that nums[i] == nums[j] and abs(i-j)<=k
# using hashset

'''def find(nums, k):
    element = set()
    for i in range(len(nums)):
        if nums[i] in element:
            return True
        element.add(nums[i])
        if len(element)>k:
            element.remove(nums[i-k])
    return False
print(find([1,2,7,7,5], 4))'''



#--- leetcode 242 given two string s and t, return true if t is an anagram of s, and false otherwise
'''
Good approach but time complexity of nlogn
def string(s,t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t

print(string("listn","silent"))'''

# using the idea of counting the numbers of characters and keep 
# incrementing or decrementing


def anagrams(s,t):
    alpha = [0]*26
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        alpha[ord(s[i])-ord('a')] += 1
        alpha[ord(t[i])-ord('a')] -= 1

    for i in alpha:
        if i !=0:
            return False
    return True
print(anagrams("sam","ams"))