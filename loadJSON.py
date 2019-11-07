import json
import os

#Note: the cards we care about each start with a newline char

def exportCardNames():
	with open ('ScryfallScraping/output.json', 'r') as file:
		my_dictionary = json.load(file)

	card_name_array = []
	#json file contains list of dictionaries. For our purposes, we only
	#	will only have one dictionary with a single element of the form:
	#	{'card_name' : ['list', 'of', 'card', 'names', 'as', 'strings']}
	for key in my_dictionary:
		card_list = key['card_name']
		for card in card_list:
			#ignore tokens, emblems, etc.
			if card[0] == '\n':
				card = card.strip()
				print(card)
				card_name_array.append(card)
			#only work with proper cards
			else:
				continue
	print(card_name_array)
	file.close()

	return card_name_array

if __name__ == '__main__':
	exportCardNames()

# def foo(dictionary):
# 	D = dictionary