#Whitespace Stego
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def whitespacestegoextract():

    convertfilename = input("\033[3;37m  >  Enter Hidden Filename  :  ")
    password = input("\033[3;37m  >  Enter Password :  ")
    print(os.system("sudo stegsnow -C -p "+ password +" "+ convertfilename +".txt"))

if __name__=="__main__":
    whitespacestegoextract()