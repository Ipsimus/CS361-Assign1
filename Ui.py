
import time



print("Please enter 1 to display a random image\n Enter 2 to end the program!")
choice = input()
action_word = "run"

while True:

    if choice == 1:
        file = open("image-service.txt", "w")
        file.write(action_word)
        file.close()

        time.sleep(5)

        file = open("image-service.txt", "r")
        message = file.read()
        file.close()

        print()