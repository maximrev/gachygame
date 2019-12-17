import tkinter as tk
from random import *

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
width = 800
height = 600
HP = 10
num_of_lines = 8
line_width = width/num_of_lines
block_height = 30
button_height = 30

class Line:
	def __init__(self, x):
		self.x = x

class Block:
	def __init__(self, x, block_height, vy):
		self.x = x - 1
		self.y = 0
		self.vy = vy
		self.height = block_height
		self.life = True
#		self.color = randrange(1, 6, 1)
#		if self.color == 1 :
		self.id = canv.create_rectangle(self.x, self.y, self.x - line_width + 1, self.y + self.height, fill = 'white')
#		else :
#			self.id = canv.create_rectangle(self.x, self.y, self.x - line_width, self.y + self.height, fill = 'white')				
	def move(self):
		if self.life == True:
			self.y += self.vy
			canv.move(self.id, 0, self.vy)
		else:
			canv.delete(self.id)
			del self

class Button:
	def __init__(self, x, button_height):
		self.x = x
		self.y = height - button_height
		self.height = button_height
		self.actionBtn = tk.Button(root,activeforeground = "white", borderwidth = 1, bg = "black", command = self.clicked).place(x = self.x, y = self.y, width = line_width, height = self.height)
#		self.id = canv.create_rectangle(self.x, self.y, self.x - line_width, self.y + self.height, fill = 'red')
	def clicked(self):
		found = 0
		for block in blocks:
			if block.x == self.x + line_width - 1:
				block.life = False
				found = 1
				continue
		if found == 1:
			HP -= 1

lines = [Line(i*line_width) for i in range(1, num_of_lines)]
blocks = [Block(lines[i-1].x, block_height * i, i/10) for i in range(1, num_of_lines)]
buttons = [Button(lines[i-1].x - line_width, button_height) for i in range(1, num_of_lines)]

def upd(event=''):
	for block in blocks :
		block.move()
	canv.update()
	root.after(1, upd)

upd()

tk.mainloop()
