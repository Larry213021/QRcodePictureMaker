from PIL import Image, ImageEnhance
import qrcode
import matplotlib.pyplot as plt


c=raw_input("please input your website:")
img = qrcode.make(c)
print(type(img))
img.save("abc.jpg")



qrcode1 = Image.open(r'C:\Users\Larrywu\Desktop\schoolHW\qrcodescanner\qrcode_generate_scanner-20190917T020508Z-001\qrcode_generate_scanner\abc.jpg').convert("RGBA")




src_size = (qrcode1.size[0], qrcode1.size[1])
qrcode1 = qrcode1.resize((99, 99))




plt.imshow(qrcode1)
plt.show()



bg = Image.open(r'C:\Users\Larrywu\Desktop\schoolHW\qrcodescanner\qrcode_generate_scanner-20190917T020508Z-001\qrcode_generate_scanner\twitch.png').convert("RGBA")



plt.imshow(bg)
plt.show()



if bg.size[0] < bg.size[1]:
    bg = bg.resize((qrcode1.size[0]-24, (qrcode1.size[0]-24)*int(bg.size[1]/bg.size[0])))
else:
    bg = bg.resize(((qrcode1.size[1]-24)*int(bg.size[0]/bg.size[1]), qrcode1.size[1]-24))




    for i in range(qrcode1.size[0] - 24):
        for j in range(qrcode1.size[1] -24):

            if i < 24 and j < 24:
                continue

            elif i < 24 and j > qrcode1.size[1] - 49:
                continue

            elif i > qrcode1.size[0] - 49 and j < 24:
                continue
            elif i % 3 == 1 and j % 3 == 1:
                continue

            elif bg.getpixel((i, j))[3] == 0:
                continue
            else:
                qrcode1.putpixel((i + 12, j + 12), bg.getpixel((i, j)))
                img = qrcode1.resize(src_size)

img.save('newqrcode.png')
plt.imshow(img)
plt.show()
plt.close()