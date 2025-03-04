In these python scripts, I had tried to
1. Clean Colorectal Cancer Global Dataset to 3 dfs
2. Using sqlalchemy ORM, create tables in sqlite
3. Retrieve data from db using ORM & SQL statement

In this branch, I changed the way checking on the existing data on db or db itself when I create tables on db using sqlalchemy ORM.
PS : Using to_sql() method cause errors because "if_exists='replace'" method overwrites tables which are created by ORM. I tried "if_exists='append' but it causes error too.
