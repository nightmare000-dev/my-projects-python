from lexicon import *
from logic import *
from dictionary import data

import json
import os
import datetime as dt

months = {
    "1": "January", "2": "February", "3": "March", "4": "April",
    "5": "May", "6": "June", "7": "July", "8": "August", "9": "September",
    "10": "October", "11": "November", "12": "December"
}

def press(): input("\nPress...")

def info():
    read_js()

    print(f"ID\tDATE\t\tDESCRIPTION\tAMOUNT")
    print(f"{value["id"]}\t{value["date"]}\t{value["description"]}\t\t${value["amount"]}\n")

def signIn():
    global upperLogin

    person = False
    read_js()

    userLogin = input("\nLogin: ")
    userPassword = input("Password: ")

    upperLogin = userLogin.upper()

    # Если список пользователей пуст, то добавляем первого
    if not data["users"]["login"]:
        data["users"]["login"].update({
            upperLogin: {
                "userLogin": userLogin,
                "userPassword": userPassword
            }
        })

        upload(data)
        return

    # Если есть хотя бы 1 пользователь,
    # то проверяем есть ли он в словаре
    else:
        if upperLogin in data["users"]["login"]:
            if userPassword == data["users"]["login"][upperLogin]["userPassword"]:
                # Если логин и пароль совпадают - вошёл в аккаунт
                person = True

            else: print(False)

        else:
            # Если логина нет — добавляем
            data["users"]["login"][upperLogin] = {
                "userLogin": userLogin,
                "userPassword": userPassword
            }

            upload(data)



cls()
signIn()
expenseId = 0 

while True:
    cls()
    invite = input("  ").lower()
    splitInvite = invite.split()

    # EXIT
    if splitInvite[0] == FUNCS["exit"]: exit()

    try:

        # ADD
        if " ".join(splitInvite[:2]) == "add --description" and splitInvite[2] and splitInvite[4] and splitInvite[3] == FUNCS["amount"]:
            cls()
            read_js()

            current_year = dt.datetime.now().year
            date = dt.datetime.now().strftime("%d.%m.%y")
            description = splitInvite[2].upper()

            if not data["expense"]["login"]: 
                expenseId += 1
                data["expense"]["login"][upperLogin] = {}

            else:
                if upperLogin not in data["expense"]["login"]: data["expense"]["login"][upperLogin] = {}

                try:
                    last_key_descr = list(data["expense"]["login"][upperLogin].keys())[-1]
                    expenseId = data["expense"]["login"][upperLogin][last_key_descr]["id"] + 1
                except: expenseId += 1

            data["expense"]["login"][upperLogin].update({
                description: {
                        "id": expenseId,
                        "date": date,
                        "description": splitInvite[2],
                        "amount": int(splitInvite[4])
                    }
            })

            print(f"\nExpense added successfully (ID: {expenseId})")

            upload(data)
            press()


        # DELETE
        elif splitInvite[0] == FUNCS["delete"] and splitInvite[1] == FUNCS["id"] and splitInvite[2].isdigit():
            cls()
            read_js()

            found = False

            for key in data["expense"]["login"][upperLogin].keys():
                if data["expense"]["login"][upperLogin][key]["id"] == int(splitInvite[2]):
                    found = True

                    print(f"\n\"{data["expense"]["login"][upperLogin][key]["description"]}\" was deleted.")
                    del data["expense"]["login"][upperLogin][key]

                    break

            if found == False: print("\nNothing found.")

            upload(data)
            press()

        # LIST
        elif  splitInvite[0] == FUNCS["list"]:
            cls()
            read_js()

            if not data["expense"]["login"][upperLogin]: print("\nNothing found.")
            for key, value in data["expense"]["login"][upperLogin].items(): info()
            
            press()

        # SUMMARY
        elif invite == FUNCS["summary"]:
            cls()
            read_js()

            if not data["expense"]["login"][upperLogin] or not data["expense"]["login"]: print("Nothing found.")
            else:
                cache = 0

                for key, value in data["expense"]["login"][upperLogin].items(): cache += value["amount"]
                print(f"Total expenses: {cache}")

            press()

        # SUMMARY MONTH
        elif splitInvite[0] == FUNCS["summary"] and splitInvite[1] == FUNCS["month"] and splitInvite[2].isdigit():
            cls()
            read_js()

            cache = 0
            userMonth = int(splitInvite[2])

            if userMonth < 0 or userMonth > 12: print("Error.")

            for key, value in data["expense"]["login"][upperLogin].items():
                strMonth = value["date"][3:5]

                if userMonth == int(strMonth): cache += value["amount"]
                else: pass

            if cache == 0: print("Empty for this month.")

            print(f"Total expenses for {months[str(userMonth)]}: {cache}")

            press()
    except: continue
