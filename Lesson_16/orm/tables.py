from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Time, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    category = Column(String(255))
    image_url = Column(String(255))
    is_active = Column(Boolean, default=True)

    venues = relationship("Venues", backref="events")
    tickets = relationship("Ticket", backref="event")

class Venues(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    capacity = Column(Integer, nullable=False)
    events = relationship('Events', back_populates='venues')

class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    city = Column(String(255))
    capacity = Column(Integer)
    image_url = Column(String(255))

class Tickets(Base):
    __tablename__ = 'tickets'

    ticket_id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.event_id'), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    type = Column(String(255))
    available_count = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.event_id'), nullable=False)
    ticket_type = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    booking_date = Column(DateTime, default=DateTime.utcnow)
    is_confirmed = Column(Boolean, default=False)

    user = relationship("User", backref="bookings")
    event = relationship("Event", backref="bookings")

