from data.data import get_data, load_data
import json

file_path = "kse_pb\kse_pb\practice_10\data\cinema_halls.json"
def create_hall(file_path):
    halls = get_data(file_path)
    new_name = input("Write the name of the hall: ")
    if new_name in halls:
        print("This hall already exists")
    else:
        rows = int(input("How many rows: "))
        columns = int(input("How many sits:"))
        new_hall_dict = {new_name: []}
        for i in range(1, rows+1):
            for j in range(1, columns+1):
                seat_dict = {f"{i},{j}": False}
                new_hall_dict[new_name].append(seat_dict)
        halls.update(new_hall_dict)
    load_data(halls, file_path)

def show_seats(file_path):
    halls = get_data(file_path)
    hall_name = input("NAme of hall: ")
    if hall_name not in halls:
        print("Hall is not existed")
    else: 
        selected_halls = halls[hall_name]
        empty_seat = []
        for seat in selected_halls:
            for key, value in seat.items():
                if value is False:
                    empty_seat.append(key)
        print(empty_seat)

while True:
    try:
        choice = int(input("0 - exit, 1 - add, 2 - free sits, 3 - book, 4 - canceled booking: "))
    except Exception as e:
        print(e)
        start = None
    if choice == 0:
        break
    elif choice == 1:
        create_hall(file_path)
        print("You created a new hall")
    elif choice == 2:
        show_seats(file_path)
    elif choice == 3:
        pass
    elif choice == 4:
        pass
