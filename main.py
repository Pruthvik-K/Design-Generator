
from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.geometry("1200x1800")
root.title("Designing with Python")


C = Canvas(root, bg="blue", height=100, width=120)
filename = PhotoImage(file ="C:/Users/Hp/Desktop/Mini Project/background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



#OPTION 1

def ColorSpiral():

    def Draw_ColorSpiral():
        if e.get() not in ['2','3','4','5','6']:
            label = Label(root1, text='Enter a valid number of sides !')
            label.grid()
        else:
            import turtle
            t = turtle.Pen()
            turtle.bgcolor("black")
            sides = int(e.get())
            colors = ["red", "yellow", "blue", "orange", "green", "purple"]
            t.speed('fastest')
            for x in range(360):
                t.pencolor(colors[x % sides])
                t.forward(x * 3 / sides + x)
                t.left(360 / sides + 1)
                t.width( int(x * (sides / 200)))
            turtle.done()
    root1 = Tk()
    label = Label(root1, text = 'Enter the number if sides you want in the spiral (2-6)',font=("Arial", 12))
    label.grid(row = 0, column= 0)
    e = Entry(root1, width = 35, borderwidth = 5,font=("Arial", 12))
    e.insert(0, random.choice(['2','3','4','5','6']))
    e.grid( row = 1, column= 0)

    b1 = Button (root1, text = 'Draw', command = Draw_ColorSpiral,font=("Arial", 12))
    b1.grid(row = 2, column= 0)




    root1.mainloop()


#OPTION 2

def Sprialmyname() :
    def Draw_SpiralMyName():
        if e2.get() not in ['3','4','5','6']:
            label = Label(root2, text='Enter a valid number of sides !',font=("Arial", 12))
            label.grid()
        else:
            import turtle
            t = turtle.Pen()
            turtle.bgcolor("black")
            colors = ["red", "yellow", "blue", "green",'violet','magenta']
            t.speed('fastest')

            your_name = str(e.get())

            for x in range(100):
                t.pencolor(colors[x % 4])

                t.penup()

                t.forward(x * 4)

                t.pendown()

                t.write(your_name, font=("Arial", int((x + 4) / 4), "bold"))
                t.left(360/int(e2.get())+2)
            turtle.done()
    root2 = Tk()
    label = Label(root2, text='Enter your name :',font=("Arial", 12))
    label.grid(row=0, column=0)
    e = Entry(root2, width=35, borderwidth=5,font=("Arial", 12))
    e.grid(row=1, column=0)
    label2 = Label(root2, text='Choose number of sides in the spiral (3-6)')
    label2.grid(row=2, column=0)
    e2 = Entry(root2, width=34, borderwidth=5,font=("Arial", 12))
    e2.insert(0, '4')
    e2.grid(row=3, column=0)
    b2 = Button(root2, text='Draw', command=Draw_SpiralMyName,font=("Arial", 12))
    b2.grid(row=5, column=0)

    root2.mainloop()



#OPTION 3

def ViralSpiral():
    def Draw_ViralSpiral():
        if e.get() not in ['2','3','4','5','6','7','8']:
            label = Label(root3, text='Enter a valid number of sides !',font=("Arial", 12))
            label.grid()
        else:
            import turtle  # Set up turtle graphics
            t = turtle.Pen()
            turtle.bgcolor("black")
            colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

            sides =int(e.get())
            t.speed(0)

            for x in range(360):

                t.pencolor(colors[x % sides])

                t.forward(x * 3 / sides + x)

                t.left(360 / sides + 2)  # Turn 360 degrees / number of sides, plus 2

                t.width(int(x * sides / 200))  # Make the pen larger as it goes outward

            turtle.done()
    root3 = Tk()
    # Ask the user for the number of sides, min 2, max 8
    label = Label(root3, text='Enter the number if sides you want in the spiral (2-8)',font=("Arial", 12))
    label.grid(row=0, column=0)
    e = Entry(root3, width=35, borderwidth=5,font=("Arial", 12))
    e.insert(0, random.choice(['2', '3', '4', '5', '6','7','8']))
    e.grid(row=1, column=0)

    b3 = Button(root3,  text='Draw', command= Draw_ViralSpiral,font=("Arial", 12))
    b3.grid(row=2, column=0)

    root3.mainloop()



#OPTION 4

def Kaleidoscope() :
    def Draw_AutoKaleidoscope():
        import random
        import turtle
        t = turtle.Pen()

        t.speed(0)
        turtle.bgcolor("black")
        colors = ["red", "orange", "blue", "green", "yellow", "purple", "white", "gray"]

        def spiral():
            colors = ["red", "orange", "blue", "green"]
            for x in range(size):
                t.pencolor(colors[x % 4])
                t.forward(x)
                t.left(91)

        def circle():
            colors = ["red", "yellow", "blue", "green"]
            for x in range(size):
                t.pencolor(colors[x % 4])
                t.circle(x)
                t.left(91)



        for n in range(50):
            size = random.randint(10, 40)
            des = random.choice([spiral, circle])

            # Generate spirals of random sizes/colors at random locations on the screen
            t.pencolor(random.choice(colors))  # Pick a random color from colors[]
            # Pick a random spiral size from 10 to 40
            # Generate a random (x,y) location on the screen

            x = random.randrange(0, turtle.window_width() // 2)
            y = random.randrange(0, turtle.window_height() // 2)
            # First spiral
            t.penup()
            t.setpos(x, y)
            t.pendown()
            des()
            # Second spiral
            t.penup()

            t.setpos(-x, y)
            t.pendown()
            des()
            # Third spiral
            t.penup()

            t.setpos(-x, -y)
            t.pendown()
            des()
            # Fourth spiral
            t.penup()
            t.setpos(x, -y)
            t.pendown()
            des()

        turtle.done()


    def click_controlled():

        import random
        import turtle
        t = turtle.Pen()
        t.speed(0)
        t.hideturtle()
        turtle.bgcolor("black")
        colors = ["red", "orange", "blue", "green", "yellow", "purple",
                      "white", "gray"]

        def draw_kaleido(x, y):
            t.pencolor(random.choice(colors))
            size = random.randint(10, 40)
            draw_spiral(x, y, size)
            draw_spiral(-x, y, size)
            draw_spiral(-x, -y, size)
            draw_spiral(x, -y, size)

        def draw_spiral(x, y, size):
            t.penup()
            t.setpos(x, y)
            t.pendown()
            for m in range(size):
                t.forward(m * 2)
                t.left(92)

        turtle.onscreenclick(draw_kaleido)
        turtle.done()

    root4= Tk()
    label = Label(root4, text='Choose the type of Kaleidoscope',font=("Arial", 12))
    label.grid(row=0, column=0,columnspan=2)

    b1 = Button(root4, text='Automatic', command= Draw_AutoKaleidoscope,font=("Arial", 12))
    b1.grid(row=1, column=0 )

    b2 = Button(root4, text='Click controlled', command=click_controlled,font=("Arial", 12))
    b2.grid(row=1, column=1)

    root4.mainloop()


#OPTION 5

def Spiral_of_Spiral():
    def Draw_Spiral_of_Spiral():
        if e.get() not in ['2','3','4','5','6']:
            label = Label(root5, text='Enter a valid number of sides !')
            label.grid()
        else:
            import turtle
            t = turtle.Pen()
            t.penup()
            turtle.bgcolor("black")
            t.speed(0)
            # Ask the user for the number of sides
            sides = int(e.get())
            colors = ["red", "yellow", "blue", "green", "purple", "orange"]
            t.width(2)
            #  outer spiral loop
            for m in range(100):
                t.forward(m * 4)
                position = t.position()  # Remember this corner of the spiral
                heading = t.heading()  # Remember the direction we were heading

                for n in range(int(m / 2)):
                    t.pendown()
                    t.pencolor(colors[n % sides])
                    t.forward(2 * n)
                    t.right(360 / sides - 2)
                    t.penup()
                t.setx(position[0])  # Go back to the big spiral's x location
                t.sety(position[1])  # Go back to the big spiral's y location
                t.setheading(heading)  # Point in the big spiral's heading
                t.left(360 / sides + 2)  # Aim at the next point on the big spiral

            turtle.done()
    root5 = Tk()
    label = Label(root5, text='Enter the number if sides you want in the spiral of spirals (2-6)',font=("Arial", 12))
    label.grid(row=0, column=0)
    e = Entry(root5, width=35, borderwidth=5,font=("Arial", 12))
    e.insert(0, random.choice(['2', '3', '4', '5', '6']),)
    e.grid(row=1, column=0)

    b5 = Button(root5, text='Draw', command=Draw_Spiral_of_Spiral,font=("Arial", 12))
    b5.grid(row=2, column=0)

    root5.mainloop()




label1 = Label(root,text = 'Select an option to draw designs ☺' , font=("Arial", 25),fg = 'black',)

label1.place(x = 330, y = 30 + 1*30, width=600 ,height=50)
B1=Button(root ,text='ColorSpiral',padx=100,pady=30, width = 5, command = ColorSpiral ,borderwidth = 5,font=("Arial", 12),)
B1.place(x = 350 ,y = 30 + 230, width=150, height=50)

B2=Button(root,text='SpiralMyName',padx=100,pady=30, width = 5, command = Sprialmyname,borderwidth = 5,font=("Arial", 12),)
B2.place(x = 750, y = 30 + 230, width=150, height=50)


B3=Button(root,text='ViralSpiral',padx=100,pady=30, width = 5 , command = ViralSpiral ,borderwidth = 5,font=("Arial", 12),)
B3.place(x = 350, y = 30 + 380, width=150, height=50)


B4=Button(root,text='Kaleidoscope',padx=100,pady=30, width = 5, command = Kaleidoscope,borderwidth = 5,font=("Arial", 12), )
B4.place(x = 750, y = 30 + 380, width=150, height=50)


B5=Button(root,text='Spiral of Spirals',padx=100,pady=30, width = 5 ,command = Spiral_of_Spiral,borderwidth = 5,font=("Arial", 12))
B5.place(x = 550, y = 550,width=150, height=50)








root.mainloop()
