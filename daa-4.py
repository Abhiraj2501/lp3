def n_queens(n, r=1, cols=[0], d1=[0], d2=[0]):
    if r == n:
        for c in cols:
            print([int(j == c) for j in range(n)])
        return True

    for c in range(n):
        if c not in cols and r-c not in d1 and r+c not in d2:
            if n_queens(n, r+1, cols+[c], d1+[r-c], d2+[r+c]):
                return True
    return False

n_queens(8)

'''-------------------------------------------------------------------