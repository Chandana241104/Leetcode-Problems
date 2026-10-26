class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        found=False
        last_seen={}
        for i in range(len(nums)):
            if nums[i] not in last_seen:
                last_seen[nums[i]]=i
            else:
                c=i-last_seen[nums[i]]
                if c<=k:
                    found=True
                    break
                else:
                    last_seen[nums[i]]=i
        return found
        