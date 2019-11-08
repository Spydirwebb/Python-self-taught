"""Practicing with modules imported from another file.
Then practicing saving and extracting data a text file

A continues game of attack or block vs a stronger computer opponent
"""


import attack

my_health = 0
my_damage = 5
their_health = 0
their_damage = 7
win = False
new_or_load = input("New(n) or Load(l) game?: ")
if (new_or_load == 'n'):
    my_health = 100
    their_health = 100
elif(new_or_load == 'l'):
    health_values = []
    with open("save_file.txt","r") as load_file:
        for item in load_file.read().split("\n"):
            health_values.append(item)
    my_health = int(health_values[0])
    their_health = int(health_values[1])
else:
    print("New Game then")
attack.print_status(my_health, their_health)
while(win == False):
    my_pick = input("Pick attack(a), block(b), quit(q) save(s): ")
    their_pick = attack.their_pick()
    if(my_pick =='a' and their_pick == 'a'):
        their_health = attack.attack(their_health,my_damage)
        my_health = attack.attack(my_health,their_damage)
    elif(my_pick == 'a' and their_pick == 'b'):
        their_health = attack.block(their_health,my_damage)
    elif(my_pick == 'b' and their_pick == 'a'):
        my_health = attack.block(my_health,their_damage)
    elif(my_pick =='b' and their_pick =='b'):
        print ("Whoosh!")
    elif(my_pick == 's'):
        with open("save_file.txt","w+") as save_file:
            save_file.write(str(my_health)+"\n")
            save_file.write(str(their_health)+"\n")
        break
    elif(my_pick =='q'):
        print("Quit!")
        break
    else:
        print ("Not a valid entry. Please try again")
        continue
    win = attack.win(my_health, their_health)
    attack.print_status(my_health, their_health)
        
        
        
