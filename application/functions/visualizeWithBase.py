from BIOImage import *

def visualizeWithBase(nucleoList, baseList):
    n = len(nucleoList)

    SCREENW = 80 * n
    SCREENH = 80 * n
    bio = BIOImage((SCREENW, SCREENH), 'white')

    center_of_rotation_x = SCREENW / 2
    center_of_rotation_y = SCREENH / 2
    radius = 30 * n

    i = 0
    x = center_of_rotation_x + radius * cos((2 * pi * i) / (n + 1))
    y = center_of_rotation_y - radius * sin((2 * pi * i) / (n + 1))
    nucleoList[0].setCords(x, y)

    for i in range(1, n):
        x = center_of_rotation_x + radius * cos((2 * pi * i) / (n + 1))
        y = center_of_rotation_y - radius * sin((2 * pi * i) / (n + 1))
        nucleoList[i].setCords(x, y)

        bio.drawCircleLine((nucleoList[i - 1].cordX, nucleoList[i - 1].cordY),
                           (nucleoList[i].cordX, nucleoList[i].cordY))

    numPairs = len(baseList)

    for i in range(0, numPairs):

        if baseList[i].orientation == 'cis':

            if baseList[i].interaction == 'WW':
                bio.drawWWcis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'WH':

                bio.drawWHcis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'HW':

                bio.drawWHcis((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                              (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'WS':

                bio.drawWScis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'SW':

                bio.drawWScis((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                              (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'HH':

                bio.drawHHcis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'HS':

                bio.drawHScis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'SH':

                bio.drawHScis((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                              (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'SS':

                bio.drawSScis((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                              (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)



        else:

            if baseList[i].interaction == 'WW':
                bio.drawWWtrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'WH':

                bio.drawWHtrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'HW':

                bio.drawWHtrans((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                                (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'WS':

                bio.drawWStrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'SW':

                bio.drawWStrans((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                                (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'HH':

                bio.drawHHtrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'HS':

                bio.drawHStrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

            elif baseList[i].interaction == 'SH':

                bio.drawHStrans((baseList[i].nTwo.cordX, baseList[i].nTwo.cordY),
                                (baseList[i].nOne.cordX, baseList[i].nOne.cordY), 50)

            elif baseList[i].interaction == 'SS':

                bio.drawSStrans((baseList[i].nOne.cordX, baseList[i].nOne.cordY),
                                (baseList[i].nTwo.cordX, baseList[i].nTwo.cordY), 50)

    for i in range(0, n):

        if i % 10 == 0:
            x = center_of_rotation_x + (radius + 150) * cos((2 * pi * i) / (n + 1))
            y = center_of_rotation_y - (radius + 150) * sin((2 * pi * i) / (n + 1))
            bio.drawNum((int(x), int(y)), str(nucleoList[i].index), 150)

        if (nucleoList[i].label == 'G'):
            bio.drawNodeG((int(nucleoList[i].cordX), int(nucleoList[i].cordY)), nucleoList[i].label, 150)
        elif (nucleoList[i].label == 'C'):
            bio.drawNodeC((int(nucleoList[i].cordX), int(nucleoList[i].cordY)), nucleoList[i].label, 150)
        elif (nucleoList[i].label == 'A'):
            bio.drawNodeA((int(nucleoList[i].cordX), int(nucleoList[i].cordY)), nucleoList[i].label, 150)
        elif (nucleoList[i].label == 'U'):
            bio.drawNodeU((int(nucleoList[i].cordX), int(nucleoList[i].cordY)), nucleoList[i].label, 150)

    #bio.show()
    bio.save("temp.png")

    return bio
