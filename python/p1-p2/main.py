from PIL import Image
from utils import basic_draw, brz_draw
import random

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

def user_input_test(lines,image):
    time_total = 0
    for x in range(lines):
        # random number generation
        x0 = random.randrange(0,200,1)
        x1 = random.randrange(0,200,1)
        y0 = random.randrange(0,200,1)
        y1 = random.randrange(0,200,1)
        # time_total += basic_draw(x0, y0, x1, y1, image)
        time_total += brz_draw(x0, y0, x1, y1, image)    
    print(f'Time total: {time_total}')
    image.show()
    
def test_line_count_long(lines, image):
    time_total_basic = 0
    time_total_brz = 0
    for x in range(lines):
        time_total_basic += basic_draw(0,0,25,25,image)
        time_total_brz += brz_draw(0,0,25,25,image)
    print(f'Time total basic: {time_total_basic}\nTime total brz: {time_total_brz}')
        
def test_line_count_short(lines, image):
    time_total_basic = 0
    time_total_brz = 0
    for x in range(lines):
        time_total_basic += basic_draw(0,0,100,100,image)
        time_total_brz += brz_draw(0,0,100,100,image)
    print(f'Time total basic: {time_total_basic}\nTime total brz: {time_total_brz}')
    
if __name__ == '__main__':
    lines = int(input('How Many Lines? (Integers only):'))
    image = Image.new('L',(200,200))
         
    # run for test
    # test_basic(image)
    # test_brz(image)
    # test_line_count_long(lines,image)
    # test_line_count_short(lines,image)
    
    # user input
    user_input_test(lines,image)
    
