// Runtime: 3042 ms (Top 5.00%) | Memory: 37.6 MB (Top 80.63%)
from collections import Counter

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        colcons = [] # preprocess columns
        for c in range(N):
            cons = []
            s = 0
            for r in range(M):
                if not matrix[r][c]:
                    s = 0
                else:
                    s += 1
                cons.append(s)
            colcons.append(cons)
        # colcons[c][r] is how much 1's we'll get if we start from column c at row r and go up

        best = 0
        for r in range(M):
            # try r as the lowest row
            C = Counter(colcons[c][r] for c in range(N))
            vs = sorted(C.keys(), reverse=True)
            cs = accumulate(C[v] for v in vs)
            for v,c in zip(vs,cs):
                best = max(best,v*c)
        return best