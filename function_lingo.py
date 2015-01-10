def greet(lang):
	if lang == 'es':
		print 'Hola!'
	elif lang == 'fr':
		print 'Bonjour!'
	elif lang == 'en':
		print 'Hello!'
	else:
		print "Sorry, I don't speak your language. Hello!"

lingo = raw_input('Please choose your language (en/es/fr): ')
greet(lingo)