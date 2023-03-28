#Emily Nixon
def count_character(word , letter):
    total= 0
    for n in word:
        if n == letter:
            total = total +1
    print(total)

count_character("banana" , "a")

#Index < len(s) will make it so that while the variable being indexed is less than the len of s, it keeps going
# s[index] != " " tells the code where the index is
# index += 1 tells the code that it is greater than 1
#print(s[index]) prints the outcome of the code
#The code is trying to count how many words are in the string, therefore it will print 3
        
