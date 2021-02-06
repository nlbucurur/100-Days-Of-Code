"""Encuentra la isla del tesoro."""

print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
""")
print("Bienvenido a la isla del tesoro.")
print("Tu misión es encontrar el tesoro.\n")

camino = input("Estás en la jungla de la isla, hay dos opciones para ir al " +
               "[m]ar o escalar la [mo]ntaña\n")

if camino == "m":
    barco = input("Ves a lo lejos un pequeño barco, ¿[v]as hacia el o le " +
                  "[g]ritas para llamar su atención\n")
    if barco == "v":
        print("Te ha comido un tiburón, game over!\n")
    else:
        print("El barco te ha ignorado, moriras de hambre. Game over!\n")
else:
    montana = input("Desde la cima de montaña ves una cueva ¿[v]as hacia " +
                    "ella o te [d]evueves al mar?\n")
    if montana == "d":
        barco = input("Ves a lo lejos un pequeño barco, ¿[n]adas hacia él " +
                      "o le [g]ritas para llamar su atención?\n")
        if barco == "n":
            print("Te ha comido un tiburón, game over!\n")
        else:
            print("El barco te ha ignorado, moriras de hambre. Game over!\n")
    else:
        color = input("encuentras tres puertas, escoge [a]marilla, " +
                      "[az]ul o [r]oja\n")
        if color == "a":
            print("Te han atacado los murcielagos y te dio coronavirus. " +
                  "Game over!\n")
        elif color == "az":
            print("Te ha atacado un jabalí. Game over!\n")
        else:
            print("Felicidades, encontraste el tesoro!\n")
