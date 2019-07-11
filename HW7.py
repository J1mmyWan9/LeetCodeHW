class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        A=nums    
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])
        """
        if len(nums)<=1:
            return True
        pos = 99999
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if pos !=99999:
                    return False
                pos=i

        if pos==len(nums)-2 or nums[pos-1]<=nums[pos+1] or nums[pos]<=nums[pos+2]:
            return True
        else:
            return False
        """
        """
        return (pos is None or pos == 0 or pos == len(nums)-2 or
                nums[pos-1] <= nums[pos+1] or nums[pos] <= nums[pos+2])
        """
