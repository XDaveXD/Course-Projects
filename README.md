

def enocode (file, key):
    with open(file, "r") as fd:
        strtowrite = ""
        filecontent = fd.read()

        for letter in filecontent:
            if 97 <= ord(letter) <= 122:
                key = key % 26
                if ord(letter) + key > 122:
                 key -= 26
                 strtowrite += chr(ord(letter) + key)
                else:
                    strtowrite += chr(ord(letter) + key)
            elif 65 <= ord(letter) <= 90:
                key = key % 26
                if ord(letter) + key > 90:
                    key -= 26
                    strtowrite += chr(ord(letter) + key)
                else:
                    strtowrite += chr(ord(letter) + key)

            elif letter == "\n":
             strtowrite = strtowrite + "\n"

            elif 32 == ord(letter):
                 strtowrite += letter

            else:
                strtowrite += letter


            with open(file +"_encoded", "w") as fde:
                fde.write(strtowrite)



def deocode (file, key):
    with open(file, "r") as fd:
        strtowrite = ""
        filecontent = fd.read()

        for letter in filecontent:
            if 97 <= ord(letter) <= 122:
                key = key % 26

                if ord(letter) - key < 97:


                    strtowrite += chr(ord(letter) - key)
                else:
                    strtowrite += chr(ord(letter) - key)

            elif 65 <= ord(letter) <= 90:
                key = key % 26
                if ord(letter) - key < 65:
                    letter = 90 == ord(letter)
                    key -= letter


                    strtowrite += chr(ord(letter) - key)
                else:
                    strtowrite += chr(ord(letter) - key)

            elif letter == "\n":
                strtowrite = strtowrite + "\n"

            elif 32 == ord(letter):
                strtowrite += letter

            else:
                strtowrite += letter
            """
            with open(file + "_Decoded", "w") as fde:
                fde.write(strtowrite)
            """


while True:

    usr_choice = input("1.Encode\n2.Decode\n3.EXIT\n")

    if usr_choice == "1":
        usr_file = input("enter direct file:\n")
        usr_key = int(input("Enter a key"))
        enocode(usr_file, usr_key)

    elif usr_choice == "2":
        usr_file = input("enter direct file:\n")
        usr_key = int(input("Enter a key"))
        deocode(usr_file, usr_key)

    elif usr_choice == "3":
     print("Thank you, bye bye!")
     break
    else:
        print("wrong input")