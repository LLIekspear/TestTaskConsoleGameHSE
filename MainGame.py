import Wolf
import Officer
import Horse
from random import randrange


already_used=[-1]
wolfs=[]
officers=[]
horses=[]
started_desk=""
a=[0]*8
for i in range(8):
    a[i]=[0]*8

#задаем случайное расположение фигур на старте
def get_start_position(wolfs_n, officers_n, horses_n):
    posx=-1
    posy=-1
    for i in range(wolfs_n):
        while([posx, posy] in already_used or [posx, posy]==[-1,-1]):
            posx=randrange(8)
            posy=randrange(8)
        a[posx][posy]=1
        already_used.append([posx, posy])
        wolf=Wolf.Wolf()
        wolf.posx=posx
        wolf.posy=posy
        wolfs.append(wolf)
        posx=-1
        posy=-1
    for i in range(officers_n):
        while([posx, posy] in already_used or [posx, posy]==[-1,-1]):
            posx=randrange(8)
            posy=randrange(8)
        a[posx][posy]=2
        already_used.append([posx, posy])
        officer=Officer.Officer()
        officer.posx=posx
        officer.posy=posy
        officers.append(officer)
        posx=-1
        posy=-1
    for i in range(horses_n):
        while([posx, posy] in already_used or [posx, posy]==[-1,-1]):
            posx=randrange(8)
            posy=randrange(8)
        a[posx][posy]=3
        already_used.append([posx, posy])
        horse=Horse.Horse()
        horse.posx=posx
        horse.posy=posy
        horses.append(horse)
        posx=-1
        posy=-1

#делаем доску-строку из массива
def get_desk(array):
    desk=""
    for j in range(8):
        for i in range(8):
            if(array[i][j]==0):
                desk+="🟩"
            elif(array[i][j]==1):
                desk+="🐺"
            elif(array[i][j]==2):
                desk+="💂"
            elif(array[i][j]==3):
                desk+="🐴"
        desk+="\n"
    return desk

get_start_position(3, 1, 1)
already_used.remove(-1)
started_desk=get_desk(a)
print("Начало игры \n")
print(started_desk)

#проверка состояния игры: продолжаем или заканчиваем
def checkGameState(wolfs):
    count_alive=0
    for wolf in wolfs:
        if(wolf.is_alive):
            count_alive+=1
    if(count_alive>0):
        return True
    return False

#основной цикл
while checkGameState(wolfs):
    flag=False
    while flag!=True:
        b=[]
        x=int(input("Введите x для хода офицером: "))
        y=int(input("Введите y для хода офицером: "))
        flag, b=Officer.action_officer_precondition(officers, x, y, a, wolfs)
        #
        if(b!=[]):
            if(b==0):
                print("Некорректный ход! Офицер может атаковать только по диагонали!")
                flag=False
            else:
                a=b[0]
                officers=b[1]
                wolfs=b[2]
    flag=False
    while flag!=True:
        x=int(input("Введите x для хода конем: "))
        y=int(input("Введите y для хода конем: "))
        flag, b=Horse.action_horse_precondition(horses, x, y, a, wolfs)
        #
        if(b!=[]):
            if(b==0):
                print("Некорректный ход! Конь может атаковать только буквой Г!")
            else:
                a=b[0]
                horses=b[1]
                wolfs=b[2]
    a, wolfs=Wolf.wolfs_action(wolfs, a)
    started_desk=get_desk(a)
    print("----------------------\n Новый раунд")
    print(started_desk)
print("----------------------\n Игра завершена!")