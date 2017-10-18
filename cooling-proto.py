# coding: utf-8

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#input temp in kelvin, time in seconds, k in 1/seconds
input_dict = {'init_temp': 373.0,
              'surrounding_temp': 293.0,
              'time_difference': 1200.0,
              'cooling_constant': 0.00150,}

data_dict = {}

def cooling_function(input_dict):
    t_0 = t_s = s = k = 0.0 #initialization

    t_0 = input_dict['init_temp']
    t_s = input_dict['surrounding_temp']
    s = input_dict['time_difference'] 
    k = input_dict['cooling_constant']

    final_temp = t_s + (t_0 - t_s) * math.exp(-(k)*s)
    
    return final_temp

final_temp = cooling_function(input_dict)

def data_array(input_dict):
    # initialize
    t_0 = t_f = s = k = 0.0 
    time_array = temp_array = []


    t_0 = input_dict['init_temp']
    t_s = input_dict['surrounding_temp']
    s = input_dict['time_difference']
    k = input_dict['cooling_constant']    

    time_array = np.linspace(0.0, s, num=10)
    data_dict['time'] = time_array
        
    def temp_func(time_array): 
        for s in time_array:
            t_f = t_s + (t_0 - t_s) * math.exp(-(k)*s)
            temp_array.append(t_f)
            
    temp_func(time_array)
    data_dict['temp'] = temp_array
    
temp_array = data_array(input_dict)

df = pd.DataFrame.from_dict(data=data_dict)
print(df)

graph = plt.plot(data_dict['time'], data_dict['temp'])
print(graph)

