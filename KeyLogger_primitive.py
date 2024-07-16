# This is a very basic keylogger. It is intended as a simple fun project to count how many keys I press during work, games or other.
# This is not malware, and should not be used as such, simply translates this: "aawAAw" into "(a:4, w:2, shift:2)"
"""
@author     - Nikola Jankovic
@date       - 15-Jun-2024
@version    - 1.0

Logs Key presses to see frequency of keys used,
No string integrity.
"""

import keyboard as kb


def main():
    # TODO create a Dictionary p = {"":""}, p.update({key:"1"}); then, temp = int(p["key"])+1; p.update({key: temp})
    Log_count = []
    Log = []

    while not kb.is_pressed("end"):
        key = kb.read_key()
        temp = str(key).lower()

        if temp not in Log:
            Log.append(temp)
            Log_count.append(1)

        else:
            Log_count[Log.index(temp)] += 1

    print("\n")

    temp = [x//2 for x in Log_count]

    strs =""
    for x in range(len(Log_count)):
        strs += Log[x] + " : " + str(temp[x]) + "\n"


    print(strs)


# Only Run if this file is Running it, not if it is called by a different file
if __name__ == "__main__":
    main()

