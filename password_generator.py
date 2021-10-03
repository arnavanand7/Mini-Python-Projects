import random

print("### P A S S W O R D   G E N E R A T O R ###")
passwordLength = int(input("Enter the length of password: "))
stringOfAlphaNumeric = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
gengeratedPassword = "".join(random.sample(stringOfAlphaNumeric, passwordLength))
print ("Your Generated Password: ", gengeratedPassword)