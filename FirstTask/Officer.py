from random import randrange

#класс офицера
class Officer:
    attack=2
    posx=-1
    posy=-1

#действие офицера
def officer_action(officers, wolfs, array, x, y, mode):
    success=0
    for officer in officers:
        for wolf in wolfs:
            if(wolf.posx==x and wolf.posy==y and mode==1):
                wolf.health-=2
                success=1
                if(wolf.health<=0):
                    wolf.is_alive=False
                    array[x][y]=0
            elif(wolf.posx==x and wolf.posy==y and mode==0):
                return 0
        if(success==0):
                array[x][y]=2
                array[officer.posx][officer.posy]=0
                officer.posx=x
                officer.posy=y
    return [array, officers, wolfs]

#предварительная проверка перед действием офицера
def action_officer_precondition(officers, x, y, array, wolfs):
    b=[]
    dx=abs(x-officers[0].posx)
    dy=abs(y-officers[0].posy)
    if(x<=7 and x>=0 and y<=7 and y>=0):
        if(dy==0):
            if(dx==1):
                b=officer_action(officers, wolfs, array, x ,y, 0)
        elif(dx==0):
            if(dy==1):
                b=officer_action(officers, wolfs, array, x ,y, 0)
        else:
            if(dx==1 and dy==1):
                b=officer_action(officers, wolfs, array, x ,y, 1)
    else:
        print("Некорректный ход! Офицер может ходить на одну клетку вокруг себя!")
        return [False, []]
    return [True, b]