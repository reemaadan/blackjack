def mark(labs, avg_assignments, test1, test2, test3):
    return 0.1 * labs + 0.24 * avg_assignments + 0.08 * test1 + 0.23 * test2 + 0.35 * test3

m = mark(65, 80, 71, 72, 84)
print(m)