#Credit Card Validator using Luhn's Algo
def checksum(num):
    length=len(num)
    total=0
    second=False
    for i in range(length-1,-1,-1):  #to start from last digit in credit card and decrement by 1
        d=int(num[i])
        if(second):
            d=d*2
            total=total + d%10
            total=total + d//10
        else:
            total+=d
        second=not second   
    if(total%10 == 0):
        temp=int(num[:2:])
        if(temp >=51 and temp <=55):
            print(f"{num} --> MasterCard")
        elif(temp==34 or temp ==37):
            print(f"{num} --> American Express")
        elif(temp<50):
            print(f"{num} --> Visa")
        else:
            print(f"{num} --> Valid but unknown type")
    else:
        print(f"{num} --> Invalid")
    return
credit=input("Enter your Credit Card number: ")
checksum(credit)