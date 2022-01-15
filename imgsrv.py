
import time

image_elements = 5

while True:

    time.sleep(1)
    file = open("image-service.txt")
    message = int(file.read())
    file.close()

    image_num = message % image_elements
    image_path = "C:\\Users\\Omar\\PycharmProjects\\CS361-Assign1\\" + str(image_num) + ".jpg"

    file = open("image-service.txt", "w")
    file.write(image_path)
    file.close()

