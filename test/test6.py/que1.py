from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self, persons):
        pass


class TwoWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 20

        if persons > 2:
            toll += (persons - 2) * 10

        return toll


class ThreeWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 30

        if persons > 3:
            toll += (persons - 3) * 20

        return toll


class FourWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 40

        if persons > 4:
            toll += (persons - 4) * 40

        return toll


class HeavyVehicle(Vehicle):

    def calculate_toll(self, persons):
        toll = 60

        if persons > 6:
            toll += (persons - 6) * 100

        return toll


while True:

    print("\n----- TOLL MENU -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice!")
        continue

    persons = int(input("Enter number of persons: "))

    if persons <= 0:
        print("Invalid number of persons!")
        continue

    if choice == 1:
        vehicle = TwoWheeler()

    elif choice == 2:
        vehicle = ThreeWheeler()

    elif choice == 3:
        vehicle = FourWheeler()

    elif choice == 4:
        vehicle = HeavyVehicle()

    total = vehicle.calculate_toll(persons)

    print("Total Toll = Rs.", total)
    