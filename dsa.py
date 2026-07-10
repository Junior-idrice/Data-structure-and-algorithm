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
word2 = ["aa","bbb"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(Alien(word2,order)) '''


#----- Leetcode 128 --------
# Longest Consecutive Sequence
'''
Given an unsorted array of integers nums, return the length of the longest 
consecutive elements. You must write an algorithm that runs in O(n) time

'''
# First approach is using sorting and the proceed
'''def Longest(array):
    if not array:
        return 0
    
    array = sorted(array)
    longest = 1
    current = 1

    for i in range(len(array) - 1):

        if array[i] == array[i + 1]:
            continue

        elif array[i] + 1 == array[i + 1]:
            current += 1
            longest = max(longest, current)

        else:
            current = 1

    return longest
print(Longest([0,0,0,4,2,3,9,7,8,1,-1]))'''

#--- Optimal solution using a HashSet
'''
def Longest(nums):
    if len(nums) == 0:
        return 0
    
    numSet = set(nums)

    longest = 1
    for i in numSet:
        if i-1 in numSet:
            continue
        else:
            currentNumber = i
            currentSub = 1

            while currentNumber + 1 in numSet:
                currentNumber +=  1
                currentSub +=1
            longest = max(longest, currentSub)   

    return longest

print(Longest([0,0,0,4,2,3,9,7,8,1,-1]))

'''


#---- leetcode 41
#   Given an unsorted integer array nums, return the smallest missing positive integer
# you must implement an algorithm that runs in O(n) time and uses constant extra space

'''
def FirstMissing(nums):

    n = len(nums)
    contains = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            contains += 1
            break
    if contains == 0:
        return 1
    
    for i in range(len(nums)):
        if nums[i]<=0 or nums[i]>n:
            nums[i]=1
    for i in range(len(nums)):
        a = abs(nums[i])
        
        if a == n:
            nums[0]  = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])

    for i in range(1, n):
        if nums[i] > 0:
            return i
    
    if nums[0] > 0:
        return n    
    return n+1

print(FirstMissing([-1,-5,-9]))'''





#### SLIDING WINDOW, NEW TOPIC
#leetcode 121

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day

you want to maximize your profit by choosing a single day to buy one stock and choosing a sifferent day in the future to sell that stocj

return the maximum profit you can achieve from this transaction. if you cannot achieve any profit, return 0
'''

'''def BestTimeToByandSellStock(prices):
    min = prices[0]
    profit = 0

    for i in range(len(prices)):
        if prices[i]<min:
            min = prices[i]
        profit  = max(profit, prices[i]-min)

    return profit 

print(BestTimeToByandSellStock([7,1,5,3,6,4]))'''


# Leetcode 567
# Permutation of String

'''
Given two string s1 and s2, return true if s2 contains a permutation of 
s1, or false otherwise.
In other words, return true if one of s1's permutation is the substring of s2

'''
'''
def PermutationOfStrings(s1, s2):
   if len(s1) > len(s2):
      return False
   
   s1Map= [0]*26
   s2Map= [0]*26

   for i in range(len(s1)):
      s1Map[ord(s1[i])- ord('a')] +=1
      s2Map[ord(s2[i])- ord('a')] +=1
    
   for i in range(len(s2)-len(s1)):

        if matches(s1Map, s2Map):
            return True
        
        s2Map[ord(s2[i+len(s1)])- ord('a')] += 1
        s2Map[ord(s2[i]) - ord('a')] -= 1
      
   return matches(s1Map,s2Map)

def matches(s1Map,s2Map):
    for i in range(26):
        if s1Map[i] != s2Map[i]:
            return False
        
    return True

print(PermutationOfStrings("ab","eidbaaooo"))'''


# Leetcode 424
# longest Repeating Character Replacement

# you are given a string s and an integer K. you can choose any character of the string 
# and change it to any other uppercase English character. You can perform this operation at most k times.

#Return the length of the longest containing the same letter you can ger after performing the above
#operations

# A brute force approach will be to take all possible substrings, then start replacing 
# and then get the one with the longest length


def characterReplacement(s, k):
    count = [0] * 26      
    left = 0
    maxOccurrence = 0
    longest = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord('A')
        count[index] += 1
        maxOccurrence = max(maxOccurrence, count[index])

        while (right - left + 1) - maxOccurrence > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest

print(characterReplacement("ABAB",2))
#This is the firsrt element of the people and the first people

