from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy
from utils import *

# global declares
global lines_array 
global transforms 
lines_array = []
transforms = create_identity_4()

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
    print(transforms)
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


def apply_transform():
    global lines_array
    global transforms
    temp_array = numpy.empty([1,6])
    # apply transform to stored lines
    for line in lines_array:
        origin_cord = [line[0],line[1],line[2],1]
        final_cord = [line[3],line[4],line[5],1]
        origin_cord = numpy.matmul(origin_cord,transforms)
        final_cord = numpy.matmul(final_cord,transforms)
        final_array = numpy.array([[origin_cord[0],origin_cord[1],origin_cord[2],
                                    final_cord[0],final_cord[1],final_cord[2]]])
        temp_array = numpy.concatenate([temp_array,final_array])
    
    temp_array = numpy.delete(temp_array,0,axis=0)
    # remove initial empty
    lines_array = temp_array
    
    # display as int for brevity
    temp_array = temp_array.astype(int)
    # temp_array
    text_box.delete('1.0','end')
    text_box.insert(END,temp_array)
    text_box_info.delete('1.0','end')
    text_box_info.insert(END,f'Length:{len(lines_array)}')

def compute_eye():
    # constants of camera and screen
    x = 6
    y = 8
    z = 7.5
    s = 15
    d = 60

    # calculate magnitude of functions
    mag = (x**2 + y**2) ** .5
    zmag = (z**2 + mag**2) ** .5
    t1 = basic_trans3(create_identity_4(), -x,-y,-z)
    t2 = numpy.array([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
    t3 = numpy.array([[-y/mag, 0, x/mag, 0],[0,1,0,0],[-x/mag,0,-y/mag,0],[0,0,0,1]])
    t4 = numpy.array([[1,0,0,0],[0,mag/zmag, z/zmag, 0],[0,-z/zmag,mag/zmag,0],[0,0,0,1]])
    t5 = numpy.array([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]])
    n = numpy.array([[d/s,0,0,0],[0,d/s,0,0],[0,0,1,0],[0,0,0,1]])

    # creating final transformation matrix
    T = numpy.matmul(t1,t2)
    T = numpy.matmul(T,t3)
    T = numpy.matmul(T,t4)
    T = numpy.matmul(T,t5)
    T = numpy.matmul(T,n)
    print(T)
    return T

def calculate_points():
    global lines_array

    transform = compute_eye()
    temp_array = numpy.empty([1,6])

    # calculate for the clipping coordinate system
    for line in lines_array:
        temps = numpy.array([line[0],line[1],line[2],1])
        tempe = numpy.array([line[3],line[4],line[5],1])
        temps = numpy.matmul(temps,transform)
        tempe = numpy.matmul(tempe,transform)
        combined = numpy.array([[temps[0],temps[1],temps[2],tempe[0],tempe[1],tempe[2]]])
        temp_array = numpy.concatenate([temp_array,combined])

    temp_array = numpy.delete(temp_array,0,axis=0)    
    print(temp_array)
    return temp_array
        

def display_image():
    # Image window
    img=Image.new('L',(1024,1024))
    
    points = calculate_points()

    # Change for Vertex
    vcx = 511.5
    vcy = 511.5
    vsy = 511.5
    vsx = 511.5

    # create image
    for cord in points:
        x0 = cord[0]
        y0 = cord[1]
        z0 = cord[2]
        x1 = cord[3]
        y1 = cord[4]
        z1 = cord[5]

        if (-z0 <= x0 <= z0) and (-z0 <= y0 <= z0):
            xc = round(x0/z0 * vsx + vcx)
            yc = round(y0/z0 * vsy + vcy)

            if (-z1 <= x1 <= z1) and (-z1 <= y1 <= z1):
                xc1 = round(x1/z1 * vsx + vcx)
                yc1 = round(y1/z1 * vsy + vcy)
                draw(xc,yc,xc1,yc1,img) 
            print(xc,yc)
                
    # Display image
    #img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
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

    # Transform
    transform_button = Button(app,text='Apply Transform',command=apply_transform)
    transform_button.grid(row=9,column=6)
    

    # Display Image
    display_button = Button(app,text='Display', command=display_image)
    display_button.grid(row=11,column=4)

    # Run App
    app.mainloop()
    

    
