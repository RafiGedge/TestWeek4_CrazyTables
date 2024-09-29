from itertools import count

from db import *


def normalize_db():
    conn = get_db_connection()
    if not conn:
        return

    query1 = """
    create table countries
    (
        country_id   SERIAL primary key,
        country_name varchar(255)
    );
    create table cities
    (
        city_id    SERIAL primary key,
        city_name  varchar(255),
        country_id integer references countries (country_id),
        latitude   NUMERIC(10, 6),
        longitude  NUMERIC(10, 6)
    );
    create table types
    (
        type_id   SERIAL primary key,
        type_name varchar(255)
    );
    create table industries
    (
        industry_id   SERIAL primary key,
        industry_name varchar(255)
    );
    create table targets
    (
        id          serial primary key,
        target_id   integer,
        city_id     integer references cities (city_id),
        type_id     integer references types (type_id),
        industry_id integer references industries (industry_id),
        priority    integer
    );
    """

    cur = conn.cursor()
    cur.execute(query1)
    conn.commit()

    query2 = """
    INSERT INTO countries (country_name)
    SELECT DISTINCT target_country
    FROM mission;
    
    INSERT INTO cities (city_name, country_id, latitude, longitude)
    SELECT DISTINCT target_city, c.country_id, target_latitude, target_longitude
    FROM mission as m JOIN countries as c ON m.target_country = c.country_name;

    INSERT INTO types (type_name)
    SELECT DISTINCT target_type
    FROM mission;
    
    INSERT INTO industries (industry_name)
    SELECT DISTINCT target_industry
    FROM mission;
    
    INSERT INTO targets (target_id, city_id, type_id, industry_id, priority)
    SELECT DISTINCT target_id, c.city_id, t.type_id, i.industry_id, target_priority
    FROM mission as m
         join cities as c on m.target_city = c.city_name
         join types as t on m.target_type = t.type_name
         join industries as i on m.target_industry = i.industry_name;

    """

    cur.execute(query2)
    conn.commit()

    cur.close()
    close_db_connection(conn)

# normalize_db()


# conn = get_db_connection()
# cur = conn.cursor()
# cur.execute("""SELECT target_id, c.city_id, t.type_id, i.industry_id, target_priority
#                 FROM mission as m
#                 join cities as c on m.target_city = c.city_name
#                 join types as t on m.target_type = t.type_name
#                 join industries as i on m.target_industry = i.industry_name;""")
# print(len(cur.fetchall()))
# for row in cur.fetchall():
#     country_name = row[1]
#     cur.execute(f"insert into countries (country_name) values ({row[1]})")
# rows = cur.fetchall()
# countries = [(row[1],) for row in rows]
# cur.executemany("INSERT INTO countries (country_name) VALUES (%s)", countries)
# conn.commit()


# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# for i in cur.fetchall():
#     a = i
#     print(a)
#     print(type(a))
#     break
# print(len(cur.fetchall()))
# a = list(set(cur.fetchall()))
# for i in range(600, 606):
#     print(a[i])
# print(list(map(lambda x: x[1], cur.fetchall())).count(None))
# a = list(filter(lambda x: x[6] is None or x[7] is None, cur.fetchall()))
# print(len(a))
# for i in a:
#     print(i)
# c = 0
# for i in cur.fetchall():
#     if i == (None, None, None, None, None, None, None, None):
#         c += 1
# print(c)
# cur.close()
# close_db_connection(conn)