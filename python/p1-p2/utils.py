from math import trunc
from tkinter import Image
import time

# basic draw drawing algorithm from in class notes
def basic_draw(x0, y0, x1, y1, image):
    # pre-calculations
    del_x = x1 - x0
    del_y = y1 - y0
    timef = 0
    
    if del_x < 0:
        # set the original x1 as x0
        # allows for drawing from left to right consistently
        temp_x = x0
        x0 = x1
        x1 = temp_x
        del_x = x1 - x0
        # change y0 and y1 as well
        temp_y = y0
        y0 = y1
        y1 = temp_y
        del_y = y1 - y0
    
    
    if del_x == 0:
        if del_y < 0:
            # change y0 and y1 as well
            temp_y = y0
            y0 = y1
            y1 = temp_y
            del_y = y1 - y0
        # vertical lines
        for y in range(del_y + 1):
            image.putpixel((x0, y0 + y), (255))        
    elif del_y == 0:
        # horizontal lines
        for x in range(del_x + 1):
            image.putpixel((x0 + x, y0), (255))
    elif del_y/del_x == 1:
        for x in range(del_x + 1):
            image.putpixel((x0 + x, y0), (255))
            y0 += 1
    elif del_y/del_x == -1:
        for x in range(del_x+ 1):
            image.putpixel((x0 + x, y0), (255))
            y0 -= 1
    else:
        # slope calculated here to prevent divide by zero error
        m = del_y / del_x
        # timer start
        time_start = time.perf_counter()
        
        # critical loop
        for i in range (del_x + 1):
            x = x0 + i
            y = m * i + y0
            y = trunc(y)
            image.putpixel((x,y), (255))
        
        # finish of critical loop, delta time calculated
        time_finish = time.perf_counter()
        timef = time_finish - time_start
    return timef

# bresenham algorithm from notes in class
# code from iq open genius
# https://iq.opengenus.org/bresenham-line-drawining-algorithm/
def brz_draw(x0, y0, x1, y1, image):
    
    # pre calculations
    del_x = x1 - x0
    del_y = y1 - y0
    x = x0
    y = y0
    timef = 0
    
    #absolute value of rate
    dx = abs(del_x)
    dy = abs(del_y)    
    
    if del_x == 0:
        if del_y < 0:
        # change y0 and y1 as well
            temp_y = y0
            y0 = y1
            y1 = temp_y
            del_y = y1 - y0
        # vertical lines
        for y_count in range(del_y + 1):
            image.putpixel((x0, y0 + y_count), (255))        
    elif del_y == 0:
        if del_x < 0:
            # change y0 and y1 as well
            temp_x = x0
            x0 = x1
            x1 = temp_x
            del_x = x1 - x0
        # horizontal lines
        for x_count in range(del_x + 1):
            image.putpixel((x0 + x_count, y0), (255))
    elif del_y/del_x == 1:  
        if del_x < 0:
            # set the original x1 as x0
            # allows for drawing from left to right consistently
            temp_x = x0
            x0 = x1
            x1 = temp_x
            del_x = x1 - x0
            # change y0 and y1 as well
            temp_y = y0
            y0 = y1
            y1 = temp_y
            del_y = y1 - y0
        for x in range(dx + 1):
            image.putpixel((x0 + x, y0), (255))
            y0 += 1
            
    elif del_y/del_x == -1:
        if del_x < 0:
            # set the original x1 as x0
            # allows for drawing from left to right consistently
            temp_x = x0
            x0 = x1
            x1 = temp_x
            del_x = x1 - x0
            # change y0 and y1 as well
            temp_y = y0
            y0 = y1
            y1 = temp_y
            del_y = y1 - y0
        for x in range(dx + 1):
            image.putpixel((x0 + x, y0), (255))
            y0 -= 1
    else:
        if dx > dy:
            pk = (2 * dy) - dx
            
            # critical loop
            time_start = time.perf_counter()
            for x_count in range(dx + 1):
                image.putpixel((x,y), (255))
                
                # ensures the slope is right
                if x0 < x1:
                    x += 1
                else:
                    x -= 1
            
                if pk < 0:
                    pk += (2* dy)
                else:
                    if y0 < y1:
                        y += 1
                    else:
                        y -= 1    
                    pk += (2* dy) - (2 * dx)
            time_end = time.perf_counter()
            return time_end - time_start
        
        else:
            pk = (2 * dx) - dy
            
            # critical loop
            time_start = time.perf_counter()
            for y_count in range(dy):
                image.putpixel((x,y), (255))
                
                # ensures slope is right
                if y0 < y1:
                        y += 1
                else:
                        y -= 1
                
                if pk < 0:
                    pk += 2 * dx
                else:
                    if x0 < x1:
                        x += 1
                    else:
                        x -= 1
    
                    pk += (2 * dx) - (2 * dy)
            time_end = time.perf_counter()
            return time_end - time_start

                
    