class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for num1 in nums:
            j=0
            for num2 in nums:
                if i<j:
                    if num1+num2==target:
                        result = [i,j]
                        return result
                
                j+=1
            i+=1
