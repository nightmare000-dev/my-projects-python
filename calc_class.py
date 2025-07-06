from lexicon._lexicon import LEXICON
from time import sleep

def value_error(): print(LEXICON["value_error"])
def output_formatter():
    sleep(0.5)
    print()

class Calculator:
    def numbers(self):
        k = 0

        while k == 0:
            try:
                self.firstNum = int(input(LEXICON["fn"]))
                self.secondNum = int(input(LEXICON["sn"]))
                k += 1
            except ValueError:
                value_error()
                continue

    def operator_choice(self):
        print()

        array = ['+', '-', '*', '/']
        k = 1

        for i in array:
            print(f"({k}) Operator ->  {i}")
            k += 1
        try:
            self.user_choice = int(input(LEXICON["us"]))
        except ValueError: value_error()

    def solving_the_problem(self):
        if self.user_choice in range(1, 4+1):
            if self.user_choice == 1:
                solution = self.firstNum + self.secondNum
                print(f"\n[SOLUTION] => {self.firstNum} + {self.secondNum} = {solution}")

            elif self.user_choice == 2:
                k = 0

                while k == 0:
                    module = input(LEXICON["module_abs"]).lower()

                    if module == "y":
                        solution = abs(self.firstNum - self.secondNum)
                        print(f"[SOLUTION] => {self.firstNum} - {self.secondNum} = {solution}")
                        k += 1
                        
                    elif module == "n":
                        solution = self.firstNum - self.secondNum
                        print(f"[SOLUTION] => {self.firstNum} - {self.secondNum} = {solution}")
                        k += 1
                        
                    else:
                        print(LEXICON["list_range"])
                        output_formatter()
                        continue

            elif self.user_choice == 3:
                solution = self.firstNum * self.secondNum
                print(f"\n[SOLUTION] => {self.firstNum} * {self.secondNum} = {solution}")

            elif self.user_choice == 4:
                k = 0

                while k == 0:
                    try:
                        module = int(input(LEXICON["module_operators"]))
                    except ValueError: value_error()

                    if module == 1:
                        solution = self.firstNum / self.secondNum
                        print(f"[SOLUTION] => {self.firstNum} / {self.secondNum} = {solution}")
                        k += 1

                    elif module == 2:
                        solution = self.firstNum // self.secondNum
                        print(f"[SOLUTION] => {self.firstNum} // {self.secondNum} = {solution}")
                        k += 1
                    
                    elif module == 3:
                        solution = self.firstNum % self.secondNum
                        print(f"[SOLUTION] => {self.firstNum} % {self.secondNum} = {solution}")
                        k += 1

                    else:
                        print(LEXICON["list_range"])
                        output_formatter()
                        continue
            
        else:
            while self.user_choice not in range(1, 4+1):
                print(LEXICON["list_range"])
                sleep(0.5)
                calc.operator_choice()
                
            else:
                try: calc.solving_the_problem()
                except: pass

def start():
    iteration = 0

    while True:
        global calc

        iteration += 1
        print(f"\nIteration -> {iteration}")

        calc = Calculator()
        calc.numbers()
        try: calc.operator_choice()
        except: break
        try: calc.solving_the_problem()
        except: pass
        output_formatter()

        process_continute = input(LEXICON["continue"]).lower()

        if process_continute == "y":
            print("-" * 120)
            continue

        elif process_continute == "n": break
        else:
            print(LEXICON["list_range"])
            break