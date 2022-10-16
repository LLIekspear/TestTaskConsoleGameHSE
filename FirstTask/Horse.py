from random import randrange

#класс коня
class Horse:
    attack=1
    posx=-1
    posy=-1

#действие коня
def horse_action(horses, wolfs, array, x, y):
    success=0
    for horse in horses:
        for wolf in wolfs:
            if(wolf.posx==x and wolf.posy==y):
                print("Ударили волка!")
                wolf.health-=1
                success=1
                if(wolf.health<=0):
                    print("Убили волка!")
                    wolf.is_alive=False
                    array[x][y]=3
                    array[horse.posx][horse.posy]=0
                    horse.posx=x
                    horse.posy=y
        if(success==0):
                array[x][y]=3
                array[horse.posx][horse.posy]=0
                horse.posx=x
                horse.posy=y
    return [array, horses, wolfs]

#проверка условий перед действием коня    
def action_horse_precondition(horses, x, y, array, wolfs):
    b=[]
    dx=abs(x-horses[0].posx)
    dy=abs(y-horses[0].posy)
    if(x<=7 and x>=0 and y<=7 and y>=0):
        if(dx*dy==2):
            b=horse_action(horses, wolfs, array, x, y)
        else:
            print("Некорректный ход! Конь может ходить только буквой Г!")
            return [False, []]
    else:
        print("Некорректный ход! Конь может ходить только буквой Г!")
        return [False, []]
    return [True, b]