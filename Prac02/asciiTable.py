__author__ = 'jc449735'
LOWER=40
UPPER=100
print("enter a number {:d} - {:d} ".format(LOWER,UPPER))
for i in range(LOWER,UPPER,11):
    print("ASCII CODE IS {:4} CHARACTER {:<9}".format(i, chr(i)))


