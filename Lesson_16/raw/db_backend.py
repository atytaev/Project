from db import (
    add_event,
    delete_event,
    update_event,
    get_event_by_name,
    get_venue_by_name,
    find_events_by_venue,
    find_events_by_partial_name,
    find_events_by_partial_name_or_description,
    book_ticket,
    cancel_booking,
    check_ticket_availability,
)

class DBBackend:
    @staticmethod
    def get_event_by_name(name):
        return get_event_by_name(name)

    @staticmethod
    def get_venue_by_name(name):
        return get_venue_by_name(name)

    @staticmethod
    def find_events_by_venue(venue_name):
        return find_events_by_venue(venue_name)

    @staticmethod
    def find_events_by_partial_name(name_part):
        return find_events_by_partial_name(name_part)

    @staticmethod
    def find_events_by_partial_name_or_description(search_term):
        return find_events_by_partial_name_or_description(search_term)