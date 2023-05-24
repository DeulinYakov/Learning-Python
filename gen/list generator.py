class Cars:
    def __int__(self, id):
        self.id = id

    def move(self):
        print('car move')

    def stop(self):
        print('stop car')


my_car = Cars()

my_car.move()
my_car.stop()

print(isinstance(my_car, Cars))