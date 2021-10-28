def writing():
    file = open("text.txt" , "w")
    user = input("Write anything")
    file.write(user)
    file.close()
writing()
def reading():
    file = open("text.txt", "r")
    read = file.read()
    print(read)    
reading()