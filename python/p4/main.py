import tkinter
import numpy

# global declares
global lines_array 
global transforms 
lines_array = []
transforms = numpy.array([[1, 0, 0,0],[0, 1, 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]])

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
    transforms = basic_translate(transforms,x_trans,y_trans)
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('translate')


def basic_scale_func():
    # initializing
    global transforms
    x_scl = 1
    y_scl = 1

    # empty checks
    if len(scale_x_entry.get()) != 0:
        x_scl = scale_x_entry.get()
    if len(scale_y_entry.get()) != 0:
        y_scl = scale_y_entry.get()

    # Add transformation back to general and show in table
    transforms = basic_scale(transforms,x_scl,y_scl)
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('basic scale')

def scale_func():
    # initializing
    global transforms
    x_scl = 1
    y_scl = 1
    cx = 0
    cy = 0

    # ensuring no empty entry
    # converted to floats to ensure no undefined behavior
    if len(scale_x_entry.get()) != 0:
        x_scl = float(scale_x_entry.get())
    if len(scale_y_entry.get()) != 0:
        y_scl = float(scale_y_entry.get())
    if len(scale_cx_entry.get()) != 0:
        cx = float(scale_cx_entry.get())
    if len(scale_cy_entry.get()) != 0:
        cy = float(scale_cy_entry.get())


    # translate to center, rotate, the return back to original
    transforms = basic_translate(transforms,-1 * cx,-1 * cy)
    transforms = basic_scale(transforms,x_scl,y_scl)
    transforms = basic_translate(transforms,cx,cy)

    # Add transformation back to table
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)

    print('scale')

def basic_rotate_func():
    # initialization
    global transforms
    theta = 0
    # in case of empty lengths
    if len(rotate_entry.get()) != 0:
        theta = float(rotate_entry.get())
    
    # perform transforms to matrix and display
    transforms = basic_rot(transforms,theta)
    print(transforms)
    transform_text_box.delete('1.0','end')
    transform_text_box.insert(END,transforms)
    print('basic rotate')
    

def rotate_func():
    global transforms
    theta = 0
    cx_rot = 0
    cy_rot = 0
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
                        float(input_x1_box.get()),float(input_y1_box.get())]])
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
        origin_cord = [line[0],line[1],1]
        final_cord = [line[2],line[3],1]

        origin_cord = numpy.matmul(origin_cord,transforms)
        final_cord = numpy.matmul(final_cord,transforms)
        final_array = numpy.array([[origin_cord[0],origin_cord[1],final_cord[0],final_cord[1]]])
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
    
def display_image():
    global lines_array
    # Image window
    img=Image.new('L',(700,700))

    # create image
    for cord in lines_array:
        x0 = int(cord[0])
        y0 = int(cord[1])
        x1 = int(cord[2])
        y1 = int(cord[3])
        draw(x0,y0,x1,y1,img)
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
    translate_label = Label(app,text='Translate (X,Y)', font=('bold', 12), pady=20)
    translate_label.grid(row=2,column=0,sticky=W)
    translate_x_entry = Entry(app, textvariable=translate_x)
    translate_x_entry.grid(row=2, column=1)
    translate_y_entry = Entry(app, textvariable=translate_y)
    translate_y_entry.grid(row=2, column=2)
    
    #  Basic Scale and Scale
    scale_x = StringVar()
    scale_y = StringVar()
    center_x = StringVar()
    center_y = StringVar()
    scale_label = Label(app,text='Scale (X,Y)', font=('bold', 12), pady=20)
    scale_label.grid(row=3,column=0,sticky=W)
    scale_x_entry = Entry(app, textvariable=scale_x)
    scale_x_entry.grid(row=3, column=1)
    scale_y_entry = Entry(app, textvariable=scale_y)
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

    # insert 
    insert_button = Button(app,text='Insert Line',command=insert_line)
    insert_button.grid(row=9,column=5)

    # Transform
    transform_button = Button(app,text='Apply Transform',command=apply_transform)
    transform_button.grid(row=9,column=6)
    
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
    
    # Display Image
    display_button = Button(app,text='Display', command=display_image)
    display_button.grid(row=11,column=4)

    # Run App
    app.mainloop()
    

    
