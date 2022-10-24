from tkinter import *
from tkinter import filedialog
from PIL import Image
from utils import *
import numpy
import math

# global declares
global lines_array 
global transforms 
lines_array = []
transforms = create_identity_4()
# Constants
N = 1000


# create App
# comes from https://www.youtube.com/watch?v=ELkaEpN29PU

def import_file():
    global lines_array
    global transforms 
    filename = filedialog.askopenfilename()
    # check for no input
    if(len(filename) != 0):
        lines_array = numpy.loadtxt(filename,delimiter=',')
        # textbox update
        text_box.delete('1.0','end')
        text_box.insert(END,lines_array)
        text_box_info.delete('1.0','end')
        text_box_info.insert(END,f'Length:{len(lines_array)}')

# exports files
def export_file():
    numpy.savetxt(f'{output_entry.get()}.csv',lines_array,delimiter=',')

# Translate function used 
def translate_func():
    global transforms 
    x_trans = 0
    y_trans = 0
    z_trans = 0
    # checks for lengtsh
    if len(translate_x_entry.get()) != 0:
        x_trans = translate_x_entry.get()
    if len(translate_y_entry.get()) != 0:
        y_trans = translate_y_entry.get()
    if len(translate_z_entry.get()) != 0:
        z_trans = translate_z_entry.get()

    # print(transforms)
    # print(trans_matrix)
    # transforms and updates user
    transforms = basic_trans3(transforms,x_trans,y_trans,z_trans)
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('translate')


def basic_scale_func():
    # initializing
    global transforms
    x_scl = 1
    y_scl = 1
    z_scl = 1

    # empty checks
    if len(scale_x_entry.get()) != 0:
        x_scl = scale_x_entry.get()
    if len(scale_y_entry.get()) != 0:
        y_scl = scale_y_entry.get()
    if len(scale_z_entry.get()) != 0:
        z_scl = scale_z_entry.get()

    # Add transformation back to general and show in table
    transforms = basic_scale3(transforms,x_scl,y_scl,z_scl)
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('basic scale')

def scale_func():
    # initializing
    global transforms
    x_scl = 1
    y_scl = 1
    z_scl = 1
    cx = 0
    cy = 0
    cz = 0

    # ensuring no empty entry
    # converted to floats to ensure no undefined behavior
    if len(scale_x_entry.get()) != 0:
        x_scl = float(scale_x_entry.get())
    if len(scale_y_entry.get()) != 0:
        y_scl = float(scale_y_entry.get())
    if len(scale_z_entry.get()) != 0:
        z_scl = float(scale_z_entry.get())

    if len(scale_cx_entry.get()) != 0:
        cx = float(scale_cx_entry.get())
    if len(scale_cy_entry.get()) != 0:
        cy = float(scale_cy_entry.get())
    if len(scale_cz_entry.get()) != 0:
        cz = float(scale_cz_entry.get())


    # translate to center, rotate, the return back to original
    transforms = basic_trans3(transforms,-cx,-cy,-cz)
    transforms = basic_scale3(transforms, x_scl, y_scl, z_scl)
    transforms = basic_trans3(transforms,cx,cy,cz)

    # Add transformation back to table
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

    print('scale')

def rotate_x_func():
    global transforms
    theta = 0

    # in case of empty lengths
    if len(rotate_entry.get()) != 0:
        theta = float(rotate_entry.get())

    transforms = basic_rotate3x(transforms, theta)

    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

def rotate_y_func():
    global transforms
    theta = 0

    # in case of empty lengths
    if len(rotate_entry.get()) != 0:
        theta = float(rotate_entry.get())
    
    transforms = basic_rotate3y(transforms, theta)
    
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

def rotate_z_func():
    global transforms
    theta = 0
    
    # in case of empty lengths
    if len(rotate_entry.get()) != 0:
        theta = float(rotate_entry.get())
        
    transforms = basic_rotate3z(transforms, theta)

    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

def rotate_func():
    global transforms
    cx_rot = 0
    cy_rot = 0
    theta = 0
    # in case of empty lengths
    if len(rotate_entry.get()) != 0:
        theta = float(rotate_entry.get())
    if len(rotate_cx_entry.get()) != 0:
        cx_rot = float(rotate_cx_entry.get())
    if len(rotate_cy_entry.get()) != 0:
        cy_rot = float(rotate_cy_entry.get())
    
    # perform transforms to matrix and display
    transforms = basic_translate(transforms,-1*cx_rot,-1*cy_rot)
    transforms = basic_rot(transforms,theta)
    transforms = basic_translate(transforms,cx_rot,cy_rot)

    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

    print('rotate')

def insert_line():
    global lines_array
    # combines new lines with a given input
    new_line = numpy.array([[float(input_x0_box.get()),float(input_y0_box.get()),
                             float(input_z0_box.get()),float(input_index.get())]])
    lines_array = numpy.concatenate((lines_array,new_line))
    text_box.delete('1.0','end')
    text_box.insert(END,lines_array)
    text_box_info.delete('1.0','end')
    text_box_info.insert(END,f'Length:{len(lines_array)}')

def apply_transform():
    global lines_array
    global transforms
    temp_array = numpy.empty([1,4])
    # apply transform to stored lines
    for line in lines_array:
        origin_cord = [line[0],line[1],line[2],1]
        origin_cord = numpy.matmul(origin_cord,transforms)
        final_array = numpy.array([[origin_cord[0],origin_cord[1],origin_cord[2],line[3]]])
        temp_array = numpy.concatenate([temp_array,final_array])
    
    temp_array = numpy.delete(temp_array,0,axis=0)
    # remove initial empty
    lines_array = temp_array
    
    # display as int for brevity
    temp_array = temp_array.astype(int)
    temp_array
    text_box.delete('1.0','end')
    text_box.insert(END,temp_array)
    text_box_info.delete('1.0','end')
    text_box_info.insert(END,f'Length:{len(lines_array)}')
    


def compute_eye(vp,D,S):
    # compute commonly used terms
    mag = (vp[0]**2 + vp[1]**2)**.5
    z_mag = (((vp[2]**2) + (vp[0]**2 + vp[1]**2))**.5)
    # t1 * t2 * t3 * t4 * t5
    t1 = numpy.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-vp[0],-vp[1],-vp[2],1]])
    t2 = numpy.array([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
    t3 = numpy.array([[-(vp[1]/(mag)), 0, (vp[0]/(mag)), 0],
          [0, 1, 0, 0],
          [-(vp[0]/(mag)), 0, -(vp[1]/(mag)),0],
          [0, 0, 0, 1]])
    t4 = numpy.array([[1, 0, 0, 0],
          [0, (mag)/z_mag, (vp[2]/z_mag), 0],
          [0, -(vp[2]/z_mag), (mag)/z_mag, 0],
          [0, 0, 0, 1]])
    t5 = numpy.array([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, -1, 0],
          [0, 0, 0, 1]])
    # print(f'{t1}\n{t2}\n{t3}\n{t4}\n{t5}')
    V = numpy.matmul(t1,t2)
    V = numpy.matmul(V,t3)
    V = numpy.matmul(V,t4)
    V = numpy.matmul(V,t5)
    
    change = numpy.array([[D/S, 0, 0, 0],[0, D/S, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    eye_transform = numpy.matmul(V,change)
    # print(eye_transform)

    return eye_transform

# removes data from array with points
def clean_array():
    global lines_array

    temp_array = numpy.empty([1,3])
    pointers = numpy.empty([1,1])
    for row in lines_array:
        temp = numpy.array([[row[0],row[1],row[2]]])
        temp_array = numpy.concatenate([temp_array,temp])
        temp_pointer = numpy.array([[row[3]]])
        pointers = numpy.concatenate([pointers, temp_pointer])

    temp_array = numpy.delete(temp_array,0,axis=0)
    
    # print(temp_array)
    return temp_array, pointers


def perspective_project():
    global lines_array
    global transforms
    # Viewport
    vp = [6,8,7.5]
    # Viewing Axis
    Z = vp[2]
    # screen size
    S = 15
    # screen distance
    D = 60
    
    eye = compute_eye(vp, D, S)
    points, pointer = clean_array()
    temp_array = numpy.empty([1,3])

    # row 
    for row in points:
        temp = [row[0],row[1],row[2],1]
        temp = numpy.matmul(temp,eye)
        final_array = numpy.array([[temp[0],temp[1],temp[2]]])
        temp_array = numpy.concatenate([temp_array,final_array])

    temp_array = numpy.delete(temp_array,0,axis=0)
    print(temp_array)
    return temp_array, pointer

def display_image():
    global lines_array
    vcx = 511.5
    vcy = 511.5
    vsy = 511.5
    vsx = 511.5

    # Image window
    img=Image.new('L',(1800,1000))
    points, direction = perspective_project()
    # print(points)
    # print(direction)
    # create image
    i = 0
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    # print(direction)
    for cord in points:
        # second x and y
        xs = points[int(direction[i])][0]
        ys = points[int(direction[i])][1]
        zs = points[int(direction[i])][2]
        print(cord[0],cord[2],cord[1])
        print(xs,ys,zs)
        if (-cord[2] <= cord[0] <= cord[2]) and (-cord[2] <= cord[1] <= cord[2]):
            x0 = cord[0]/cord[2] * vsx + vcx
            y0 = cord[1]/cord[2] * vsy + vcy
            x0 = int(x0)
            y0 = int(y0)
            # print(x0,y0)
            # draw(x0,y0,x0,y0,img)
            # if it should draw to the next point
            if (-zs <= xs <= zs) and (-zs <= ys <= zs):
                x1 = xs/zs * vsx + vcx
                y1 = ys/zs * vsy + vcy
                
                x1 = int(x0)
                y1 = int(y0)
                # print(x0,y0,x1,y1)
                draw(x0,y0,x1,y1,img)
        # print(x0,y0,x1,y1)
        i = i + 1
            
    # Display image
    img.show()
    
    print('display')

if __name__ == '__main__':
    # App Init
    app = Tk()
    app.title('Transmongus')
    app.geometry('1000x800')
    
    # output file
    output_text = StringVar()
    output_entry = Entry(app, textvariable=output_text)
    output_entry.grid(row=0, column=2)
    
    # Buttons and Boxes
    # translate X and Y
    translate_x = StringVar()
    translate_y = StringVar()
    translate_z = StringVar()
    translate_label = Label(app,text='Translate (X,Y)', font=('bold', 12), pady=20)
    translate_label.grid(row=2,column=0,sticky=W)
    translate_x_entry = Entry(app, textvariable=translate_x)
    translate_x_entry.grid(row=2, column=1)
    translate_y_entry = Entry(app, textvariable=translate_y)
    translate_y_entry.grid(row=2, column=2)
    translate_z_entry = Entry(app, textvariable=translate_z)
    translate_z_entry.grid(row=2, column=3)
    
    #  Basic Scale and Scale
    scale_x = StringVar()
    scale_y = StringVar()
    scale_z = StringVar()
    center_x = StringVar()
    center_y = StringVar()
    center_z = StringVar()
    scale_label = Label(app,text='Scale (X,Y)', font=('bold', 12), pady=20)
    scale_label.grid(row=3,column=0,sticky=W)
    scale_x_entry = Entry(app, textvariable=scale_x)
    scale_x_entry.grid(row=3, column=1)
    scale_y_entry = Entry(app, textvariable=scale_y)
    scale_y_entry.grid(row=3, column=2)
    scale_z_entry = Entry(app, textvariable=scale_z)
    scale_z_entry.grid(row=3, column=3)
    
    scale_label = Label(app,text='Scale (X,Y)', font=('bold', 12), pady=20)
    scale_label.grid(row=3,column=0,sticky=W)
    scale_cx_entry = Entry(app, textvariable=center_x)
    scale_cx_entry.grid(row=4, column=1)
    scale_cy_entry = Entry(app, textvariable=center_y)
    scale_cy_entry.grid(row=4, column=2)
    scale_cz_entry = Entry(app, textvariable=center_z)
    scale_cz_entry.grid(row=4, column=3)

    # Basic Rotate
    rotate = StringVar()
    rotate_center_x = StringVar()
    rotate_center_y = StringVar()
    rotate_center_z = StringVar()
    
    rotate_label = Label(app,text='Rotate', font=('bold', 12), pady=20)
    rotate_label.grid(row=5,column=0,sticky=W)
    
    rotate_entry = Entry(app, textvariable=rotate)
    rotate_entry.grid(row=5, column=1)
    
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
    translate_button.grid(row=2,column=4)

    # scale button
    basic_scale_button = Button(app,text='B.Scale', command=basic_scale_func)
    basic_scale_button.grid(row=3,column=4)

    scale_button = Button(app,text='Scale', command=scale_func)
    scale_button.grid(row=4,column=4)
    
    # rotate button
    rotate_x = Button(app,text='Rotate (X)', command=rotate_x_func)
    rotate_x.grid(row=5,column=4)
    
    rotate_y = Button(app,text='Rotate (Y)', command=rotate_y_func)
    rotate_y.grid(row=5,column=5)
    
    rotate_z = Button(app,text='Rotate (Z)', command=rotate_z_func)
    rotate_z.grid(row=5,column=6)

    # insert 
    insert_button = Button(app,text='Insert Line',command=insert_line)
    insert_button.grid(row=9,column=5)

    # Transform
    transform_button = Button(app,text='Apply Transform',command=apply_transform)
    transform_button.grid(row=9,column=6)
    
    # add data files inputs
    input_x0 = StringVar()
    input_y0 = StringVar()
    input_z0 = StringVar()
    input_index = StringVar()

    input_label = Label(app, text='Lines')
    input_label.grid(row=9,column=0)
    input_x0_box = Entry(app, textvariable=input_x0)
    input_x0_box.grid(row=9,column=1, sticky=W)
    input_y0_box = Entry(app, textvariable=input_y0)
    input_y0_box.grid(row=9,column=2, sticky=W)
    input_z0_box = Entry(app, textvariable=input_z0)
    input_z0_box.grid(row=9,column=3, sticky=W)
    input_index = Entry(app, textvariable=input_index)
    input_index.grid(row=9,column=4,sticky=W)
    
    # Display Image
    display_button = Button(app,text='Display', command=display_image)
    display_button.grid(row=11,column=4)

    # Run App
    app.mainloop()
    

    
