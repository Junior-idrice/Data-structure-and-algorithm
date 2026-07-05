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

'''
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
print(anagrams("sam","ams"))'''


#given an array of strings strs, group the anagrams together.
#you can return the answer in any order


'''def Anagram(strs):
    if len(str) == 0:
        return []
    ansmap = {}
    count = [0]*26
    for c in strs:
        count[ord(c)- 'a'] +=1 '''

#La methode est simple, il  
    
#leetcode 
'''
Given an integer array nums, return an array answer such that answer[i] equal to the product
of all the elements of nums except nums[i]
the time complexity should be O(n) without using division operation
'''
'''def excepself(nums):
    result = []
    for i in (range(len(nums))):
        result.append(1)
    pre = 1
    post = 1

    for i in range(len(nums)):
        result[i] = pre
        pre = nums[i] * pre

    for i in range(len(nums) - 1, -1, -1): 
        result[i] = result[i]*post
        post = post*nums[i]

    return result

print(excepself([4,5,3]))'''

#------------------------ TOP K FREQUENCY ELEMENTS ---------------------#
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order
'''
# we will use HashMap + Heap(Priority Queue )
'''import heapq
def Top(nums, k):
    if k == len(nums):
        return nums
    
    count = {}
    for n in nums:
        count[n] = count.get(n,0) + 1
    import heapq

    heap = []

    for n in count:
        heapq.heappush(heap, (count[n], n))

        if len(heap) > k:
            heapq.heappop(heap)
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(heap)[1])

    return ans

print(Top([1, 2, 1], 2))
'''





'''
----leetcode 
converting Roman numeral to Integers


def RomansToInter(value):
    values = {
        "I":1, 
        "V":5, 
        "X":10, 
        "L":50, 
        "C":100, 
        "D":500, 
        "M":1000, 
        "IV": 4, 
        "IX": 9, 
        "XL":40, 
        "XC":90, 
        "CD":400, 
        "CM":900 
    }
    
    
    total = 0
    i = 0

    while i<len(value):
        if i<len(value)-1:
            twosymbols = value[i:i+2]
            if twosymbols in values.keys():
                total += values.get(twosymbols)
                i += 2
                continue


        onesymbol = value[i:i+1]
        total += values.get(onesymbol)
        i +=1
    
    return sum 

print(RomansToInter("MDXXI"))
'''


#leetcode 953
# verifying an Alien Dictionary

'''
In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order.The order of the alphabet is some permutations of lovwercase letters

Given a sequence of words written in the alien language, and the order of the alphabet, return true iff the given words are sortedlexicographically in this alien language
'''

def Alien(words, order):
    orderMap = {}
    for i in range(len(order)):
        orderMap[order[i]] = i
    
    for i in range(len(words)-1):
        for j in range(len(words[i])):

            if (j>= len(words[i+1])):
                return False
            
            if words[i][j] != words[i + 1][j]:
                currentLetter = orderMap.get(words[i][j])
                nextLetter = orderMap.get(words[i+1][j])

                if nextLetter < currentLetter:
                    return False
                else:
                    break


    return True

word1 = ["hello","leetcode"] 
word2 = ["aa","bbb","aa"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(Alien(word2,order))