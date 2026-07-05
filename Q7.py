Divi = lambda no:(no%5==0)

def main():
    print("enter  number:")
    value=int(input())

    

    ret=Divi(value)

    if(ret==True):
        print("Numer is divisible by 5")
    else:
        print("Number is not divisible by 5")



if __name__=="__main__":
    main()


