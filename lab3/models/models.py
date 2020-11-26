from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Table

Base = declarative_base()

form_phone_links = Table('form_phone_links', Base.metadata,
                         Column('form_id', Integer, ForeignKey('forms.id')),
                         Column('phone_id', Integer, ForeignKey('phones.id')),
                         Column('quantity', Integer)
                         )


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    forms = relationship("Form")

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Customer(id={}, name='{}', email='{}')>" \
            .format(self.id, self.name, self.email)


class Form(Base):
    __tablename__ = 'forms'
    id = Column(Integer, primary_key=True)
    payment_method = Column(String)
    ship_date = Column(Date)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    phones = relationship('Phone', secondary=form_phone_links, back_populates='forms')

    def __init__(self, id, payment_method, ship_date, customer_id):
        self.id = id
        self.payment_method = payment_method
        self.ship_date = ship_date
        self.customer_id = customer_id

    def __repr__(self):
        return "<Form(id={}, payment_method='{}', ship_date='{}', customer_id={})>" \
            .format(self.id, self.payment_method, self.ship_date, self.customer_id)


class Phone(Base):

    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    company = Column(String)
    price = Column(Integer)

    forms = relationship("Form", secondary=form_phone_links, back_populates="phones")

    def __init__(self, id, model, company, price):
        self.id = id
        self.model = model
        self.company = company
        self.price = price

    def __repr__(self):
        return "<Phone(id={}, model='{}', company='{}', price={})>" \
                .format(self.id, self.model, self.company, self.price)