from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):  # pass in the y that will go in
    def __init__(self):
        self.random_y = 0
        self.cars = []

    def car(self, y):
        super().__init__()
        self.penup()
        # self.setheading(270)
        self.hideturtle()
        self.goto(280, y)
        self.showturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.random_y = random.randint(-250, 250)
        self.cars.append(self)

    def move_cars(self, cars):
        for each_car in cars:
            each_car.setx(each_car.xcor() - MOVE_INCREMENT)

    def update_cars(self):
        car_maker = random.randint(0, 6)
        if car_maker == 3:
            self.car(self.random_y)
        self.move_cars(self.cars)

    def crash(self, player):
        print("entered crash")
        for a_car in self.cars:
            if player.distance(a_car) < 50:
                print("recognized crash")
                return True
            else:
                return False

    def reset(self):
        for each_car in self.cars:
            each_car.hideturtle()
        self.__init__()