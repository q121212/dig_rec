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
  for i in range(28):
    for j in range(28):
      image.putpixel((i,j), int(data[28*i+j]))
      # print(image.getpixel((i,j)), data[28*i+j])
  image.show()
  pass


def counter_of_frequency_of_numbers(data):
  frequency_of_numbers = [0] * 10
  for i in range(len(data)):
    for j in range(10):
      if data[i][0] == str(j):
        frequency_of_numbers[j]+=1
  for i in range(10):
    print('{0}: {1}'.format(i, frequency_of_numbers[i]))

def examples_by_numbers(data):
  data_by_numbers = [[], [], [], [], [], [], [], [], [], []]

  for i in range(len(data)):
    for j in range(10):
      if data[i][0] == str(j):
        data_by_numbers[j].append(data[i])
  return data_by_numbers



# for zero:
# in train.csv have zeroes with:
#  1) line in zero's circle
#  2) with a circuit which is interrupted at the boundary of the figure and the alleged beyond its bordersю
# If for zeroes pattern searching we will be use circuit searching, then: 
#  most of these zeroes with first future can be detected by reducing the line width to 1 px

# for 'one' digits:
# In most cases, this is a straight or nearly straight line located in different directionsю
# sometimes this line is curved line, or, also sometimes it has check mark, like the seven 

if __name__ == '__main__':
  data = database()
  # counter_of_frequency_of_numbers(data)
  
  # # draw the first 20 images
  # for i in range(20):
  #   draw_image(data[i][1:])


  # draw first 20 images from data list, sorted by numbers 
  data_by_numbers = examples_by_numbers(data)
  for i in range(20):
    draw_image(data_by_numbers[1][i][1:])



  

  pass