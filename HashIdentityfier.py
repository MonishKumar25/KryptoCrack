#haiti
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def hashid():

    hash = input(cyan+"  >  Enter Hash : ")
    print(os.system("sudo haiti -e "+hash))


if __name__=="__main__":
    hashid()