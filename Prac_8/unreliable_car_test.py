from Prac_8.unreliable_car import UnreliableCar

def main():
    new_car = UnreliableCar('Jeep', 200, 30)
    print(new_car.drive(40))
    print("fuel =", new_car.fuel)
    print("odo =", new_car.odometer)
    print(new_car.drive(40))
    print("fuel =", new_car.fuel)
    print("odo =", new_car.odometer)
    print(new_car.drive(40))
    print("fuel =", new_car.fuel)
    print("odo =", new_car.odometer)

main()
