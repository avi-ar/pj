def reciver(): 
    num1= int(input("please insert number "))
    sum = 0 
    try:
        while sum >= 0 :
            sum = int(input("please insert number "))
            sum = (sum + num1)
            print(sum)
    except:print("err")


def reciver1():
    word = input("please insert a word")
    word1 = "tbd"
    try:
        while word1 != word:
            word = input("please insert a word")
            word1 = word
            word = input("please insert a word")
            if word == word1: print("gj")
            break
    except:print("ERR")