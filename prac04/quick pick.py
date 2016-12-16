__author__ = 'jc449735'
from random import randint
no_of_picks=int(input("pick your quick pick "))
lists = []
nu = 0
for num in range(0,no_of_picks):
    nu = randint(1 , 45)
    for j in range(0 , 6):
        while nu in lists:
            nu = randint(1, 45)
        lists.append(nu)
    print(sorted(lists))
    lists = []