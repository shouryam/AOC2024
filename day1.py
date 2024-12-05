import re
import heapq

"""
Problem:
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

Solution:
Use two heaps and add all the numbers in the list. Then pop each number for heap and accumulate the distance
If the length of the list is n then the time complexity is 

Building heaps: O(n) -> heapifying a list of n elements takes O(n) time due to siftdown operation

Popping elements: O(nlogn) -> popping n elements from a heap of n elements takes O(logn) time for each pop operation

Overall time complexity: O(n) + O(nlogn) = O(nlogn)
"""

leftList = []
rightList = []


with open('day1.txt') as f:
    lines = f.readlines()
    length = len(lines)
    
    for line in lines:
        #split the line using regex into two numbers
        nums = re.split(r'[\s,]+', line)
        num1 = int(nums[0])
        num2 = int(nums[1])

        leftList.append(num1)
        rightList.append(num2)

# Copy the lists
heap1 = leftList[:]
heap2 = rightList[:]

heapq.heapify(heap1)
heapq.heapify(heap2)

dist = 0

while heap1:
    num1 = heapq.heappop(heap1)
    num2 = heapq.heappop(heap2)
    dist += abs(num1 - num2)


print ("The sum of the distances is: " + str(dist))
        
# Similarity Score Problem

"""
Problem: 
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Solution:

frequency dictionary for the right list? Go through the left and then multiply
frequency dict of both lists and then mutiply the values of the keys that are common times the key

Time Complexity:
Build the freqeuncy dicts O(n)
Go through the frequency dict O(unique left values) < O(n)

"""

from collections import defaultdict

leftFreq = defaultdict(int)
rightFreq = defaultdict(int)

for num in leftList:
    leftFreq[num] += 1

for num in rightList:
    rightFreq[num] += 1

sim_score = 0
for key, value in dict(leftFreq).items():
    sim_score += key * value * rightFreq[key]

print("The Similarlity Score is " + str(sim_score))




