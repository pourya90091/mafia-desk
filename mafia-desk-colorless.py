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

print("----------------------\nMAFIA desk\n")
print("for quit, type 'exit'\n")

# ---------------------- <take player count> ----------------------
while True:
    try:
        playerCount = input("enter plyaer count : ")

        if playerCount == "exit" or int(playerCount) == 0:
            raise KeyboardInterrupt("exit")
        elif int(playerCount) < 6:
            raise KeyError
        else:
            playerCount = int(playerCount)
            break
    except ValueError:
        print("player count must be integer number\n")
    except KeyError as error:
        print("minimum player for mafia is 6\n")
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
                name = input(f"\nenter name player {n} : ")

                if name == "exit":
                    raise KeyboardInterrupt("exit")
                elif name == "":
                    raise ValueError("player name can not be empty")
                elif name in playersName:
                    raise ValueError("player name must be unique")
            except ValueError as error:
                print(f"{error}")
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
                print(f"\n\n*** mafia win ***\nGGWP\n")
                break

            if all_roles.count("normal mafia") + all_roles.count("godFather") == 0:
                print(f"\n\n*** village win ***\nGGWP\n")
                break


            print(f"\ncommands ---> {GodOptions}\n{GodOptionsA}")
            try:
                Godchoice = input("command : ")
                if Godchoice == "exit":
                    raise KeyboardInterrupt("exit")
            except KeyboardInterrupt:
                break

            if Godchoice in GodOptions or Godchoice in GodOptionsA:
                if Godchoice == "checkPlayer" or Godchoice == "CP":
                    name = input("\nenter player name : ")
                    if name in players.keys():
                        print(f"{name} role : {players[name]}")
                    else:
                        print("this player not defined (or already removed)")
                elif Godchoice == "removePlayer" or Godchoice == "RP":
                    name = input("\nenter player name : ")
                    if name in players.keys():
                        print(f"{name} ({players[name]}) was removed")
                        n = players.pop(name)
                        all_roles.remove(n)
                    else:
                        print("this player not defined (or already removed)")
                elif Godchoice == "inquiryPlayer" or Godchoice == "IP":
                    name = input("\nenter player name : ")
                    if name in players.keys():
                        if players[name] == "normal mafia":
                            print("yes")
                        else:
                            print("no")
                    else:
                        print("this player not defined (or already removed)")
                elif Godchoice == "checkAllPlayers" or Godchoice == "CAP":
                    for player in players.items():
                        print(f"\n{player[0]} role : {player[1]}")
                    print(f"\nalive players : {len(players)}")
            else:
                print("command not defined")
        # ------------------------------------- </main> -------------------------------------
