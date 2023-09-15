from jsgf import parse_grammar_string

filename = 'ru_grammar.txt'
#filename = 'JSGF_en_ext.txt'

with open(filename, 'r') as file:
    s = file.read()

grammar = parse_grammar_string(s)

def check_utterance(utt, grammar):
	try:
		rule = grammar.find_matching_rules(utt)[0]
		print(utt + ' - ' + 'found\n')
		print(rule.compile())
		return True
	except:
		print(utt + ' - ' + 'no rules found')
		return False

# test utterances

#[i want to listen to]<unk> [jazz]<genre> [music]<unk>
#[play me]<unk> [ummagumma]<album> [by]<unk> [pink floyd]<artist>
#[put]<unk> [lady gaga]<artist> [on]<unk>

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
'''
utterances = ['can you play the beatles',
				'can you put on paranoid android',
				'i want to listen to radiohead',
				'i want to listen to jazz music',
				'play me ummagumma by pink floyd',
				'put lady gaga on'];
'''

for utt in utterances:
	check_utterance(utt, grammar)
