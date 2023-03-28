#Emily Nixon
def until_dot(statement):
    index = 0
    while index < len(statement) and statement[index] != ".":
        index +=1
    print(statement[:index])

until_dot("This is a sentence. This is another sentence.")
until_dot("please work omg")

#Don't use break at all 
def find_512():
    for x in range(100):
        for y in range(100):
            if x*y == 512:
                return f"{x} * {y} == 512"
print(find_512())


        
    
