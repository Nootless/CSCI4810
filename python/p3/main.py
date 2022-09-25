from tkinter import *
from PIL import Image
import utils


# create App
# comes from https://www.youtube.com/watch?v=ELkaEpN29PU
def app_init():
    app = Tk()
    app.title('Transmongus')
    app.geometry('1000x800')
    
    # add data files inputs
    input_text = StringVar()
    input_label = Label(app,text='Input File', font=('bold', 12), pady=20)
    input_label.grid(row=0,column=0,sticky=W)
    input_entry = Entry(app, textvariable=input_text)
    input_entry.grid(row=0, column=1)

    # output file
    output_text = StringVar()
    output_label = Label(app,text='Output File', font=('bold', 12), pady=20)
    output_label.grid(row=1,column=0,sticky=W)
    output_entry = Entry(app, textvariable=output_text)
    output_entry.grid(row=1, column=1)
    
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
    rottate_cx_entry = Entry(app, textvariable=rotate_center_x)
    rottate_cx_entry.grid(row=6, column=1)
    rottate_cy_entry = Entry(app, textvariable=rotate_center_y)
    rottate_cy_entry.grid(row=6, column=2)
    
    # Buttons
    # import button
    import_button = Button(app,text='Import File',command=import_file)
    import_button.grid(row=0,column=2)

    # export button
    export_button = Button(app, text='Export File',command=export_file)
    export_button.grid(row=1, column=2)

    # translate button
    translate_button = Button(app, text='Translate',command=translate_func)
    translate_button.grid(row=2,column=3)

    # scale button
    basic_scale_button = Button(app,text='Basic Scale', command=basic_scale_func)
    basic_scale_button.grid(row=3,column=3)

    scale_button = Button(app,text='Scale', command=scale_func)
    scale_button.grid(row=4,column=3)
    
    # rotate button
    basic_rotate_button = Button(app,text='Basic Rotate', command=basic_rotate_func)
    basic_rotate_button.grid(row=5,column=3)

    rotate_button = Button(app,text='Rotate',command=rotate_func)
    rotate_button.grid(row=6,column=3)

    
    return app

def import_file():
    print('import file')

def export_file():
    print('export file')

def translate_func():
    print('translate function')

def basic_scale_func():
    print('basic scale')

def scale_func():
    print('scale')

def basic_rotate_func():
    print('basic rotate')

def rotate_func():
    print('rotate')

if __name__ == '__main__':
    app = app_init()
    app.mainloop()    

    
