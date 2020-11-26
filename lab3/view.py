class View(object):

    # menu

    @staticmethod
    def display_menu():
        return input('\nWhat would you like to work with?\n\n +'
                     '\t(1) Customer\n +'
                     '\t(2) Form\n +'
                     '\t(3) Mobile phone\n +'
                     '\t(0) Exit\n')

    @staticmethod
    def display_customer_menu():
        return input('\nWhat would you like to do:\n\n'
                     '\t(1) Display all customers\n'
                     '\t(2) Display customer by id\n'
                     '\t(3) Update customer\n'
                     '\t(4) Add customer\n'
                     '\t(5) Delete customer\n'
                     '\t(6) Generate random customer\n'
                     '\t(7) Search\n'
                     '\t(0) Go back\n')

    @staticmethod
    def display_phone_menu():
        return input('\nWhat would you like to do:\n\n'
                     '\t(1) Display all phones\n'
                     '\t(2) Display phone by id\n'
                     '\t(3) Update phone\n'
                     '\t(4) Add phone\n'
                     '\t(5) Delete phone\n'
                     '\t(6) Generate random phone\n'
                     '\t(7) Search\n'
                     '\t(0) Go back\n')

    @staticmethod
    def display_form_menu():
        return input('\nWhat would you like to do:\n\n'
                     '\t(1) Display all forms\n'
                     '\t(2) Display form by id\n'
                     '\t(3) Update form\n'
                     '\t(4) Add form\n'
                     '\t(5) Delete form\n'
                     '\t(6) Generate random form\n'
                     '\t(7) Search\n'
                     '\t(8) Get forms phones\n'
                     '\t(9) Add phone to form\n'
                     '\t(10) Update quantity of phones in form\n'
                     '\t(11) Delete forms phone\n'
                     '\t(12) Generate forms phones\n'
                     '\t(0) Go back\n')

    @staticmethod
    def display_update_customer():
        return input('\nChoose option:\n\n'
                     '\t(1) Name\n'
                     '\t(2) Email\n')

    @staticmethod
    def display_update_form():
        return input('\nChoose option:\n\n '
                     '\t(1) Payment method\n'
                     '\t(2) Ship date\n'
                     '\t(3) Customer id\n')

    @staticmethod
    def display_update_phone():
        return input('\nChoose option:\n\n'
                     '\t(1) Model\n'
                     '\t(2) Company\n'
                     '\t(3) Price\n')

    # show

    @staticmethod
    def show_customers(items):
        print('--- CUSTOMERS LIST ---')
        if items is None:
            print('There is no such customers.')
        else:
            for i, item in enumerate(items):
                print('{}. id - '.format(i + 1), item.id, ', name - ', item.name,
                      ', email - ', item.email)

    @staticmethod
    def show_forms(items):
        print('--- FORMS LIST ---')
        if items is None:
            print('There is no such forms.')
        else:
            for i, item in enumerate(items):
                print('{}. id - '.format(i + 1), item.id, ', payment method - ', item.payment_method,
                      ', ship date - ', item.ship_date, ', customer id - ', item.customer_id)

    @staticmethod
    def show_phones(items):
        print('--- PHONES LIST ---')
        if items is None:
            print('There is no such phones.')
        else:
            for i, item in enumerate(items):
                print('{}. id - '.format(i + 1), item.id, ', model - ', item.model,
                      ', company - ', item.company, ', price - ', item.price)

    @staticmethod
    def show_customer(customer):
        if customer is None:
            print('There is no such customer.')
        else:
            print('id - ', customer.id, ', name - ', customer.name,
                  ', email - ', customer.email)

    @staticmethod
    def show_form(form):
        if form is None:
            print('There is no such form.')
        else:
            print('id - ', form.id, ', payment method - ', form.payment_method,
                  ', ship date - ', form.ship_date, ', customer id - ', form.customer_id)

    @staticmethod
    def show_phone(phone):
        if phone is None:
            print('There is no such phone.')
        else:
            print('id - ', phone.id, ', model - ', phone.model,
                  ', company - ', phone.company, ', price - ', phone.price)

    @staticmethod
    def show_link_form_phone(res):
        if res.rowcount == 0:
            print('Error! There is no such ids.')
        else:
            for row in res:
                print('form id - ', row['form_id'],
                      ', phone id - ', row['phone_id'],
                      ', quantity - ', row['quantity'])

    # operations

    @staticmethod
    def get_item_id():
        return input('\nEnter id: ')

    @staticmethod
    def get_value(value):
        return input('Enter a ' + value + ': ')

    @staticmethod
    def get_search_date(value):
        print('Enter a date ' + value + ': ')

    @staticmethod
    def get_number_of_random():
        return input("\nEnter number of random data: ")

    @staticmethod
    def get_search(value):
        return input('Enter a search ' + value + ': ')

    # delete operations

    @staticmethod
    def display_deletion(id):
        if id is None:
            print('Error! There is no data with such id.')
        else:
            print('We have just removed id = \'{}\' from our list: \n'.format(id))

    @staticmethod
    def display_customer_deletion(customer):
        if customer is None:
            print('Error! There is no data with such id.')
        else:
            print('We have just removed it from our list: \n'
                  'id - ', customer.id, ', name - ', customer.name,
                  ', email - ', customer.email)

    @staticmethod
    def display_form_deletion(form):
        if form is None:
            print('Error! There is no data with such id.')
        else:
            print('We have just removed it from our list: \n '
                  'id - ', form.id, ', payment method - ', form.payment_method,
                  ', ship date - ', form.ship_date, ', customer id - ', form.customer_id)

    @staticmethod
    def display_phone_deletion(phone):
        if phone is None:
            print('Error! There is no data with such id.')
        else:
            print('We have just removed it from our list: \n'
                  'id - ', phone.id, ', model - ', phone.model,
                  ', company - ', phone.company, ', price - ', phone.price)

    @staticmethod
    def display_form_phone_deletion(res):
        if res.rowcount == 0:
            print('Error! There is no data with such ids.')
        else:
            for row in res:
                print('We have just removed it from our list: \n'
                      'form id - ', row['form_id'],
                      ', phone id - ', row['phone_id'],
                      ', quantity - ', row['quantity'])

    @staticmethod
    def display_query_time(time):
        print("Query time: ", time)

    @staticmethod
    def customer_form(form):
        if form is None:
            return print('\nThe customer doesn\'nt have orders.')

        print('id - ', form.id, ', payment method - ', form.payment_method, ', ship date - ',
              form.ship_date, ', customer id - ', form.customer_id)

    # random

    @staticmethod
    def random_result():
        print('The data was successfully inserted!')

    # errors

    @staticmethod
    def display_menu_error():
        print('\nNot a number!')

    @staticmethod
    def no_such_option():
        return print('\nNo such an option!')

    @staticmethod
    def display_exception(err):
        print(err)

    @staticmethod
    def display_fk_customer_exception(err):
        print('Error! There is no such customer id!. See error: ', err)

    @staticmethod
    def display_generate_error(err):
        print('Error! The generated data was not inserted!\n {}'.format(err.args[0]))

    @staticmethod
    def display_number_error():
        return print('\nIt is not number.')

    @staticmethod
    def display_empty_error():
        return print('\nNothing was entered. Try again: ')

    @staticmethod
    def display_email_error():
        return print('It is not email. Try again: ')

    @staticmethod
    def display_date_error():
        return print('It is not date. Try again: ')

    @staticmethod
    def display_price_error():
        return print('It is not price.')

    # exceptions

    @staticmethod
    def display_item_already_stored_error(item_type, err):
        print('Hey! We already have this in our {} list!'
              .format(item_type))
        print('{}'.format(err.args[0]))

    @staticmethod
    def display_item_not_yet_stored_error(item, err):
        print('We don\'t have {} in our list. Please insert it first!'
              .format(item.upper()))
        print('{}'.format(err.args[0]))

    @staticmethod
    def display_incorrect_fk_id(err):
        print('Incorrect id! See error: ')
        print('{}'.format(err.args[0]))
