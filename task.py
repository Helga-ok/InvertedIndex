import pymorphy2, sys, re
from collections import OrderedDict

input_file = sys.argv[1]
morph = pymorphy2.MorphAnalyzer()
text = open(input_file).read()


def clear_text(text_for_clear):
	clear_text = re.sub(r'[\n\t\r\.\(\)\{\}\[\]\+\?\!\*\"\'«»%:,–]', " ", text_for_clear, flags = re.U | re.I | re.M)
	return clear_text

def get_normal_form(word):
	return morph.parse(word)[0].normal_form

def main():
	dictionary = dict()
	i = 0
	count_of_tokens = 0
	count_of_terms = 0
	count_of_chars_token = 0
	count_of_chars_term = 0
	input_text = open(input_file)
	for line in input_text.read().split('\n'):
		clean_text = clear_text(line)
		for word in clean_text.split(' '):
			if word is not '':
				count_of_tokens += 1
				count_of_chars_token += len(word)
				normal_word = get_normal_form(word)
				if normal_word in dictionary:
					dictionary[normal_word].add(i)
				else:
					count_of_chars_term += len(normal_word)
					dictionary[normal_word] = set()
					dictionary[normal_word].add(i)
			else: continue
		i += 1
	input_text.close()
	d = sorted(dictionary.items())
	output_file = open('indexes.txt', 'w')
	for item in d:
		output_file.write(str(item[0]))
		for v in item[1]:
			output_file.write(' ' + str(v))
		output_file.write('\n')
	output_file.close()
	count_of_terms = len(d)
	print('Количество токенов: ' + repr(count_of_tokens))
	print('Количество терминов: ' + repr(count_of_terms))
	print('Средняя длина токена: ' + repr(count_of_chars_token//count_of_tokens))	
	print('Средняя длина термина: ' + repr(count_of_chars_term//count_of_terms))
main()
