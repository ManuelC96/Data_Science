# Game (hangman)
# coding = uth-8
import random
import csv
import string

# data extraction
vocabulary = []
with open("netflix_titles.csv", encoding="utf8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        countries = row["country"].split(",")

        if "Italy" in countries:
            vocabulary.append(row["title"])

# game global variable
letters = [""]
attempts = 5
guessed = ""
# random word initialization
random.seed(a=0)
random_index =  random.randrange(0, len(vocabulary))
word = vocabulary[random_index].lower()
print(word)

def init_gussed(plainText):
    w=""
    for i in plainText:
        if i.isspace() or i in string.punctuation  :
            w += i
        else:
            w +="-"
    return w
def check_letter(l, w):
    found = False
    for i in w:
        if l == i:
            found = True
            break
    return found

def find_occ(l, w):
    occ = []
    for i in range(len(w)):
        if l == word[i]:
            occ.append(i)
    return occ

def sub_letters(l, pos, g):
    letter_list = list(g)
    letter_list[pos] = l
    return "".join(letter_list)
    



guessed = init_gussed(word)
print(guessed)
# game loop
game = True
while game:
    print("Try to guess\n Film is: {0}".format(guessed))

    print("You have {0} attempts".format(attempts))

    choice = input("Guess the film ( 0 to exit ) ")

    if choice == str(0):
        print("You loose")
        print("Film is {}".format(word))
        game = False

    elif choice.lower() == word:
        print("You win")
        game = False

    else:
        print("\n Error ")
        print("\n Extracted letters = {}  ".format(letters))
        choice = input("Choose a letter \n")
        choice.lower()
        if check_letter(choice, letters):
            print("letter arleady choice")
        else:
            letters.append(choice)
            if check_letter(choice, word):
                occ = find_occ(choice, word)
                for pos in occ:
                    guessed = sub_letters(choice, pos, guessed)
                    print(guessed)


            else:
                print("Letter not in word")
                attempts -= 1
                if attempts == 0:
                    print("You loose, no more attempt")
                    print("Film was {}".format(word))
                    game = False
