

import random 

# The len of wanted password
password_length = int(input("the length of your password: "))

# Simple infostructure of the password generator
pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"

# Random function that takes the pass_data and combine it with pass_data
password = "".join(random.sample(pass_data, password_length))
print(password)






























