# Program to display the Fibonacci sequence up to n-th term

terms = int(input("How many terms do you want:\n "))

# first two terms
c1, c2 = 0, 1
count = 0

# check if the number of terms is valid
if terms <= 0:
   print("enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(c1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(c1)
       nth = c1 + c2
       # update values
       c1 = c2
       c2 = nth
       count += 1