import tkinter as tk
import math
import time
from random import *
from pynput import keyboard
from pynput.keyboard import Key, Listener
import threading
import os
import pygame as pg
from playsound import playsound


width = 1366
height = 700
#HP = 50
score = 0
num_of_lines = 5
line_width = width/num_of_lines
block_height = 70
button_height = 30
vy = 200
tick = 10
keys = [i for i in range(1, num_of_lines)]
pressed = [0 for i in range(1, num_of_lines)]
pressed_enter = [0 for i in range(1, num_of_lines)]
mode = 1
blocks = []
xline = [0 for i in range(2)]
max_num=0


def lets_play():
	root = tk.Tk()
	root.title("Anal Piano")
	root.geometry("1366x768")

	C = tk.Canvas(root, bg="blue", height=1366, width=768)
	filename = tk.PhotoImage(master = C, file = "white1.png")
	background_label = tk.Label(root, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)


	C.pack()

	btn = tk.Button(root, text="PIANO PIANO", background="grey", foreground="white", activebackground="grey", activeforeground="white", padx="20", pady="8", font="50", command = autors)
   
	btn.place(relx=.2, rely=.2, anchor="c", height=60, width=200, bordermode=tk.OUTSIDE)

	btn1 = tk.Button(root, text="start game", background="grey", foreground="white", activebackground="red", activeforeground="green", padx="20", pady="8", font="16", command = start)

	btn1.place(relx=.48, rely=.43, anchor="c", height=60, width=200, bordermode=tk.OUTSIDE)

	btn2 = tk.Button(root, text="music", background="grey", foreground="white", activebackground="red", activeforeground="green", padx="20", pady="8", font="16")
	btn2.place(relx=.48, rely=.75, anchor="c", height=60, width=130, bordermode=tk.OUTSIDE)
	root.mainloop()

def autors():


	root = tk.Tk()
	root.title("Anal Piano")
	root.geometry("1366x768")
	
	C = tk.Canvas(root, bg="blue", height=1366, width=768)
	filename = tk.PhotoImage(master = C,file = "white1.png")
	background_label = tk.Label(root, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	root.mainloop()


class Line:
	def __init__(self, x):
		self.x = x

class Block:
	def __init__(self, line, x, y, block_height, vy, col_num):
		self.x = x - 1
		self.y = y
		self.vy = vy
		self.line = line
		self.height = block_height
		self.times = [time.time(), time.time()]
		self.life = True
		self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#		self.color = '#%02x%02x%02x' % (randint(0,255), randint(0,255), randint(0,255))
#		self.color = randrange(1, 6, 1)
#		if self.color == 1 :
		self.id = canv.create_rectangle(self.x, self.y, self.x - line_width + 1, self.y + self.height, fill = self.colors[5-col_num])
#		else :
#			self.id = canv.create_rectangle(self.x, self.y, self.x - line_width, self.y + self.height, fill = 'white')				
	def move(self):
		if self.life == True:
			if self.y > buttons[self.line].y:
				self.life = False
#				global HP
#				HP -= 1
			self.delta_t = self.times[0] - self.times[1]
			self.times[1] = self.times[0]
			self.times[0] = time.time()
			self.y += self.delta_t * self.vy
			canv.move(self.id, 0, self.delta_t * self.vy)
		else:
			canv.delete(self.id)
			del self

class Button:
	def __init__(self, line, x, button_height):
		self.x = x
		self.y = height - button_height
		self.line = int(line)
		self.height = button_height
		self.actionBtn = tk.Button(root2, text = self.line + 1, fg = 'red', activeforeground = "white", borderwidth = 1, bg = "black", command = self.clicked)
		self.actionBtn.place(x = self.x, y = self.y, width = line_width, height = self.height)
	def clicked(self):
#		buf = 0
		for block in blocks:
			if block.line == self.line:
				if block.y + block.height >= self.y and block.y <= self.y:
					if block.life == True:
						block.life = False
						global score 
						score += 1
#					buf = 1
#		if buf == 0:
#			global HP
#			HP -= 1

class HP_Bar:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.label = tk.Label(root2, text = score)
		self.label.place(x = self.x, y = self.y)
	def upd(self):
#		if HP == 0:
#			lose()
		self.label.config(text = score)
		
def lose():				#change it
	os._exit(1)

def on_press(key):
	for i in range(1, num_of_lines):
		if "'" + str(keys[i-1]) + "'" == str(key):
			if pressed[i-1] == 0:
				buttons[i-1].clicked()
				buttons[i-1].actionBtn.config(bg='white')
				pressed[i-1] = 1
		if key == Key.enter:
			if pressed_enter[0] == 0:
				pressed_enter[0] = 1
				write_timecode()


def on_release(key):
	for i in range(1, num_of_lines):
		if "'" + str(keys[i-1]) + "'" == str(key):
			if pressed[i-1] == 1:
				buttons[i-1].actionBtn.config(bg='black')
				pressed[i-1] = 0		
	if key == Key.enter:
		pressed_enter[0] = 0

	if key == Key.esc:
		if mode == 0:
			timecodes.close()
		os._exit(1)

def start_capture():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

def music(filename):
	playsound(filename)
'''	pg.mixer.init()
	pg.mixer.music.load(filename)
	pg.mixer.music.play()'''

def write_timecode():
	time_now = time.time()
	if mode == 0:
		timecodes.write(str(time_now - time_begin) + '\n')

def create_blocks(filename_timecodes):
	ready_timecodes = open(filename_timecodes, "r")
	col_num = 0
	for line in ready_timecodes:
		xline[1] = randint(0, num_of_lines - 2)
		while xline[1] == xline[0]:
			xline[1] = randint(0, num_of_lines - 2)
		xline[0] = xline[1]
		y = height - button_height - block_height/2 - vy*float(line)
		blocks.append(Block(xline[1], lines[xline[1]].x, y, block_height, vy, col_num % 6))
		col_num += 1
		global max_num
		max_num += 1

def upd(event=''):
	for block in blocks :
		block.move()
	hp_bar.upd()
	canv.update()
	root2.after(tick, upd)

def start():
	global root2, canv, lines, buttons, time_begin, hp_bar
	root2 = tk.Tk()
	fr = tk.Frame(root2)
	root2.geometry('1366x700')
	canv = tk.Canvas(root2, bg='white', height=height, width=width)
	canv.pack(expand=1)
	
	hp_bar = HP_Bar(0, 0)
	
	lines = [Line(i*line_width) for i in range(1, num_of_lines)]
	#blocks = [Block(i-1, lines[i-1].x, block_height * i, i/10) for i in range(1, num_of_lines)]
	if mode == 0:
		timecodes = open("timecodes.txt","w+")
	else:
		create_blocks("timecodes.txt")
	buttons = [Button(i-1, lines[i-1].x - line_width, button_height) for i in range(1, num_of_lines)]

	time_begin = time.time()
	
	thread1 = threading.Thread(target = start_capture)
	thread1.start()
	
	filename = 'music/Junost_v_sapogah.mp3'
	thread2 = threading.Thread(target = music, args = (filename, ))
	thread2.start()

	upd()
	root2.mainloop()


lets_play()
