Minnum = lambda no1,no2:(no1<no2)

def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())


    ret=Minnum(value1,value2)

    if(ret==True):
        print("Numer 1 is minimum")
    else:
        print("Number 2 is minimum")



if __name__=="__main__":
    main()


