class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def back(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n+1):
                path.append(num)
                back(num+1, path)
                path.pop()

        back(1, [])
        return result
        