
from PIL import Image
# import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b , alpha = 256):
	if alpha == 0:
		return ' '
	lenth 	=	len(ascii_char)
	gray 	=	int(0.3 * r + 0.59 * g + 0.11 * b)
	unit 	=	256/lenth;

	return ascii_char[int(gray/unit)]

IMG 	=	'ascii_dora.png'

if __name__ == '__main__':

	im 				=	Image.open(IMG)
	WIDTH, HEIGHT 	=	im.size
	WIDTH 			=	min(WIDTH, 100)
	HEIGHT 			=	min(HEIGHT, 100)
	im 				=	im.resize((WIDTH, HEIGHT), Image.NEAREST)#重新设置图片的大小
	txt 			=	""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			# print(im.getpixel((i,j)))
			txt +=	get_char(*im.getpixel((j,i)))	#im.getpixel((x,y)) 获取图片坐标x,y的 像素值
		txt +=	'\n'

	print(txt)

	with open("output.txt", 'w') as f:
		f.write(txt)
















