

def displaly():
    print("welcome")

def Sum(n1,n2):
    z=n1+n2
    print("z={}.".format(z))

def Sum_r(n1,n2):
    return n1+n2
    

def main():

    displaly()
    displaly()
    displaly()
    displaly()
    Sum(3,5)
    k=Sum_r(10,20)
    print("k={}.".format(k))
if __name__=='__main__':main()