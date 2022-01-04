class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def __repr__(self):
        return f"{self.name} : {self.role}"

GodOptions = ["checkPlayer", "removePlayer", "checkAllPlayers"]
roles = ["doctor", "godFather", "detective", "normal mafia"]
players = []
playersName = []

print("\033[92mMAFIA desk\033[0m\n")
while True:
    try:
        playerCount = int(input("enter plyaer count : "))
        if playerCount < 6:
            print("\033[31mminimum player for mafia is\033[0m \033[33m6\033[0m\n")
        else:
            break
    except: print("\033[31mplayer count must be integer number\033[0m\n")

for n in range(1, playerCount+1):
    while True:
        try:
            player = Player(input(f"\nenter name player \033[36m{n}\033[0m : "), "normal person")
            if player.name == "":
                raise ValueError("player name can not be empty")
            elif player.name in playersName:
                raise ValueError("player name must be unique")
        except ValueError as error:
            print(f"\033[31m{error}\033[0m")
        else:
            break

    playersName.append(player.name)
    players.append((player.name, player.role))

players = dict(players)

# ---------------- for randomize ----------------
playersName = set(playersName)

roles = set(roles)
# ---------------- for randomize ----------------

iter_playersName = iter(playersName)

for role in roles:
    players[next(iter_playersName)] = role


all_roles = list(players.values())

while True:
    if all_roles.count("normal person") + all_roles.count("doctor") + all_roles.count("detective") == \
        all_roles.count("normal mafia") + all_roles.count("godFather"):
        print(f"\n\n*** \033[31mmafia win\033[0m ***\nGGWP")
        break
    
    if all_roles.count("normal mafia") + all_roles.count("godFather") == 0:
        print(f"\n\n*** \033[32mvillage win\033[0m ***\nGGWP")
        break


    print(f"\n\033[32mcommands --->\033[0m \033[35m{GodOptions}\033[0m")
    Godchoice = input("command : ")
    if Godchoice == "exit":
        break

    if Godchoice in GodOptions:
        if Godchoice == "checkPlayer":
            check = input("\n\033[33menter player name\033[0m : ")
            if check in players.keys():
                print(f"\033[36m{check}\033[0m role : \033[36m{players[check]}\033[0m")
            else:
                print("\033[31mthis player not defined\033[0m (or already removed)")
        elif Godchoice == "removePlayer":
            check = input("\n\033[33menter player name\033[0m : ")
            if check in players.keys():
                n = players.pop(check)
                all_roles.remove(n)
                print(f"{check} is \033[31mremoved\033[0m")
            else:
                print("\033[31mthis player not defined\033[0m (or already removed)")
        elif Godchoice == "checkAllPlayers":
            for player in players.items():
                print(f"\n\033[36m{player[0]}\033[0m role : \033[36m{player[1]}\033[0m")
            print(f"\nalive players : \033[33m{len(players)}\033[0m")
            
    else:
        print("\033[31mcommand not defined\033[0m")
