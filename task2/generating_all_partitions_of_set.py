def generate_partitions(n: int):
    P = list(range(1, n + 1))
    БЛОК = [1] * (n + 1)
    ВПЕР = [True] * (n + 1)
    СЛЕД = [0] * (n + 1)
    ПРЕД = [0] * (n + 1)

    def print_partition():
        subsets = []
        for i in set(БЛОК):
            subsets.append(
                ''.join(str(P[j - 1]) for j in range(1, n + 1) if БЛОК[j] == i)
            )
        partition = f"({')('.join(subsets)})"
        print(partition)

    print_partition()
    j = n
    while j > 1:
        k = БЛОК[j]
        if ВПЕР[j]:
            if СЛЕД[k] == 0:
                СЛЕД[k] = j
                ПРЕД[j] = k
                СЛЕД[j] = 0
            if СЛЕД[k] > j:
                ПРЕД[j] = k
                СЛЕД[j] = СЛЕД[k]
                ПРЕД[СЛЕД[j]] = j
                СЛЕД[k] = j
            БЛОК[j] = СЛЕД[k]
        else:
            БЛОК[j] = ПРЕД[k]
            if k == j:
                if СЛЕД[k] == 0:
                    СЛЕД[ПРЕД[k]] = 0
                else:
                    СЛЕД[ПРЕД[k]] = СЛЕД[k]
                    ПРЕД[СЛЕД[k]] = ПРЕД[k]
        print_partition()
        j = n
        while j > 1 and (
            (ВПЕР[j] and (БЛОК[j] == j)) or (not ВПЕР[j] and (БЛОК[j] == 1))
        ):
            ВПЕР[j] = not ВПЕР[j]
            j -= 1
