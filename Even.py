def num(): 
    a=int(input(" "))
    if(a==0):
        print("invalid")
    elif(a>1):
        a=a%2
        if(a==0):
            print("Even")  
        else:
            print("Odd")
    else:
      print("invalid")

num()
