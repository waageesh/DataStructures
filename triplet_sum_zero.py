def triplet(a):
    found = False
    n = len(a)
    tbl = set()
    for i in range(n-1):
        for j in range(i+1,n):
            x = -(a[i] + a[j])
            if x in tbl:
                print('triplets found',x,a[i],a[j])
            else:
                tbl.add(a[j])

a = [0, -1, 2, -3, 1]
obj = triplet(a)
print(obj)