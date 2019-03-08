#from sys import maxint

def max_contiguous_sum(a,size):
    max_sum = -9223372036854775808
    max_so_far = 0
    for i in range(0,size):
        max_so_far +=a[i]
        if (max_sum<max_so_far):
            max_sum = max_so_far

    return max_so_far

a = [-13, -3, -25, 20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
obj = max_contiguous_sum(a,len(a))
print(obj)