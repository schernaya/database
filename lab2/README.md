Лабораторна робота № 2.
Створення додатку бази даних, орієнтованого на взаємодію з СУБД PostgreSQL
Обрана предметна галузь - онлайн-магазин продажу мобільних телефонів.

customer

|name|data_type|not null|PK|FK|
|--|--|--|--|--|
|id|integer|yes|yes|
|name|text|yes|no|
|email|text|yes|no|

form

|name|data_type|not null|PK|FK|
|--|--|--|--|--|
|id|integer|yes|yes|
|payment_method|text|yes|no|
|ship_date|time without time zone|yes|no|
|customer_id|integer|yes|no|customer.id|

form_phone

|name|data_type|not null|PK|FK|
|--|--|--|--|--|
|form_id|integer|yes|yes|form.id
|phone_id|integer|yes|yes|phone.id
|quantity|integer|yes|no|

phone

|name|data_type|not null|PK|FK|
|--|--|--|--|--|
|id|integer|yes|yes|
|model|text|yes|no|
|company|text|yes|no|
|price|price|yes|no|


