name = str(input("Name: "))
age = int(input("Age: "))
height = int(input("Height(cm): "))
power = int(input("Power(1-10): "))
starter = int(input("Starter Pack Dollar: "))

if age >= 18:
    if starter > 10000:
        print("Pass")
    else:
        if height >= 180:
            print("Pass")
        else:
            if power >= 7:
                print("Pass")
            else:
                print("False")
else:
    print("False")