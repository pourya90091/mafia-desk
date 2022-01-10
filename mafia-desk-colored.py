class Player:
    def __init__(self, name="", role="normal person"):
        self.name = name
        self.role = role
    def __repr__(self):
        return f"{self.name} : {self.role}"

GodOptions = ["checkPlayer", "removePlayer", "inquiryPlayer", "checkAllPlayers"]
GodOptionsA = ["CP", "RP", "IP", "CAP"]
roles = ["doctor", "godFather", "detective", "normal mafia"]
players = []
playersName = []
exit = False

print("----------------------\n\033[92mMAFIA desk\033[0m\n")
print("for quit, type '\033[31mexit\033[0m'\n")

# ---------------------- <take player count> ----------------------
while True:
    try:
        playerCount = input("enter plyaer count : ")

        if playerCount == "exit" or int(playerCount) == 0:
            raise KeyboardInterrupt
        elif int(playerCount) < 6:
            raise KeyError
        else:
            playerCount = int(playerCount)
            break
    except ValueError:
        print("\033[31mplayer count must be integer number\033[0m\n")
    except KeyError:
        print("\033[31mminimum player for mafia is\033[0m \033[33m6\033[0m\n")
    except KeyboardInterrupt:
        exit = True
        break
# ---------------------- </take player count> ----------------------

if exit == False:

    # ---------------------- <generate players> ----------------------
    for n in range(1, playerCount+1):
        if exit == True:
            break

        while True:
            try:
                name = input(f"\nenter name player \033[36m{n}\033[0m : ")

                if name == "exit":
                    raise KeyboardInterrupt
                elif name == "":
                    raise ValueError("player name can not be empty")
                elif name in playersName:
                    raise ValueError("player name must be unique")
            except ValueError as error:
                print(f"\033[31m{error}\033[0m")
            except KeyboardInterrupt:
                exit = True
                break
            except NameError:
                exit = True
                break
            else:
                player = Player(name)
                playersName.append(player.name)
                players.append((player.name, player.role))
                break
    # ---------------------- </generate players> ----------------------

    if exit == False:

        players = dict(players)

        # ---------------- <randomize> ----------------
        playersName = set(playersName)
        roles = set(roles)

        iter_playersName = iter(playersName)

        for role in roles:
            players[next(iter_playersName)] = role
        # ---------------- </randomize> ----------------

        all_roles = list(players.values())

        # ------------------------------------- <main> -------------------------------------
        while True:
            if all_roles.count("normal person") + all_roles.count("doctor") + all_roles.count("detective") == \
                all_roles.count("normal mafia") + all_roles.count("godFather"):
                print(f"\n\n*** \033[31mmafia win\033[0m ***\nGGWP\n")
                break

            if all_roles.count("normal mafia") + all_roles.count("godFather") == 0:
                print(f"\n\n*** \033[32mvillage win\033[0m ***\nGGWP\n")
                break


            print(f"\n\033[32mcommands --->\033[0m \033[35m{GodOptions}\033[0m\n\033[32m{GodOptionsA}\033[0m")
            try:
                Godchoice = input("command : ")
                if Godchoice == "exit":
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                break

            if Godchoice in GodOptions or Godchoice in GodOptionsA:
                if Godchoice == "checkPlayer" or Godchoice == "CP":
                    name = input("\n\033[33menter player name\033[0m : ")
                    if name in players.keys():
                        print(f"\033[36m{name}\033[0m role : \033[36m{players[name]}\033[0m")
                    else:
                        print("\033[31mthis player not defined\033[0m (or already removed)")
                elif Godchoice == "removePlayer" or Godchoice == "RP":
                    name = input("\n\033[33menter player name\033[0m : ")
                    if name in players.keys():
                        print(f"\033[36m{name}\033[0m (\033[36m{players[name]}\033[0m) was \033[31mremoved\033[0m")
                        n = players.pop(name)
                        all_roles.remove(n)
                    else:
                        print("\033[31mthis player not defined\033[0m (or already removed)")
                elif Godchoice == "inquiryPlayer" or Godchoice == "IP":
                    name = input("\n\033[33menter player name\033[0m : ")
                    if name in players.keys():
                        if players[name] == "normal mafia":
                            print("\033[32myes\033[0m")
                        else:
                            print("\033[31mno\033[0m")
                    else:
                        print("\033[31mthis player not defined\033[0m (or already removed)")
                elif Godchoice == "checkAllPlayers" or Godchoice == "CAP":
                    for player in players.items():
                        print(f"\n\033[36m{player[0]}\033[0m role : \033[36m{player[1]}\033[0m")
                    print(f"\nalive players : \033[33m{len(players)}\033[0m")
            else:
                print("\033[31mcommand not defined\033[0m")
        # ------------------------------------- </main> -------------------------------------
