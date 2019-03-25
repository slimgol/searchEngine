import re

'''Module to remove special characters from a given string.
Note, the following function will accept a string.'''

regExp = r"[^a-zA-Z0-9]+"#Regular expression.

'''Accepts a string of text, removes all of the special characters and returns a new string.'''
def remove_special_chars(text):
	new_array = []
	for token in text.split():
		new_array.append(re.sub(regExp,'',token))
	return ' '.join(new_array)

print(remove_special_chars("Hello? ? How are you today lady in red? Okayyy!!!"))


	
