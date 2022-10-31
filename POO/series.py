class Series(object):
    #
    def gen_n (self, n):
        return list (range (1, n + 1))
    #
    def gen_n2 (self, n):
        l = [i**2 for i in range(1, n+1)]
        return l
    #
    def gen_fibo (self, n):
        #
        fn = [1]
        #
        if n>1:
            fn.append(1)
            for _ in range(2, n+1):
                f = fn[-1] + fn[-2]
                fn.append(f)
        elif n==1:
            fn.append(1)
        return fn
