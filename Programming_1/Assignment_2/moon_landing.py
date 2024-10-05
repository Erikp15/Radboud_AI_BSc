#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_platform(total_height, ground_len, platform_pos, platform_len):
    """This function creates a string that when printed will render on the 
    terminal an image containing a 'wall', a 'ground' and a 'platform'. 
    
    TOTAL_HEIGHT: the height of the wall to be printed (y-axis)
    GROUND_LEN: the length of the ground
    PLATFORM_POS: the position of the platform along the x-axis
    PLATFORM_LEN: the length of the platform
    """
    
    platform = ''
    for i in range(total_height):
        platform += '\n'+'|'
    # guideline += '\n'+(width)*'_'
    platform += '\n'+(platform_pos-platform_len//2)*'_'+'|'+(platform_len)*'_'+'|'+(ground_len-platform_pos-platform_len//2)*'_'
    return platform

def create_rocket(total_height, height, position):
    """This function creates a string that when printed will render on the 
    terminal the image of a rocket.
    
    TOTAL_HEIGHT: the height of the image to be printed (y-axis)
    HEIGHT: the height of the rocket
    POSITION: the position of the rocket along the x-axis
    """
    
    rocket_drawing = """
      |      
     / \\    
    / _ \\   
   |.o '.|   
   |'._.'|   
   |     |   
 ,'|  |  |`. 
/  |  |  |  \\
|,-'--|--'-.|"""
    
    
    rocket_lines = rocket_drawing.splitlines()
    rocket = ''
    for i in range(total_height-height-rocket_height):
        rocket+='\n'
    for line in rocket_lines:
        rocket+= position*' ' + line+'\n'
    for i in range(height):
        rocket+='\n'        
    return rocket

rocket_height = 10
rocket_altitude = 15

max_altitude = 20
platform_target = 30
platform_len = 5
ground_len = 50

my_platform = create_platform(max_altitude, ground_len, platform_target, platform_len)

start_point = 15
my_rocket = create_rocket(max_altitude, rocket_altitude, start_point)

print(my_rocket)
print(my_platform)

