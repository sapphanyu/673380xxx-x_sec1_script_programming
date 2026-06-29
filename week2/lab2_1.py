num = int(input("Enter a number: ") )
if num < 0:
    text = f"{num} is negative"
elif num > 0:
    text = f"{num} is positive"
else:
    text = f"{num} is zero"

if num == 0:
    print("1")
elif num % 2 == 0:
    print("2")
else:
    print("3")
