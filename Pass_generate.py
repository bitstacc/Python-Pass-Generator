#generate password which is tough to break

#To generate a random output we will use the module named random.
#In order to use this module we need to first import it.
import random

#Now we have to create our variables
#These will be incorperated into our password.
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%^&*()"

#Here we create our variables for password creation.
#An we sset the length we wish our password to be.
Use_for = lower_case + upper_case + number + symbols
length_for_pass = 8

#Here we will create our password = "" because we don't know our pass yet.
#We then use the join fuction to combine .sample 
# (which means to use our variables for pass in Random order)
#And we set that to follow our other variables as such...
# (Use_for, length_for_pass), 
password = "".join(random.sample(Use_for, length_for_pass))

#Finally we tell the computer to print our password!
print("Generated password is =", password)