class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        res=[0]*n

        for i in range(k):
            res[0]=nums[n-1]
            res[1:n]=nums[0:n-1]
            nums[:]=res[:]
        