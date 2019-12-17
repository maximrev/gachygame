from tkinter import *
from random import *

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv =Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
width = 800
height = 600


for i in range (1, 7) :
	canv.create_line(i * width/8, 0, i * width/8, height)

class Key:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.vy = 0
		self.life = True
		self.color = randrange(1, 6, 1)
		if self.color == 1 :
			self.id = canv.create_rectangle(self.x, self.y, self.x + width/8, self.y + height/5, fill = 'black')
		else :
			self.id = canv.create_rectangle(self.x, self.y, self.x + width/8, self.y + height/5, fill = 'white')				
	def move_key(self):
		self.y += self.vy
		canv.move(self.id, 0, self.vy)

keys = []
keys.append(Key())
keys[0].vy = 5

def upd(event=''):
	for key in keys :
		key.move_key()
	canv.update()
	root.after(100, upd)

upd()

mainloop()
