class Solution:
    def asteroidsDestroyed(self, y: int, x: List[int]) -> bool:
        for i in sorted(x):
            if i>y: return False
            y+=i
        return True