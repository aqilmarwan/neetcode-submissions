class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort list ascending
        # subtract max i and nax - 1 i 
        # replace val in List of stones
        # sort list ascending

        while len(stones) > 1:   
            stones.sort()

            cur = stones.pop() - stones.pop()
            
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0
