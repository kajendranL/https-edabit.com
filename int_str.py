def findLargestNum(nums):
	return max(nums)
	
	


def findLargestNum1(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest



print(findLargestNum([4, 5, 1, 3])) # 5
print(findLargestNum([300, 200, 600, 150])) # 600
print(findLargestNum([1000, 1001, 857, 1])) #? 1001

print(findLargestNum1([4, 5, 1, 3])) # 5
print(findLargestNum1([300, 200, 600, 150])) # 600
print(findLargestNum1([1000, 1001, 857, 1])) #? 1001
