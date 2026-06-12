print("welcome to the data analyzer and transformer program")
while True:

  print("main menu:")
  print("press 1 Input Data ")
  print("press 2 Display Data Summary")
  print("press 3 Calculate Factorial")
  print("press 4 Filter Data by Threshold")
  print("press 5 Sort data")
  print("press 6 Dispaly Dataset Statistics")
  print("press 7 Exit program")
  choice = int(input("Enter your choice: "))
  match choice:   
     case 1:
         size = int(input("Enter your data for a 1d array:"))
         arr = []
         for i in range(size):
              ele = int(input("Enter element: "))
              arr.append(ele)
         print("list:",arr)
         print("Data has been stored successfully!")
         print()
         
     case 2:
         print("Data summary:")
         print()
         print("Total elements:",len(arr))
         print("Minimum value:",min(arr))
         print("Mximum value:",max(arr))
         print("Sum of all value:",sum(arr))
         average = sum(arr) / len(arr)
         print("Average value:", average)
         print()
         
     case 3:
         factorial = int(input("Enter a number to calculate its factorial:"))
         print()
         print("factorial of 5 is:")
         def fact(n):
             if n<=1:
                 return 1
             else:
                 return n * fact(n-1)
         ans = fact(5)
         print(ans)
         print()
     case 4: 
         print("Enter a Threshold value To Filter out data above this value:")
         print()

         threshold = int(input("Enter Threshold value: "))

         above = list(filter(lambda x: x > threshold, arr))
         below = list(filter(lambda x: x < threshold, arr))
         equal = list(filter(lambda x: x == threshold,arr))

         print(f"values above {threshold}: {above}")
         print(f"values below {threshold}: {below}")
         print(f"values equal to {threshold}: {equal}")
         print()
     case 5:
         print("menu")
         print("1.Ascending order.")
         print("2.Desecending order.")
         print("3.Exit From This Program.")
         print()
         sort = int(input("choose sorting option:"))
         print()
         match sort:
             case 1:
                 print("Sorted Data In Ascending order:")
                 arr.sort()
                 print(arr)
                 print()
             case 2:
                 print("Sorted Data In Descending order:")
                 arr.sort(reverse=True)
                 print(arr)
                 print()
     case 6:
         print("Dataset Statistics:")
         print()
         print("Minimum value:",min(arr))
         print("Mximum value:",max(arr))
         print("Sum of all value:",sum(arr))
         print("Average value:", average)
         print()
         
         
     case 7:
         print("Exiting program-------")
         print("Thank you for using the data analyzer and transformer program.goodbye!")
         break
