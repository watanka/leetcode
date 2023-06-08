class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls = [n for n in nums if n != val]

        nums[:] = ls[:]

        return len(nums)
