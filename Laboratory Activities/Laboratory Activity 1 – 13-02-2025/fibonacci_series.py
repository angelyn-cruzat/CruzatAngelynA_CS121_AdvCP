num = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1

if num < 0:
    print("Please Enter a Positive number.")
else:
    print("Fibonacci series:", end=" ")
    for _ in range (num):
        print(first_term, end= " ")
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
    print()

