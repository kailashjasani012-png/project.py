print("welcome to the pattern generator and number analyzer!")
while True:
    print("1.generate a pattern")
    print("2.analyzea range of numbers")
    print("3.exit")

    choice = int(input("Enter your choice :"))
    match choice:
        case 1:
            rawnumber=int(input("Enter the number of raw for the pattern:"))
            for i in range(1,rawnumber+1):
                for _ in range(1,5-i):
                     print(" ",end="")
                for j in range(1,i+1):
                     print("*",end=" ")
                print()

                
                
        case 2:
             start = int(input("Enter the starting number:"))
             end = int(input("Enter the ending number:"))
             x = 0
             for i in range(start,end+1):
                if i %2 == 0:
                    print(i,end=" ")
                    print(":-number is even")
                else:
                    print(i,end=" ")
                    print(":-number is odd")

        case 3:
            print("exiting program-------")
            break
        case _:print("wrong choice")
