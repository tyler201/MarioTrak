# MarioTrak


import tkinter
import tkinter.messagebox
from collections import Counter
import sys
assert sys.version_info >= (3,6)

def user_search(username):
    users = open("UserDB.txt", "r")
    for user in users.readlines():
        user = (user.strip()).split(" : ")
        try:
            if user[1] == username:
                show = tkinter.Toplevel()
                label1 = tkinter.Label(show, text="Stats for " + user[1] + ":")
                label2 = tkinter.Label(show, text="ID: " + user[0])
                label3 = tkinter.Label(show, text="Races played: " + user[2])
                label4 = tkinter.Label(show, text="Races won: " + user[3])
                try:
                    label5 = tkinter.Label(show, text="Percentage: " + str(round((int(user[2])/int(user[3]))*100, 0)))
                except:
                    if user[2] == "0":
                        label5 = tkinter.Label(show, text="Percentage: 100.0")
                    else:
                        label5 = tkinter.Label(show, text="Percentage: 0.0")
                label1.grid(padx=20, pady=10, row=1, column=1)
                label2.grid(padx=20, pady=10, row=2, column=1)
                label3.grid(padx=20, pady=10, row=3, column=1)
                label4.grid(padx=20, pady=10, row=4, column=1)
                label5.grid(padx=20, pady=10, row=5, column=1)
                break
        except IndexError:
            pass
    else:
        print("User not found!")


def showhistory():
    view = tkinter.Toplevel()
    hdb = open("historyDB.txt", "r")
    lines = hdb.readlines()
    hdb.close()
    udb = open("userDB.txt", "r")
    users = udb.readlines()
    udb.close()
    cdb = open("characterDB.txt", "r")
    characters = cdb.readlines()
    cdb.close()
    rdb = open("trackDB.txt", "r")
    tracks = rdb.readlines()
    rdb.close()
    title = tkinter.Label(view, text="Race History")
    data = []
    for y in lines:
        y = y.strip().split(" : ")
        for user in users:
            user = user.strip().split(" : ")
            if y[0] == user[0]:
                y[0] = user[1]
            elif y[1] == user[0]:
                y[1] = user[1]
            elif y[2] == user[0]:
                y[2] = user[1]
            elif y[3] == user[0]:
                y[3] = user[1]
        for character in characters:
            character = character.strip().split(" : ")
            if y[4] == character[0]:
                y[4] = character[1]
            elif y[5] == character[0]:
                y[5] = character[1]
            elif y[6] == character[0]:
                y[6] = character[1]
            elif y[7] == character[0]:
                y[7] = character[1]
        for track in tracks:
            print(track)
            track = track.strip().split(" : ")
            if y[8] == track[0]:
                y[8] = track[1]
            elif y[9] == track[0]:
                y[9] = track[1]
            elif y[10] == track[0]:
                y[10] = track[1]
            elif y[11] == track[0]:
                y[11] = track[1]
        for user in users:
            user = user.strip().split(" : ")
            if y[12] == user[0]:
                y[12] = user[1]
            elif y[13] == user[0]:
                y[13] = user[1]
            elif y[14] == user[0]:
                y[14] = user[1]
            elif y[15] == user[0]:
                y[15] = user[1]
        data.append(y[0] + " : " + y[1] + " : " + y[2] + " : " + y[3] + " : " + y[4] + " : " + y[5] + " : " + y[6]  +
                    " : " + y[7]  + " : " + y[8]  + " : " + y[9] + " : " + y[10] + " : " + y[11] + " : " + y[12]  +
                    " : " + y[13] + " : " + y[14] + " : " + y[15])
    title.grid(padx=20, pady=10, row=1, column=1, columnspan=17)
    tkinter.Label(view, width=15, text="Player 1", relief="ridge").grid(row=2, column=1)
    tkinter.Label(view, width=15, text="Player 2", relief="ridge").grid(row=2, column=2)
    tkinter.Label(view, width=15, text="Player 3", relief="ridge").grid(row=2, column=3)
    tkinter.Label(view, width=15, text="Player 4", relief="ridge").grid(row=2, column=4)
    tkinter.Label(view, width=15, text="P1 Character", relief="ridge").grid(row=2, column=5)
    tkinter.Label(view, width=15, text="P2 Character", relief="ridge").grid(row=2, column=6)
    tkinter.Label(view, width=15, text="P3 Character", relief="ridge").grid(row=2, column=7)
    tkinter.Label(view, width=15, text="P4 Character", relief="ridge").grid(row=2, column=8)
    tkinter.Label(view, width=15, text="Track 1", relief="ridge").grid(row=2, column=9)
    tkinter.Label(view, width=15, text="Track 2", relief="ridge").grid(row=2, column=10)
    tkinter.Label(view, width=15, text="Track 3", relief="ridge").grid(row=2, column=11)
    tkinter.Label(view, width=15, text="Track 4", relief="ridge").grid(row=2, column=12)
    tkinter.Label(view, width=15, text="Track 1 Winner", relief="ridge").grid(row=2, column=13)
    tkinter.Label(view, width=15, text="Track 2 Winner", relief="ridge").grid(row=2, column=14)
    tkinter.Label(view, width=15, text="Track 3 Winner", relief="ridge").grid(row=2, column=15)
    tkinter.Label(view, width=15, text="Track 4 Winner", relief="ridge").grid(row=2, column=16)
    num = 2
    for x in data:
        num = num + 1
        x = x.strip().split(" : ")
        num2 = 0
        for entity in x:
            num2 = num2 + 1
            tkinter.Label(view, width=15, text=entity, relief="ridge").grid(row=num, column=num2)

def create_user(name):
    nametaken = False
    if name == "":
        nametaken = True
    ufile = open("userDB.txt", "r")
    contents = ufile.readlines()
    for people in contents:
        people = people.split(" : ")
        try:
            if name == people[1]:
                nametaken = True
                break
        except IndexError:
            pass
    if nametaken == True:
        ufile.close()
        tkinter.messagebox.showinfo("Error!", "Name not valid! Please enter a name that is valid.")
    else:
        id = str(len(contents))
        if len(id) == 1:
            id = "0" + id
        ufile.close()
        ufile = open("userDB.txt", "w")
        for x in contents:
            ufile.write(x)
        if contents == []:
            print("File empty, no newline.")
        else:
            ufile.write("\n")
        ufile.write(id + " : " + name + " : " + "0" + " : " + "0")
        ufile.close()
        lfile = open("leaderDB.txt", "r")
        contents = lfile.readlines()
        lfile.close()
        lfile = open("leaderDB.txt", "w")
        for x in contents:
            lfile.write(x)
        if contents == []:
            print("File empty, no newline.")
        else:
            lfile.write("\n")
        lfile.write(id + " : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0 : 0")
        tkinter.messagebox.showinfo("Success!", name.title() + " has been added to the database!")


def TrackSearch(trackname):
    tracks = open("trackDB.txt", "r")
    for track in tracks.readlines():
        track = (track.strip()).split(" : ")
        try:
            if track[1] == trackname:
                show = tkinter.Toplevel()
                label1 = tkinter.Label(show, text="Stats for " + track[1] + ":")
                label2 = tkinter.Label(show, text="ID: " + track[0])
                label3 = tkinter.Label(show, text="Cup: " + track[2])
                label4 = tkinter.Label(show, text="Times played: " + track[3])
                ldb = open("leaderDB.txt", "r")
                vals = ldb.readlines()
                ldb.close()
                coursevals = {}
                for x in vals:
                    x = x.strip().split(" : ")
                    coursevals[x[0]] = x[int(track[0])+1]
                key, value = max(coursevals.items(), key=lambda x: x[1])
                udb = open("userDB.txt", "r")
                users = udb.readlines()
                udb.close()
                name = "None"
                for y in users:
                    y = y.strip().split(" : ")
                    if y[0] == key:
                        name = str(y[1])
                    else:
                        pass
                label5 = tkinter.Label(show, text="Best user: " + name)
                label1.grid(padx=20, pady=10, row=1, column=1)
                label2.grid(padx=20, pady=10, row=2, column=1)
                label3.grid(padx=20, pady=10, row=3, column=1)
                label4.grid(padx=20, pady=10, row=4, column=1)
                label5.grid(padx=20, pady=10, row=5, column=1)
        except IndexError:
            pass


def NewRace(p1, p2, p3, p4, c1, c2, c3, c4, r1, r2, r3, r4, rw1, rw2, rw3, rw4):
    udb = open("userDB.txt", "r")
    contents = udb.readlines()
    udb.close()
    for x in contents:
        x = x.split(" : ")
        if x[1] == p1:
            p1 = x[0]
            print("P1")
        elif x[1] == p2:
            p2 = x[0]
            print("P2")
        elif x[1] == p3:
            p3 = x[0]
            print("P3")
        elif x[1] == p4:
            p4 = x[0]
            print("P4")
        if x[1] == rw1:
            rw1 = x[0]
            print("RW1")
        elif x[1] == rw2:
            rw2 = x[0]
            print("RW2")
        elif x[1] == rw3:
            rw3 = x[0]
            print("RW3")
        elif x[1] == rw4:
            rw4 = x[0]
            print("RW4")

    cdb = open("characterDB.txt", "r")
    contents = cdb.readlines()
    cdb.close()
    for x in contents:
        x = x.strip().split(" : ")
        print(x[1],c1,c2,c3,c4)
        if x[1] == c1:
            c1 = x[0]
            print("C1")
        elif x[1] == c2:
            c2 = x[0]
            print("C2")
        elif x[1] == c3:
            c3 = x[0]
            print("C3")
        elif x[1] == c4:
            c4 = x[0]
            print("C4")

    tdb = open("trackDB.txt", "r")
    contents = tdb.readlines()
    tdb.close()
    for x in contents:
        x = x.split(" : ")
        if x[1] == r1:
            r1 = x[0]
            print("R1")
        elif x[1] == r2:
            r2 = x[0]
            print("R2")
        elif x[1] == r3:
            r3 = x[0]
            print("R3")
        elif x[1] == r4:
            r4 = x[0]
            print("R4")

    words = [rw1, rw2, rw3, rw4]
    most_common_words = [word for word, word_count in Counter(words).most_common()]
    if len(most_common_words) == 4:
        overall = "None"
    else:
        overall = most_common_words[0]
    with open("historyDB.txt", "r") as history:
        old = history.readlines()
        history.close()
    new = open("historyDB.txt", "w")
    new.write(str(p1 + " : " + p2 + " : " + p3 + " : " + p4 + " : " + c1 + " : " + c2 + " : " + c3 + " : " + c4 + " : "
                  + r1 + " : " + r2 + " : " + r3 + " : " + r4 + " : " + rw1 + " : " + rw2 + " : " + rw3 + " : " + rw4 +
                  " : " + overall) + "\n")
    for race in old:
        new.write(race)
    new.close()

    udb = open("userDB.txt", "r")
    old = udb.readlines()
    print(old)
    udb.close()
    new = []
    done = []
    for x in old:
        try:
            x = x.strip().split(" : ")
            y = x
            x[1]
            ylist = y

            if x[0] == p1 or x[0] == p2 or x[0] == p3 or x[0] == p4:
                print(done)
                if ylist[0] not in done:
                    print("Adding race to",x[0])
                    try:
                        y = str(
                            "{0} : {1} : {2} : {3}".format(ylist[0], ylist[1], str(int(ylist[2]) + 4), ylist[3]))

                        done.append(ylist[0])
                    except ZeroDivisionError:
                        y = str(ylist[0] + " : " + ylist[1] + " : " + str(int(ylist[2]) + 4) + " : " + ylist[3])
                        done.append(ylist[0])
                else:
                    print("")

            if x[0] == rw1 or x[0] == rw2 or x[0] == rw3 or x[0] == rw4:
                    for cheese in range([rw1, rw2, rw3, rw4].count(x[0])):
                        print("Adding win to",x[1])
                        y = ylist[0] + " : " + ylist[1] + " : " + str(int(y.split(" : ")[2])) + " : " + str(int(ylist[3])+1)
                        ylist = y.split(" : ")
                        print(ylist)
            print(y)
            new.append(y)

        except IndexError:
            print("empty")
            pass

    udb = open("userDB.txt", "w")
    for x in new:
        udb.write(x + "\n")

    tdb = open("trackDB.txt", "r")
    contents = tdb.readlines()
    tdb.close()
    newvars = []
    for x in contents:
        x = x.strip().split(" : ")
        if x[0] == r1:
            x[3] = int(x[3])+1
        if x[0] == r2:
            x[3] = int(x[3])+1
        if x[0] == r3:
            x[3] = int(x[3])+1
        if x[0] == r4:
            x[3] = int(x[3])+1
        y = x[0] + " : " + x[1] + " : " + x[2] + " : " + str(x[3]) + " : " + x[4]
        newvars.append(y)
    tdb = open("trackDB.txt", "w")
    for x in newvars:
        tdb.write(x + "\n")
    tdb.close()

    ldb = open("leaderDB.txt", "r")
    contents = ldb.readlines()
    ldb.close()
    newcontent = []
    for x in contents:
        x = x.strip().split(" : ")
        try:
            x[1]
        except IndexError:
            pass
        if x[0] == rw1:
            x[int(rw1) + 1] = str(int(x[int(rw1) + 1]) + 1)
        elif x[0] == rw2:
            x[int(rw2) + 1] = str(int(x[int(rw2) + 1]) + 1)
        elif x[0] == rw3:
            x[int(rw3) + 1] = str(int(x[int(rw3) + 1]) + 1)
        elif x[0] == rw4:
            x[int(rw4) +1 ] = str(int(x[int(rw4) + 1]) + 1)
        else:
            x = x
        newcontent.append(x)
    ldb = open("leaderDB.txt", "w")
    for x in newcontent:
        z = ""
        for y in range(len(x)):
            z = z + x[y] + " : "
        z = z[:-2]
        ldb.write(z + "\n")
    ldb.close()
    tkinter.messagebox.showinfo("Success!", overall.title() + ", You won! Your stats have been updated!")


# UserSearch("Test")
# TrackSearch("Rainbow Road")
# NewRace("00", "01", "02", "03", "18", "12", "21", "14", "12", "13", "14", "15", "01", "03", "02", "00", "00")
# CreateUser("Test3")


def LogWindow():

    def PChanged(p1var, p2var, p3var, p4var, playinglist, *args):
        print("I'm doing something!")
        playinglist["player1"] = str(p1var.get())
        playinglist["player2"] = str(p2var.get())
        playinglist["player3"] = str(p3var.get())
        playinglist["player4"] = str(p4var.get())
        print(playinglist)
        menu1 = RaceWin1["menu"]
        menu1.delete(0, "end")
        menu2 = RaceWin2["menu"]
        menu2.delete(0, "end")
        menu3 = RaceWin3["menu"]
        menu3.delete(0, "end")
        menu4 = RaceWin4["menu"]
        menu4.delete(0, "end")
        for x in playinglist.values():
            menu1.add_command(label=x, command=lambda v=x: rw1var.set(v))
            menu2.add_command(label=x, command=lambda v=x: rw2var.set(v))
            menu3.add_command(label=x, command=lambda v=x: rw3var.set(v))
            menu4.add_command(label=x, command=lambda v=x: rw4var.set(v))
        Player1.update()




    playinglist = {"player1": "", "player2": "", "player3": "", "player4": ""}
    playerlist = []
    charlist = []
    tracklist = []
    log = tkinter.Toplevel()

    players = open("userDB.txt", "r")
    playersvar = players.readlines()
    players.close()
    for x in playersvar:
        try:
            playerlist.append(x.split(" : ")[1].strip())
        except IndexError:
            pass

    tracks = open("trackDB.txt", "r")
    tracksvar = tracks.readlines()
    tracks.close()
    for x in tracksvar:
        try:
            tracklist.append(x.split(" : ")[1].strip())
        except IndexError:
            pass

    characters = open("characterDB.txt", "r")
    charvar = characters.readlines()
    characters.close()
    for x in charvar:
        try:
            charlist.append(x.split(" : ")[1].strip())
        except IndexError:
            pass

    p1var = tkinter.StringVar()
    p1var.set("Player 1")
    p2var = tkinter.StringVar()
    p2var.set("Player 2")
    p3var = tkinter.StringVar()
    p3var.set("Player 3")
    p4var = tkinter.StringVar()
    p4var.set("Player 4")
    c1var = tkinter.StringVar()
    c1var.set("Character 1")
    c2var = tkinter.StringVar()
    c2var.set("Character 2")
    c3var = tkinter.StringVar()
    c3var.set("Character 3")
    c4var = tkinter.StringVar()
    c4var.set("Character 4")
    r1var = tkinter.StringVar()
    r1var.set("Track 1")
    r2var = tkinter.StringVar()
    r2var.set("Track 2")
    r3var = tkinter.StringVar()
    r3var.set("Track 3")
    r4var = tkinter.StringVar()
    r4var.set("Track 4")
    rw1var = tkinter.StringVar()
    rw1var.set("Winner 1")
    rw2var = tkinter.StringVar()
    rw2var.set("Winner 2")
    rw3var = tkinter.StringVar()
    rw3var.set("Winner 3")
    rw4var = tkinter.StringVar()
    rw4var.set("Winner 4")
    p1var.trace_variable("w",
                         lambda name1, name2, op, x=100, y=200: PChanged(p1var, p2var, p3var, p4var, playinglist, name1,
                                                                         name2, op))
    p2var.trace_variable("w",
                         lambda name1, name2, op, x=100, y=200: PChanged(p1var, p2var, p3var, p4var, playinglist, name1,
                                                                         name2, op))
    p3var.trace_variable("w",
                         lambda name1, name2, op, x=100, y=200: PChanged(p1var, p2var, p3var, p4var, playinglist, name1,
                                                                         name2, op))
    p4var.trace_variable("w",
                         lambda name1, name2, op, x=100, y=200: PChanged(p1var, p2var, p3var, p4var, playinglist, name1,
                                                                         name2, op))

    playerlabel = tkinter.Label(log, text="Players:")
    Player1 = tkinter.OptionMenu(log, p1var, *playerlist)
    Player1.config(width=10)
    Player2 = tkinter.OptionMenu(log, p2var, *playerlist)
    Player2.config(width=10)
    Player3 = tkinter.OptionMenu(log, p3var, *playerlist)
    Player3.config(width=10)
    Player4 = tkinter.OptionMenu(log, p4var, *playerlist)
    Player4.config(width=10)
    characterlabel = tkinter.Label(log, text="Characters:")
    Character1 = tkinter.OptionMenu(log, c1var, *charlist)
    Character1.config(width=10)
    Character2 = tkinter.OptionMenu(log, c2var, *charlist)
    Character2.config(width=10)
    Character3 = tkinter.OptionMenu(log, c3var, *charlist)
    Character3.config(width=10)
    Character4 = tkinter.OptionMenu(log, c4var, *charlist)
    Character4.config(width=10)
    racelabel = tkinter.Label(log, text="Tracks:")
    Race1 = tkinter.OptionMenu(log, r1var, *tracklist)
    Race1.config(width=10)
    Race2 = tkinter.OptionMenu(log, r2var, *tracklist)
    Race2.config(width=10)
    Race3 = tkinter.OptionMenu(log, r3var, *tracklist)
    Race3.config(width=10)
    Race4 = tkinter.OptionMenu(log, r4var, *tracklist)
    Race4.config(width=10)
    winnerlabel = tkinter.Label(log, text="Winners:")
    RaceWin1 = tkinter.OptionMenu(log, rw1var, *playinglist)
    RaceWin1.config(width=10)
    RaceWin2 = tkinter.OptionMenu(log, rw2var, *playinglist)
    RaceWin2.config(width=10)
    RaceWin3 = tkinter.OptionMenu(log, rw3var, *playinglist)
    RaceWin3.config(width=10)
    RaceWin4 = tkinter.OptionMenu(log, rw4var, *playinglist)
    RaceWin4.config(width=10)
    logbutton = tkinter.Button(log, text="Confirm Results!", command= lambda: NewRace(p1var.get(), p2var.get(),
                                                                                      p3var.get(), p4var.get(),
                                                                                      c1var.get(), c2var.get(),
                                                                                      c3var.get(), c4var.get(),
                                                                                      r1var.get(), r2var.get(),
                                                                                      r3var.get(), r4var.get(),
                                                                                      rw1var.get(), rw2var.get(),
                                                                                      rw3var.get(), rw4var.get()))
    playerlabel.grid(padx=20, pady=10, row=1, column=1, columnspan=4)
    Player1.grid(row=2, column=1, ipadx=20)
    Player2.grid(row=2, column=2, ipadx=20)
    Player3.grid(row=2, column=3, ipadx=20)
    Player4.grid(row=2, column=4, ipadx=20)
    characterlabel.grid(padx=20, pady=10, row=3, column=1, columnspan=4)
    Character1.grid(row=4, column=1, ipadx=20)
    Character2.grid(row=4, column=2, ipadx=20)
    Character3.grid(row=4, column=3, ipadx=20)
    Character4.grid(row=4, column=4, ipadx=20)
    racelabel.grid(padx=20, pady=10, row=5, column=1, columnspan=4)
    Race1.grid(row=6, column=1, ipadx=20)
    Race2.grid(row=6, column=2, ipadx=20)
    Race3.grid(row=6, column=3, ipadx=20)
    Race4.grid(row=6, column=4, ipadx=20)
    winnerlabel.grid(padx=20, pady=10, row=7, column=1, columnspan=4)
    RaceWin1.grid(row=8, column=1, ipadx=20)
    RaceWin2.grid(row=8, column=2, ipadx=20)
    RaceWin3.grid(row=8, column=3, ipadx=20)
    RaceWin4.grid(row=8, column=4, ipadx=20)
    logbutton.grid(row=9,column=2,ipadx=20, columnspan=2)


def UserWindow():
    newusr = tkinter.Toplevel(top)
    UserLabel = tkinter.Label(newusr, text="Name:")
    TextEntry = tkinter.Entry(newusr)
    GoButton = tkinter.Button(newusr, text="Add User!", command=lambda: create_user(TextEntry.get()))
    UserLabel.grid(padx=20, pady=10, row=1, column=2)
    TextEntry.grid(padx=20, pady=10, row=1, column=3)
    GoButton.grid(padx=20, pady=10, row=2, column=2, columnspan=2)


def PickSearch(mode, query):
    print("I'm doin something.")
    print(mode)
    if mode == "User":
        user_search(query)
    elif mode == "Track":
        TrackSearch(query)


def StatsWindow():

    def GetList(modestr, *args):
        print("Doing stuff")
        print(modestr)
        if modestr == "User":
            print("User")
            x = open("userDB.txt", "r")
        elif modestr == "Track":
            print("Track")
            x = open("trackDB.txt", "r")

        y = x.readlines()
        menu = Selector["menu"]
        menu.delete(0, "end")
        for z in y:
            z = z.strip().split(" : ")
            menu.add_command(label=z[1], command=lambda v=z[1]: query.set(v))
            query.set(z[1])

    possible = [""]
    view = tkinter.Toplevel()
    mode = tkinter.StringVar()
    mode.set("User")
    mode.trace_variable("w", lambda name1, name2, op: GetList(mode.get()))
    query = tkinter.StringVar()
    query.set("Select...")
    SearchLabel = tkinter.Label(view, text="Search Options:")
    SearchButton = tkinter.Button(view, text="Search!", command=lambda: PickSearch(mode.get(), query.get()))
    Selector = tkinter.OptionMenu(view, query, *possible)
    UserSearch = tkinter.Radiobutton(view, text="User Search", variable=mode, value="User")
    TrackSearch = tkinter.Radiobutton(view, text="Track Search", variable=mode, value="Track")
    ShowHistory = tkinter.Button(view, text="Show Race History", command=lambda: showhistory())
    SearchLabel.grid(padx=20, pady=10, row=1, column=1, columnspan=2)
    Selector.grid(padx=20, pady=10, row=2, column=1, columnspan=2)
    UserSearch.grid(padx=20, pady=10, row=3, column=1, columnspan=2)
    TrackSearch.grid(padx=20, pady=10, row=4, column=1, columnspan=2)
    SearchButton.grid(padx=20, pady=10, row=5, column=1)
    ShowHistory.grid(padx=20, pady=10, row=5, column=2)


top = tkinter.Tk()
top.title("MarioTrak 1.0")

Input = tkinter.Button(text="Input Race Data", command=LogWindow)
View = tkinter.Button(text="View Statistics", command=StatsWindow)
Title = tkinter.Label(text="Current Leaders (Best win/loss ratio)", relief="flat")
New = tkinter.Button(text="Create New User", command=UserWindow)

Input.grid(padx=20, pady=10, row=1, column=1)
View.grid(padx=20, pady=10, row=1, column=4)
Title.grid(padx=20, pady=10, row=2, column=2, columnspan=2, rowspan=1)
New.grid(padx=20, pady=10, row=1, column=2, columnspan=2)

tablecontents = open("userDB.txt", "r")
userdata = tablecontents.readlines()
tablecontents.close()
userdict = {}
number = -1

print(len(userdata))
for empty in userdata:
    number = number + 1
    try:
        x = userdata[number].split(" : ")
        x = x[1].strip()
        y = userdata[number].split(" : ")
        y = y[3].strip() + "/" + y[2].strip()
    except IndexError:
        x = ""
        y = ""
    userdict[x] = y

num = 3
for entry in sorted(userdict.items(), key=lambda x: x[1], reverse=True):
    num = num + 1
    Label = tkinter.Label(text=entry[0], width=20, relief="ridge", padx=15)
    Label2 = tkinter.Label(text=entry[1], width=20, relief="ridge", padx=15)
    Label.grid(row=num, column=2)
    Label2.grid(row=num, column=3)
top.wait_window()
top.mainloop()
