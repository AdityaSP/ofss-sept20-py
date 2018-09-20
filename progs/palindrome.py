ui = input("Enter a string:").lower()

print("-"*30)
if ui == ui[::-1] :
    print("Yay! Its a palindrome")
else:
    print("Not a palindrome")
print("-"*30)