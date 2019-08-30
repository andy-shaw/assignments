'''

since classes are complex, this is an example to go over completely

'''


class Car:
    miles = 5000
    engine_cylinders = 4
    model = 'honda'

    def __init__(self, miles, engine_cylinders, model):
        if miles: self.miles = miles
        if engine_cylinders: self.engine_cylinders = engine_cylinders
        if model: self.model = model

    def __str__(self):
        return '<Car> ' + ' miles:' + str(self.miles) + ' engine_cylinders:' + str(self.engine_cylinders) + ' model:' + str(self.model)

    def reset_odometer(self):
        self.miles = 0
        print 'reset_odometer'

    def log_trip(self, miles):
        self.miles += miles
        print 'log trip:', miles

    def new_engine(self, engine_cylinders):
        self.engine_cylinders = engine_cylinders
        self.reset_odometer()







print 'Bought a new car!'
car1 = Car(1200, 3, None)
print car1

car1.log_trip(800)
print car1

car1.log_trip(400)
print car1

car1.log_trip(1200)
print car1

car1.new_engine(4)
print car1