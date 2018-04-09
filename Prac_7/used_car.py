"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_7.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, 'Leroy')
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    my_limo = Car(100, 'Jenkins')
    my_limo.add_fuel(20)
    print('Limo has {} fuel remaining'.format(my_limo.fuel))
    my_limo.drive(115)
    print('odo = {}'.format(my_limo.odometer))
    print(my_limo)

main()