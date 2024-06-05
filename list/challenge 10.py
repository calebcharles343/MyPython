challenge = 'find the words starting with the given letter in a list'
food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

letter = input('Enter a letter')
for x in food:
     if x.startswith(letter):
         print(x)