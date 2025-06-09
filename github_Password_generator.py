from random import *
import string

alphabet_upper = string.ascii_uppercase # 2
alphabet_lower = string.ascii_lowercase
nums = '1234567890' # 4
symbols = '!?/,._-+*%$#&()[]<>~' # 1
password = ''

for alpL in range(4):
    ran_alp_low = choice(alphabet_lower)
    password += ran_alp_low
        
for alpU in range(2):
    ran_alp_up = choice(alphabet_upper)
    password += ran_alp_up
        
for nms in range(4):
    ran_nums = choice(nums)
    password += ran_nums
    
for symb in range(2):
    ran_symb = choice(symbols)
    password += ran_symb

pass_list = list(password)
shuffle(pass_list)

result = ''.join(pass_list)

print(result)