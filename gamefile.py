from tkinter import *
from random import *

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv =Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
width = 800
height = 600
num_of_lines = 8
line_width = width/num_of_lines
block_height = 5
class Line:
	def __init__(self, x):
		self.x = x

class Block:
	def __init__(self, x, block_height, vy):
		self.x = x
		self.y = 0
		self.vy = vy
		self.block_height = block_height
		self.life = True
		self.color = randrange(1, 6, 1)
		if self.color == 1 :
			self.id = canv.create_rectangle(self.x, self.y, self.x - line_width, self.y + block_height, fill = 'black')
		else :
			self.id = canv.create_rectangle(self.x, self.y, self.x - line_width, self.y + block_height, fill = 'white')				
	def move(self):
		self.y += self.vy
		canv.move(self.id, 0, self.vy)

lines = [Line(i*line_width) for i in range(1, num_of_lines)]

blocks = [Block(lines[i-1].x, block_height * i, i/10) for i in range(1, num_of_lines)]

def upd(event=''):
	for block in blocks :
		block.move()
	canv.update()
	root.after(1, upd)

upd()

mainloop()
