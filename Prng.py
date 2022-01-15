# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time, random

while True:

    time.sleep(1)
    file = open("image-service.txt")
    message = file.read()
    file.close()

    if message == "run":

        random.seed(705)
        rand_num = random.randint(1, 999999999)

        file = open("image-service.txt", "wt")
        file.write(str(rand_num))
        file.close()









# 1.jpg: "Marlbrough Landscape." by Bernard Spragg is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/licenses/cc0/1.0/?ref=openverse&atype=rich
# 2.jpg: "Cleveland Landscape" by U.S. Geological Survey is licensed under CC PDM 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/mark/1.0/?ref=openverse&atype=rich
# 3.jpg: "2007.09 - 'Sunny still life seascape of splashing surf'. and granular rocks on the shore near Petit-Dalle in Normandy France; French landscape photography, Fons Heijnsbroek" by Amsterdam free photos & pictures of the Dutch city is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse&atype=rich
# 4.jpg: "2011.08 - 'View over the urban landscape to the North of Amsterdam - seen from the bridge Nescio-brug over the canal Amsterdam-Rijn-kanaal; geotag free urban picture, in public domain / Commons CCO; city photography by Fons Heijnsbroek, The Netherlands" by Amsterdam free photos & pictures of the Dutch city is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse&atype=rich
# 5.jpg: "landscape" by waldemarjan is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0/?ref=openverse&atype=rich