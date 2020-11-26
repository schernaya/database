import postgres_backend
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func, and_, update, case, select
from sqlalchemy.orm import sessionmaker

from models.models import Customer, Form, Phone, form_phone_links

Base = declarative_base()


class Model(object):

    def __init__(self, url='postgresql+psycopg2://postgres:08042002@localhost/test'):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self._connection = postgres_backend.connect_to_db()

    @property
    def connection(self):
        return self._connection

    #  read operations

    def read_customer(self, id):
        return self.session.query(Customer).get(id)

    def read_form(self, id):
        return self.session.query(Form).get(id)

    def read_phone(self, id):
        return self.session.query(Phone).get(id)

    def read_customers(self):
        return self.session.query(Customer).all()

    def read_forms(self):
        return self.session.query(Form).all()

    def read_phones(self):
        return self.session.query(Phone).all()

    def read_forms_phone(self, form_id):
        form = self.session.query(Form).get(form_id)
        if form is None:
            return []
        return form.phones

    # create operations

    def create_customer(self, item):
        self.session.add(item)
        self.session.commit()
        return item

    def create_form(self, item):
        self.session.add(item)
        self.session.commit()
        return item

    def create_phone(self, item):
        self.session.add(item)
        self.session.commit()
        return item

    def create_form_phone(self, form_id, phone_id, quantity):
        req = form_phone_links.insert() \
            .returning(form_phone_links.c.form_id,
                       form_phone_links.c.phone_id,
                       form_phone_links.c.quantity).values(
            form_id=form_id, phone_id=phone_id, quantity=quantity)
        res = self.session.execute(req)
        self.session.commit()
        return res

    # update operations

    def update_customer(self, item):
        self.session.query(Customer) \
            .filter(Customer.id == item.id) \
            .update({
            Customer.name: item.name,
            Customer.email: item.email
        })
        customer = self.session.query(Customer).get(item.id)
        return customer

    def update_form(self, item):
        self.session.query(Form) \
            .filter(Form.id == item.id) \
            .update({
            Form.payment_method: item.payment_method,
            Form.ship_date: item.ship_date,
            Form.customer_id: item.customer_id
        })
        form = self.session.query(Form).get(item.id)
        return form

    def update_phone(self, item):
        self.session.query(Phone) \
            .filter(Phone.id == item.id) \
            .update({
            Phone.model: item.model,
            Phone.company: item.company,
            Phone.price: item.price
        })
        phone = self.session.query(Phone).get(item.id)
        return phone

    def update_form_phone(self, form_id, phone_id, quantity):
        req = form_phone_links.update() \
            .returning(form_phone_links.c.form_id,
                       form_phone_links.c.phone_id,
                       form_phone_links.c.quantity)\
            .where(and_(form_phone_links.c.form_id == form_id,
                   form_phone_links.c.phone_id == phone_id))\
            .values(quantity=quantity)
        res = self.session.execute(req)
        self.session.commit()
        return res

    # delete operations

    def delete_customer(self, item_id):
        self.session.query(Customer).filter(Customer.id == item_id).delete()
        res = self.session.commit()
        return res

    def delete_form(self, item_id):
        self.session.query(Form).filter(Form.id == item_id).delete()
        res = self.session.commit()
        return res

    def delete_phone(self, item_id):
        self.session.query(Phone).filter(Phone.id == item_id).delete()
        res = self.session.commit()
        return res

    def delete_form_phone(self, form_id, phone_id):
        req = form_phone_links.delete() \
            .returning(form_phone_links.c.form_id,
                       form_phone_links.c.phone_id,
                       form_phone_links.c.quantity) \
            .where(and_(form_phone_links.c.form_id == form_id,
                        form_phone_links.c.phone_id == phone_id))
        res = self.session.execute(req)
        self.session.commit()
        return res

        # random

    def random_customers(self, num):
        res = postgres_backend.random_customers(
            self.connection, num)
        return res

    def random_forms(self, num):
        res = postgres_backend.random_forms(
            self.connection, num)
        return res

    def random_phones(self, num):
        res = postgres_backend.random_phones(
            self.connection, num)
        return res

    def random_form_phone(self, num):
        res = postgres_backend.random_form_phone(
            self.connection, num)
        return res

    # search

    def search_customers(self, name, email, date_from, date_to):
        res = postgres_backend.search_customers(
            self.connection, name, email, date_from, date_to)
        if res is None:
            return None
        return list(map(lambda x: Customer(x['id'], x['name'], x['email']), res))

    def search_forms(self, payment_method, quantity, company):
        res = postgres_backend.search_forms(
            self.connection, payment_method, quantity, company)
        if res is None:
            return None
        return list(map(lambda x: Form(x['id'], x['payment_method'],
                                       x['ship_date'], x['customer_id']), res))

    def search_phones(self, price_from, price_to, quantity):
        res = postgres_backend.search_phones(
            self.connection, price_from, price_to, quantity)
        if res is None:
            return None
        return list(map(lambda x: Phone(x['id'], x['model'], x['company'], x['price']), res))

    def rollback(self):
        postgres_backend.rollback(self.connection)
