import re
import zipfile
from PIL import Image, ExifTags, ImageDraw, ImageGrab, ImageEnhance, ImageOps
import webcolors
import codecs
import itertools as it


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
    for i in range(4, 607, 7):
        color = pix[i, 47]
        colorcodes.append(color)
        coord = (i, 47)
        coords.append(coord)
        name, closest_name = get_colour_name(color)
        colors.append(name)
        closest.append(closest_name)
    # print(colors)
    # print(closest)
    setcolors = set(colors)
    setclosest = set(closest)
    # print(setcolors)
    # print(setclosest)
    # print(colorcodes)
    setcolorcodes = set(colorcodes)
    # print(setcolorcodes)
    # print(len(setcolorcodes))
    # print(coords)
    letters = []
    text = ""
    for codes in colorcodes:
        letters.append(chr(codes[0]))
    for letter in letters:
        text += letter
    print(text)
    nums = re.findall("\d+", text)
    print(nums)
    for num in nums:
        print(chr(int(num)))


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
    # print(img.size)
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
    # print(setxlist)
    # print(setylist)
    imgbytes = img.tobytes()
    # imgbitmap = img.tobitmap()
    # print(imgbytes)
    # print(imgbytes.decode("raw"))
    # print(imgbitmap)
    res = pix[4, 47]
    print(res)
    print(res[0])
    print(chr(res[0]))


def level8():
    # un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    # pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    usernameen = \
        b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    passworden = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
    usernamede = codecs.decode(usernameen, "bz2")
    passwordde = codecs.decode(passworden, "bz2")
    print(usernamede.decode("utf-8"))  # huge
    print(passwordde.decode("utf-8"))  # file


def level9():
    first = [146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170,
             329, 170, 320, 170,
             310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194, 307,
             191, 312, 190, 316,
             190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197,
             383, 196, 387, 192,
             389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393,
             216, 390, 215, 385,
             215, 379, 213, 373, 213, 365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215,
             306, 216, 296, 218,
             290, 221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291,
             273, 289, 278, 287,
             279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295, 299, 300, 301,
             304, 304, 320, 305,
             327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302, 393,
             324, 391, 333, 387,
             328, 375, 329, 367, 329, 353, 330, 341, 331, 328, 336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343,
             269, 344, 262, 346,
             259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286,
             354, 279, 352, 268,
             352, 257, 351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339,
             132, 330, 122, 327,
             120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134,
             228, 136, 221, 137,
             214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159, 134, 157, 134, 160, 130, 170,
             125, 176, 114, 176,
             102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124, 115,
             120, 115, 115, 117,
             113, 120, 109, 122, 102, 122, 100, 121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100,
             130, 108, 132, 110,
             133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171,
             109, 171, 107, 161,
             111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276, 143,
             290, 148, 310, 151,
             332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399]

    second = [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168,
              157, 163, 157, 159,
              157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218,
              143, 220, 132, 220,
              125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97,
              167, 89, 164, 81, 162,
              77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115,
              146, 114, 155, 115,
              158, 121, 157, 128, 156, 134, 157, 136, 156, 136]
    #
    # print(len(first))
    # print(len(second))
    # print(len(set(first)))
    # print(len(set(second)))
    # sumfirst = sum(first)
    # print(sumfirst)
    # print(chr(sumfirst))
    # sumsecond = sum(second)
    # print(sumsecond)
    # print(chr(sumsecond))
    # sumit = sumfirst + sumsecond
    # print(sumit)
    # print(chr(sumit))
    img = Image.open("good.jpg")
    x, y = img.size
    pix = img.load()
    # print(pix[x-1, y-1])
    # color, closest_color = get_colour_name(pix[x-1, y-1])
    # print(color)
    # print(closest_color)
    # for i, j in img._getexif().items():
    #     if i in ExifTags.TAGS:
    #         print(ExifTags.TAGS[i] + " - " + str(j))
    # a = "hallo "
    # b = "du!"
    # print(a.join(b))
    coords = []
    x_coords = []
    y_coords = []
    print(img.size)
    for i in range(1, y):
        for v in first:
            if pix[v, i] == (0, 0, 0):
                # print("(" + str(v) + "," + str(i) + ")")
                coords.append((v, i))
                x_coords.append(v)
                y_coords.append(i)
    # print(coords)
    # print(set(coords))
    # print(set(x_coords))
    # print(set(y_coords))
    coords = []
    i = 0
    for a in first:
        if i % 2 == 0:
            coords.append((a, first[i+1]))
        i += 1
        if i == len(first):
            break
    print(coords)
    coords2 = []
    i = 0
    for a in second:
        if i % 2 == 0:
            coords2.append((a, second[i+1]))
        i += 1
        if i == len(second):
            break
    draw = ImageDraw.Draw(img)
    i = 1
    try:
        for coord in coords:
            # print(coord)
            # print(coords[i])
            draw.line([coord, coords[i]], 128)
            i += 1
    except IndexError:
        img.save("test.jpg", "JPEG")
        newimg = Image.open("test.jpg")
        newimg.show()
    # i = 0
    # try:
    #     for coord in coords2:
    #         draw.line(([coord, coords2[i]]), 128)
    #         i += 1
    # except IndexError:
    #     img.save("test.jpg", "JPEG")
    #     newimg = Image.open("test.jpg")
    #     newimg.show()


def level10():
    #  a = [1, 11, 21, 1211, 111221,...
    # zahl = "1221"
    # ergebnis = re.findall("\d", zahl)
    # count = 0
    # a = []
    # for i in ergebnis:
    #     if count == 0:
    #         a.append(i)
    #     if count > 0:
    #         if i == ergebnis[count-1]:
    #             a.append(i)
    #     count += 1
    # print(a)
    zahl = "1"
    for i in range(0, 30):
        test = []
        for j, g in it.groupby(zahl):
            # print(j)
            # print(list(g))
            a = list(g)
            # print(a)
            length = len(a)
            test.append(str(length) + j)
        # print(test)
        zahl = ""
        for i in test:
            # print(i)
            zahl += i
    print("Ergebnis: ", zahl)
    print(len(zahl))
    #  5808


def level11():
    img = Image.open("cave.jpg")
    info = img.info
    print(info)
    pix = img.load()
    raw = img.tobytes()
    # print(raw)
    colors = img.getcolors(1000000)
    print(len(colors))
    print(len(colors)/2)
    odd = []
    even = []
    data = img.getdata()
    # print(data)
    # print(list(data))
    # for val in list(data):
    #     if val%2 == 0:
    #         even.append(val)
    #     else:
    #         odd.append(val)
    print("Ungerade:")
    print(odd)
    print("Gerade:")
    print(even)
    # print(list(data))
    print("before")
    for i, j in img._getexif().items():
        if i in ExifTags.TAGS:
            print(ExifTags.TAGS[i] + " - " + str(j))
        else:
            print("No Tag")
    print("after")
    bands = img.getbands()
    # print(bands)
    histogram = img.histogram()
    print(histogram)
    for val in histogram:
        if val%2 == 0:
            even.append(val)
        else:
            odd.append(val)
    print("Gerade:")
    print(even)
    print(len(even))
    print("Ungerade:")
    print(odd)
    print(len(odd))
    img.putdata(even)
    # img.save("even.jpg")
    # img.show("even")
    img.putdata(odd)
    # img.save("odd.jpg")
    # img.show("odd")
    # tell = img.tell()
    # print(tell)
    # test = img.split()
    # print(test)
    # for img in test:
    #     img.show()
    screenshot = ImageGrab.grab()
    # screenshot.show("PythonScreenShot")
    enhancer = ImageEnhance.Sharpness(img)
    # for i in range(8):
    #     factor = i/4
    #     enhancer.enhance(factor).show("sharpness %f" % factor)
    # invert = ImageOps.invert(img)
    # invert.show()
    # split = invert.split()
    # for i in split:
    #     i.show()
    # contrast = ImageOps.autocontrast(img)
    # contrast.show()
    size = (int(img.size[0]/2), int(img.size[1]/2))
    img1 = Image.new("RGB", size)
    pixnew = img1.load()
    print(img.size)
    print(img1.size)
    count = 0
    pixel_1 = []
    coords_1 = []
    pixel_2 = []
    coords_2 = []
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if count%2 == 0:
                pixel_1.append(pix[x, y])
                coords_1.append((x, y))
                # print(1)
            else:
                pixel_2.append(pix[x, y])
                coords_2.append((x, y))
                # print(0)
            count += 1
    print(len(pixel_1))
    print(len(coords_1))
    print(len(pixel_2))
    print(len(coords_2))
    print(img1.size[0]*img1.size[1])
    print(img.size[0]*img.size[1])
    count = 0
    for y in range(img1.size[1]):
        for x in range(img1.size[0]):
            pixnew[x, y] = pixel_2[count]
            count += 1
    img1.show()
    pixel = img.getpixel((1, 1))
    pix_1 = []
    pix_2 = []
    pix_3 = []
    with open("pixel1", "w") as f:
        f.write("[")
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pix_1.append(img.getpixel((x, y))[0])
                if y is img.size[1]-1 and x is img.size[0]-1:
                    print("hey")
                f.write(str(img.getpixel((x, y))[0]) + ",")
                # print(img.getpixel((x, y))[0])
                pix_2.append(img.getpixel((x, y))[1])
                # print(img.getpixel((x, y))[1])
                pix_3.append(img.getpixel((x, y))[2])
                # print(img.getpixel((x, y))[2])
        f.write("]")
    print(len(pix_1))
    print(len(pix_2))
    print(len(pix_3))
    x, y = 0, 0
    print(img.size[0])
    for pixel in pix_1:
        img.putpixel((x, y), pixel)
        if x == img.size[0]-1:
            x = 0
            y += 1
        else:
            x += 1
    img.show()
    x, y = 0, 0
    for pixel in pix_2:
        img.putpixel((x, y), pixel)
        if x == img.size[0]-1:
            x = 0
            y += 1
        else:
            x += 1
    img.show()
    x, y = 0, 0
    for pixel in pix_2:
        img.putpixel((x, y), pixel)
        if x == img.size[0]-1:
            x = 0
            y += 1
        else:
            x += 1
    img.show()

if __name__ == "__main__":
    level11()
