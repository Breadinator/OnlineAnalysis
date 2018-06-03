import json #not used in the actual program, but I used it for testing and I'm lazy af
from urllib.request import urlopen

class get:
	def word(word):
		url = "https://api.pearson.com/v2/dictionaries/entries?headword=" + str(word)
		return json.loads(urlopen(url).read().decode())

class analyse:
	def type(word):
		info = get.word(word)['results']
		types = {
			'noun': 0,
			'verb': 0,
			'adjective': 0,
			'adverb': 0,
			'pronoun': 0,
			'preposition': 0,
			'conjunction': 0,
			'determiner': 0,
			'exclamation': 0,
			'other': 0
		}
		for i in info:
			if i['headword'] == word:
				orig = types.copy()
				if 'part_of_speech' in i:
					wtype = i['part_of_speech']

					if " noun" in wtype:
						types['noun'] += 1
					if wtype[0:4] == "noun":
						types['noun'] += 1

					if " verb" in wtype:
						types['verb'] += 1
					if wtype[0:4] == "verb":
						types['verb'] += 1

					if "adj" in wtype:
						types['adjective'] += 1
					elif "adjective" in wtype:
						types['adjective'] += 1

					if "adv" in wtype:
						types['adverb'] += 1
					elif "adverb" in wtype:
						types['adverb'] += 1

					if "pronoun" in wtype:
						types['pronoun'] += 1

					if "prep" in wtype:
						types['preposition'] += 1
					elif "preposition" in wtype:
						types['preposition'] += 1

					if "conj" in wtype:
						types['conjunction'] += 1

					if "determiner" in wtype:
						types['determiner'] += 1
					if "article" in wtype:
						types['determiner'] += 1

					if "exclamation" in wtype:
						types['exclamation'] += 1
					if "interj" in wtype:
						types['exclamation'] += 1



					if types == orig:
						#print(wtype)
						types['other'] += 1

					''' OLD SHIT
					if wtype == "interj":
						wtype = "interjection"
					elif wtype == "phrasal verb":
						wtype = "verb"

					if wtype in types:
						types[wtype] = types[wtype] + 1
					else:
						types[wtype] = 1
					'''
		return types
		