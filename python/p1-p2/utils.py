from math import trunc
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
            x = x0 + i # shift over
            y = m * i + y0 # calculate y point from slope and initial
            y = trunc(y) # truncate to work on int point system
            image.putpixel((x,y), (255))
        
        # finish of critical loop, delta time calculated
        time_finish = time.perf_counter()
        timef = time_finish - time_start
    return timef

# bresenham algorithm from notes in class
# https://csustan.csustan.edu/~tom/Lecture-Notes/Graphics/Bresenham-Line/Bresenham-Line.pdf
# Bresenham algorithm from California State University
def brz_draw(x0, y0, x1, y1, image):
    
    # pre calculations
    timef = 0
    dx = x1 - x0
    dy = y1 - y0
    # copy
    d_x = dx
    d_y = dy 
    
    # slope checks
    if dy < 0:
        # invert dy
        dy = -dy
        step_y = -1
    else:
        step_y = 1
    
    if dx < 0:
        # invert dx
        dx = -dx
        step_x = -1
    else:
        step_x = 1
    
    # bit shift dy and dx (multiply by 2)
    dy <<= 1;
    dx <<= 1;
    
    if d_x == 0:
        # vertical line
        # assigns the lower bound to y0
        if y1 < y0:
            y0 = y1
            d_y = -d_y
        for y_range in range(d_y + 1): 
            image.putpixel((x0, y0 + y_range), (255))
            
    elif d_y == 0:
        # horizontal line
        # assigns lower bound to x0
        if x1 < x0:
            x0 = x1
            d_x = -d_x
        for x_range in range(d_x + 1):
            image.putpixel((x0 + x_range, y0), (255))
    elif d_y/d_x == 1:
        # 45 degree line
        # rearranges to assign lower bound to both y0 and x0
        # to allow for inverted input
        if x1 < x0:
            y0 = y1
            x0 = x1
            d_x = - d_x
            d_y = - d_y
        for x_range in range(d_x + 1):
            image.putpixel((x0 + x_range, y0), (255))
            y0 += 1
    elif d_y/d_x == -1:
        # 315 degree line
        # rearranges to assign lower bound to both y0 and x0
        # to allow for inverted input 
        if x1 < x0:
            y0 = y1
            x0 = x1
            d_x = - d_x
            d_y = - d_y
        for x_range in range(d_x + 1):
            image.putpixel((x0 + x_range, y0), (255))
            y0 -= 1     
    else:
        # uses x as the iterator, y as the calculated point
        if dx > dy:
            # this is the amount y has increased since last increment
            # used to represent if y needs to increase or stay the same
            fraction = dy - (dx >> 1)
            
            # critical loop
            time_start = time.perf_counter()
            while x0 != x1:
                image.putpixel((x0,y0),(255))
                # if y needs to increase, adjust y by the step and
                # decrement the fraction two times the difference in x0 and x1
                # otherwise the y stays at its current value
                x0 += step_x
                if fraction >= 0:
                    y0 += step_y
                    fraction -= dx
                fraction += dy
            time_end = time.perf_counter()
            timef = time_end - time_start
            
        else:
            # uses y as the iterator, x as the calculated point
            # this is the amount x has increased since last increment
            # used to represent if x needs to increase or stay the same
            fraction = dx - (dy >> 1)
            
            # critical loop
            time_start = time.perf_counter()
            while y0 != y1:
                image.putpixel((x0,y0),(255))
                # if x needs to increase, adjust x by the step and
                # decrement two times the difference in y0 and y1
                # otherwise the x stays at its current value
                if fraction >= 0:
                    x0 += step_x
                    fraction -= dy
                y0 += step_y
                fraction += dx
            time_end = time.perf_counter()
            timef = time_end - time_start
    return timef
            
    
    

                
    