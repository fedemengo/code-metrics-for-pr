
def dec2bin(n):
    print('dec2bin({})'.format(n))
    if n == 0:
        return ''
    else:
        return dec2bin(n//2) + str(n % 2)
