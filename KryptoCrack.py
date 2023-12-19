#KryptoCrack
#Color
grey    = "\033[1;37m"
red     = "\033[1;31m"
green   = "\033[1;32m"
yellow  = "\033[1;33m"
cyan    = "\033[1;96m"
purple  = "\033[1;35m"


def main_menu():

    print(green+"""  

    |+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|
    |+|                                                                                                                                             |+|
    |+|    888    d8P  8888888b. Y88b   d88P 8888888b. 88888888888 .d88888b.        .d8888b.  8888888b.         d8888  .d8888b.  888    d8P         |+|
    |+|    888   d8P   888   Y88b Y88b d88P  888   Y88b    888    d88P" "Y88b      d88P  Y88b 888   Y88b       d88888 d88P  Y88b 888   d8P          |+|
    |+|    888  d8P    888    888  Y88o88P   888    888    888    888     888      888    888 888    888      d88P888 888    888 888  d8P           |+|
    |+|    888d88K     888   d88P   Y888P    888   d88P    888    888     888      888        888   d88P     d88P 888 888        888d88K            |+|
    |+|    8888888b    8888888P"     888     8888888P"     888    888     888      888        8888888P"     d88P  888 888        8888888b           |+|
    |+|    888  Y88b   888 T88b      888     888           888    888     888      888    888 888 T88b     d88P   888 888    888 888  Y88b          |+|
    |+|    888   Y88b  888  T88b     888     888           888    Y88b. .d88P      Y88b  d88P 888  T88b   d8888888888 Y88b  d88P 888   Y88b         |+|
    |+|    888    Y88b 888   T88b    888     888           888     "Y88888P"        "Y8888P"  888   T88b d88P     888  "Y8888P"  888    Y88b        |+|
    |+|                                                                                                                                             |+|
    |+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|
    
    """) 
                                                                                                                                  
    print("\033[1;31m                                                                                   Author      :"+grey+" SUSIL KUMAR R M")
    print("\033[1;31m                                                                                   Register No :"+grey+" 39120126")
    print("\033[1;31m                                                                                   Email ID    :"+grey+" susilmanoharan@gmail.com")
    print("""
    """)
                                                                                                                                   

    print(red+"                 Note : "+cyan+"Krypto Crack is a Cryptographic Tool deals with Hashing, Crypto Analysis & Stegnography")
    

    print("""
    """)
    print(purple+"      [+] Tools : ")

    print(yellow+"""
        [1]  Convert Text to Hash using MD5, SHA1, SHA256, SHA512""")      
    print(cyan+"""    ________________________________________________""")
    print(yellow+"""
        [2]  Convert File to Hash using MD5, SHA1, SHA256, SHA512""")
    print(cyan+"""    ________________________________________________""")
    print(yellow+"""
        [3]  Hash Identifier 
        [4]  Hashcat
        [5]  John The Ripper""")
    print(cyan+"""    _______________________________________________""")
    print(yellow+"""
        [6]  Metadata collector - File
        [7]  Metadata collector - Photo
        [8]  Metadata collector - Video""")
    print(cyan+"""    _______________________________________________""")
    print(yellow+"""
        [9]  Whitespace Steganography Embed
        [10] Whitespace Steganography Extract""")
    print(cyan+"""    ________________________________________________""")
    print(yellow+"""
        [11] Image Steganography Embed
        [12] Image Steganography Extract
    
    """)
                                            
    kryptocrack() 

def kryptocrack():

    from TextHash import texttohash
    from FileHash import filetohash
    from HashIdentityfier import hashid
    from Hashcat import hashcat
    from JohnTheRipper import jtr
    from MetadataCollectorFile import metadatacollectorfile
    from MetadataCollectorPhoto import metadatacollectorphoto
    from MetadataCollectorVideo import metadatacollectorvideo
    from WhitespaceStegoEmbed import whitespacestegoembed
    from WhitespaceStegoExtract import whitespacestegoextract
    from ImgStegnoEmbed import imgstegnoembed
    from ImgStegnoExtract import imgstegnoextract


    inp = (input(grey + "  >  Enter The Option from "+green+"[1-16]"+grey+" OR "+red+"[exit]"+grey+" to Exit $ "))
    
    if (inp == '1'):
        texttohash()

    elif (inp == '2'):
        filetohash()

    elif (inp == '3'):
        hashid()
    
    elif (inp == '4'):
        hashcat()
    
    elif (inp == '5'):
        jtr()

    elif (inp == '6'):
        metadatacollectorfile()
    
    elif (inp == '7'):
        metadatacollectorphoto()
    
    elif (inp == '8'):
        metadatacollectorvideo()

    elif (inp == '9'):
        whitespacestegoembed()
    
    elif (inp == '10'):
        whitespacestegoextract()

    elif (inp == '11'):
        imgstegnoembed()
        
    elif (inp == '12'):
        imgstegnoextract()

    elif (inp == 'exit'):
        print(cyan+"""                                             
                                                                                See You Soon !!! 
        """)
        exit()

    elif (inp == 'ls'):
        print("\033[2;31m       [+] Tools : ")

        print("""\033[1;34m
    

        [1]  Convert Text to Hash using MD5, SHA1, SHA256, SHA512     
    ________________________________________________________________
    
        [2]  Convert File to Hash using MD5, SHA1, SHA256, SHA512
    ________________________________________________________________
    
        [3]  Hash Identifier 
        [4]  Hashcat
        [5]  John The Ripper
    ________________________________________________________________

        [6]  Metadata collector - File
        [7]  Metadata collector - Photo
        [8]  Metadata collector - Video
    ________________________________________________________________

        [9]  Whitespace Steganography Embed
        [10] Whitespace Steganography Extract
    ________________________________________________________________

        [11] Steganography Embed
        [12] Steganography Extract
    
        """)

    else:
        print(red + "Enter an valid option")

    while True:
        kryptocrack()
    


if __name__ == "__main__":
    main_menu()