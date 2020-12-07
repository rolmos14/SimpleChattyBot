bot_name = "Tak"
bot_year = "2020"
print(f"Hello! My name is {bot_name}.\n"
      f"I was created in {bot_year}.")

user_name = input("Please, remind me your name.\n")
print(f"What a great name you have, {user_name}!")

print("Let me guess your age.\n"
      "Enter remainders of dividing your age by 3, 5 and 7.")
remainder3, remainder5, remainder7 = int(input()), int(input()), int(input())
user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {user_age}; that's a good time to start programming!")

final_count = int(input("Now I will prove to you that I can count to any number you want.\n"))
for num in range(final_count + 1):
    print(str(num) + "!")


print('''Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
''')

while True:
    user_answer = int(input())
    if user_answer == 2:
        break
    print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
