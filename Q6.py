Oddeven = lambda no:(no%2==1)

def main():
    print("enter  number:")
    value=int(input())

    

    ret=Oddeven(value)

    if(ret==True):
        print("Numer is odd")
    else:
        print("Number is not odd")



if __name__=="__main__":
    main()


