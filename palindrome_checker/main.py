# palindrome_checker
with open('palindrome_checker/input.txt', 'r') as f:
  input = f.read()

item_list = input.splitlines()

results = {}
for item in item_list:
	# filter and count alfanumeric characters
	alphanum_chars = ''
	for char in item:
		if char.isalnum():
			alphanum_chars += char.lower()
	unique_count = len(set(alphanum_chars))

	# checl if palindrome
	if alphanum_chars == alphanum_chars[::-1]:
		results[item] = ("YES", unique_count)
	else:
		results[item] = ("NO", -1)

# print results
for palindrome_result, unique_count in results.values():
	print(f"{palindrome_result}, {unique_count}")