from twisted.enterprise import adbapi

dbpool = adbapi.ConnectionPool("psycopg2", dbname='twisted', host='10.0.2.2', user='sukach', password='204839')