#Whitespace Stego Embed
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def whitespacestegoembed():

    filename =  input("\033[3;37m  >  Enter Filename  :  ")
    message = input("\033[3;37m  >  Enter the Message : ")
    convertfilename = input("\033[3;37m  >  Enter Hidden Filename  :  ")
    hiddenmessage = input("\033[3;37m  >  Enter the Message to Hide (No space): ")
    password = input("\033[3;37m  >  Enter Password :  ")
    print(os.system("sudo echo "+ message +" > "+ filename +".txt"))
    print(os.system("sudo stegsnow -C -p "+ password +" -m "+hiddenmessage+" "+ filename +".txt "+ convertfilename +".txt"))
    print(os.system("sudo rm "+ filename +".txt"))

if __name__=="__main__":
    whitespacestegoembed()