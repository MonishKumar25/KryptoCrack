#Hashcat
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def hashcat():

    hash =  input("\033[3;37m  >  Enter Hash        :  ")
    htype = input("\033[3;37m  >  Enter HashType    :  ")
    print(os.system(" echo "+ hash +" >> hash.txt"))
    print(os.system(" sudo hashcat -m "+ htype +" -a 0 hash.txt rockyou.txt "))
    


if __name__=="__main__":
    hashcat()