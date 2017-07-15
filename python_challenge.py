import re
import zipfile
from PIL import Image, ExifTags
import webcolors
import string


def level6():
    comments = []
    try:
        d = 90052
        while True:
            with zipfile.ZipFile("channel.zip") as fzip:
                with fzip.open(str(d) + ".txt") as f:
                    for line in f:
                        d = re.findall(b"\d+", line)[0].decode("utf-8")
                        print(d)
                        comments.append((fzip.getinfo(str(d) + ".txt").comment).decode("utf-8"))
    except IndexError:
        print("comments: ", len(comments))
        print(comments)
        # for i in comments:
        #     print(i)
        count_star = 0
        count_spaces = 0
        count_new_lines = 0
        count_O = 0
        count_X = 0
        count_Y = 0
        count_G = 0
        count_E = 0
        count_N = 0
        star = "*"
        space = " "
        new_line = "\\n"
        O = "O"
        X = "X"
        Y = "Y"
        G = "G"
        E = "E"
        N = "N"
        for i in comments:
            if i == star:
                count_star += 1
            elif i == space:
                count_spaces += 1
            elif i == new_line:
                count_new_lines += 1
            elif i == O:
                count_O += 1
            elif i == X:
                count_X += 1
            elif i == Y:
                count_Y += 1
            elif i == G:
                count_G += 1
            elif i == E:
                count_E += 1
            elif i == N:
                count_N += 1
        print("'*': ", count_star)
        print("' ': ", count_spaces)
        print("'\\n': ", count_new_lines)
        print("'O': ", count_O)
        print("'X': ", count_X)
        print("'Y': ", count_Y)
        print("'G': ", count_G)
        print("'E': ", count_E)
        print("'N': ", count_N)
        text = ""
        for i in comments:
            text += i
        print(text)

colors = []
closest = []
colorcodes = []

def level7():
    global colors
    global closest
    global colorcodes
    png = Image.open("oxygen.png")
    pix = png.load()
    coords = []
    for i in range(1, 607):
        color = pix[i, 47]
        colorcodes.append(color)
        coord = (i, 47)
        coords.append(coord)
        name, closest_name = get_colour_name(color)
        colors.append(name)
        closest.append(closest_name)
    print(colors)
    print(closest)
    setcolors = set(colors)
    setclosest = set(closest)
    print(setcolors)
    print(setclosest)
    print(colorcodes)
    setcolorcodes = set(colorcodes)
    print(setcolorcodes)
    print(len(setcolorcodes))
    print(coords)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def resize_img():
    xlist = []
    ylist = []
    img = Image.open("oxygen.png")
    pix = img.load()
    print(img.size)
    x, y = img.size
    for i in range(1, 95):
     for v in range(1, 607):
         color = pix[v, i]
         if color in colorcodes and i is not 20:
             xlist.append(v)
             ylist.append(i)
             # print("x: ", v, "y: ", i)
    setxlist = set(xlist)
    setylist = set(ylist)
    print(setxlist)
    print(setylist)



if __name__ == "__main__":
    print(string.ascii_letters[29])
    level7()
    resize_img()