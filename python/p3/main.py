from tkinter import *
from tkinter import filedialog
from PIL import Image
import utils
import numpy

# global declares
global lines_array
global transforms 
transforms = numpy.array([[1, 0, 0],[0, 1, 0], [0, 0, 1]])

# create App
# comes from https://www.youtube.com/watch?v=ELkaEpN29PU

def import_file():
    global lines_array
    global transforms 
    filename = filedialog.askopenfilename()
    # check for no input
    if(len(filename) != 0):
        lines_array = numpy.genfromtxt(f'{filename}',delimiter=',')
        # textbox update
        text_box.delete('1.0','end')
        text_box.insert(END,lines_array)
        text_box_info.delete('1.0','end')
        text_box_info.insert(END,f'Length:{len(lines_array)}')


def export_file():
    numpy.savetxt(f'{output_entry.get()}.csv',lines_array,delimiter=',')

def basic_translate(original, t_x,t_y):
    global lines_array
    global transforms 
    trans_matrix = numpy.array([[1, 0, 0],[0, 1, 0],[t_x,t_y, 1]])
    trans_matrix = trans_matrix.astype(float)
    return numpy.matmul(original,trans_matrix)

def translate_func():
    global lines_array
    global transforms 
    x_trans = 0
    y_trans = 0
    # checks for lengtsh
    if len(translate_x_entry.get()) != 0:
        x_trans = translate_x_entry.get()
    if len(translate_y_entry.get()) != 0:
        y_trans = translate_y_entry.get()

    # multiply and add transforms to transform matrix
    trans_matrix = numpy.array([[1, 0, 0],[0, 1, 0],[translate_x_entry.get(),translate_y_entry.get(), 1]])
    trans_matrix = trans_matrix.astype(float)
    
    # print(transforms)
    # print(trans_matrix)
    # transforms and updates user
    transforms = basic_translate(transforms,translate_x_entry.get(),translate_y_entry.get())
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('translate')

def basic_scale_func():
    print('basic scale')

def scale_func():
    print('scale')

def basic_rotate_func():
    print('basic rotate')

def rotate_func():
    print('rotate')

def display_image():
    print('display')

def insert_line():
    print('insert Line')
if __name__ == '__main__':
    

    app = Tk()
    app.title('Transmongus')
    app.geometry('1000x800')
    
    # add data files inputs

    input_x0 = StringVar()
    input_x1 = StringVar()
    input_y0 = StringVar()
    input_y1 = StringVar()
    
    input_label = Label(app, text='Lines')
    input_label.grid(row=9,column=0)
    input_x0_box = Entry(app, textvariable=input_x0)
    input_x0_box.grid(row=9,column=1, sticky=W)
    input_y0_box = Entry(app, textvariable=input_y0)
    input_y0_box.grid(row=9,column=2, sticky=W)
    input_x1_box = Entry(app, textvariable=input_x1)
    input_x1_box.grid(row=9,column=3,sticky=W)
    input_y1_box = Entry(app, textvariable=input_y1)
    input_y1_box.grid(row=9,column=4,sticky=W)
    
    # output file
    output_text = StringVar()
    output_entry = Entry(app, textvariable=output_text)
    output_entry.grid(row=0, column=2)
    
    # translate X and Y
    x_text = StringVar()
    y_text = StringVar()
    translate_label = Label(app,text='Translate (X,Y)', font=('bold', 12), pady=20)
    translate_label.grid(row=2,column=0,sticky=W)
    translate_x_entry = Entry(app, textvariable=x_text)
    translate_x_entry.grid(row=2, column=1)
    translate_y_entry = Entry(app, textvariable=y_text)
    translate_y_entry.grid(row=2, column=2)
    
    #  Basic Scale and Scale
    trans_x = StringVar()
    trans_y = StringVar()
    center_x = StringVar()
    center_y = StringVar()
    scale_label = Label(app,text='Scale (X,Y)', font=('bold', 12), pady=20)
    scale_label.grid(row=3,column=0,sticky=W)
    scale_x_entry = Entry(app, textvariable=trans_x)
    scale_x_entry.grid(row=3, column=1)
    scale_y_entry = Entry(app, textvariable=trans_y)
    scale_y_entry.grid(row=3, column=2)
    
    scale_label = Label(app,text='Scale (X,Y)', font=('bold', 12), pady=20)
    scale_label.grid(row=3,column=0,sticky=W)
    scale_cx_entry = Entry(app, textvariable=center_x)
    scale_cx_entry.grid(row=4, column=1)
    scale_cy_entry = Entry(app, textvariable=center_y)
    scale_cy_entry.grid(row=4, column=2)
    
    # Basic Rotate
    rotate = StringVar()
    rotate_center_x = StringVar()
    rotate_center_y = StringVar()
    
    rotate_label = Label(app,text='Rotate(deg,Cx,Cy)', font=('bold', 12), pady=20)
    rotate_label.grid(row=5,column=0,sticky=W)
    
    rotate_entry = Entry(app, textvariable=rotate)
    rotate_entry.grid(row=5, column=1)
    rotate_cx_entry = Entry(app, textvariable=rotate_center_x)
    rotate_cx_entry.grid(row=6, column=1)
    rotate_cy_entry = Entry(app, textvariable=rotate_center_y)
    rotate_cy_entry.grid(row=6, column=2)
    
    # displays data points
    text_box_label = Label(app, text='Points and Transforms')
    text_box_label.grid(row=11,column=0)
    text_box = Text(app, width=20, height=15)
    text_box.grid(row=11,column=1)

    text_box_info = Text(app,width=10,height=1)
    text_box_info.grid(row=11,column=3)

    transform_text_box = Text(app,width=20,height=15)
    transform_text_box.grid(row=11,column=2)
    
    # Buttons
    # import button
    import_button = Button(app,text='Import File',command=import_file)
    import_button.grid(row=0,column=0)

    # export button
    export_button = Button(app, text='Export File',command=export_file)
    export_button.grid(row=0, column=3)

    # translate button
    translate_button = Button(app, text='Translate',command=translate_func)
    translate_button.grid(row=2,column=3)

    # scale button
    basic_scale_button = Button(app,text='B.Scale', command=basic_scale_func)
    basic_scale_button.grid(row=3,column=3)

    scale_button = Button(app,text='Scale', command=scale_func)
    scale_button.grid(row=4,column=3)
    
    # rotate button
    basic_rotate_button = Button(app,text='B.Rotate', command=basic_rotate_func)
    basic_rotate_button.grid(row=5,column=3)

    rotate_button = Button(app,text='Rotate',command=rotate_func)
    rotate_button.grid(row=6,column=3)

    # Display Image
    display_button = Button(app,text='Display', command=display_image)
    display_button.grid(row=11,column=4)

    # insert 
    insert_button = Button(app,text='Insert Line',command=insert_line)
    insert_button.grid(row=9,column=5)

    app.mainloop()
    

    
