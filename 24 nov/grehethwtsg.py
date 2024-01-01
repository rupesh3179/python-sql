class HotelManagement:
    def __init__(self):
        self.rooms = {}
        self.guests = {}

    def display_menu(self):
        print("\n------ Hotel Management System ------")
        print("1. Display All Rooms")
        print("2. Display All Guests")
        print("3. Check-In a Guest")
        print("4. Check-Out a Guest")
        print("5. Quit")

    def display_rooms(self):
        print("\n------ All Rooms ------")
        for room_number, status in self.rooms.items():
            print(f"Room {room_number}: {'Occupied' if status else 'Vacant'}")

    def display_guests(self):
        print("\n------ All Guests ------")
        for room_number, guest_name in self.guests.items():
            print(f"Room {room_number}: {guest_name}")

    def check_in_guest(self):
        room_number = int(input("Enter Room Number: "))
        guest_name = input("Enter Guest Name: ")

        if room_number in self.rooms and not self.rooms[room_number]:
            self.rooms[room_number] = True
            self.guests[room_number] = guest_name
            print(f"{guest_name} checked into Room {room_number}.")
        else:
            print("Invalid room number or room is already occupied.")

    def check_out_guest(self):
        room_number = int(input("Enter Room Number for Check-Out: "))

        if room_number in self.rooms and self.rooms[room_number]:
            guest_name = self.guests.pop(room_number)
            self.rooms[room_number] = False
            print(f"{guest_name} checked out from Room {room_number}.")
        else:
            print("Invalid room number or room is already vacant.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.display_rooms()
            elif choice == "2":
                self.display_guests()
            elif choice == "3":
                self.check_in_guest()
            elif choice == "4":
                self.check_out_guest()
            elif choice == "5":
                print("Exiting Hotel Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    hotel = HotelManagement()
    hotel.run()
