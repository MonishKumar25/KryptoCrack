
#Stegno Embed
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def imgstegnoembed():
    
    text=    input("\033[3;37m  >  Enter Text                               :  ")
    embed=   input("\033[3;37m  >  Enter Filename to Embed Secretfile.txt   :  ")
    print(os.system("sudo echo "+ text +" >> Secretfile.txt "))
    print(os.system("sudo steghide embed -cf "+ embed +" -ef Secretfile.txt"))
    print(os.system("rm Secretfile.txt"))


if __name__=="__main__":
    imgstegnoembed()