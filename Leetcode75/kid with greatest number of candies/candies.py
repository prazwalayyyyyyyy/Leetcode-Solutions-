class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # initial solution
        # list = []
        # for candy in candies:
        #     if candy + extraCandies >= max(candies):
        #         list.append(True)
        #     else:
        #         list.append(False)
        # return list

        return [num + extraCandies >= max(candies) for num in candies]