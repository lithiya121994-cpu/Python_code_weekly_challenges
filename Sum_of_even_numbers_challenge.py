n=int(input("Enter a number:"))
if n>0:
    even_sum = 0
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
            count += 1
    print(" ")
    print("Sum of the evn numbers is:", even_sum)
    print("Number of even numbers:", count)
else:
    print("Enter a number greater than 0")
