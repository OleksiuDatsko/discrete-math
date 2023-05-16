class algo1_11:
    def __init__(self, n: int) -> None:
        self.P = [i + 1 for i in range(n)]

    def B(self, m, i):
        if (m % 2 == 0) and (m > 2):
            if i < m - 1:
                return i
            else:
                return m - 2
        else:
            return m - 1

    def PERM(self, m):
        if m == 1:
            print(self.P)
        else:
            for i in range(1, m + 1):
                self.PERM(m - 1)
                if i < m:
                    a = m - 1
                    b = self.B(m - 1, i)
                    self.P[b], self.P[a] = self.P[a], self.P[b]
