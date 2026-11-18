def sum_c(long n):
    cdef long long total = 0
    cdef long i
    for i in range(n):
        total += i * i
    return total