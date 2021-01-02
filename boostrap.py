from searching import Searching
import time
sObj = Searching()

d = {
    1: "CHECK SUBTRING MATCHING",
    2: "SORT NUMBERS",

}

def print_d(d):
    for k, v in d.items():
        print(f"[{k}]: {v}")

rep = None
while rep != "exit":
    time.sleep(0.5)
    print("Choose  anumber from menu : ")
    print_d(d)
    rep = int(input("> "))

    if rep == 1:
        string = input("Enter a word: ")
        sub = input("Enter a substring: ")
        sObj.set_string_sub(string, sub)
        print(sObj.subString())
    elif rep == 2:
        pass

    else:
        print("UNKOWN COMAND.")
