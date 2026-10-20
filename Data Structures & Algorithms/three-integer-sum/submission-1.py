class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        #l = 0
        #r = n - 1
        # m = l+1 ( at start) 
        nums.sort()
        sums = []
        #at start, l = 0, at end l = len(nums) - 1
        for l in range(n):
            if nums[l] > 0:
                break
            elif l > 0 and nums[l-1] == nums[l]:
                continue
            m = 0
            r = n - 1
            m = l + 1

            while m < r:
                summation = nums[l] + nums[m] + nums[r]
                if summation != 0:
                    if summation > 0:
                        r -= 1
                    else:
                        m += 1
                else:
                    sums.append([nums[l], nums[m], nums[r]])
                    r -= 1
                    while nums[r+1] == nums[r] and m < r:
                        r -= 1
                    m += 1
                    while nums[m-1] == nums[m] and m < r:
                        m += 1
                    
            l += 1
        return sums
                    


