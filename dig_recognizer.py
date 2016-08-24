#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Digit recognizer for Kaggle competition (https://www.kaggle.com/c/digit-recognizer).'''

import os
import csv
from PIL import Image

def database():
  path_to_data = os.path.abspath(os.path.join('.', 'data_files/train.csv'))
  with open(path_to_data, 'r', newline = '') as datafile:
    data_from_file = csv.reader(datafile)
    header = next(data_from_file)
    data = [] 
    for line in data_from_file:
      data.append(line)
  return data


def draw_image(data):
  image = Image.new('L', (28, 28))
  # img = image.load()
  for i in range(28):
    for j in range(28):
      # img[i, j] = data[28*i+j]
      image.putpixel((i,j), int(data[28*i+j]))
      print(image.getpixel((i,j)), data[28*i+j])
      # print(img[i, j], data[28*i+j])
  image.show()
  # bytes(data[0][1:], 'utf-8')
  pass



if __name__ == '__main__':
  data = database()
  for i in range(20):
    draw_image(data[i][1:])
  pass