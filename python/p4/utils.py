from math import trunc
import time
import numpy

# bresenham algorithm from notes in class
# https://csustan.csustan.edu/~tom/Lecture-Notes/Graphics/Bresenham-Line/Bresenham-Line.pdf
# Bresenham algorithm from California State University
def draw(x0, y0, x1, y1, image):
    
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


# Set of basic transformations that are independent of program
def basic_translate(original, t_x,t_y):
    print(t_x,t_y)
    t_x = float(t_x)
    t_y = float(t_y)
    trans_matrix = numpy.array([[1, 0, 0],[0, 1, 0],[t_x,t_y, 1]])

    return numpy.matmul(original,trans_matrix)

def basic_rot(original, theta):
    theta = float(theta)
    trans_matrix = numpy.array([[numpy.cos(numpy.radians(theta)),numpy.sin(-(numpy.radians(theta))), 0],
                                [numpy.sin(numpy.radians(theta)),numpy.cos(numpy.radians(theta)),0],[0,0,1]])
    return numpy.matmul(original,trans_matrix)

def basic_scale(original,r_x,r_y):
    trans_matrix = numpy.array([[r_x,0,0],[0,r_y,0],[0,0,1]])
    trans_matrix = trans_matrix.astype(float)

    return numpy.matmul(original,trans_matrix)

def basic_trans3(original, t_x, t_y, t_z):
    t_x = float(t_x)
    t_y = float(t_y)
    t_z = float(t_z)
    trans_matrix = numpy.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[t_x,t_y,t_z,1]])
    
    return numpy.matmul(original, trans_matrix)

def basic_scale3(original,sx,sy,sz):
    trans_matrix = numpy.array([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
    trans_matrix = trans_matrix.astype(float)

    return numpy.matmul(original,trans_matrix)

# about of z axis
def basic_rotate3z(original,theta):
    theta = float(theta)
    trans_matrix = numpy.array([[numpy.cos(numpy.radians(theta)),numpy.sin((numpy.radians(theta))),0,0],
                                [numpy.sin(-numpy.radians(theta)),numpy.cos(numpy.radians(theta)),0,0],
                                [0,0,1,0],[0,0,0,1]])
    return numpy.matmul(original,trans_matrix)

def basic_rotate3y(original,theta):
    theta = float(theta)
    trans_matrix = numpy.array([[numpy.cos(numpy.radians(theta)),0,numpy.sin((-numpy.radians(theta))),0],
                                [0,1,0,0],
                                [numpy.sin(numpy.radians(theta)),0,numpy.cos(numpy.radians(theta)),0],
                                [0,0,0,1]])
    return numpy.matmul(original,trans_matrix)

def basic_rotate3x(original,theta):
    theta = float(theta)
    trans_matrix = numpy.array([[1,0,0,0],
                                [0,numpy.cos(numpy.radians(theta)),numpy.sin((numpy.radians(theta))),0],
                                [0,numpy.sin(-numpy.radians(theta)),numpy.cos(numpy.radians(theta)),0],
                                [0,0,0,1]])
    return numpy.matmul(original,trans_matrix)