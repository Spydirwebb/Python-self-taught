import random

def attack(health,damage):
    chance = random.randint(1,10)
    if(chance >=9):
        print("***Missed!***")
        return health
    else:
        return (health-damage)

def block(health,damage):
    chance = random.randint(1,5)
    if(chance > 2):
        print ("xxxBlocked!xxx")
    else:
        health = health-damage
    return health
    
def print_status(my_health, their_health):
    print ("My Health: {}".format(my_health))
    print("Their health: {}".format(their_health))

def win(my_health, their_health):
    if(my_health <=0  and their_health<=0):
        print("---Mutual loss!---")
        return True
    elif(my_health <=0 ):
        print("---He won!---")
        return True
    elif(their_health <=0):
        print("+++I won!+++")
        return True
    else:
        return False

def their_pick():
    rando = random.randint(1,10)
    if(rando>7):
        return 'b'
    else:
        return 'a'

