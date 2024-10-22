import math
import os

from db_backend import DBBackend
import db

def clear_console():
    os.system('clear')

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

class ServiceManager:

    def _draw_menu(self):
        print(
            '0. Get all events\n'
            '1. Add event\n'
            '2. Get event by name\n'
            '3. Get events by location\n'
            '4. Get events by partial name\n'
            '5. Book ticket\n'
            '6. Cancel a reservation\n'
            '-1. Exit\n'
        )

    def run_operation(self):
        while True:
            self._draw_menu()
            choice = input('Choose an operation: ')

            match choice:
                case '0':
                    all_events = DBBackend.get_all_events()
                    for event in all_events:
                        print(
                            f"ID: {event.event_id}, Название: {event.name}, Дата: {event.date}, Время: {event.time}, Место: {event.location.name}")
                case '1':
                    event_data = {
                        "name": input("name:"),
                        "description": input("description:"),
                        "date": input("date:"),
                        "time": input("time:"),
                        "location_id": int(input("location_id:")),
                        "category": input("category:")
                    }
                    print(DBBackend.add_event(event_data))
                case '2':
                    name = input('Name:')
                    event = DBBackend.get_event_by_name(name)
                    print(event)
                case '3':
                    location = input('location:')
                    events_by_location = DBBackend.get_events_by_location(location)
                    print(events_by_location)
                case '4':
                    partial_name = input('partial_name:')
                    events_by_partial_name = DBBackend.get_events_by_partial_name()
                    print(events_by_partial_name)
                case '5':
                    user_id = int(input('user_id:'))
                    event_id = int(input('event_id:'))
                    ticket_type = input('ticket_type:')
                    quantity =int(input('quantity:'))
                    DBBackend.book_ticket(user_id, event_id, ticket_type, quantity)
                    print('booked')
                case '6':
                    booking_id = input('booking_id:')
                    DBBackend.cancel_booking(booking_id)
                    print('cancelled')
                case '-1':
                    return
def library_controller():
    ServiceManager().run_operation()

if __name__ == "__main__":
    library_controller()