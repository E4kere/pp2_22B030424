import psycopg2 as pyg

conn = pyg.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = '050208551027',
                  port = '5432' 
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE phone_book (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) 
    phone_number VARCHAR(255) NOT NULL
    
);
""")


    
conn.commit()


cur.close()
conn.close()