class KthLargest:

        #appennd
        #sort 
        #find val of n - k 

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) -  self.k]
