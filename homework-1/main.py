"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

password_db = os.getenv('PostgresPSW')
# Подключение к БД north
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=password_db
)

def csv_to_list_tuple(file_path):
    """Функция преобразует csv файл в список кортежей"""
    data_list = []
    with open(file_path, encoding='utf-8') as f:
        read_csv = csv.reader(f)
        for row in read_csv:
            row = tuple(row)
            data_list.append(row)
    return data_list


# Создаем список с данными покупателей
customers_list = csv_to_list_tuple('north_data/customers_data.csv')

# Создаем список с данными работников
employee_list = csv_to_list_tuple('north_data/employees_data.csv')

# Создаем список с данными заказов
order_list = csv_to_list_tuple('north_data/orders_data.csv')

# Заполняем таблицы БД north данными, полученными из файлов csv
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_list[1:])

        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employee_list[1:])

        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", order_list[1:])
finally:
    conn.close()
