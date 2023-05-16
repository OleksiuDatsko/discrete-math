from task1.generating_all_permutations import algo1_11
from task2.generating_all_partitions_of_set import generate_partitions

if __name__ == '__main__':
    n = 4
    test_algo1_11 = algo1_11(n)
    print(f"\nAlgo 1.11: \nn = {n}")
    test_algo1_11.PERM(n)

    print(f"\nAlgo 1.19: \nn = {n}")
    generate_partitions(n)
    