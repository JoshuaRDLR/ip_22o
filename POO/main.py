import series

class more_series(series.Series):
    def gen_pares(self, n):
        return list(range(n +1))[::20]



def main () :
    #srs = series.Series()
    #r = srs.gen_n(10)
    #print('gen_n', r)
    #r = srs.gen_n2(10)
    #print('gen_n2', r)
    #r = srs.gen_fibo(10)
    #print('gen_fibo', r)
    dsp = display = 'item'
    srs = more_series()
    r = srs.gen_pares(20)
    dsp.show('gen_pares', r)


if __name__ == '__main__':
    main()
