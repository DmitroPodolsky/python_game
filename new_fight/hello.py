import main_game
from pi_болото import гнилой_мертвец,мерзкая_слизь,дикий_туземец
from pi_пустыня import песчанный_червь,разбойник,ядовитый_скорпион
import путешественник,мертвец_некромант,многоножка,оживший_скелет
import живая_плоть,культист,страж
def v(c):
    if main_game.a==1:
        if c==1:
            return мерзкая_слизь.name,1,мерзкая_слизь.a
        elif c==2:
            return гнилой_мертвец.name,2,гнилой_мертвец.a
        elif c==3:
            return дикий_туземец.name,3,дикий_туземец.a
    elif main_game.a==2:
        if c==1:
            return песчанный_червь.name,1,песчанный_червь.a
        elif c==2:
            return разбойник.name,2,разбойник.a
        elif c==3:
            return ядовитый_скорпион.name,3,ядовитый_скорпион.a
    elif main_game.a==3:
        if c==1:
            return многоножка.name,1,многоножка.a
        elif c==2:
            return оживший_скелет.name,2,оживший_скелет.a
        elif c==3:
            return путешественник.name,3,путешественник.a
        elif c==4:
            return мертвец_некромант.name,4,мертвец_некромант.a
    elif main_game.a==4:
        if c==1:
            return культист.name,1,культист.a
        elif c==2:
            return живая_плоть.name,2,живая_плоть.a,
        elif c==3:
            return страж.name,3,страж.a