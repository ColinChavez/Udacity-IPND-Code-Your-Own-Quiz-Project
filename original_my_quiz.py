import time

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

quiz_template = {'easy': '''Water exists in __1__ states. Water in the ocean would be a __2__. If water is frozen then
it becomes a __3__. When water boils it turns into a __4__.\n''', 'medium': '''Space is known as the __1__ frontier. 
Did you know that the __2__ was once part of Earth? Harry Kerry once said, If the moon was made of __3__ would you eat it?
The __4__ that astronauts have left on the moon will be there for 100,000,000 years.\n''','hard':  '''The closest star to earth 
besides the sun is __1__. That star is 4.2 __2__ away. It would take approximatley 500,000 earth __3__ to travel to __1__. 
Scientific research states that __1__ is located in the __4__ zone, which means it could support life\n'''}
#variable that contains a dictionary with nested lists
my_answers = {'easy': ['three', 'liquid', 'solid', 'gas'], 
		'medium': ['final', 'moon', 'rib', 'footprints'], 
		'hard': ["alpha centauri", "light years", "years", "habitable" ]} 

blanks = ["__1__", "__2__", "__3__", "__4__", "__5__"]

user_answers = []

def check_answers(level_difficulty,blank_counter,lives): #Compares user's input with the value of each list in the my_answers dictionary to see if the answer is right or wrong.
	print quiz_template[level_difficulty]
	print "What is the answer to " + blanks[blank_counter] + "?\n"
	user_answer = raw_input()
	user_answers.append(user_answer)
	for level,answers in sorted(my_answers.items()):
		for answer in answers:
			if user_answer in answers:
			#if user_answers == len(my_answers[level_difficulty]):
				return correct(level_difficulty,blank_counter,lives)
			else:
				return wrong(level_difficulty,blank_counter,lives)

def correct(level_difficulty,blank_counter,lives): #Ends the program if all answers are correct or outputs the users current level, increases the index by 1 and the users current lives
	print "That's Correct!\n" 
	if blank_counter == 3:
		print "Congratulations! You passed the quiz with " + str(lives) + " lives remaining!"
		return
	else:
		print "Let's continue with the " + level_difficulty + " Quiz\n"
		return check_answers(level_difficulty, blank_counter + 1, lives)

def wrong(level_difficulty,blank_counter,lives): #Deducts a life from the user and outputs all current values or ends the quiz if there are no more lives
	print "Sorry, that is wrong answer."
	lives -= 1
	print "You have " + str(lives) + " lives left."
	if lives == 0:
		print"Game Over"
	else:
		return check_answers(level_difficulty, blank_counter, lives)


def life(level_difficulty): #User chooses lives, initialize counter index, outputs assigned values
	blank_counter = 0 
	lives = int(raw_input("Choos your lives: "))
	print "\nYou will have " + str(lives) + " lives\n"
	print "Begin " + level_difficulty + " Quiz:\n"
	check_answers(level_difficulty.lower(),blank_counter,lives)


def quiz_intro(): #Quiz Intro function starts the quiz and outputs the user's level based on their input.
	print "Welcome to the Quiz, Please select easy | medium | hard to continue"
	level_difficulty = raw_input("Choose Your Fate: ")
	if level_difficulty.lower() == "easy":
		print "Easy? I'm dissapointed in you.\n"
		return life(level_difficulty)
	elif level_difficulty.lower() == "medium":
		print "Challenge Accepted\n"
		return life(level_difficulty)
	elif level_difficulty.lower() == "hard":
		print "Are you sure you want to lose?"
		time.sleep(2)
		print "Too late now..."
		time.sleep(1)
		print "Let the Games Begin!\n"
		return life(level_difficulty)
	else:
		print "Access Denied. This message will self destruct"


print quiz_intro()


		# for help with debuggin I used
		# print "variable: ", variable 
		# to test complex functions 
		# debug using scientific method
		#assert statements will crash the function if there is an error 
		#range'''

