# Pig Latin Translator in Python!
# This little program was the second homework project given in the
# Intro to C class and arguably the most fun. It was interesting
# making the functions to take care of each use case depending on the
# word being translated, though there were a few EXTREMELY long lines
# of code. I'm wondering if the same will happen in Python.
# ~~~/\/\/\Old code from C template\/\/\/~~~
# def Welcome():
# 	print("\nHello and welcome to the Pig Latin Translator!")
# 	print("You can enter a word of your choosing and it will be translated into Pig Latin!\n")
# def GetWord():
# 	return input("Enter your word: ")
# def VowelRule(string):
# 	return string.lower() + "ay"
# def ConsonantRule(string):
# 	return string[1:].lower() + string[0].lower() + "ay"
# def TwoLetterRule(string):
# 	return string[2:].lower() + string[:2].lower() + "ay"
# def Translation(string):
# 	print("The translated word is:",string)
# 	print("\n")
# def Quit():
# 	print("If you are finished and would like to exit, type a zero 0.\nIf you would like to continue, type a one 1.")
# 	return input("1 or 0? ")

def WhichRule(string):
	if any(char.isdigit() for char in string):
		return 0
	if len(string) == 0:
		return 4
	if len(string) < 2:
		return 5
	test = string[:2].lower()
	if test[0] == "a" or test[0] == "e" or test[0] == "i" or test[0] == "o" or test[0] == "u":
		return 1
	elif test[1] == "a" or test[1] == "e" or test[1] == "i" or test[1] == "o" or test[1] == "u" or test[1] == "y":
		return 2
	else:
		return 3
VowelRule = lambda s: s.lower() + "way"
ConsonantRule = lambda s: s[1:].lower() + s[0].lower() + "ay"
TwoLetterRule = lambda s: s[2:].lower() + s[:2].lower() + "ay"
print("\nHello and welcome to the Pig Latin Translator!")
print("You can enter a word of your choosing and it will be translated into Pig Latin!\n")
quit = 1
while quit:
	givenword = input("Enter your word: ")
	print("Just to be sure, you typed", givenword)
	rule = WhichRule(givenword)
	if rule == 1:
		transword = VowelRule(givenword)
	elif rule == 2:
		transword = ConsonantRule(givenword)
	elif rule == 3:
		transword = TwoLetterRule(givenword)
	elif rule == 0:
		print("What you entered is not a word. Try again.\n")
		continue
	elif rule == 4:
		print("You didn't enter a word. Type any word you want to translate.\n")
		continue
	elif rule == 5:
		print("What you entered is too short. Try a longer word.\n")
		continue
	print("The translated word is: " + transword + "\n")
	print("If you are finished and would like to exit, type a zero 0.\nIf you would like to continue, type a one 1.")
	quit = int(input("1 or 0? "))
else:
	print("Thank you for using this program! I greatly appreciate it!")
# And so, after having completed this program in Python, I have to
# say, it was much easier writing the code in Python and it took less
# time and less steps. What took me two functions to do in C took me
# a few lines at most in Python. And because Python isn't as limited
# as C, I had less trouble with compiling. Start to finish, this
# probably took maybe an hour at most to do. Probably less if I
# actually timed myself. Overall, I love Python.

# So, after learning a bit more about Python, I understand now why coders
# like to use Python and its ability to shorten code. I changed all the
# simple functions into lambdas to keep it close and moved other bits of
# code that didn't require a function. It looks neater.