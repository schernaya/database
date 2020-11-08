import postgres_backend

from models.customer import Customer
from models.form import Form
from models.phone import Phone


class Model(object):

    def __init__(self):
        self._connection = postgres_backend.connect_to_db()

    @property
    def connection(self):
        return self._connection

    #  read operations

    def read_customer(self, id):
        res = postgres_backend.select_customer(self.connection, id)
        if res is None:
            return None
        return Customer(res['id'], res['name'], res['email'])

    def read_form(self, id):
        res = postgres_backend.select_form(self.connection, id)
        if res is None:
            return None
        return Form(res['id'], res['payment_method'], res['ship_date'], res['customer_id'])

    def read_phone(self, id):
        res = postgres_backend.select_phone(self.connection, id)
        if res is None:
            return None
        return Phone(res['id'], res['model'], res['company'], res['price'])

    def read_customers(self):
        res = postgres_backend.select_customers(
            self.connection)
        if res is None:
            return None
        return list(map(lambda x: Customer(x['id'], x['name'], x['email']), res))

    def read_forms(self):
        res = postgres_backend.select_forms(
            self.connection)
        if res is None:
            return None
        return list(map(lambda x: Form(x['id'], x['payment_method'], x['ship_date'], x['customer_id']), res))

    def read_phones(self):
        res = postgres_backend.select_phones(
            self.connection)
        if res is None:
            return None
        return list(map(lambda x: Phone(x['id'], x['model'], x['company'], x['price']), res))

    def read_forms_phone(self, id):
        res = postgres_backend.select_forms_phones(
            self.connection, id)
        if res is None:
            return None
        return list(map(lambda x: Phone(x['id'], x['model'], x['company'], x['price']), res))

    # create operations

    def create_customer(self, item):
        customer = Customer(item[0], item[1], item[2])
        res = postgres_backend.insert_customer(
            self.connection, customer)
        if res is None:
            return None
        return Customer(res['id'], res['name'], res['email'])

    def create_form(self, item):
        form = Form(item[0], item[1], item[2], item[3])
        res = postgres_backend.insert_form(
            self.connection, form)
        if res is None:
            return None
        return Form(res['id'], res['payment_method'], res['ship_date'], res['customer_id'])

    def create_phone(self, item):
        phone = Phone(item[0], item[1], item[2], item[3])
        res = postgres_backend.insert_phone(
            self.connection, phone)
        if res is None:
            return None
        return Phone(res['id'], res['model'], res['company'], res['price'])

    def create_form_phone(self, form_id, phone_id, quantity):
        res = postgres_backend.insert_form_phone(
            self.connection, form_id, phone_id, quantity)
        if res is None:
            return None
        return res

    # update operations

    def update_customer(self, item):
        res = postgres_backend.update_customer(
            self.connection, item)
        if res is None:
            return None
        return Customer(res['id'], res['name'], res['email'])

    def update_form(self, item):
        res = postgres_backend.update_form(
            self.connection, item)
        if res is None:
            return None
        return Form(res['id'], res['payment_method'], res['ship_date'], res['customer_id'])

    def update_phone(self, item):
        res = postgres_backend.update_phone(
            self.connection, item)
        if res is None:
            return None
        return Phone(res['id'], res['model'], res['company'], res['price'])

    def update_form_phone(self, form_id, phone_id, quantity):
        res = postgres_backend.update_form_phone(
            self.connection, form_id, phone_id, quantity)
        if res is None:
            return None
        return res

    # delete operations

    def delete_customer(self, item_id):
        res = postgres_backend.delete_customer(
            self.connection, item_id)
        if res is None:
            return None
        return Customer(res['id'], res['name'], res['email'])

    def delete_form(self, item_id):
        res = postgres_backend.delete_form(
            self.connection, item_id)
        if res is None:
            return None
        return Form(res['id'], res['payment_method'], res['ship_date'], res['customer_id'])

    def delete_phone(self, item_id):
        res = postgres_backend.delete_phone(
            self.connection, item_id)
        if res is None:
            return None
        return Phone(res['id'], res['model'], res['company'], res['price'])

    def delete_form_phone(self, form_id, phone_id):
        res = postgres_backend.delete_form_phone(
            self.connection, form_id, phone_id)
        if res is None:
            return None
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
