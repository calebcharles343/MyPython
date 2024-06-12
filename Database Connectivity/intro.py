# into to database
'''
Certainly! Let's explore some **database terminology in Python**:

1. **SQLite**:
   - SQLite is a C library that provides a lightweight, disk-based database.
   - It doesn't require a separate server process and allows access using a nonstandard variant of SQL.
   - You can use SQLite for internal data storage or prototype applications before migrating to larger databases like PostgreSQL or Oracle.
   - The `sqlite3` module in Python provides an SQL interface compliant with the DB-API 2.0 specification¹.

2. **Dictionaries**:
   - Python dictionaries are associative arrays consisting of key-value pairs.
   - Define a dictionary using curly braces (`{}`) with comma-separated key-value pairs.
   - Dictionaries allow efficient lookups based on keys and are commonly used for data mapping and caching².

3. **Database Tutorials**:
   - If you're interested in working with databases in Python, check out tutorials covering SQL, NoSQL, and database interaction³⁴.

Feel free to explore these resources for more in-depth information! 🐍📊

Source: Conversation with Copilot, 6/11/2024
(1) sqlite3 — DB-API 2.0 interface for SQLite databases - Python. https://docs.python.org/3/library/sqlite3.html.
(2) Dictionaries in Python – Real Python. https://realpython.com/python-dicts/.
(3) Python Database Tutorials – Real Python. https://realpython.com/tutorials/databases/.
(4) Python Database Tutorials – PYnative. https://pynative.com/python/databases/.
(5) undefined. https://www.sqlite.org.
(6) undefined. https://www.w3schools.com/sql/.

Terminology
1. Relation
2. Record => Rows
3. Field => columns
4. Primary key => Means it's unique and not null
5. relationship
6. foreign key => Foreign key refers to a primary key of another table, and
it can have only those values which are already present in the primary key.

7. constraints => foreign key and primary key together forms a relationship
between tables which are called constraints
'''