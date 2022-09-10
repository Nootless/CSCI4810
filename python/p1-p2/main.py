from PIL import Image
from utils import basic_draw, brz_draw
import random

### README 
# To run this, you must have PIL package installed
# utils.py needs to be in the same directory
# math, random, and time come native with Python
def test_basic(image):
    
    # Horizontal Line Test Case
    basic_draw(0, 150, 100, 150, image)
    image.show()
    
    # Vertical Line Test Case
    basic_draw(100, 0, 100, 150, image)
    image.show()
    
    ## Positive Slope Test Case ##
    # Slope greater than 1
    basic_draw(25, 0, 50, 50, image)
    image.show()
    # Slope equal to 1
    basic_draw(50, 0, 100, 50, image)
    image.show()
    # Slope less than 1
    basic_draw(100, 0, 150, 25, image)
    image.show()
    
    ## Negative Slope Test Case ##
    
    # Slope greater than -1
    basic_draw(25, 50, 50, 0, image)
    image.show()
    # Slope equal to -1
    basic_draw(50, 50, 100, 0, image)
    image.show()
    # Slope less than -1
    basic_draw(100, 25, 150, 0, image)
    image.show()
    
    ### Backwards X ###
    
    # Horizontal Line Test Case
    basic_draw(100, 100, 0, 100, image)
    image.show()
    # Vertical Line Test Case
    basic_draw(150, 150, 150, 0, image)
    image.show()
    
    ## Positive Slope ##
    
    # Slope greater than 1
    basic_draw(50, 100, 25, 50, image)
    image.show()
    # Slope equal to 1
    basic_draw(100, 100, 50, 50, image)
    image.show()
    # Slope less than 1
    basic_draw(150, 50, 100, 25, image)
    image.show()
    
    ## Negative slope ##
    
    # Slope greater than -1
    basic_draw(50, 50, 25, 100, image)
    image.show()
    # Slope equal to 1
    basic_draw(100, 50, 50, 100, image)
    image.show()
    # Slope less than 1
    basic_draw(150, 25, 100, 50, image)
    image.show()
    
def test_brz(image):
    
    # Horizontal Line Test Case
    brz_draw(0, 150, 100, 150, image)
    image.show()
    # Vertical Line Test Case
    brz_draw(100, 0, 100, 150, image)
    image.show()
    
    ## Positive Slope Test Case ##
    # Slope greater than 1
    brz_draw(25, 0, 50, 50, image)
    image.show()
    # Slope equal to 1
    brz_draw(50, 0, 100, 50, image)
    image.show()
    # Slope less than 1
    brz_draw(100, 0, 150, 25, image)
    image.show()
    
    ## Negative Slope Test Case ##
    
    # Slope greater than -1
    brz_draw(25, 50, 50, 0, image)
    image.show()
    # Slope equal to -1
    brz_draw(50, 50, 100, 0, image)
    image.show()
    # Slope less than -1
    brz_draw(100, 25, 150, 0, image)
    image.show()
    
    ### Backwards X ###
    
    # Horizontal Line Test Case
    brz_draw(100, 100, 0, 100, image)
    image.show()
    # Vertical Line Test Case
    brz_draw(150, 150, 150, 0, image)
    image.show()
    
    ## Positive Slope ##
    
    # Slope greater than 1
    brz_draw(50, 100, 25, 50, image)
    image.show()
    # Slope equal to 1
    brz_draw(100, 100, 50, 50, image)
    image.show()
    # Slope less than 1
    brz_draw(150, 50, 100, 25, image)
    image.show()
    
    ## Negative slope ##
    
    # Slope greater than -1
    brz_draw(50, 50, 25, 100, image)
    image.show()
    # Slope equal to 1
    brz_draw(100, 50, 50, 100, image)
    image.show()
    # Slope less than 1
    brz_draw(150, 25, 100, 50, image)
    image.show()
    
# this function is used as the main program
# Bresenham algorithm picture follows basic algorithm picture
def user_input_test(lines,image,image2):
    time_total_basic = 0
    time_total_brz = 0
    for x in range(lines):
        # random number generation
        x0 = random.randrange(0,200,1)
        x1 = random.randrange(0,200,1)
        y0 = random.randrange(0,200,1)
        y1 = random.randrange(0,200,1)
        time_total_basic += basic_draw(x0, y0, x1, y1, image)
        time_total_brz += brz_draw(x0, y0, x1, y1, image2)    
    print(f'Time total_basic: {time_total_basic}\nTime total brz: {time_total_brz}')
    image.show()
    image2.show()
    
# this function is to test the time of longer lines    
def test_line_count_long(lines, image):
    time_total_basic = 0
    time_total_brz = 0
    for x in range(lines):
        time_total_basic += basic_draw(0,0,100,150,image)
        time_total_brz += brz_draw(0,0,100,150,image)
    print(f'Time total basic: {time_total_basic}\nTime total brz: {time_total_brz}')

# this function is to test the time of shorter lines
def test_line_count_short(lines, image):
    time_total_basic = 0
    time_total_brz = 0
    for x in range(lines):
        time_total_basic += basic_draw(0,0,25,20,image)
        time_total_brz += brz_draw(0,0,25,20,image)
    print(f'Time total basic: {time_total_basic}\nTime total brz: {time_total_brz}')


# this function is to test for slope differences using short lines
def test_slopes(lines, image):
    time_total_basic_greater = 0
    time_total_basic_lesser = 0
    time_total_brz_greater = 0
    time_total_brz_lesser = 0
    
    for x in range(lines):
        # >1 Slope
        time_total_basic_greater += basic_draw(0,0,20,25,image)
        time_total_brz_greater += brz_draw(0,0,20,25,image)
        
        # <1 Slope
        time_total_basic_lesser += basic_draw(0,0,25,20,image)
        time_total_brz_lesser += brz_draw(0,0,25,20,image)
    print(f'Time total basic <1: {time_total_basic_lesser}\
            \nTime total basic >1: {time_total_basic_greater}\
            \nTime total brz < 1: {time_total_brz_lesser}\
            \nTime total brz > 1: {time_total_brz_greater}\n')

    
if __name__ == '__main__':
    lines = int(input('How Many Lines? (Integers only):'))
    image = Image.new('L',(200,200))
    image2 = Image.new('L',(200,200))  
    # user input
    user_input_test(lines,image,image2)
         
    # run for test - used to display functionality
    # test_basic(image)
    # test_brz(image)
    
    # repitition tests - time comparisons
    # for x in [1,10,100,1000,10000,100000]:
    #     print(f'{x} Lines')
    #     test_line_count_long(x,image)
    #     test_line_count_short(x,image)
    #     test_slopes(x,image)
    
