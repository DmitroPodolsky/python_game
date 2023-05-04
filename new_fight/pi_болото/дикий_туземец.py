from random import randint

a=100
b=30
c=10
name='дикий_туземец'
def first_ability(s):
    global c
    print(f'{c}+2={c+2}')
    c+=2
    return randint(b-10,b)
def second_ability():
    global b
    global c
    global a
    if c>=0:
        print(f'{b}+5={b+5} and {c}-2={c-2}')
        b+=5
        c-=2
    else:
        z=randint(0,b)
        print(f'{a}-{b}={a-b} but {b}=def')
        c=z
        a-=b
        return 0
    return randint(0,b-15)
def death(a,b):
    b+=20
    a+=10
    return a, b