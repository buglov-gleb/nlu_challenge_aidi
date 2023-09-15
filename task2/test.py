from jsgf import parse_grammar_string

filename = 'ru_grammar.txt'

with open(filename, 'r') as file, open('ru_utterances.txt', 'r') as utt_file:
    s = file.read()
    utterances = utt_file.readlines()

grammar = parse_grammar_string(s)

def check_utterance(utt, grammar):
	try:
		rule = grammar.find_matching_rules(utt)[0]
		print(utt + ' - ' + 'rule\'s found')
		return True
	except:
		print(utt + ' - ' + 'no rules found')
		return False

for utt in utterances:
	check_utterance(utt[0:-1], grammar)
