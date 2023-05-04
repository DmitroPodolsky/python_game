from random import randint
from оживший_скелет import a as hp, b as damage, c as defense
from многоножка import a as hp1, b as damage1, c as defense1
from путешественник import a as hp2, b as damage2, c as defense2
from мертвец_некромант import a as hp3, b as damage3, c as defense3
import main_game
def v():
   main_game.a = 3
   a=randint(1,4)
   if a==1:
      print(f'вам попался противник - многоножка\nhp - {hp1}\ndamage - {damage1}\ndefense - {defense1}\n')
      return 1
   elif a==2:
      print(f'вам попался противник - оживший_скелет\nhp - {hp}\ndamage - {damage}\ndefense - {defense}\n')
      return 2
   elif a==3:
      print(f'вам попался противник - путешественник\nhp - {hp2}\ndamage - {damage2}\ndefense - {defense2}\n')
      return 3
   elif a==4:
      print(f'вам попался противник - мертвец_некромант\nhp - {hp3}\ndamage - {damage3}\ndefense - {defense3}\n')
      return 4