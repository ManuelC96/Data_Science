from PIL import Image
import matplotlib.pyplot as plt


# img = plt.imread("pexels-kevin-bidwell-2380794.jpg")
# print(img.shape)
# plt.imshow(img)
# plt.show()

image = Image.open("pexels-kevin-bidwell-2380794.jpg")
grayScale = image.convert("LA")




grayScale2 = grayScale.resize(size=(90,90))

for px in grayScale2.getdata():
    # print(px)
    pass

charSet = ["^", "/", "$", "%", "#", "@"]

pixel = grayScale2.getdata()
pixelList = list()

for px in grayScale2.getdata():
    pixelList.append(px[0])

pixelListSorted = pixelList.copy()
pixelListSorted.sort(reverse=True)
# print(pixelListSorted)

max_RGB_val = pixelListSorted[0]
# print(max_RGB_val)

interval = int(max_RGB_val / len(charSet))

# print(interval)

superString = ""

for px in pixelList:
    # print(int(px/interval))
    superString += charSet[int(px/interval) -1 ]

with open("ASCII_art.jpg", "w") as out:
    for i in range(0,len(superString),grayScale2.width): 
        nextLine = '\n'
        out.write(superString[i:i+grayScale2.width])
        out.write(nextLine)

# print(superString)








































# plt.imshow(grayScale)
# plt.show()