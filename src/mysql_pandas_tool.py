#!usr/bin/env ipython

"""A script for MySQL-Pandas.DataFrame connection

@author: albert zhang

This is a simple script using *SQLAlchemy* to read and write pd.DataFrame.

"""

import numpy as np
import pandas as pd
From sqlalchemy import create_engine, MetaData, TEXT, Integer, Float, DateTime,
Table, Column


#############################
# The first step is to create an engine
# Use `mysqlconnector` as driver program, others include `mysqldb` etc.
# Here, use `root` user, other users can be used, check mysql users via 
#   `SELECT user FROM mysql` in mysql terminal
# `password` is the password for the user
# `@localhost` represents the server, here we use local server, default port is 
#    3306
# `dbname` is the database name
engine = create_engin("mysql+mysqlconnector://root:"+"password"+"@localhost/dbname")
meta = MetaData(bind=engine) # create metadata for the database


#############################
# Then, we assume data is stored in `df1` (which is a pd.DataFrame), we wan to 
#   store it in the database `example`
# First of all, we drop any existing tables
table_1.drop(engine) # assume `table_1` is the name for table 1

# Second, we create SQLAlchemy.Table to specify format the structure of database
#   tables
table_1 = Table('table1', meta,
                Column('ID', Integer, primary_key = True, autoincrement = False),
                Column('date', DateTime, nullable = False),
                Column('value', Float, nullable = True),
                extend_existing = True
                )

talbe_2 = Table('table2', meta,
                Column('ID', Integer, ForeignKey('table1.ID')),
                Column('date', DateTime, nullable = False),
                Column('value', Float, nullable = True),
                Column('character', TEXT, nullable = True),
                extend_existing = True
                )

meta.create_all(engine) # will create all tables together
meta.create(table_2) # will only create table 2

# Now, we have created some emtpy tables with specified stucture
# The next step is to store DataFrame to database
# pandas comes to default functions to do so
df1.to_sql('table1', engine, if_exists = 'append', index = True)
df2.to_sql('table2', engine, if_exists = 'append', index = True)
# `if_exists='append'` append data to existsing table
# `index=True` write the DataFrame index as a column


#############################
# Now, assume we have database stored in mysql, we want to extract data to DataFrame
# Use the same engine
df1_copy = pd.read_sql_table('table1', engine)
df2_cpy = pd.read_sql_table('table2', engine)

# We can also do query through `pd.read_sql` or `pd.read_sql_query`, which will
#   read queries into pd.DataFrame
        
