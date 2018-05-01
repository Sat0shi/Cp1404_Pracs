from Prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    limo = SilverServiceTaxi('Stretch Hummer', 200, 5)
    limo.drive(40)
    print(limo)
    print("Cost of trip ${:.2f}".format(limo.get_fare()))
    limo.start_fare()
    limo.drive(60)
    print(limo)
    print("Cost of trip ${:.2f}".format(limo.get_fare()))
    limo.start_fare()
    limo.drive(35)
    print(limo)
    print("Cost of trip ${:.2f}".format(limo.get_fare()))

main()
