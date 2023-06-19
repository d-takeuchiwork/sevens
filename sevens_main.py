from tkinter import *
import random
import time
import operator
import os
root = Tk()
root.title(u'sevens')
path = os.getcwd()



#カードの構造体
class Card:
    def __init__ (self,suit,rank,image,back_image):
        self.suit = suit
        self.rank = rank
        self.image = image
        self.back_image = back_image
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank


#初期値の入力
CARDDECK = [] #山札
HAND = [0] * 12 #手札
NPC1 = [0] * 12#相手の手札
NPC2 = [0] * 12
NPC3 = [0] * 12
backimage = PhotoImage(file = "./gif/z2.gif") #背面の画像生成
PLACE = [[Card(-1,-1,backimage,backimage) for i in range(13)] for j in range(4)] #場の初期化
canvas = Canvas(root,width = 1440,height = 900)
npctuenF = 0
game_endflag = 0




#カードを初期の位置に入れる関数
def card_set():
    global backimage
    for s in range(4):
        for r in range(13):
            name = "./gif/"
            if s == 0:
                name += "s"
            elif s == 1:
                name += "h"
            elif s == 2:
                name += "c"
            else:
                name += "d"
            name += str(r+1)
            name += ".gif"
            image = PhotoImage(file = name)
            card = Card(s, r+1, image, backimage)


            #7図柄のときは場に入れる
            if r == 6:
                if s == 0:
                    PLACE[0][6] = card
                elif s == 1:
                    PLACE[1][6] = card
                elif s == 2:
                    PLACE[2][6] = card
                else:
                    PLACE[3][6] = card
            else:
                CARDDECK.append(card)

#山札のカードをシャッフルする関数
def card_deal():
    random.shuffle(CARDDECK)
    j = 0
    k = 0
    l = 0
    for i in range(len(CARDDECK)):
        if i < 12:
            HAND[i] = CARDDECK[i]
        elif i < 24:
            NPC1[j] = CARDDECK[i]
            j+=1
        elif i < 36:
            NPC2[k] = CARDDECK[i]
            k+=1
        else:
            NPC3[l] = CARDDECK[i]
            l+=1

    HAND.sort(key = operator.attrgetter("suit"))
    HAND.sort(key = operator.attrgetter("rank"))

#カードを出力する関数
def ShowBan():
    canvas.pack()
    canvas.create_rectangle(0,0,1440,850,fill = "green")

    #NPCの手札を裏面で表示する
    pos = 100
    pos1 = 590
    pos2 = 1080
    for i in range(len(NPC1)):

        canvas.create_image(pos ,75 ,image = NPC1[i].back_image)
        pos += 20

    for i in range(len(NPC2)):
        canvas.create_image(pos1 ,75 ,image = NPC2[i].back_image)
        pos1 += 20

    for i in range(len(NPC3)):
        canvas.create_image(pos2 ,75 ,image = NPC3[i].back_image)
        pos2 += 20

    #場に出ているカードを表示する。
    pos = 100
    hei = 250
    for i in range(4):
        for j in range(13):
            canvas.create_image(pos ,hei ,image = PLACE[i][j].image)
            pos += 80
        hei += 120
        pos = 100

    #自分の手札を表で表示する
    pos = 100
    for i in range(len(HAND)):
        canvas.create_image(pos ,775 ,image = HAND[i].image)
        pos += 50



def npczturn():
    CARDNUMBER = []
    global npctuenF
    npctuenF = 0


    #NPC1の番
    for i in range(len(NPC1)):
        if NPC1[i].rank == 1:
            if PLACE[NPC1[i].suit][NPC1[i].rank].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif NPC1[i].rank == 13:
            if PLACE[NPC1[i].suit][NPC1[i].rank-2].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif PLACE[NPC1[i].suit][NPC1[i].rank].suit >= 0 or PLACE[NPC1[i].suit][NPC1[i].rank-2].suit >= 0:
            CARDNUMBER.append(i)

    if len(CARDNUMBER) > 0:
        random.shuffle(CARDNUMBER)

        PLACE[ NPC1[CARDNUMBER[0]].suit][ NPC1[ CARDNUMBER[0] ].rank - 1] = NPC1[CARDNUMBER[0]]
        del NPC1[CARDNUMBER[0]]

        ShowBan()

    CARDNUMBER.clear()

    #NPC2の番
    for i in range(len(NPC2)):
        if NPC2[i].rank == 1:
            if PLACE[NPC2[i].suit][NPC2[i].rank].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif NPC2[i].rank == 13:
            if PLACE[NPC2[i].suit][NPC2[i].rank-2].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif PLACE[NPC2[i].suit][NPC2[i].rank].suit >= 0 or PLACE[NPC2[i].suit][NPC2[i].rank-2].suit >= 0:
            CARDNUMBER.append(i)

    if len(CARDNUMBER) > 0:
        random.shuffle(CARDNUMBER)

        PLACE[ NPC2[CARDNUMBER[0]].suit][ NPC2[ CARDNUMBER[0] ].rank - 1] = NPC2[CARDNUMBER[0]]
        del NPC2[CARDNUMBER[0]]
        ShowBan()
    CARDNUMBER.clear()

    #NPC3の番
    for i in range(len(NPC3)):
        if NPC3[i].rank == 1:
            if PLACE[NPC3[i].suit][NPC3[i].rank].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif NPC3[i].rank == 13:
            if PLACE[NPC3[i].suit][NPC3[i].rank-2].suit >= 0:
                CARDNUMBER.append(i)
            else:
                continue

        elif PLACE[NPC3[i].suit][NPC3[i].rank].suit >= 0 or PLACE[NPC3[i].suit][NPC3[i].rank-2].suit >= 0:
            CARDNUMBER.append(i)

    if len(CARDNUMBER) > 0:
        random.shuffle(CARDNUMBER)

        PLACE[ NPC3[CARDNUMBER[0]].suit][ NPC3[ CARDNUMBER[0] ].rank - 1] = NPC3[CARDNUMBER[0]]
        del NPC3[CARDNUMBER[0]]
        ShowBan()
    if len(HAND) == 0 or len(NPC1) == 0 or len(NPC2) == 0 or len(NPC3) == 0:
        game_end()

#カードがクリックされた際に起こす関数
def click(event):
    mX = event.x
    mY = event.y
    cardnumber = -1
    pos = 60
    global npctuenF
    global game_endflag

    for i in range(len(HAND)):
        if mX>pos and mX<pos+50 and mY>715 and mY<835:
            cardnumber = i
            break
        pos += 50

    #手札以外をクリックした場合
    if cardnumber < 0:
        return

    #出せるカードであれば場に出す
    if game_endflag == 0:
        if HAND[i].rank == 1:
            if PLACE[HAND[i].suit][HAND[i].rank].suit >= 0:
                PLACE[HAND[i].suit][HAND[i].rank-1] = HAND[i]
                del HAND[i]
                npctuenF = 1

        elif HAND[i].rank == 13:
            if  PLACE[HAND[i].suit][HAND[i].rank-2].suit >= 0:
                PLACE[HAND[i].suit][HAND[i].rank-1] = HAND[i]
                del HAND[i]

                npctuenF = 1

        elif PLACE[HAND[i].suit][HAND[i].rank].suit >= 0 or PLACE[HAND[i].suit][HAND[i].rank-2].suit >= 0:
            PLACE[HAND[i].suit][HAND[i].rank-1] = HAND[i]
            del HAND[i]
            npctuenF = 1

        ShowBan()

    if len(HAND) == 0 or len(NPC1) == 0 or len(NPC2) == 0 or len(NPC3) == 0:
        game_end()

    if npctuenF == 1:
        npczturn()

def user_pass():
    npczturn()

def game_end():
    global game_endflag
    if len(HAND) == 0:
        Label(root, text = "YOU WIN",width = 15,height = 5,font = ("",32),fg ="red").place(x = 600,y = 350)
        game_endflag = 1
    elif len(NPC1) == 0:
        Label(root, text = "YOU LOSE\nNPC1 WIN",width = 15,height = 5,font = ("",32),fg = "blue").place(x = 600,y = 350)
        game_endflag = 1

    elif len(NPC2) == 0:
        Label(root, text = "YOU LOSE\nNPC2 WIN",width = 15,height = 5,font = ("",32),fg = "blue").place(x = 600,y = 350)
        game_endflag = 1
    elif len(NPC3) == 0:
        Label(root, text = "YOU LOSE\nNPC3 WIN",width = 15,height = 5,font = ("",32),fg = "blue").place(x = 600,y = 350)
        game_endflag = 1


def exitbutton():
    quit()

def set():
    card_set()
    card_deal()
    ShowBan()


if __name__ == '__main__':
    set()
    canvas.pack()
    if game_endflag == 0:
        canvas.bind("<ButtonPress-1>", click)
        passbutton1 = Button(root,text = "パス",width = 10,height = 4,command = user_pass).place(x = 1300,y = 650)
    passbutton2 = Button(root,text = "EXIT",width = 10,height = 4,command = exitbutton).place(x = 1300,y = 750)

    if len(HAND) == 0 or len(NPC1) == 0 or len(NPC2) == 0 or len(NPC3) == 0:
        game_end()

    root.mainloop()
