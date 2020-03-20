# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:15:25 2020

@author: kaimo
"""
from tkinter import Tk
from tkinter import Frame

class Window:
  __windowAttribute = {
    'title'    : "Analysis Image",
    'resize'   : True,
    'icono'    : '../hola.ico',
    'color_bg' : 'black',   # Color background
    'relief'   : 'ridge'
  }

  __frameAttribute = {
    'width'    : 480,
    'height'   : 320,
    'color_bg' : 'grey',
    'cursor'   : 'arrow',
    'border'   : 20,
    'fill'     : 'both',   # x: horizontal, y: vertical
    'expand'   : 1         # Expand all whole window
  }

  def __init__(self):
    root = Tk()
    self.setWindow(root)
    self.setFrame(root)
    root.mainloop()

  def setFrame(self, root):
    frame = Frame(root)
    frame.pack()
    self.adaptFrame(frame)
    self.dimensionFrame(frame)
    self.colorFrame(frame)
    self.cursorFrame(frame)
    
  # =========================
  #  FRAME'S FUNCTIONS
  # =========================
  def adaptFrame(self, frame):
    fill_   = self.getFill()
    expand_ = self.getExpand()
    frame.pack( fill = fill_, expand = expand_)

  def dimensionFrame(self, frame):
    width_  = self.getWidth()
    height_ = self.getHeight()
    frame.config(width = width_, height = height_)

  def colorFrame(self, frame):
    color_bg = self.getColorBG('frame')
    border  = self.getBorder()
    frame.config(bg = color_bg)
    frame.config(bd = border)
  
  def cursorFrame(self, frame):
    cursor_ = self.getCursor()
    frame.config(cursor = cursor_)

  # =========================
  #  WINDOW'S FUNCTIONS
  # =========================
  def setWindow(self, root):
    self.titleWindow(root)
    self.iconoWindow(root)
    self.isResizable(root)
    self.colorWindow(root)
    self.reliefWindow(root)

  def titleWindow(self, root):
    title  = self.getTitle()
    root.title(title)

  def iconoWindow(self, root):
    icono = self.getIcono()
    root.iconbitmap(icono)

  def isResizable(self, root):
    resize = self.getResize()
    if resize:
      root.resizable(1,1)
    else:
      root.resizable(0,0)    

  def colorWindow(self, root):
    color = self.getColorBG('window')
    root.config(bg = color)

  def reliefWindow(self, root):
    relief_ = self.getRelief()
    root.config(relief = relief_)

  # ==============================
  #  WINDOW'S GETTERS AND SETTERS
  # ==============================
  def getTitle(self):
    return self.__windowAttribute['title']

  def setTitle(self, title):
    self.__windowAttribute['title'] = title

  def getResize(self):
    return self.__windowAttribute['resize']

  def setResize(self, resize):
    self.__windowAttribute['resize'] = resize

  def getIcono(self):
    return self.__windowAttribute['icono']

  def setIcono(self, icono):
    self.__windowAttribute['icono'] = icono

  def getColorBG(self, widget = 'window'):
    if widget == 'window':
      return self.__windowAttribute['color_bg']
    elif widget == 'frame':
      return self.__frameAttribute['color_bg']
  
  def setColorBG(self, color, widget = 'window'):
    if widget == 'window':
      self.__windowAttribute['color_bg'] = color
    elif widget == 'frame':
      self.__frameAttribute['color_bg'] = color
  
  def getRelief(self):
    return self.__windowAttribute['relief']
  
  def setRelief(self, relief):
    self.__windowAttribute['relief'] = relief

  # ==============================
  #  FRAME'S GETTERS AND SETTERS
  # ==============================
  def getWidth(self):
    return self.__frameAttribute['width']

  def setWidth(self, width):
    self.__frameAttribute['width'] = width

  def getHeight(self):
    return self.__frameAttribute['height']

  def setHeight(self, height):
    self.__frameAttribute['height'] = height
 
  def getCursor(self):
    return self.__frameAttribute['cursor']
  
  def setCursor(self, cursor):
    self.__frameAttribute['cursor'] = str(cursor)

  def getBorder(self):
    return self.__frameAttribute['border']
  
  def setBorder(self, border):
    self.__frameAttribute['border'] = int(border)

  def getFill(self):
    return self.__frameAttribute['fill']
  
  def setFill(self, fill):
    self.__frameAttribute['fill'] = str(fill)

  def getExpand(self):
    return self.__frameAttribute['expand']

  def setExpand(self, expand):
    if expand:
      self.__frameAttribute['expand'] = 1
    else:
      self.__frameAttribute['expand'] = 0
  
v = Window()
