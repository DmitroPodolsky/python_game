from random import randint
import hero

a = 8
b=12
c=6
accept=1
def ability():
    print(f'{hero.a}-5={hero.a-5} dmg+5')
    hero.a-=5
    x = randint(5, hero.b)+10
    return x