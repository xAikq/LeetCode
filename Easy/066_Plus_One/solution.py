class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num: int = int("".join(map(str, digits)))
        num += 1

        result: List[int] = list(map(int, str(num)))

        return result