from PIL import Image
from tkinter import Tk
from utils import basic_draw, brz_draw
import random

if __name__ == '__main__':
    lines = int(input('How Many Lines? (Integers only):'))
    image = Image.new('L',(200,200))

    # Horizontal Line Test Case
    # Vertical Line Test Case
    # Positive Slope Test Case
    # Negative Slope Test Case
    
    time_total = 0
    for x in range(lines):
        # random number generation
        x0 = random.randrange(0,200,1)
        x1 = random.randrange(0,200,1)
        y0 = random.randrange(0,200,1)
        y1 = random.randrange(0,200,1)
        time_total += brz_draw(10, 100, 100, 50, image)
        
    print(f'Time total: {time_total}')
    # rotated and flipped as python image starts its axis from top left
    image = image.rotate(180)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    image.show()
    
