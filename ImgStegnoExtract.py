#Stegno Extract
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def imgstegnoextract():
                                    
    embed=   input("\033[3;37m  >  Enter Filename to Extract Secretfile.txt    :  ")
    
    print(os.system("sudo steghide extract -sf "+ embed ))
    print(os.system("cat Secretfile.txt"))


if __name__=="__main__":
    imgstegnoextract()