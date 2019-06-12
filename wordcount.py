from nltk.corpus import stopwords
import re
import enchant

suffix = ['able','ac','acity','ocity','ade','age','aholic','oholic','al','algia','an','ian','ance','ant','ar','ard',
'arian','arium','ary','ate','ation','ative','cide','cracy','crat','cule','cy','cycle','dom','dox','ectomy','ed','ee',
'eer','emia','en','ence','ency','ent','er','ern','escence','ese','esque','ess','est','etic','ette','ful','fy','gam',
'gon','hood','ial','ian','iasis','iatric','ible','ic','ile','ily','ine','ing','ion','ious','ish','ism','ist','ite',
'itis','ity','ive','ization','ize','less','let','like','ling','loger','log','ly','ment','ness','oid','ology','oma',
'onym','opia','opsy','or','ory','osis','ostomy','ous','path','pathy','phile','phobia','phone','phyte','plegia','plegic',
'pnea','s','scopy','scribe','sect','ship','sion','some','sophy','th','tion','tome','trophy','tude','ty','ular','uous',
'ure','ward','ware','wise','y']


def root_mode(word):
	for i in range(suffix):
		pattern = re.compile(suffix[i] + "$")
		if re.search(pattern,word):
			word = re.split(pattern,word)[0]
	return word

#parses the text file and returns a list of words
def parse(file):
    with open(file, 'rb') as f:
        return  re.findall(re.compile('\w+'), f.read().lower())

#checks for an stop words present in the  text file
def stop_words_remove(word_list):
	filtered_words = []
	for word in word_list:
		if word not in stopwords.words('english'):
			filtered_words.append(word)
	print(filtered_words)
	print("filtered_words")
	return filtered_words

#checks if a word is present in the US English dictionary
def check_valid_word(word):
	d = enchant.Dict("en_US")
	return word if word != "" and d.check(word) and len(word) > 1 and not is_number(word) else ""

#checks if a string is a number 
def is_number(s):
    try:
        float(s)
        int(s)
        return True
    except ValueError:
        return False

#parses the dictionary to return the key with the max value
def getMax(dictionary):
	v, k =list(dictionary.values()), list(dictionary.keys())
	return k[v.index(max(v))]

#returns the final dictionary of root words from the text file with the word count 
def final_word(filename):
	word_list, output = stop_words_remove(parse(filename)), {}
	print(word_list)
	print("WORD LIST")

	for i in range(0,len(word_list)):
		print(i/float(len(word_list))*100)
		if check_valid_word(word_list[i]):
			if check_valid_word(root_mode(word_list[i])):
				insert_word = root_mode(word_list[i])
				output[insert_word] = output[insert_word] + 1 if insert_word in output else 1
			else:
				output[word_list[i]] = output[word_list[i]] + 1 if word_list[i] in output else 1
	
	return output

def top30FrequentWords(filename):
	i, result, output = 30, [], final_word(filename)
	print(output)
	print(len(output))
	while i and len(output.keys()):
		result.append(getMax(output))
		output.pop(getMax(output), None)
		i -= 1
	print("TOP 30 Words")

	return result


print(top25FrequentWords('/Users/yimingdai/Downloads/words.txt'))
