from sys import argv
from math import sqrt

def computePrime(max):
    if max<2 :
        print 'Max is too small. Prime number starts from 2.'
        return
    primenumbers=[2]
    for i in range(2,max+1) :
        for j in primenumbers :
            if i%j==0 :break
            if j> sqrt(i) :
                primenumbers.append(i)
                break
    print primenumbers

computePrime(int(argv[1]))

