#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Digit recognizer for Kaggle competition (https://www.kaggle.com/c/digit-recognizer).'''

import os
import csv
from PIL import Image
import math

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

def freq_of_pixels(image):
  '''Frequencies of pixels in horiz and vert lines of image.
  Actually, any of vars, for example, horiz_freq_sum is a list with len == width_image items where is frequencies of width and height pixels. It's important note!'''
  
  horiz_freq_sum, vert_freq_sum = [0] * int(len(image)**0.5), [0] * int(len(image)**0.5)
  for i in range(len(image)):
    if int(image[i]) != 0:
      horiz_freq_sum[(i)//int(len(image)**0.5)] += 1
      vert_freq_sum[(i)%int(len(image)**0.5)] += 1
  print('''Horiz_lines: {0} 
Vert_lines: {1}'''.format(horiz_freq_sum, vert_freq_sum))
  return [horiz_freq_sum, vert_freq_sum]
    

def caclulations_for_one_as_line(image):
  h_and_v_freq = freq_of_pixels(image)
  horiz_freq_sum = h_and_v_freq[0]
  vert_freq_sum = h_and_v_freq[1]
  h_counter, v_counter = 0, 0
  for i in range(len(horiz_freq_sum)):
    if horiz_freq_sum[i] > 1: #another variants: !=0, for example
      h_counter += 1
    if vert_freq_sum[i] > 1:  #another variants: !=0, for example  
      v_counter += 1
  
    h_start, v_start, h_end, v_end = 0, 0, 0, 0
  for i in range(len(horiz_freq_sum)):
    if horiz_freq_sum[i] != 0 and h_start == 0:
      h_start = i
    if horiz_freq_sum[i] != 0 and h_start != 0:
      h_end = i
  for i in range(len(vert_freq_sum)):
    if vert_freq_sum[i] != 0 and v_start == 0:
      v_start = i
    if vert_freq_sum[i] != 0 and v_start != 0:
      v_end = i

  h_v = [h_counter, v_counter]
      
  h_line = h_end+1 - h_start
  v_line = v_end+1 - v_start

  dgre = round(math.degrees(math.atan(h_line / v_line)))
  
  return [horiz_freq_sum, vert_freq_sum, h_counter, v_counter, h_start, v_start, h_end, v_end, h_v, h_line, v_line, dgre]
    
def neuron_one_as_line(image):
  result_of_one_as_line_cheking = caclulations_for_one_as_line(image)
  
  horiz_freq_sum = result_of_one_as_line_cheking[0]
  vert_freq_sum = result_of_one_as_line_cheking[1]
  h_counter = result_of_one_as_line_cheking[2]
  v_counter = result_of_one_as_line_cheking[3]
  h_start = result_of_one_as_line_cheking[4]
  v_start = result_of_one_as_line_cheking[5]
  h_end = result_of_one_as_line_cheking[6]
  v_end = result_of_one_as_line_cheking[7]
  h_v = result_of_one_as_line_cheking[8]
  h_line = result_of_one_as_line_cheking[9]
  v_line = result_of_one_as_line_cheking[10]
  dgre = result_of_one_as_line_cheking[11]
    

  print('h_counter: {0}, v_counter: {1}, h_start: {2}, h_end: {3}, v_start: {4}, v_end: {5}, {6},{7},{8}'.format(h_counter, v_counter, h_start, h_end, v_start, v_end, h_line, v_line, dgre))
  
  neuron_output = False
  
  # for case when line is horizontal or vertical
  if max(h_v) / min(h_v) >= 1.5: # need to think more about this coef, or in another way - normalization of data before start this neuron
    neuron_output = True
  
  # for case when line is diagonal
  else:
    shift = round((h_counter ** 2 + v_counter ** 2) ** 0.5) #shift is a rounded value of hypotenuse
    new_image = image_rotation(image, dgre)
    result_of_one_as_line_cheking = caclulations_for_one_as_line(new_image)
  
    horiz_freq_sum = result_of_one_as_line_cheking[0]
    vert_freq_sum = result_of_one_as_line_cheking[1]
    h_counter = result_of_one_as_line_cheking[2]
    v_counter = result_of_one_as_line_cheking[3]
    h_start = result_of_one_as_line_cheking[4]
    v_start = result_of_one_as_line_cheking[5]
    h_end = result_of_one_as_line_cheking[6]
    v_end = result_of_one_as_line_cheking[7]
    h_v = result_of_one_as_line_cheking[8]
    h_line = result_of_one_as_line_cheking[9]
    v_line = result_of_one_as_line_cheking[10]
    dgre = result_of_one_as_line_cheking[11]
    
    if max(h_v) / min(h_v) >= 1.5: # need to think more about this coef, or in another way - normalization of data before start this neuron
      neuron_output = True
    else:
    # for case when one has check mark (like seven)... NEED to Write!!!!
      neuron_output = False
  
  
  print(neuron_output)
  return neuron_output
    

def image_rotation(image, angle):
  '''This method rotate original image to new image with line in the center'''
  img = Image.new('L', (28, 28))
  for i in range(28):
    for j in range(28):
      img.putpixel((i,j), int(image[28*i+j]))
  new_image = img.rotate(angle, expand=True)    
  # print(new_image)
  # new_image.show()
  ni_load = new_image.load()
  
  image_pixels = []
  new_image_width = new_image.size[0]
  print(new_image_width)
  for i in range(new_image_width**2):
    # print(i//new_image_width, i%new_image_width)
    try: # BUG: in some cases for unknown reasons without try it doesnt work!
      image_pixels.append(str(ni_load[i//new_image_width, i%new_image_width]))
    except:
      pass
  
  return image_pixels
  
  
# for zero:
# in train.csv have zeroes with:
#  1) line in zero's circle
#  2) with a circuit which is interrupted at the boundary of the figure and the alleged beyond its bordersю
# If for zeroes pattern searching we will be use circuit searching, then: 
#  most of these zeroes with first future can be detected by reducing the line width to 1 px

# for 'one' digits:
# In most cases, this is a straight or nearly straight line located in different directions.
# sometimes this line is curved line, or, also sometimes it has check mark, like the seven 

if __name__ == '__main__':
  data = database()
  # counter_of_frequency_of_numbers(data)
  
  # # draw the first 20 images
  # for i in range(20):
  #   draw_image(data[i][1:])


  # # draw last 5 images from data list, sorted by numbers 
  data_by_numbers = examples_by_numbers(data)
  
  
  # for i in range(4679, 4684):
    # draw_image(data_by_numbers[1][i][1:])

  for i in range(3):
    freq_of_pixels(data_by_numbers[1][i][-3:])
    

  counter = 0
  for i in range(len(data_by_numbers[1])):
    if neuron_one_as_line(data_by_numbers[1][i][1:]) == True:
      counter += 1
   
  print(len(data_by_numbers[1]), counter)

  pass
