# Bruk Tewelde
# PSID 1834503

d={}
for i in range(5):
    j=int(input("Enter player %s's jersey number:\n" % str(i+1)))
    r=int(input("Enter player %s's rating:\n" % str(i+1)))

    if j not in d:
        d[j]=r
    print()

print("ROSTER")
for m,v in sorted(d.items()):
    print("Jersey number: %d, Rating: %d" % (m,v))
def print_menu():
   menuOp = """MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit

Choose an option:"""
   return menuOp
# These lines of code represents what will the user need to input when choosing the "a" option
def main():
    while(True):
        x = input()
        if(x=='a'):
            j=int(input("Enter a new player jersey number:\n"))
            r=int(input("Enter player''s rating:\n"))
            if j not in d:
                d[j]=r
            else:
                print("\nThe Player already in the list")
# These lines of code represents the output roster option on the menu
        elif(x=='o'):
            print("ROSTER")
            for m,v in sorted(d.items()):
                print("Jersey number:%d,Rating:%d" % (m,v))
# These lines of code represents the remove player option
        elif(x=='d'):
            j=int(input("\nEnter a jersey number:\n"))

            if j in d:
                del d[j]
            else:
                print("\nThe Player is not in the list")
# These lines of code represents the updating roster option on the menu
        elif(x=='u'):
            j=int(input("\nEnter a jersey number:\n"))

            if j in d:
                r=int(input("\nEnter a new rating for the player:\n"))
                d[j]=r
            else:
                print("\nThe Player is not in the list")
# These lines of code represents the output of the players rating on the menu
        elif(x=='r'):
            r=int(input("\nEnter a rating:\n"))

            for m,v in sorted(d.items()):
                if v > r:
                    print("Jersey number:%d,Rating:%d" % (m,v))
# These lines of code represents the option on the menu to quit
        elif(x=='q'):
            print()
            break
# These line of code represents what will be output when chosing the options and inputing players and ratings
print()
print(print_menu())
