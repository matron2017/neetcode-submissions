class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if more than 0, stop
        # if 2 oit of 3, no otehr variaiton (no doulbes)
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1

                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
        
        return ans