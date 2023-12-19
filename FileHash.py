#File hash md5
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def filetohash():
    
    text=input("\033[3;37m  >  Enter Text to Store in the File  :  ")
    filename=input("\033[3;37m  >  Enter filename to create (.txt)  :  ")
    hashformat=input("\033[3;37m  >  Enter Hash Format (MD5, SHA1, SHA256, SHA512):  ")
    print(os.system("sudo echo "+ text +" >> "+filename))
    print(os.system("sudo "+ hashformat +"sum "+ filename))


if __name__=="__main__":
    filetohash()()