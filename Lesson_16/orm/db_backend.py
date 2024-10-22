from db import get_session

from tables import (
    Event,
    Venues,
    Tickets,
    Booking,
    Location,
)
class DBBackend:
    @staticmethod
    def get_all_events(session):
        events = session.query(Event).all()
        return events

    @staticmethod
    def add_event(session, event_data):
        event = Event(**event_data)
        session.add(event)
        session.commit()

    @staticmethod
    def get_event_by_name(session, name):
        event = session.query(Event).filter_by(name=name).first()
        return event

    @staticmethod
    def get_events_by_location(session, location_name):
        events = session.query(Event).join(Location).filter(Location.name == location_name).all()
        return events

    @staticmethod
    def get_events_by_partial_name(session, partial_name):
        events = session.query(Event).filter(Event.name.like(f"%{partial_name}%")).all()
        return events

    @staticmethod
    def book_ticket(session, user_id, event_id, ticket_type, quantity):
        event = session.query(Event).filter_by(event_id=event_id).first()
        ticket = session.query(Tickets).filter_by(event_id=event_id, type=ticket_type).first()

        if ticket and ticket.available_count >= quantity:
            booking = Booking(
                user_id=user_id,
                event_id=event_id,
                ticket_type=ticket_type,
                quantity=quantity,
                total_price=ticket.price * quantity
            )
            session.add(booking)
            ticket.available_count -= quantity
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def cancel_booking(session, booking_id):
        booking = session.query(Booking).filter_by(booking_id=booking_id).first()
        if booking:
            event_id = booking.event_id
            ticket_type = booking.ticket_type
            quantity = booking.quantity

            ticket = session.query(Tickets).filter_by(event_id=event_id, type=ticket_type).first()
            if ticket:
                ticket.available_count += quantity
                session.delete(booking)
                session.commit()
                return True
        return False