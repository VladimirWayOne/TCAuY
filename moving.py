import turtle
import time

screen = turtle.Screen()

shapes = []
robot = r"pictures\mr_free.gif"
robot_busy = r"pictures\mr_busy.gif"
cut_busy = r"pictures\cut_busy.gif"
cut_free = r"pictures\cut_free.gif"
stat_r_l = r"pictures\stat_rob_l.gif"
stat_r_r = r"pictures\stat_rob_r.gif"
tok_busy = r"pictures\tok_busy.gif"
tok_free = r"pictures\tok_free.gif"
frez_busy = r"pictures\frez_busy.gif"
frez_free = r"pictures\frez_free.gif"


class new_turtle:
    def __init__(self, x, y, image):

        self.turtle = turtle.Turtle()
        try:
            self.turtle.shape(image)
        except:
            screen.addshape(image)
            self.turtle.shape(image)
            print("new shape added: {}".format(image))

        self.turtle.penup()
        self.turtle.setx(x)
        self.turtle.sety(y)

    def change_shape(self, new_shape):
        global shapes
        try:
            self.turtle.shape(new_shape)
        except:
            if new_shape not in shapes:
                shapes.append(new_shape)
                screen.addshape(new_shape)
                self.turtle.shape(new_shape)
                print("new shape added: {}".format(new_shape))


if __name__ == "__main__":
    my_t2 = new_turtle(-20, -20, cut_free)
    time.sleep(1)
    my_t = new_turtle(10, 100, robot)
    my_t.turtle.speed("slowest")
    my_t.change_shape(robot_busy)
    my_t.turtle.forward(0)
    my_t.turtle.goto(my_t2.turtle.xcor(), my_t2.turtle.ycor())
    my_t2.change_shape(cut_busy)
    time.sleep(5)
    my_t2.change_shape(cut_free)
    my_t.turtle.goto(10, 100)
    my_t.change_shape(robot)
    turtle.mainloop()
