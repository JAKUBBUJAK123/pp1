code = "0805"

attempt = 0
while attempt <3 :
    pin = str(input("enter the pin: "))
    if pin == code :
        print("correct")
        break

    else:
        print("incorrect")
        attempt +=1
else:
    print("sorry your payment card has been blocked")