import psycopg2

connection = psycopg2.connect(
  database="test", 
  host="127.0.0.1", 
  user="n8",
  password="n8", 
  port="5432"
)