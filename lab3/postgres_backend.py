import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import ProgrammingError

DB_name = 'test'


def connect_to_db():
    connection = psycopg2.connect(user="postgres", password="08042002", host="localhost", database="test")
    connection.autocommit = True
    cursor = connection.cursor(cursor_factory=DictCursor)
    return cursor


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


# random

def random_customers(conn, num):
    sql = "INSERT into customers (name, email) " \
          "SELECT " \
          "(case (random() * 5)::int " \
          "when 0 then 'Viktor Petrovich' " \
          "when 1 then 'Tatiana Nikolaevna' " \
          "when 2 then 'Ruslan Anatolich' " \
          "when 3 then 'Andrii Vasylovych' " \
          "when 4 then 'Nataliya Antonivna' " \
          "when 5 then 'Sophie Chorna' " \
          "when 6 then 'Irina Mikhailovna' " \
          "when 7 then 'Victoria Igorevna' " \
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
    sql = "insert into forms (payment_method, ship_date, customer_id) " \
          "select " \
          "(case (random() * 7)::int " \
          "when 0 then 'PayPal' " \
          "when 1 then 'EasyPay' " \
          "when 2 then 'WebMoney' " \
          "when 3 then 'Privat24' " \
          "when 4 then 'Bitcoin Cash' " \
          "when 5 then 'Yandex money' " \
          "when 6 then 'Visa' " \
          "when 7 then 'QIWI' " \
          "end) as payment_method," \
          "((current_date - floor(random()* (365-0+ 1) + 0)*('1 day')::interval)::date)," \
          "fk_customer_id() " \
          "from GENERATE_SERIES(1, {}) ".format(num)
    conn.execute(sql)


def random_phones(conn, num):
    sql = "insert into phones (model, company, price) " \
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
    sql = "insert into form_phone_links (form_id, phone_id, quantity) " \
          "select fk_form_id(), fk_phone_id(), " \
          "floor(random() * (20 - 1) + 1) + 1" \
          "FROM generate_series(1, '{}')".format(num)
    conn.execute(sql)

    # search


def search_customers(conn, name, email, date_from, date_to):
    sql = "SELECT DISTINCT customers.id, name, email FROM customers " \
          "INNER JOIN forms ON forms.customer_id = customers.id " \
          "WHERE (name LIKE '%{}%') AND (email LIKE '%{}%') " \
          "AND (ship_date >= '{}') AND (ship_date <= '{}')" \
          "ORDER BY customers.id ASC". \
        format(name, email, date_from, date_to)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def search_forms(conn, payment_method, quantity, company):
    sql = "SELECT DISTINCT forms.id, forms.payment_method, " \
          "forms.ship_date, forms.customer_id FROM forms " \
          "INNER JOIN form_phone_links ON forms.id = form_phone_links.form_id " \
          "INNER JOIN phones ON phones.id = form_phone_links.phone_id " \
          "WHERE (payment_method LIKE '%{}%') AND (quantity = '{}') " \
          "AND (company LIKE '%{}%') " \
          "ORDER BY forms.id". \
        format(payment_method, quantity, company)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def search_phones(conn, price_from, price_to, quantity):
    sql = "SELECT DISTINCT phones.id, phones.model, " \
          "phones.company, phones.price FROM phones " \
          "INNER JOIN form_phone_links ON phones.id = form_phone_links.phone_id " \
          "WHERE (price >= '{}') AND (price <= '{}') " \
          "AND (quantity = '{}') " \
          "ORDER BY phones.id". \
        format(price_from, price_to, quantity)
    conn.execute(sql)
    results = conn.fetchall()
    if conn.rowcount == 0:
        return None
    return results


def rollback(conn):
    sql = "ROLLBACK"
    conn.execute(sql)

# def main():
#     conn.close()
