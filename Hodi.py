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

def biggerlist():
    list1 = [1,2,4,17,32]
    list2 = [45,67,12,-40,78]

    list1sum = sum(list1)
    list2sum = sum(list2)
    try:
        if list1sum> list2sum:
        print("list 1 is bigger")
        else: print("list2 is the bigger one :) ")
    except:print("err")
