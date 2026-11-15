frequency = {'codingal': 3, 'is': 2, 'for': 2, 'coding': 1}

number = int(input("Enter a number to check its frequency: "))

found = False
for word, count in frequency.items():
	if count == number:
		print(word, "appears", count, "time(s)")
		found = True

if not found:
	print("No words have that frequency.")
