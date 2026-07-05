Chkeven = lambda no:(no%2==0)

def main():
    print("enter  number:")
    value=int(input())

    

    ret=Chkeven(value)

    if(ret==True):
        print("Numer even")
    else:
        print("Number is not even")



if __name__=="__main__":
    main()


