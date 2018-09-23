
import datetime

def main():
    DOB=input('Enter your DOB:')
    YearNow=datetime.datetime.now().year
    Myage=YearNow-int(DOB)
    print("You age is {}".format(Myage))


if __name__=='__main__':main()