answer = input("What is the Answer to the Great Question of life, the universe, and everything? ")
answer = answer.strip()
if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
