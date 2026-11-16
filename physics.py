
# COS 101 PHYSICS CALCULATOR

# Function to calculate Speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        result = distance / time
        print("Speed =", result, "m/s")


# Function to calculate Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    result = mass * acceleration
    print("Force =", result, "N")


# Function to calculate Density
def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))

    if volume == 0:
        print("Volume cannot be zero.")
    else:
        result = mass / volume
        print("Density =", result, "kg/m^3")


# Function to calculate Work Done
def work_done():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    result = force_value * distance
    print("Work Done =", result, "J")


# Function to calculate Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


# Main program
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Work Done")
    print("5. Kinetic Energy")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        speed()

    elif choice == "2":
        force()

    elif choice == "3":
        density()

    elif choice == "4":
        work_done()

    elif choice == "5":
        kinetic_energy()

    else:
        print("Invalid choice. Select 1-5.")
        continue

    answer = input("Would you like to continue? (yes/no): ")

    if answer.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
