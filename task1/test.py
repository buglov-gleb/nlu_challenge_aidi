from jsgf import parse_grammar_string

filename = 'en_grammar.txt'

with open(filename, 'r') as file:
    s = file.read()

grammar = parse_grammar_string(s)

def check_utterance(utt, grammar):
	try:
		rule = grammar.find_matching_rules(utt)[0]
		print(utt + ' - ' + 'rule\'s found')
		return True
	except:
		print(utt + ' - ' + 'no rules found')
		return False

utterances = ['can you play the beatles',
				'can you put on paranoid android',
				'i want to listen to radiohead',
				'i want to listen to jazz music',
				'play me ummagumma by pink floyd',
				'put lady gaga on'];

for utt in utterances:
	check_utterance(utt, grammar)
