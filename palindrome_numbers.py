num = input("Enter a number: ")

baligtad_num = ""
for digit in num:
    baligtad_num = digit + baligtad_num

if num == baligtad_num:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")