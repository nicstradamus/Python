print("Let's see how long you have lived in days, minutes and seconds.")
name = input("Name: ")
print("now enter you age")
age = int(input("age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926

print("{} has been alive for {} days, {} minutes, and {} seconds".format(
      name,days,minutes,seconds))
