from email.errors import NonPrintableDefect
from fastapi import FastAPI
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor, DictCursor

class DBConnection:
	def __init__(self, conn, dispose):
		self.connection = conn
		self._dispose = dispose

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.dispose()

	def dispose(self):
		self._dispose(self.connection)

	def get_connection(self):
		return self.connection

	def execute(self,query,*args, cursor_factory=RealDictCursor):
		try:
			cursor= self.connection.cursor(cursor_factory=cursor_factory)
			cursor.execute(query,args)
			row = cursor.fetchall()
			return row
		except Exception as e :
			print(" db execute ", e) 
		finally:
			cursor.close()
		

	def insertDB(self, table, colum, param, *args, cursor_factory=DictCursor):
		sql = " INSERT INTO {table}({colum}) VALUES ({param}) ;".format(table=table,colum=colum,param=param)
		
		try:
			cursor= self.connection.cursor(cursor_factory=cursor_factory)
			cursor.execute(sql, args)
			self.connection.commit()
			return True
		except Exception as e :
			print(" db execute ", e) 
			return False
		finally:
			cursor.close()

	def selectDB(self, table,colum, query = None, *args, cursor_factory=RealDictCursor):
		query = query or ''
		sql = " SELECT {colum} from {table} {query}".format(colum=colum,table=table, query=query)
		try:
			cursor= self.connection.cursor(cursor_factory=cursor_factory)
			cursor.execute(sql,args)
			row = cursor.fetchall()
			return row
		except Exception as e :
			print(" db execute ", e) 
		finally:
			cursor.close()

class DBPool:
	def __init__(self, app: FastAPI = None, **kwargs):
		self._postgreSQL_pool = None
		if app is not None:
			self.init_app(app=app, **kwargs)


	def init_app(self, app: FastAPI, **kwargs):

		if (self._postgreSQL_pool):
				self._postgreSQL_pool.closeall()

		self._db_user = kwargs.get("DB_USER") or 'postgres'
		self._db_pw = kwargs.get("DB_PW") or '1234'
		self._db_host = kwargs.get("DB_HOST") or '10.99.80.67'
		self._db_port = kwargs.get("DB_PORT") or '5432'
		self._db_name = kwargs.get("DB_NAME") or 'postgres'

		@app.on_event("startup")
		def startup():
			self._postgreSQL_pool = pool.ThreadedConnectionPool(1, 20,user = self._db_user,
										password = self._db_pw,
										host = self._db_host,
										port = self._db_port,
										database = self._db_name)

		@app.on_event("shutdown")
		def shutdown():	
			if (self._postgreSQL_pool):
				self._postgreSQL_pool.closeall()

	def get_connection(self) -> DBConnection:
		if (self._postgreSQL_pool):
			con = self._postgreSQL_pool.getconn()
			return DBConnection(con, self.put_connection)

	def put_connection(self, conn):
		if (self._postgreSQL_pool):
			self._postgreSQL_pool.putconn(conn)


db_pool = None
def get_db_pool():
	global db_pool
	if db_pool is None:
		db_pool = DBPool()

	return db_pool

def get_db_conn() -> DBConnection:
	dbpool = get_db_pool()
	if dbpool is None:
		return None

	return dbpool.get_connection()
