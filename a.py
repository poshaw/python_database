#! /usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector as sql

mdb = sql.connect(
		host='localhost',
		user='user',
		password='password')

mcur = mdb.cursor(buffered=True)

mcur.execute('CREATE DATABASE IF NOT EXISTS testdb')

mcur.execute('USE testdb')

mcur.execute('''CREATE TABLE IF NOT EXISTS lists(
					id INT AUTO_INCREMENT PRIMARY KEY,
					todo VARCHAR(100) NOT NULL,
					completed BOOL DEFAULT FALSE)''')

mcur.execute('SHOW TABLES')
for x in mcur:
	print(x[0])

mcur.execute('DROP DATABASE testdb')

mcur.execute('SHOW DATABASES')
for x in mcur:
	print(x[0])
