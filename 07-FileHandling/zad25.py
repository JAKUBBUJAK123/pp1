import re
text = 'To be, or not to be, that is the question'

count = re.findall('[ ]' , text)
wordnum = len(count) + 1

print(wordnum)
