print("-----CAlCULATER-----")        
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")  
print("4. Division")
print("5. Exit")

while True:
    choice=int(input("please enter your choice: "))
    if choice==1:
        num1=float(input("pleaser enter the first number  : "))
        num2=float(input("please enter the second number  : "))
        sum=num1+num2
        print("the sum of two numbers is: ",sum)
    
    elif choice==2:    
       num1=float(input("pleaser enter the first number : "))
       num2=float(input("please enter the second number :  "))
       sub=num1-num2
       print("the subtraction of two numbers is: ",sub)
        
       
    elif choice==3:
        num1=float(input("pleaser enter the first number : "))
        num2=float(input("please enter the second number : "))
        
        mul=num1*num2
        print("the multiplication of two numbers is: ",mul)
          
    
             
    elif choice==4:
        num1=float(input("pleaser enter the first number : "))
        num2=float (input("please enter the second number  : "))
        if  num2==0:
            print("Division by zero is not allowed. Please enter a non-zero second number.")
            continue
        else:
         div=num1/num2
         print("the division of two numbers is: ",div)
         
     

    elif choice==5:
        print("THANK YOU FOR USING CALCULATOR")
        break
    else:
        print("Invalid choice. Please try again.")

