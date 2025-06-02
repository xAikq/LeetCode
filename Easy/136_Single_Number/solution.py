class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen: Dict[int, int] = dict(map(lambda x: (x, 0), nums))
        for num in nums:
            seen[num] += 1
            if seen[num] == 2:
                seen.pop(num)

        return seen.popitem()[0]