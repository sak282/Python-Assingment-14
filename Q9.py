Multnum = lambda no1,no2:no1*no2

def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())


    ret=Multnum(value1,value2)

    print("Multiplication of numbers is:",ret)


if __name__=="__main__":
    main()


