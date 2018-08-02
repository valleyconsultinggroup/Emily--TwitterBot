import requests
import re

#Animal Farm by George Orwell
API_TOKEN = 'b5c0c36756189b44983028c4d400b9ab'
TEXT = 'http://gutenberg.net.au/ebooks01/0100011h.html'
API_URL = 'http://api.diffbot.com/v3/article'

def get_article (article_URL):
	request_parameter = {
		'token': API_TOKEN,
		'url': article_URL
	}

	r = requests.get(API_URL, params = request_parameter)
	# print(r)
	res_text = r.json()['objects'][0]
	# print(res_text)
	return res_text['text']

#splitting up article

#remove punctuation
def remove_punctuation(x):
	no_punctuation = re.sub('[,.()]', '', x)
	no_punc_text = re.sub('--', ' ', x)
	return no_punc_text

#remove caps
def remove_caps(x):
	if x.isupper() and x != "I":
		x = x.lower()
	elif x[0].isupper():
		x = x.lower().capitalize()
	else:
		x = x.lower()
	return x

def split(x):

	split_text = x.split(" ")
	token_dict = {}

	for i in split_text:
		i = remove_punctuation(i).lower()
		if i in token_dict:
			token_dict[i] += 1
		else:
			token_dict[i] = 1

	if '' in token_dict:
		del token_dict['']

	return token_dict

def create_word_list(filename):
	corpus = open(filename, 'r')
	word_list = [remove_caps(x) for x in re.findall(r"[\w']+|[.,!?;]", corpus.read())]
	corpus.close()
	return word_list

if __name__ == '__main__':
	edited_art = get_article(TEXT)
	print(type(edited_art))
	print(split(edited_art))