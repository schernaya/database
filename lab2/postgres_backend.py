import psycopg2
from psycopg2.extras import DictCursor

DB_name = 'test'


def connect_to_db():
    connection = psycopg2.connect(user="postgres", password="08042002", host="localhost", database="test")
    connection.autocommit = True
    cursor = connection.cursor(cursor_factory=DictCursor)
    return cursor


from psycopg2 import OperationalError, IntegrityError, ProgrammingError


def connect(func):
    def inner_func(conn, *args, **kwargs):
        try:
            conn.execute(
                'SELECT name FROM sqlite_temp_master WHERE type="table";')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db()
        return func(conn, *args, **kwargs)

    return inner_func


def disconnect_from_db(db=None, conn=None):
    if db is not DB_name:
        print("You are trying to disconnect from a wrong DB")
    if conn is not None:
        conn.close()


# select operations

def select_customer(conn, item_id):
    sql = 'SELECT * FROM customer WHERE id={}'.format(item_id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def select_form(conn, item_id):
    sql = 'SELECT * FROM form WHERE id={}'.format(item_id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def select_phone(conn, item_name):
    sql = 'SELECT * FROM phone WHERE id={}'.format(item_name)
    conn.execute(sql)
    result = conn.fetchone()
    return result


# select all operations

def select_customers(conn):
    sql = 'SELECT * FROM customer'
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def select_forms(conn):
    sql = 'SELECT * FROM form'
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def select_phones(conn):
    sql = 'SELECT * FROM phone'
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def select_forms_phones(conn, id):
    sql = 'SELECT phone.id, phone.model, phone.company, phone.price FROM phone ' \
          'INNER JOIN form_phone ON phone.id = form_phone.phone_id ' \
          'WHERE form_phone.form_id = \'{}\''.format(id)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


# insert operations

def insert_customer(conn, customer):
    sql = "INSERT INTO customer (name, email) VALUES ('{}', '{}')" \
          "RETURNING *" \
        .format(customer.name, customer.email)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def insert_form(conn, form):
    sql = "INSERT INTO form (payment_method, ship_date, customer_id) VALUES ('{}', '{}', '{}')" \
          "RETURNING *" \
        .format(form.payment_method, form.ship_date, form.customer_id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def insert_phone(conn, phone):
    sql = "INSERT INTO phone (model, company, price) VALUES ('{}', '{}', '{}')" \
          "RETURNING *" \
        .format(phone.model, phone.company, phone.price)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def insert_form_phone(conn, form, phone, quantity):
    sql = "INSERT INTO form_phone (form_id, phone_id, quantity) VALUES ('{}', '{}', '{}')" \
          "RETURNING *" \
        .format(form, phone, quantity)
    conn.execute(sql)
    result = conn.fetchone()
    return result


#  update operations

def update_customer(conn, customer):
    sql = "UPDATE customer SET name = '{}', email = '{}' " \
          "WHERE  id = {} " \
          "RETURNING * ".format(customer.name, customer.email, customer.id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def update_form(conn, form):
    sql = "UPDATE form SET payment_method = '{}', ship_date = '{}', customer_id = '{}' " \
          "WHERE  id = '{}' " \
          "RETURNING *".format(form.payment_method, form.ship_date, form.customer_id, form.id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def update_phone(conn, phone):
    sql = "UPDATE phone SET model = '{}', company = '{}', price = '{}' " \
          "WHERE  id = '{}' " \
          "RETURNING *".format(phone.model, phone.company, phone.price, phone.id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


def update_form_phone(conn, form_id, phone_id, quantity):
    sql = "UPDATE form_phone SET quantity = '{}' " \
          "WHERE  form_id = '{}' AND" \
          "phone_id = '{}' " \
          "RETURNING *".format(phone_id, quantity, form_id)
    conn.execute(sql)
    result = conn.fetchone()
    return result


# delete operations

def delete_customer(conn, item_id):
    sql_check = 'SELECT * FROM customer WHERE id={}'.format(item_id)
    conn.execute(sql_check)
    res = conn.fetchone()
    if res is None:
        return None
    else:
        sql = 'DELETE FROM customer WHERE id={} ' \
              'RETURNING *'.format(item_id)
        conn.execute(sql)
        result = conn.fetchone()
        return result


def delete_form(conn, item_id):
    sql_check = 'SELECT * FROM form WHERE id={}'.format(item_id)
    conn.execute(sql_check)
    res = conn.fetchone()
    if res is None:
        return None
    else:
        sql = 'DELETE FROM form WHERE id={} ' \
              'RETURNING *'.format(item_id)
        conn.execute(sql)
        result = conn.fetchone()
        return result


def delete_phone(conn, item_id):
    sql_check = 'SELECT * FROM phone WHERE id={}'.format(item_id)
    conn.execute(sql_check)
    res = conn.fetchone()
    if res is None:
        return None
    else:
        sql = 'DELETE FROM phone WHERE id={} ' \
              'RETURNING *'.format(item_id)
        conn.execute(sql)
        result = conn.fetchone()
        return result


def delete_form_phone(conn, form_id, phone_id):
    sql_check = "SELECT * FROM form_phone WHERE form_id = '{}' AND " \
                "phone_id = '{}'".format(form_id, phone_id)
    conn.execute(sql_check)
    res = conn.fetchone()
    if res is None:
        return None
    else:
        sql = "DELETE FROM form_phone WHERE " \
              "form_id = '{}' AND phone_id = '{}' " \
              "RETURNING *".format(form_id, phone_id)
        conn.execute(sql)
        result = conn.fetchone()
        return result


# random

def random_customers(conn, num):
    sql = "INSERT into customer (name, email) " \
          "SELECT " \
          "(case (random() * 5)::int " \
          "when 0 then 'Viktor Petrovich' " \
          "when 1 then 'Tatiana Nikolaevna' " \
          "when 2 then 'Ruslan Anatolich' " \
          "when 3 then 'Andrii Vasylovych' " \
          "when 4 then 'Nataliya Antonivna' " \
          "when 5 then 'Sophie' " \
          "end) as name, " \
          "'user_' || seq || '@' || " \
          "(case (random() * 3)::int " \
          "when 0 then 'gmail.com' " \
          "when 1 then 'hotmail.com' " \
          "when 2 then 'yahoo.com' " \
          "when 3 then 'ex.ua' " \
          "end) as email " \
          "from GENERATE_SERIES(1, {}) as seq " \
          "RETURNING *".format(num)
    conn.execute(sql)


def random_forms(conn, num):
    sql = "insert into form(payment_method, ship_date, customer_id) " \
          "select " \
          "(case (random() * 7)::int " \
          "when 0 then 'PayPal' " \
          "when 1 then 'Tatiana Nikolaevna' " \
          "when 2 then 'WebMoney' " \
          "when 3 then 'Privat24' " \
          "when 4 then 'Bitcoin Cash' " \
          "when 5 then 'Yandex money' " \
          "when 6 then 'Visa' " \
          "when 7 then 'QIWI' " \
          "end) as payment_method," \
          "((current_date - floor(random()* (365-0+ 1) + 0)*('1 day')::interval)::date) as ship_date," \
          "fk_customer_id() " \
          "from GENERATE_SERIES(1, {}) ".format(num)
    conn.execute(sql)


def random_phones(conn, num):
    sql = "insert into phone(model, company, price) " \
          "select chr(trunc(65+random()*25)::int) || seq.a as company, " \
          "(case (random() * 5)::int " \
          "when 0 then 'Samsung' " \
          "when 1 then 'LG' " \
          "when 2 then 'IPhone' " \
          "when 3 then 'Sony' " \
          "when 4 then 'Xiaomi' " \
          "when 5 then 'Huawei' " \
          "end) as model, " \
          "(random()*(500-100+1)+100)::float8::numeric::money as price " \
          "from GENERATE_SERIES(1, {}) as seq(a)".format(num)
    conn.execute(sql)


def random_form_phone(conn, num):
    sql = "insert into form_phone (form_id, phone_id, quantity) " \
          "select fk_form_id(), fk_phone_id(), " \
          "floor(random() * (20 - 1) + 1) + 1" \
          "FROM generate_series(1, '{}')".format(num)
    conn.execute(sql)

    # search


def search_customers(conn, name, email, date_from, date_to):
    sql = "SELECT DISTINCT customer.id, name, email FROM customer INNER JOIN form ON form.customer_id = customer.id " \
          "WHERE (name LIKE '%{}%') AND (email LIKE '%{}%') " \
          "AND (ship_date >= '{}') AND (ship_date <= '{}')" \
          "ORDER BY customer.id ASC". \
        format(name, email, date_from, date_to)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def search_forms(conn, payment_method, quantity, company):
    sql = "SELECT DISTINCT form.id, form.payment_method, " \
          "form.ship_date, form.customer_id FROM form " \
          "INNER JOIN form_phone ON form.id = form_phone.form_id " \
          "INNER JOIN phone ON phone.id = form_phone.phone_id " \
          "WHERE (payment_method LIKE '%{}%') AND (quantity = '{}') " \
          "AND (company LIKE '%{}%') " \
          "ORDER BY form.id".format(
        payment_method, quantity, company)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def search_phones(conn, price_from, price_to, quantity):
    sql = "SELECT DISTINCT phone.id, phone.model, " \
          "phone.company, phone.price FROM phone " \
          "INNER JOIN form_phone ON phone.id = form_phone.phone_id " \
          "WHERE (price >= '{}') AND (price <= '{}') " \
          "AND (quantity = '{}') " \
          "ORDER BY phone.id".format(
        price_from, price_to, quantity)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results

# def main():
#     conn.close()
