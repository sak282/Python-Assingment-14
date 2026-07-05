Maxnum = lambda no1,no2,no3:no1

def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())

    print("enter third number:")
    value3=int(input())


    ret=Maxnum(value1,value2)

    if(ret==True):
        print("Numer 1 is max")
    else:
        print("Number 2 is max")



if __name__=="__main__":
    main()


