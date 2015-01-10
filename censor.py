"""Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:
			censor("this hack is wack hack", "hack")
should return
			"this **** is wack ****"

Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word."""

def censor(text, word):
	split_text = text.split()
	split_censored = []

	for words in split_text:
		if words == word:
			split_censored.append(len(word) * "*")
		else:
			split_censored.append(words)

	censored_text = " ".join(split_censored)
	return censored_text

print censor("this hack is wack hack", "hack")