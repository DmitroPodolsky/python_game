from random import randint
a=200
a0=200
b=7
c=0
name='мерзкая_слизь'
def first_ability():
    global a
    w=randint(0,b)
    print(f'{w}+half damage {w//2}')
    return w+w//2
def second_ability():
    global a
    print(f'{a}+100={a+100}')
    a+=100
    return 0
def death(a,b):
    b+=18
    a+=10
    return a,b