#To find the greatest no. among three
a = input("enter the 1st no.")
b = input("enter the 2nd no.")
c = input("enter the 3rd no.") 
num1 = int(a)
num2 = int(b)
num3 = int(c)

if(num1>num2 and num1>num3):
        print("num1 is greatest")
elif(num2>num1 and num2>num3):
    print("num2 is grestest")
else:
    print("num3 is grestest")
    