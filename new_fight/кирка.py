from random import randint
import hero

a=20
b=10
c=2
accept = 1
def ability():
    c=randint(1,2)
    if c==2:
        print('вы откололи с врага кусок души')
        print(f'{hero.con}+2={hero.con+2}')
        return randint(b,hero.b)
    else:
        return randint(b,hero.b)