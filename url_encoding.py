import os


def clear(): os.system("cls" if os.name == "nt" else "clear")


options = ["URL Encoding"]
settings = [False]


def strToHex(string: str):
    res = []
    for s in string:
        res.append(hex(ord(s)))
    return res


def hexToStr(hex: str):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value


def main():
    clear()
    opt = input(" [1] Encode Hex\n [2] Decode Hex\n [3] Settings\nOption: ")

    try:
        # ==== STRING TO HEX ====
        if opt == "1":
            string = input("\n[?] String: ")

            if (string != "" and string != " " and string != None):
                if settings[0]:
                    print("[+] Hex: https://" +
                          "".join(strToHex(string)).replace("0x", "%"))
                else:
                    print("[+] Hex: " +
                          "".join(strToHex(string)).replace("0x", " "))
            else:
                print("[-] Invalid Input: '%s'" % string)
        # ========================
        # ==== HEX TO STRING =====
        elif opt == "2":
            hex = input("\n[?] Hex: ")

            if (hex != "" and hex != " " and hex != None):
                print("[+] String: " + hexToStr(hex))
            else:
                print("Invalid Input: '%s'" % hex)
        # ========================
        # ======= SETTINGS =======
        elif opt == "3":
            print("\n\n---SETTINGS---")
            print(" [1] URL Encoding: " + str(settings[0]))
            print("--------------\n")

            try:
                setting = int(input("[?] Change Setting [1,2,...]: "))
                toggle = input("[?] Toggle '%s' [y/n]: " %
                               options[setting-1]).lower()

                if toggle == "y":
                    settings[setting-1] = True
                    print(f"""\n[+] Successfully toggled setting to 'True'
Press [ENTER] to continue""")
                    input()
                    main()
                else:
                    print("\nPress [ENTER] to continue")
                    input()
                    main()
            except IndexError:
                print("Invalid Input\nPress [ENTER] to return")
                input()
                main()
        # ========================

        else:
            print("[-] Invalid Input: '%s'" % opt)
    except Exception as e:
        print("[-] Error: " + str(e))


if __name__ == "__main__":
    main()

# terrifictable.pw                  ->                  https://%74%65%72%72%69%66%69%63%74%61%62%6c%65%2e%70%77
