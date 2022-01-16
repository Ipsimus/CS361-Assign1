
import time

action_word = "run"

print("Please enter 1 to display a random image file path\n")
choice = int(input("Your choice: "))

while True:

    if choice == 1:
        file = open("image-service.txt", "w")
        file.write(action_word)
        file.close()

        time.sleep(20)

        file = open("image-service.txt", "r")
        message = file.read()
        file.close()
