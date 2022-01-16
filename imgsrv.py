import os
import time

image_elements = 5

while True:

    time.sleep(5)
    file = open("image-service.txt")

    try:
        message = int(file.read())

    except:
        continue

    file.close()

    image_num = message % image_elements
    file_names = os.listdir("images")

    image_path = os.getcwd() + "\\images\\" + file_names[0]

    file = open("image-service.txt", "w")
    file.write(image_path)
    file.close()



