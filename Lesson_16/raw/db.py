from constants import DB_CONNECTION
from db_connect import DBConnect

db = DBConnect(**DB_CONNECTION)

def _add_cursor_wrapper(func):
    def wrapper (*args, **kwargs):
        with db.get_connection().cursor() as cur:
            return func(cur, *args, **kwargs)
    return wrapper

@_add_cursor_wrapper
def add_event (cur, name, description, venue_id, date, time, price):
    cur.execute(
        '''
        INSERT INTO Events (name, description, venue_id, date, time, price) 
        VALUES (%s, %s, %s, %s, %s, %s)
        ''',
        (name, description, venue_id, date, time, price)
    )

@_add_cursor_wrapper
def delete_event(cur, event_id):
    cur.execute("DELETE FROM Events WHERE id = %s", (event_id,))


@_add_cursor_wrapper
def update_event(cur, event_id, price):
    cur.execute("UPDATE Events SET price = %s WHERE id = %s", (price, event_id))


@_add_cursor_wrapper
def get_event_by_name(cur, name):
    cur.execute("SELECT * FROM Events WHERE name = %s", (name, ))
    return cur.fetchone()

@_add_cursor_wrapper
def get_venue_by_name(cur, name):
    cur.execute("SELECT * FROM Venues WHERE name = %s", (name,))
    return cur.fetchone()

@_add_cursor_wrapper
def find_events_by_venue(cur, venue_name):
    cur.execute('''
            SELECT e.* 
            FROM Events e
            JOIN Venues v ON e.venue_id = v.id
            WHERE v.name = %s
        ''',
        (venue_name,)
    )
    return cur.fetchall()

@_add_cursor_wrapper
def find_events_by_partial_name(cur, name_part):
    cur.execute("SELECT * FROM Events WHERE name LIKE %s", ('%' + name_part + '%',))
    return cur.fetchall()

@_add_cursor_wrapper
def find_events_by_partial_name_or_description(cur, search_term):
    cur.execute("SELECT * FROM Events WHERE name LIKE %s OR description LIKE %s",
                ('%' + search_term + '%', '%' + search_term + '%',))
    return cur.fetchall()

@_add_cursor_wrapper
def book_ticket(cur, ticket_id):
    cur.execute("UPDATE Tickets SET status = 'booked' WHERE id = %s", (ticket_id,))

@_add_cursor_wrapper
def cancel_booking(cur, ticket_id):
    cur.execute("UPDATE Tickets SET status = 'available' WHERE id = %s", (ticket_id,))

@_add_cursor_wrapper
def check_ticket_availability(cur, event_id):
    cur.execute("SELECT COUNT(*) FROM Tickets WHERE event_id = %s AND status = 'available'", (event_id,))
    return cur.fetchone()[0]



