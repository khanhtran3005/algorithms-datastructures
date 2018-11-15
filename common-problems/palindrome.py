def parlindrome(string):
	return parlindromeHelper(string, 0, len(string) - 1)

def parlindromeHelper(string, left, right):
	if left >= right:
		return True;
	else:
		# print(string[left], string[right])
		return string[left] == string[right] and parlindromeHelper(string, left + 1, right - 1)


def parlindrome_2(string):
	left = 0
	right = len(string) - 1

	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1

	return True
	
print(parlindrome_2('rottor'))
print(parlindrome('motor'))
print(parlindrome('rotor'))