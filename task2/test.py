from jsgf import parse_grammar_string

filename = 'ru_grammar.txt'

with open(filename, 'r') as file:
    s = file.read()

grammar = parse_grammar_string(s)

def check_utterance(utt, grammar):
	try:
		rule = grammar.find_matching_rules(utt)[0]
		print(utt + ' - ' + 'rule\'s found\n')
		return True
	except:
		print(utt + ' - ' + 'no rules found')
		return False

utterances = ['можешь сыграть the beatles',
				'можешь поставить параноид андроид',
				'я хочу послушать радиохед',
				'я хотел бы послушать джазовую музыку',
				'сыграй мне умагума от пинк флоидов',
				'включи нам чего-нибудь из джаза',
				'запусти медл пинк флоидов',
				'мы хотели бы послушать лэди гагу',
				'сыграй хей джуд',
				'вруби леди гагу'];

for utt in utterances:
	check_utterance(utt, grammar)
