#Akhil Senthil
#aksenthi@ucsc.edu
#This program uses the makeSieve function to identify prime numbers with the given input from a user.


import math




def makeSieve(n):
	primes = [False, False]
	for i in range(0, n + 1):
		if i > 1:
			for num in range(2, i):
				if i%num == 0:
					primes.append(False)
					break
			else:
				primes.append(True) 

	return primes
def getPrimes(n):
	#nums = []
	j = makeSieve(n)
	rows = 0
	for i in range(len(j)):
		if j[i] ==  True:
			print(str(i), end = ' ')
			rows = rows + 1
			if rows % 10 == 0:
				print('')
			


	print('')



		

#main_program

if __name__=='__main__':
	print('')
	user = int(input('Enter a positive integer: '))
	pos = False
	if user > 0:
		pos = True
	while pos ==  False:
		user = int(input('Please enter a positive integer: '))
		if user > 0:
			pos = True
	s = makeSieve(user)
	counter = 0
	for i in range(len(s)):
		if s[i] == True:
			counter = counter + 1
	print('')
	print('There are ' + str(counter) + ' prime numbers less than or equal to ' + str(user) + ':')
	print('')
	getPrimes(user)
	if user > 1:
		print('')
	
#end if
