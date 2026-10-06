class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        else:
            return False