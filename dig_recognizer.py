#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Digit recognizer for Kaggle competition (https://www.kaggle.com/c/digit-recognizer).'''

import os
import csv
import PIL

def database():
  path_to_data = os.path.abspath(os.path.join('.', 'data_files/train.csv'))
  with open(path_to_data, 'r', newline = '') as datafile:
    data_from_file = csv.reader(datafile)
    header = next(data_from_file)
    data = [] 
    for line in data_from_file:
      data.append(line)
  return len(data)

def draw_image(image):
  
  pass

if __name__ == '__main__':
  print(database())
  pass