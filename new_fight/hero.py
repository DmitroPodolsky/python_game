from text import a as ran
from random import randint
import галуши, футболка_месси, сандали, лахмотья, палка, ржавая_труба,кирка,серая_мантия,сапог,катана,пистолет,сапоги_ордена
import fight

a=140#hp
a0=140
b=12#dmg
b0=12
c=0#def
c0=0
f1=0#weapons
f2=0#armors
f3=0#boots
a1,b1,c1=0,0,0
a2,b2,c2=0,0,0
a3,b3,c3=0,0,0
i = 0
u = 0
l0=50
l=0
con=40
kal='attack'

#boloto:
gniloy = False
dikiy = False
slis = False

#desert:
pes = False
rasboy = False
skorpion = False

#shahta
mnogonog = False
skelet = False
puteshes = False
nekromant = False

#mansion
strag = False
kultist = False
live_body = False


def first_ability():
    if f1==0:
        return randint(0,b)
    elif f1==1:
        return ржавая_труба.ability()
    elif f1==2:
        return палка.ability()
    elif f1==3:
        return кирка.ability()
    elif f1==4:
        return катана.ability()
def second_ability():
    if f2==0:
        global a
        global b
        print(f'{a}+8={a+8}')
        a+=8
        fight.i1=3
        return randint(0,b//2)
    elif f2==1:
        return футболка_месси.ability()
    elif f2==2:
        return лахмотья.ability()
    elif f2==3:
        return серая_мантия.ability()
    elif f2==4:
        return пистолет.ability()

def third_ability():
    if f3==0:
        fight.i2 = 2
        global a
        global c
        print(f'{a}-5={a-5} and def +1')
        a-=5
        c+=1
        return 0
    elif f3==2:
        return сандали.ability()
    elif f3==1:
        return галуши.ability()
    elif f3==3:
        return сапог.ability()
    elif f2==4:
        return сапоги_ордена.ability()
def fort_ability():
    global kal
    kal='dodge'
    return 0