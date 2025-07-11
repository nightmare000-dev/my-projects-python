from lexicon import MENU, FUNCS, LIST_MENU

import copy
import datetime as dt
import os
import json

ts_id = 0 # id for task
state = ["todo", "in-progress", "done"] # state for task

# output information
def info():
    print("-" * 100)
    print(f"\nTask name: {key}")
    print(f"Id: {value["id"]}")
    print(f"Description: {value["description"]}")
    print(f"Status: {value["status"]}")
    print(f"Created at {value["createdAt"]}")
    print(f"Time: {value["time"]}\n")
    print("-" * 100)

# continue programm
def press(): input("\nPress ENTER to continue\n")

# output menu options of all lists
def list_menu():
    print()
    num = 1

    for key, value in LIST_MENU.items(): 
        print(f"({num}) -- {value} --\t\t\t<$ {key}>")
        num += 1

# output menu options
def menu():
    print()
    num = 1

    for key, value in MENU.items(): 
        print(f"({num}) -- {value} --\t\t\t<$ {key}>")
        num += 1

while True:
    os.system("clear")
    menu()

    option = input("\n$ ").split()

    # if <$ exit>
    if option[0] == FUNCS["exit"]: exit()

    # if <$ all>
    elif option[0] == FUNCS["list-all"]:
        os.system("clear")
        list_menu()
        
        option_list = input(f"\n$ ")

        # if <$ list>
        if option_list == FUNCS["list"]:
            os.system("clear")

            # reading file json
            with open("list_todo.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # if dict "all" don't have any task
            if not data["all"]: print([])

            for key, value in data["all"].items(): info()
            
            press()

        # if <$ list todo>
        elif option_list == FUNCS["list todo"]:
            os.system("clear")

            # reading file json
            with open("list_todo.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # if dict "all" don't have any task
            if not data["todo"]: print([])

            for key, value in data["todo"].items(): info()

            press()

        # if <$ list in-progress>
        elif option_list == FUNCS["list in-progress"]:
            os.system("clear")

            # reading file json
            with open("list_todo.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # if dict "all" don't have any task
            if not data["in-progress"]: print([])

            for key, value in data["in-progress"].items(): info()
            
            press()

        # if <$ list done>
        elif option_list == FUNCS["list done"]:
            os.system("clear")

            # reading file json
            with open("list_todo.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # if dict "all" don't have any task
            if not data["done"]: print([])
                

            for key, value in data["done"].items(): info()

            press()

    # if <$ add task_name>
    elif option[0] == FUNCS["add"] and option[1]:
        descr = input("Description : ")
        date_now = dt.datetime.now().strftime("%d.%m.%y")
        str_option = ' '.join(option[1:])
        now = dt.datetime.now()
        current_time = now.time()
        formatted = current_time.strftime("%H:%M:%S")
        os.system("clear")

        # reading json
        with open("list_todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data["all"]: ts_id += 1
        else:
            last_key = list(data["all"].keys())[-1]
            ts_id = data["all"][last_key]["id"] + 1

        data["all"].update({
                str_option: {
                        "id": ts_id,
                        "description": descr,
                        "status": state[0],
                        "createdAt": date_now,
                        "time": formatted,
                        "updatedAt": date_now
                    }
            })

        data["todo"].update({
                str_option: {
                        "id": ts_id,
                        "description": descr,
                        "status": state[0],
                        "createdAt": date_now,
                        "time": formatted,
                        "updatedAt": date_now
                    }
            })
        
        print(f"Task \"{str_option}\" just added")

        # writing changes
        with open("list_todo.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        press()

    # if <$ delete task_id>
    elif option[0] == FUNCS["delete"] and option[1].isdigit():
        os.system("clear")

        # reading json
        with open("list_todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if len(data["all"]) == 0: print("Todo list is empty")
        
        found = False

        # find the task by id
        for keys in data["all"].keys():
            if data["all"][keys]["id"] == int(option[1]):
                print(f"Task \"{keys}\" was deleted")
                del data["all"][keys]
                found = True

                try: del data["todo"][keys]
                except: pass

                try: del data["in-progress"][keys]
                except: pass

                try: del data["done"][keys]
                except: pass
                break

        if found == False: print("Task by id not found")    
        
        with open("list_todo.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        press()

    # if <$ mark-done task_id>
    elif option[0] == FUNCS["mark-done"] and option[1].isdigit():
        os.system("clear")
        found = False

        # reading json
        with open("list_todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for keys in data["all"].keys():
            if data["all"][keys]["id"] == int(option[1]):
                found = True

                print(f"Task \"{keys}\" changed to done")
                data["all"][keys]["status"] = state[2]
                data["done"][keys] = data["all"][keys]

                try: del data["todo"][keys]
                except: pass
                
                try: del data["in-progress"][keys]
                except: pass
    
                break

        with open("list_todo.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        if found == False: print("Task by id not found")

        press()

    # if <$ mark-in-progress task_id>
    elif option[0] == FUNCS["mark-in-progress"] and option[1].isdigit():
        os.system("clear")
        found = False

        # reading json
        with open("list_todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for keys in data["all"].keys():
            if data["all"][keys]["id"] == int(option[1]):
                found = True

                print(f"Task \"{keys}\" changed to in-progress")
                data["all"][keys]["status"] = state[1]
                data["in-progress"][keys] = data["all"][keys]

                try:
                    del data["todo"][keys]
                except: pass
    
                break

        with open("list_todo.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        if found == False: print("Task by id not found")

        press()

    # if <$ update task_id task_new_name>
    elif option[0] == FUNCS["update"] and option[1].isdigit() and option[2]:
        os.system("clear")
        found = False

        # reading json
        with open("list_todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        
        for keys in data["all"].keys():
            if data["all"][keys]["id"] == int(option[1]):
                found = True
                print(f"Task \"{keys}\" changed to \"{option[2]}\"")

                keys_value = data["all"][keys]
                del data["all"][keys]
                data["all"][option[2]] = keys_value

                try: 
                    keys_value = data["todo"][keys]
                    del data["todo"][keys]
                    data["todo"][option[2]] = keys_value
                except: pass

                try:
                    keys_value = data["in-progress"][keys]
                    del data["in-progress"][keys]
                    data["in-progress"][option[2]] = keys_value
                except: pass

                try: 
                    keys_value = data["done"][keys]
                    del data["done"][keys]
                    data["done"][option[2]] = keys_value
                except: pass

                break

        with open("list_todo.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        if found == False: print("Task by id not found")

        press()
