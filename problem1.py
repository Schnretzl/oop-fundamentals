# 1. City Infrastructure Management System

# Task 1: Vehicle Registration System
from vehicle import Vehicle

my_old_car = Vehicle(123456, "Sedan", "Wesley")
my_old_car.update_owner("Alice")
my_new_car = Vehicle(1645287, "SUV", "Bob")
my_new_car.update_owner("Wesley")

print(f"I sold my car to {my_old_car.owner}.")
print(f"I purchased car {my_new_car.registration_number}, so it now belongs to {my_new_car.owner}!")