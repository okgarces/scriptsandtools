

def check_palindrome(text):
	
	text_len = len(text)

	is_palindrome = True
	for i in range(text_len/2):
		print "Las letras a compara: %s y %s" % (text[i], text[text_len-1-i])
		if text[i] != text[text_len-1-i]:
			is_palindrome = False

	print is_palindrome


check_palindrome('')