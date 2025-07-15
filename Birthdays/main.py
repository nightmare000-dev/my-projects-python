from lexicon import *
from rich.console import Console

import datetime as dt
import os
import json
import calendar

console = Console()
person_id = 0

# continue programm
def press(): input("\nPress ENTER to continue...")

# main logic
def algorithm(p_day, p_month, p_year):
    global current_year

    read_json()

    k = 0

    while k == 0:
        birthday_person = dt.datetime(current_year, p_month, p_day)
        difference = birthday_person - current_date
        days = difference.days

        if days < 0:
            current_year += 1
            difference = birthday_person - current_date
            continue
        
        else:
            data["all"][key_name]["Remaining"] = days
            data["all"][key_name]["Will be"] = current_year - p_year

            data["defaults"][key_name]["Remaining"] = days
            data["defaults"][key_name]["Will be"] = current_year - p_year
            k += 1

# full list information output
def info():
    print('=' * 100)
    console.print(f"\n[bold]Name:[/] [italic]{value["Name"]}[/]")
    console.print(f"[bold]Surname:[/] [italic]{value["Surname"]}[/]")
    console.print(f"[bold]ID:[/] {value["id"]}")
    console.print(f"[bold]Status:[/] {value["Status"]}")
    console.print(f"[bold]Birthday:[/] {value["Birthday"]}")
    console.print(f"[bold]Left until birthday:[/] {value["Remaining"]}")
    console.print(f"[bold]Will be:[/] {value["Will be"]}")
    console.print(f"[bold]Added at:[/] {value["AddedAt"]}")
    console.print(f"[bold]Time:[/] {value["Time"]}\n")
    print('=' * 100)

# upload json
def upload(variable):
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(variable, f, ensure_ascii=False, indent=4)

def read_json():
    global data

    with open('config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

# menu options output
def menu():
    os.system("clear")
    max_length = max(len(value) for value in MENU.values())

    for key, value in MENU.items():
        print(f"{value:{max_length}}\t{key}")

while True:
    menu()

    invite = input("\n> ").lower().split()

    # EXIT
    if invite[0] == FUNCS["f_exit"]: exit()

    # LIST
    elif invite[0] == FUNCS["f_list"]:
        os.system("clear")

        read_json()

        if not data["all"]: print("There is no one on your list.")
        for key, value in data["all"].items(): info()

        press()

    # FAV LIST
    elif invite[0] == "fav" and invite[1] == "list":
        os.system("clear")

        read_json()

        if not data["favorites"]: console.print("There is no one on your [bold]favorites[/] list.")
        for key, value in data["favorites"].items(): info()

        press()

    # DEF LIST
    elif invite[0] == "def" and invite[1] == "list":
        os.system("clear")

        read_json()

        if not data["defaults"]: console.print("There is no one on your [bold]defaults[/] list.")
        for key, value in data["defaults"].items(): info()

        press()

    # ADD NEW PERSON
    elif invite[0] == FUNCS["f_add"]:
        os.system("clear")

        current_year = dt.datetime.now().year
        current_date = dt.datetime.now()

        date_now = dt.datetime.now().strftime("%d.%m.%y")
        now = dt.datetime.now()
        current_time = now.time()
        formatted = current_time.strftime("%H:%M:%S")

        name = input("Name: ")
        surname = input("Surname: ")
        person_day = int(input(f"Day of {name}: "))

        if 1 <= person_day <= 31: pass
        else: exit()

        person_month = int(input(f"Month of {name}: "))

        if person_month == 2 and person_day > calendar.monthrange(current_year, person_month)[1]: exit()
        else: pass

        if 1 <= person_month <= 12: pass
        else: exit()

        person_year = int(input(f"Year of {name}: "))

        if 1900 <= person_year <= current_year: pass
        else: exit()

        person_birthday = dt.datetime(person_year, person_month, person_day).strftime("%d.%m.%y")
        key_name = name.upper()

        read_json()

        if not data["all"]: person_id += 1
        else:
            last_key = list(data["all"].keys())[-1]
            person_id = data["all"][last_key]["id"] + 1

        data["all"].update({
            key_name: {
                "id": person_id,
                "Name": name,
                "Surname": surname,
                "Status": "default",
                "Day": person_day,
                "Month": person_month,
                "Year": person_year,
                "Birthday": person_birthday,
                "AddedAt": date_now,
                "Time":  formatted
            }
        })

        data["defaults"].update({
            key_name: {
                "id": person_id,
                "Name": name,
                "Surname": surname,
                "Status": "default",
                "Day": person_day,
                "Month": person_month,
                "Year": person_year,
                "Birthday": person_birthday,
                "AddedAt": date_now,
                "Time":  formatted
            }
        })

        console.print(f"\n[bold]{name} {surname} added[/] to your list")

        upload(data)

        read_json()
        algorithm(person_day, person_month, person_year)
        upload(data)

        press()

    # DELETE PERSON
    try:
        if invite[0] == FUNCS["f_delete"] and invite[1].isdigit():
            os.system("clear")

            read_json()

            if len(data["all"]) == 0: print("There is no one on your list.")
            found = False

            for key in data["all"].keys():
                if data["all"][key]["id"] == int(invite[1]):
                    found = True

                    console.print(f"[bold]{data["all"][key]["Name"]} {data["all"][key]["Surname"]}[/] was [bold]removed[/] from your list.")
                    del data["all"][key]

                    try: del data["favorites"][key]
                    except: pass

                    try: del data["defaults"][key]
                    except: pass

                    break

            if found == False: print("Nothing found.")

            upload(data)

            press()
    except: pass

    # FAVORITE ID
    try:
        if invite[0] == FUNCS["f_fav"] and invite[1].isdigit():
            os.system("clear")
            found = False

            read_json()

            if len(data["all"]) == 0: print("Your list is empty.")

            for key in data["all"].keys():
                if data["all"][key]["id"] == int(invite[1]):
                    found = True

                    try:
                        data["all"][key]["Status"] = "favorite"
                        data["favorites"][key] = data["all"][key]
                        del data["defaults"][key]
                        console.print(f"[bold]{data["all"][key]["Name"]}'s[/] status has been changed to [bold]favorite.[/]")
                    except: console.print(f"[bold]{data["all"][key]["Name"]}[/] already [bold]favorite.[/]")

                    break

            if found == False: print("Nothing found.")

            upload(data)

            press()
    except: pass

    # DEFAULT ID
    try:
        if invite[0] == FUNCS["f_def"] and invite[1].isdigit():
            os.system("clear")
            found = False

            read_json()

            for key in data["all"].keys():
                if data["all"][key]["id"] == int(invite[1]) and data["all"][key]["Status"] == "favorite":
                    found = True

                    try:
                        data["all"][key]["Status"] = "default"
                        data["defaults"][key] = data["all"][key]
                        console.print(f"[bold]{data["favorites"][key]["Name"]}'s[/] status has been changed to [bold]default.[/]")
                        del data["favorites"][key]
                    except: pass

                    break

                elif data["all"][key]["id"] == int(invite[1]) and data["all"][key]["Status"] == "default":
                    found = True
                    console.print(f"[bold]{data["all"][key]["Name"]}[/] already [bold]default.[/]")

                elif len(data["favorites"]) == 0: print("Your favorites list is empty.")

            if found == False and len(data["favorites"]) >= 1: print("Nothing found.")

            upload(data)
            
            press()
    except: pass
