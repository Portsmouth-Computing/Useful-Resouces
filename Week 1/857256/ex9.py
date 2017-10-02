"""[harder] Write a function selectCoins that asks the user to enter an amount of money
(in pence) and then outputs the number of coins of each denomination (from £2 down
to 1p) that should be used to make up that amount exactly (using the least possible
number of coins). For example, if the input is 292, then the function should report:
1 × £2, 0 × £1, 1 × 50p, 2 × 20p, 0 × 10p, 0 × 5p, 1 × 2p, 0 × 1p. (Hint: use integer
division and remainder).
"""


def selectCoins():
    while True:
        pence = input("Amount of cash in pence: ")
        if pence.isnumeric():
            break
        else:
            print("Please input a number")
    pence = int(pence)
    pence_list = [200,100,50,20,10,5,2,1]
    pence_used = {200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
    pence_left = pence
    while pence_left != 0:
        for pence_test in pence_list:
            while pence_left != 0 and (pence_left - pence_test) > -1:
                pence_used[pence_test] += 1
                pence_left -= pence_test
    print("£2 x {}, £1 x {}, 50p x {}, 20p x {}, 10p x {}, 5p x {}, 2p x {}, 1p x {}".format(pence_used[200],pence_used[100],pence_used[50],pence_used[20],pence_used[10],pence_used[5],pence_used[2],pence_used[1]))


selectCoins()
