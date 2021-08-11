def swap(L, i, j):
   temp = L[i]
   L[i] = L[j]
   L[j] = temp
# end of swap()

def sort(L):  # implements the Bubble Sort algorithm
   for i in range(len(L)-1,0,-1):  
      for j in range(i):
         if L[j]>L[j+1]:
            swap(L, j, j+1)
         # end if
      # end inner for
   # end outer for
# end sort()

def BinSearch(x, L):
   left = 0
   right = len(L)-1
   while left<=right:   # search space is not empty
      m = (left+right)//2
      if x == L[m]:
         return m
      elif x < L[m]:
         right = m-1
      else:  #  L[m] < x 
         left = m+1
      # end if-elif-else
   # end while
   # if this line is reached, None is returned
# end of BinSearch()


#-- main program --------------------------------------------------------------


# Search a list of words for a target 
target = 'seven'
words = ['one','two','three','four','five','six','seven','eight','nine','ten']

print(words)
sort(words)  # list must be sorted for binary search to work
print(words)
position = BinSearch(target, words)
print(target, 'found at position', position)


# Search a list of numbers for a target
target = 13
numbers = [2, 5, 7, 11, 15, 16, 20, 25]  # this list happens to already be sorted

print(numbers)
position = BinSearch(target, numbers)
print(target, 'found at position', position)
