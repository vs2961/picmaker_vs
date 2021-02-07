import random

def write_image(color_arr, fil):
    for i in color_arr:
        toWrite = ""
        for j in i:
            toWrite += " ".join([str(x) for x in j]) + " "
        fil.write(toWrite + "\n")

pic = open("cyberspace.ppm", "w")
pic.write("P3\n500, 500\n 255\n")

color_arr1 = [[[(i % (j + 1)), (j % (i + 1)), i + j] for j in range(284, 34, -1)] for i in range(284, 34, -1)]
color_arr2 = [[[(i % (j + 1)), (j % (i + 1)), j + i] for j in range(35, 285)] for i in range(284, 4, -1)]
color_arr3 = [[[(i % (j + 1)), (j % (i + 1)), i + j] for j in range(284, 34, -1)] for i in range(35, 285)]
color_arr4 = [[[(i % (j + 1)), (j % (i + 1)), j + i] for j in range(35, 285)] for i in range(35, 285)]

for i in range(len(color_arr1)):
    color_arr1[i] += color_arr2[i]
for i in range(len(color_arr3)):
    color_arr1.append(color_arr3[i] + color_arr4[i])

write_image(color_arr1, pic)
pic.close()
