from random import randint
from pi_пустыня.песчанный_червь import a as hp, b as damage, c as defense
from pi_пустыня.разбойник import a as hp1, b as damage1, c as defense1
from pi_пустыня.ядовитый_скорпион import a as hp2, b as damage2, c as defense2
import main_game
def v():
   main_game.a = 2
   a=randint(1,3)
   if a==1:
      print(f'вам попался противник - песчанный червь\nhp - {hp}\ndamage - {damage}\ndefense - {defense}\n')
      return 1
   elif a==2:
      print(f'вам попался противник - разбойник\nhp - {hp1}\ndamage - {damage1}\ndefense - {defense1}\n')
      return 2
   elif a==3:
      print(f'вам попался противник - ядовитый скорпион\nhp - {hp2}\ndamage - {damage2}\ndefense - {defense2}\n')
      return 3