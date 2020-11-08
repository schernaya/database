import os
import datetime
import time

from model import Model
from view import View


class Controller(object):

    def __init__(self):
        self.view = View()
        self.model = Model()

    in_customer_menu = True
    in_form_menu = True
    in_phone_menu = True

    def start(self):
        in_menu = True
        os.system('clear')
        while in_menu:
            option_entity = self.view.display_menu()
            if option_entity.isdigit():

                if option_entity == '1':
                    in_customer_menu = True

                    while in_customer_menu:
                        customer_option = self.view.display_customer_menu()

                        if customer_option == '1':
                            self.show_customers()

                        elif customer_option == '2':
                            self.show_customer_option()

                        elif customer_option == '3':
                            self.update_customer_option()

                        elif customer_option == '4':
                            self.create_customer_option()

                        elif customer_option == '5':
                            self.delete_customer_option()

                        elif customer_option == '6':
                            self.random_customer_option()

                        elif customer_option == '7':
                            self.search_customer_option()

                        elif customer_option == '0':
                            in_customer_menu = False
                        else:
                            self.view.no_such_option()

                elif option_entity == '2':
                    in_form_menu = True

                    while in_form_menu:
                        form_option = self.view.display_form_menu()
                        if form_option == '1':
                            self.show_forms()

                        elif form_option == '2':
                            self.show_form_option()

                        elif form_option == '3':
                            self.update_form_option()

                        elif form_option == '4':
                            self.create_form_option()

                        elif form_option == '5':
                            self.delete_form_option()

                        elif form_option == '6':
                            self.random_form_option()

                        elif form_option == '7':
                            self.search_form_option()

                        elif form_option == '8':
                            self.show_forms_phone_option()

                        elif form_option == '9':
                            self.create_form_phone_option()

                        elif form_option == '10':
                            self.update_form_phone_option()

                        elif form_option == '11':
                            self.delete_form_phone_option()

                        elif form_option == '12':
                            self.random_form_phone_option()

                        elif form_option == '0':
                            in_form_menu = False
                            continue
                        else:
                            self.view.no_such_option()
                            continue

                elif option_entity == '3':
                    in_phone_menu = True

                    while in_phone_menu:
                        phone_option = self.view.display_phone_menu()
                        if phone_option == '1':
                            self.show_phones()

                        elif phone_option == '2':
                            self.show_phone_option()

                        elif phone_option == '3':
                            self.update_phone_option()

                        elif phone_option == '4':
                            self.create_phone_option()

                        elif phone_option == '5':
                            self.delete_phone_option()

                        elif phone_option == '6':
                            self.random_phones_option()

                        elif phone_option == '7':
                            self.search_phones_option()

                        elif phone_option == '0':
                            in_phone_menu = False
                            continue
                        else:
                            self.view.no_such_option()
                            continue

                elif option_entity == '0':
                    break
                else:
                    self.view.no_such_option()
            else:
                self.view.display_menu_error()

    # update operations

    def update_customer(self, customer):
        try:
            result = self.model.update_customer(customer)
            self.view.show_customer(result)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(customer.id, e)

    def update_form(self, form):
        try:
            result = self.model.update_form(form)
            self.view.show_form(result)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(form.id, e)

    def update_phone(self, phone):
        try:
            result = self.model.update_phone(phone)
            self.view.show_phone(result)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(phone.id, e)

    def update_form_phone(self, form_id, phone_id, quantity):
        try:
            result = self.model.update_form_phone(form_id, phone_id, quantity)
            self.view.show_link_form_phone(result)
        except Exception as e:
            self.view.display_exception(e)

    # create operations

    def create_customer(self, row):
        try:
            res = self.model.create_customer(row)
            self.view.show_customer(res)
        except Exception as e:
            self.view.display_exception(e)

    def create_form(self, row):
        try:
            res = self.model.create_form(row)
            self.view.show_form(res)
        except Exception as e:
            self.view.display_fk_customer_exception()

    def create_phone(self, row):
        try:
            res = self.model.create_phone(row)
            self.view.show_phone(res)
        except Exception as e:
            self.view.display_exception(e)

    def create_form_phone(self, form_id, phone_id, quantity):
        try:
            res = self.model.create_form_phone(
                form_id, phone_id, quantity)
            self.view.show_link_form_phone(res)
        except Exception as e:
            self.view.display_incorrect_fk_id(e)

    # delete operations

    def delete_customer(self, item_id):
        try:
            res = self.model.delete_customer(item_id)
            self.view.display_customer_deletion(res)
        except Exception as e:
            self.view.display_exception(e)

    def delete_form(self, item_id):
        try:
            res = self.model.delete_form(item_id)
            self.view.display_form_deletion(res)
        except Exception as e:
            self.view.display_exception(e)

    def delete_phone(self, item_id):
        try:
            res = self.model.delete_phone(item_id)
            self.view.display_phone_deletion(res)
        except Exception as e:
            self.view.display_exception(e)

    def delete_form_phone(self, form_id, phone_id):
        try:
            res = self.model.delete_form_phone(form_id, phone_id)
            self.view.display_form_phone_deletion(res)
        except Exception as e:
            self.view.display_exception(e)

    # select operations

    def show_customers(self):
        items = self.model.read_customers()
        self.view.show_customers(items)

    def show_forms(self):
        items = self.model.read_forms()
        self.view.show_forms(items)

    def show_phones(self):
        items = self.model.read_phones()
        self.view.show_phones(items)

    def show_customer(self, item_name):
        try:
            item = self.model.read_customer(item_name)
            self.view.show_customer(item)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(item_name, e)

    def show_form(self, item_name):
        try:
            item = self.model.read_form(item_name)
            self.view.show_form(item)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(item_name, e)

    def show_phone(self, item_name):
        try:
            item = self.model.read_phone(item_name)
            self.view.show_form(item)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(item_name, e)

    def show_forms_phone(self, item_id):
        try:
            form = self.model.read_form(item_id)
            self.view.show_form(form)
            if form is not None:
                item = self.model.read_forms_phone(item_id)
                self.view.show_phones(item)
        except Exception as e:
            self.view.display_item_not_yet_stored_error(item_id, e)

    def get_date(self):
        while True:
            try:
                year = int(self.view.get_value('year'))
                month = int(self.view.get_value('month'))
                day = int(self.view.get_value('day'))
                ship_date = datetime.date(year, month, day)
                return ship_date
            except ValueError:
                self.view.display_date_error()

    # random

    def random_customers(self, num):
        try:
            start_time = time.time()
            self.model.random_customers(num)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.random_result()
        except Exception as e:
            self.view.display_generate_error(e)

    def random_forms(self, num):
        try:
            start_time = time.time()
            self.model.random_forms(num)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.random_result()
        except Exception as e:
            self.view.display_generate_error(e)

    def random_phones(self, num):
        try:
            start_time = time.time()
            self.model.random_phones(num)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.random_result()
        except Exception as e:
            self.view.display_generate_error(e)

    def random_form_phone(self, num):
        try:
            start_time = time.time()
            self.model.random_form_phone(num)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.random_result()
        except Exception as e:
            self.view.display_generate_error(e)

    # search

    def search_customers(self, name, email, date_from, date_to):
        try:
            start_time = time.time()
            res = self.model.search_customers(name, email, date_from, date_to)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.show_customers(res)
        except Exception as e:
            self.view.display_exception(e)

    def search_forms(self, payment_method, quantity, company):
        try:
            start_time = time.time()
            res = self.model.search_forms(payment_method, quantity, company)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.show_forms(res)
        except Exception as e:
            self.view.display_exception(e)

    def search_phones(self, price_from, price_to, quantity):
        try:
            start_time = time.time()
            res = self.model.search_phones(price_from, price_to, quantity)
            end_time = time.time()
            self.view.display_query_time(end_time - start_time)
            self.view.show_phones(res)
        except Exception as e:
            self.view.display_exception(e)

    # customer menu

    def show_customer_option(self):
        id = self.view.get_item_id()
        while not id.isnumeric():
            id = self.view.get_item_id()
        self.show_customer(id)

    def update_customer_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            item_id = self.view.get_item_id()

        customer = self.model.read_customer(item_id)
        if customer is not None:
            self.view.show_customer(customer)
            option_update = self.view.display_update_customer()
            if option_update == '1':
                value = self.view.get_value('name')
                while len(value) == 0:
                    self.view.display_empty_error()
                    value = self.view.get_value('name')
                customer.name = value

            elif option_update == '2':
                value = self.view.get_value('email')
                while len(value) == 0:
                    self.view.display_empty_error()
                    value = self.view.get_value('email')
                customer.email = value

            self.update_customer(customer)
        else:
            self.view.show_customer(customer)

    def create_customer_option(self):
        name = self.view.get_value('name')
        while len(name) == 0:
            self.view.display_empty_error()
            name = self.view.get_value('name')

        email = self.view.get_value('email')
        while len(email) == 0 or not email.__contains__('@'):
            self.view.display_email_error()
            email = self.view.get_value('email')
        row = ['', name, email]
        self.create_customer(row)

    def delete_customer_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            item_id = self.view.get_item_id()
        self.delete_customer(item_id)

    def random_customer_option(self):
        num = self.view.get_number_of_random()
        while not num.isnumeric:
            num = self.view.get_number_of_random()
        self.random_customers(num)

    def search_customer_option(self):
        name = self.view.get_search('name')
        while len(name) == 0:
            self.view.display_empty_error()
            name = self.view.get_search('name')

        email = self.view.get_search('email')
        while len(email) == 0:
            self.view.display_empty_error()
            email = self.view.get_search('email')

        self.view.get_search_date('to')
        date_from = self.get_date()
        self.view.get_search_date('from')
        date_to = self.get_date()
        self.search_customers(name, email, date_from, date_to)

    # form menu

    def show_form_option(self):
        id = self.view.get_item_id()
        while not id.isnumeric():
            id = self.view.get_item_id()
        self.show_form(id)

    def update_form_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            item_id = self.view.get_item_id()

        form = self.model.read_form(item_id)
        if form is not None:
            self.view.show_form(form)
            option_update = self.view.display_update_form()
            if option_update == '1':
                value = self.view.get_value('payment method')
                while len(value) == 0:
                    self.view.display_empty_error()
                    self.view.get_value('payment method')
                form.payment_method = value

            elif option_update == '2':
                value = self.get_date()
                form.ship_date = value
            elif option_update == '3':
                value = self.view.get_value('customer id')
                while not value.isnumeric():
                    self.view.display_number_error()
                    value = self.view.get_value('customer id')
                form.customer_id = value
            self.update_form(form)
        else:
            self.view.show_form(form)

    def create_form_option(self):
        pay_method = self.view.get_value('payment method')
        while len(pay_method) == 0:
            self.view.display_empty_error()
            pay_method = self.view.get_value('payment method')

        ship_date = self.get_date()
        customer_id = self.view.get_value('customer id')
        while len(customer_id) == 0 or not customer_id.isnumeric():
            self.view.display_empty_error()
            customer_id = self.view.get_value('customer id')
        row = ['', pay_method, ship_date, customer_id]
        self.create_form(row)

    def delete_form_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            item_id = self.view.get_item_id()
        self.delete_form(item_id)

    def random_form_option(self):
        num = self.view.get_number_of_random()
        while not num.isnumeric:
            num = self.view.get_number_of_random()
        self.random_forms(num)

    def search_form_option(self):
        pay_method = self.view.get_value('payment method')
        while len(pay_method) == 0:
            self.view.display_empty_error()
            pay_method = self.view.get_value('payment method')

        quantity = self.view.get_value('quantity')
        while not quantity.isnumeric():
            self.view.display_number_error()
            quantity = self.view.get_value('quantity')

        company = self.view.get_value('company')
        while len(company) == 0:
            self.view.display_empty_error()
            company = self.view.get_value('company')

        self.search_forms(pay_method, quantity, company)

    def show_forms_phone_option(self):
        id = self.view.get_item_id()
        while not id.isnumeric():
            id = self.view.get_item_id()
        self.show_forms_phone(id)

    def create_form_phone_option(self):
        form_id = self.view.get_value('form id')
        while not form_id.isnumeric():
            form_id = self.view.get_value('form id')

        phone_id = self.view.get_value('phone id')
        while not phone_id.isnumeric():
            phone_id = self.view.get_value('phone id')

        quantity = self.view.get_value('quantity')
        while not quantity.isnumeric():
            quantity = self.view.get_value('quantity')

        self.create_form_phone(form_id, phone_id, quantity)

    def update_form_phone_option(self):
        form_id = self.view.get_value('form id')
        while not form_id.isnumeric():
            self.view.display_number_error()
            form_id = self.view.get_value('form id')

        phone_id = self.view.get_value('phone id')
        while not phone_id.isnumeric():
            self.view.display_number_error()
            phone_id = self.view.get_value('phone id')

        quantity = self.view.get_value('quantity')
        while not quantity.isnumeric():
            self.view.display_number_error()
            quantity = self.view.get_value('quantity')

        self.update_form_phone(form_id, phone_id, quantity)

    def delete_form_phone_option(self):
        form_id = self.view.get_value('form id')
        while not form_id.isdigit():
            self.view.display_number_error()
            form_id = self.view.get_value('form id')

        phone_id = self.view.get_value('phone id')
        while not phone_id.isdigit():
            self.view.display_number_error()
            phone_id = self.view.get_value('phone id')

        self.delete_form_phone(form_id, phone_id)

    def random_form_phone_option(self):
        num = self.view.get_number_of_random()
        while not num.isdigit():
            self.view.display_number_error()
            num = self.view.get_number_of_random()

        self.random_form_phone(num)

    # phone menu

    def show_phone_option(self):
        id = self.view.get_item_id()
        while not id.isnumeric():
            self.view.display_number_error()
            id = self.view.get_item_id()
        self.show_phone(id)

    def update_phone_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            self.view.display_number_error()
            item_id = self.view.get_item_id()

        phone = self.model.read_phone(item_id)
        if phone is not None:
            self.view.show_phone(phone)
            option_update = self.view.display_update_phone()
            if option_update == '1':
                value = self.view.get_value('model')
                while len(value) == 0:
                    self.view.display_empty_error()
                    value = self.view.get_value('model')
                phone.model = value

            elif option_update == '2':
                value = self.view.get_value('company')
                while len(value) == 0:
                    self.view.display_empty_error()
                    value = self.view.get_value('company')
                phone.model = value

            elif option_update == '3':
                value = self.view.get_value('price')
                while not value.isnumeric():
                    self.view.display_price_error()
                    value = self.view.get_value('price')
                phone.price = value
            self.update_phone(phone)
        else:
            self.view.show_phone(phone)

    def create_phone_option(self):
        model = self.view.get_value('model')
        while len(model) == 0:
            self.view.display_empty_error()
            model = self.view.get_value('model')

        company = self.view.get_value('company')
        while len(company) == 0:
            self.view.display_empty_error()
            company = self.view.get_value('company')

        price = self.view.get_value('price')
        while len(price) == 0 or not price.isnumeric():
            price = self.view.get_value('price')
        row = ['', model, company, price]
        self.create_phone(row)

    def delete_phone_option(self):
        item_id = self.view.get_item_id()
        while not item_id.isnumeric():
            self.view.display_number_error()
            item_id = self.view.get_item_id()
        self.delete_phone(item_id)

    def random_phones_option(self):
        num = self.view.get_number_of_random()
        while not num.isnumeric:
            self.view.display_number_error()
            num = self.view.get_number_of_random()
        self.random_phones(num)

    def search_phones_option(self):
        price_from = self.view.get_value('price from')
        while not price_from.isnumeric():
            self.view.display_price_error()
            price_from = self.view.get_value('price from')

        price_to = self.view.get_value('price to')
        while not price_to.isnumeric():
            self.view.display_price_error()
            price_to = self.view.get_value('price to')

        quantity = self.view.get_value('quantity')
        while not quantity.isnumeric():
            self.view.display_number_error()
            quantity = self.view.get_value('quantity')

        self.search_phones(price_from, price_to, quantity)
