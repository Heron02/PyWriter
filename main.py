import sys

import keyboard
import time

def type_character(character):
    if character == 'a':
        keyboard.press_and_release('a')
    elif character == 'b':
        keyboard.press_and_release('b')
    elif character == 'c':
        keyboard.press_and_release('c')
    elif character == 'd':
        keyboard.press_and_release('d')
    elif character == 'e':
        keyboard.press_and_release('e')
    elif character == 'f':
        keyboard.press_and_release('f')
    elif character == 'g':
        keyboard.press_and_release('g')
    elif character == 'h':
        keyboard.press_and_release('h')
    elif character == 'i':
        keyboard.press_and_release('i')
    elif character == 'j':
        keyboard.press_and_release('j')
    elif character == 'k':
        keyboard.press_and_release('k')
    elif character == 'l':
        keyboard.press_and_release('l')
    elif character == 'm':
        keyboard.press_and_release('m')
    elif character == 'n':
        keyboard.press_and_release('n')
    elif character == 'ñ':
        keyboard.press_and_release('alt+164')
    elif character == 'o':
        keyboard.press_and_release('o')
    elif character == 'p':
        keyboard.press_and_release('p')
    elif character == 'q':
        keyboard.press_and_release('q')
    elif character == 'r':
        keyboard.press_and_release('r')
    elif character == 's':
        keyboard.press_and_release('s')
    elif character == 't':
        keyboard.press_and_release('t')
    elif character == 'u':
        keyboard.press_and_release('u')
    elif character == 'v':
        keyboard.press_and_release('v')
    elif character == 'w':
        keyboard.press_and_release('w')
    elif character == 'x':
        keyboard.press_and_release('x')
    elif character == 'y':
        keyboard.press_and_release('y')
    elif character == 'z':
        keyboard.press_and_release('z')
    # ... y así sucesivamente para todas las letras
    elif character == 'A':
        keyboard.press_and_release('shift+a')
    elif character == 'B':
        keyboard.press_and_release('shift+b')
    elif character == 'C':
        keyboard.press_and_release('shift+c')
    elif character == 'D':
        keyboard.press_and_release('shift+d')
    elif character == 'E':
        keyboard.press_and_release('shift+e')
    elif character == 'F':
        keyboard.press_and_release('shift+f')
    elif character == 'G':
        keyboard.press_and_release('shift+g')
    elif character == 'H':
        keyboard.press_and_release('shift+h')
    elif character == 'I':
        keyboard.press_and_release('shift+i')
    elif character == 'J':
        keyboard.press_and_release('shift+j')
    elif character == 'K':
        keyboard.press_and_release('shift+k')
    elif character == 'L':
        keyboard.press_and_release('shift+l')
    elif character == 'M':
        keyboard.press_and_release('shift+m')
    elif character == 'N':
        keyboard.press_and_release('shift+n')
    elif character == 'Ñ':
        keyboard.press_and_release('shift+alt+n')
    elif character == 'O':
        keyboard.press_and_release('shift+o')
    elif character == 'P':
        keyboard.press_and_release('shift+p')
    elif character == 'Q':
        keyboard.press_and_release('shift+q')
    elif character == 'R':
        keyboard.press_and_release('shift+r')
    elif character == 'S':
        keyboard.press_and_release('shift+s')
    elif character == 'T':
        keyboard.press_and_release('shift+t')
    elif character == 'U':
        keyboard.press_and_release('shift+u')
    elif character == 'V':
        keyboard.press_and_release('shift+v')
    elif character == 'W':
        keyboard.press_and_release('shift+w')
    elif character == 'X':
        keyboard.press_and_release('shift+x')
    elif character == 'Y':
        keyboard.press_and_release('shift+y')
    elif character == 'Z':
        keyboard.press_and_release('shift+z')
    elif character == '1':
        keyboard.press_and_release('1')
    elif character == '2':
        keyboard.press_and_release('2')
    elif character == '3':
        keyboard.press_and_release('3')
    elif character == '4':
        keyboard.press_and_release('4')
    elif character == '5':
        keyboard.press_and_release('5')
    elif character == '6':
        keyboard.press_and_release('6')
    elif character == '7':
        keyboard.press_and_release('7')
    elif character == '8':
        keyboard.press_and_release('8')
    elif character == '9':
        keyboard.press_and_release('9')
    elif character == ' ':
        keyboard.press_and_release('space')
    elif character == ')':
        keyboard.press_and_release('shift+9')
    elif character == '(':
        keyboard.press_and_release('shift+8')
    elif character == "'":
        keyboard.press_and_release("'")
    elif character == "-":
        keyboard.press_and_release("-")
    elif character == "_":
        keyboard.press_and_release("shift+-")
    elif character == "|":
        keyboard.press_and_release("altgr+1")
    elif character == "/":
        keyboard.press_and_release("shift+7")
    elif character == "'\'":
        keyboard.press_and_release("alt_gr+º")
    elif character == 'ñ':
        keyboard.press_and_release('alt+164')
    elif character == 'Ñ':
        keyboard.press_and_release('shift+alt+n')
    elif character == "´":
        keyboard.press_and_release("`")
    elif character == " ":
        keyboard.press_and_release("space")

    else:
        keyboard.press_and_release(character)

def reset_program():
    keyboard.press_and_release('escape')
    #main(1)
    main()


def main():
    while True:

        if keyboard.is_pressed('insert'):
            """for j in range(100000):
                text = ""
                     _________
                    |         |
                    |  Hola   |
                    |_________|""

                #text = "Mensaje numero %s para Puchi" % i
                for character in range(len(text)):
                    type_character(text[character])
                    if keyboard.is_pressed('escape'):
                        reset_program()
                    time.sleep(0.3)
                keyboard.press_and_release('enter')
                keyboard.press_and_release('y')
                #i += 1
                """

            lista = ["Hola"]
            for valor in lista:
                for character in valor:
                    type_character(character)
                    if keyboard.is_pressed('escape'):
                        reset_program()
                    time.sleep(0.001)
                keyboard.press_and_release('enter')



if __name__ == "__main__":
    #main(2)
    main()