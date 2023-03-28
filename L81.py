#Emily Nixon
def total_length(word, letter):
    total = 0
    total = len(word) + len(letter)
    print (total)

total_length("Queen","rules")

s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])
            

    
# the index=0 tells where to begin the loop over the word
#this means that while the index of the word is less than the length of the word, to keep going
#this means to move onto the next character in the word
#this prints the indexing of each word
