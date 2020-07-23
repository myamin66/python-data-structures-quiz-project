import random

def get_def_and_pop(word_list, word_dict):#returns a tuple
	random_index = random.randrange(len(word_list))#generate random index
	word = word_list.pop(random_index)#pops random words from the list
	definition = word_dict.get(word)#gets value of random key
	return word,definition#returns a tuple (word, definition(value))


def get_word_defination(rawstring):#takes rawstring and returns a tuple
    word, definition = rawstring.split(',', 1)   # Getting key and its value from raw string
    return word, definition # returns a tuple



fh = open("data.csv","r")#reads 'data.csv' file and it contains duplicate data
wd_list = fh.readlines() 

#writing into the dataSet.csv with no duplicate data
wd_set = set(wd_list)
fh = open("dataSet.csv", "w")
fh.writelines(wd_set)

#creating dictionary
word_dict = dict()
for rawstring in wd_set:        #for eachloop
    word, definition = get_word_defination(rawstring)
    word_dict[word] = definition #dictionary

while True:
	wd_list = list(word_dict)#getting a list of keys
	choice_list = []#creating empty list
	for x in range(4):#creating four choices	
		word, definition = get_def_and_pop(wd_list, word_dict)
		choice_list.append(definition)
	#shuffle the choices, we have avoided the loops
	random.shuffle(choice_list)
	print(word)#choosing correct definition 
	print("-------------")
	#printing the choices using for each loop
	for idx, choice in enumerate(choice_list):
		print(idx+1, choice)#index starts with one 
	choice = int(input("Enter 1,2,3,4; 0 to exit"))#getting input and converting it in int
	if choice_list[choice-1] == definition:
		print("Correct!\n")
	elif choice == 0:
		exit(0)#when input is zero, exit
	else:
		print("Incorrect!\n")


