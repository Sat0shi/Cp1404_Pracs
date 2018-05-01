from Prac_8.taxi import Taxi
from Prac_8.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    user_selection = input("q)uit, c)hoose taxi, d)rive")
    while user_selection != 'q':
        if user_selection == 'q':
            print(trip_cost())
            print('Taxis are now: {}'.format(taxi_list()))




def choose_taxi():
    print('Taxis available: {}'.format(taxi_list()))
    taxi_chosen = input()

def drive():


def trip_cost():


def taxi_list():



main()