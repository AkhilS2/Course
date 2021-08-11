import math

def squares(n):
	squares= []
	for i in range (1, n+1):
		squares.append(i ** 2)
	return tuple(squares)

print(squares(10))

def wordFreq(s):
	words = s.split()
	wordFreq = {}
	for i in range(len(words)):
		if i == 0:
			wordFreq[words[i]] = 1
		elif words[i] in wordFreq:
			wordFreq[words[i]] += 1
		else:
			wordFreq[words[i]] = 1
	return wordFreq
	#for i in range(len(words)):


print(wordFreq('One two three four four two two three three'))