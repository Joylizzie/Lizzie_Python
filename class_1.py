class Car():
    def __init__(self,make,model,year):
        """Initialize car attibutes."""
        self.make = make
        self.model = model
        self.year = year

        # fuel capacity and level in gallons.
        self .fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        '''Fill gas tank to capacity.'''
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

        def drive(self):
            """Simulate driving."""
            print("The car is moving.")

            my_car = Car('audi','a4','2016')
            print(my_car.make)
            print(my_car.model)
            print(my_car.year)

            my_car.fill_tank()
            my_car.drive()
