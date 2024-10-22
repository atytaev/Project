from db_backend import DBBackend
import db
# class ServiceManager:
#
#     def _draw_menu(self):
#         print(
#             '0. Add event\n'
#             '1. Delete event\n'
#             '2. Update event\n'
#             '3. Get event by name\n'
#             '4. Get venue by name\n'
#             '5. Find events by venue\n'
#             '6. Find events by partial name\n'
#             '7. Find events by partial name or description\n'
#             '8. Book ticket\n'
#             '9. Cancel booking\n'
#             '10. Check ticket availability\n'
#             '-1. Exit\n'
#         )
#
#     def run_operation(self):
#         while True:
#             self._draw_menu()
#             choice = input('Choose an operation: ')
#
#             match choice:
#                 case '0':
#                     name = input('name')
#                     description = input('description')
#                     venue_id = input(' venue_id')
#                     date = input('date')
#                     time = input('time')
#                     price = input('price')
#                     db.add_event(name, description, venue_id, date, time, price)
#                     print('Event added')
#                 case '1':
#                     event_id = input('event_id:')
#                     db.delete_event(event_id)
#                     print('The event has been deleted')
#                 case '2':
#                     update_event = input('update_event:')
#                     db.update_event(update_event)
#                     print('the event has been updated')
#                 case '3':
#                     name = input('Name:')
#                     print(db.get_event_by_name(name))
#                 case '4':
#                     name = input('Name:')
#                     print(db.get_venue_by_name(name))
#                 case '5':
#                     venue_name = input('venue_name:')
#                     print(db.find_events_by_venue(venue_name))
#                 case '6':
#                     name_part = input('name_part:')
#                     print(db.find_events_by_partial_name(name_part))
#                 case '7':
#                     search_term = input('search_term:')
#                     print(db.find_events_by_partial_name_or_description(search_term))
#                 case '8':
#                     ticket_id = input('ticket_id:')
#                     print(db.book_ticket(ticket_id))
#                 case '9':
#                     ticket_id = input('ticket_id:')
#                     print(db.cancel_booking(ticket_id))
#                 case '10':
#                     event_id = input('event_id:')
#                     print(db.check_ticket_availability(event_id))
#                 case '-1':
#                     return

# def library_controller():
#     ServiceManager().run_operation()

if __name__ == "__main__":
    # library_controller()
    from db import get_event_by_name, get_venue_by_name
    breakpoint()