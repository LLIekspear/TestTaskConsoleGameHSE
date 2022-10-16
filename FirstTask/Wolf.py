from random import randrange

#класс волка
class Wolf:
    health=2
    posx=-1
    poxy=-1
    is_alive=True

#проврека на возможность передвижения на клетку
def check(x, y, array):
    if(array[x][y]==0):
        return True
    return False

#действие волка, можно все укоротить, как это сделано с офицером или лошадью, но тут важен случайный выбор направления движения,
#поэтому лучше оставить так
def wolfs_action(wolfs, array):
    for elem in wolfs:
        flag_going=randrange(10)
        if(flag_going>3 and elem.is_alive):
            temp=randrange(8)
            if(temp==0):
                #вправо идем, если возможно
                if(elem.posx+1<=7):
                    if(check(elem.posx+1, elem.posy, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx+1][elem.posy]=1
                        elem.posx=elem.posx+1
            elif(temp==1):
                if(elem.posx-1>=0):
                    #влево идем, если возможно
                    if(check(elem.posx-1, elem.posy, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx-1][elem.posy]=1
                        elem.posx=elem.posx-1
            elif(temp==2):
                if(elem.posy-1>=0):
                    #вверх идем, если возможно
                    if(check(elem.posx, elem.posy-1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx][elem.posy-1]=1
                        elem.posy=elem.posy-1
            elif(temp==3):
                if(elem.posy+1<=7):
                    #вниз идем, если возможно
                    if(check(elem.posx, elem.posy+1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx][elem.posy+1]=1
                        elem.posy=elem.posy+1
            elif(temp==4):
                if(elem.posx+1<=7 and elem.posy-1>=0):
                    #вправо-вверх идем, если возможно
                    if(elem.posx==7 and elem.posy==0):
                        pass
                    elif(check(elem.posx+1, elem.posy-1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx+1][elem.posy-1]=1
                        elem.posy=elem.posy-1
                        elem.posx=elem.posx+1
            elif(temp==5):
                if(elem.posx+1<=7 and elem.posy+1<=7):
                    #вправо-вниз идем, если возможно
                    if(elem.posx==7 and elem.posy==7):
                        pass
                    elif(check(elem.posx+1, elem.posy+1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx+1][elem.posy+1]=1
                        elem.posy=elem.posy+1
                        elem.posx=elem.posx+1
            elif(temp==6):
                if(elem.posx-1>=0 and elem.posy-1>=0):
                    #влево-вверх идем, если возможно
                    if(elem.posx==0 and elem.posy==0):
                        pass
                    elif(check(elem.posx-1, elem.posy-1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx-1][elem.posy-1]=1
                        elem.posy=elem.posy-1
                        elem.posx=elem.posx-1
            elif(temp==7):
                if(elem.posx-1>=0 and elem.posy+1<=7):
                    #влево-вних идем, если возможно
                    if(elem.posx==0 and elem.posy==7):
                        pass
                    elif(check(elem.posx-1, elem.posy+1, array)):
                        array[elem.posx][elem.posy]=0
                        array[elem.posx-1][elem.posy+1]=1
                        elem.posy=elem.posy+1
                        elem.posx=elem.posx-1
    return [array, wolfs]