from neon_connect import conn

cur = conn.cursor()
try:

    cur.execute('''
             CREATE TABLE Client(
             id SERIAL PRIMARY KEY NOT NULL,
             name VARCHAR NOT NULL,
             email VARCHAR NOT NULL,
             password VARCHAR NOT NULL,
             birthdate DATE   
                          
             );
             
             CREATE TABLE Products(
             
             id SERIAL PRIMARY KEY NOT NULL,
             name VARCHAR NOT NULL,
             description VARCHAR NOT NULL,
             codebar BIGINT NOT NULL,
             price DOUBLE PRECISION NOT NULL
             );
             
             CREATE TABLE Kart (
             
             id SERIAL PRIMARY KEY NOT NULL,
             id_client INT NOT NULL,
             id_product INT NOT NULL,
             FOREIGN KEY (id_client) REFERENCES Client(id),
             FOREIGN KEY (id_product) REFERENCES Products(id)
             ); 
             
             CREATE TABLE Employee(
             
             id SERIAL PRIMARY KEY NOT NULL,
             name VARCHAR NOT NULL,
             bage_number INT NOT NULL,
             email VARCHAR NOT NULL,
             birthdate DATE,
             password VARCHAR NOT NULL
             
             );
             
             CREATE TABLE Manager(
             
             id SERIAL PRIMARY KEY NOT NULL,
             name VARCHAR NOT NULL,
             bage_number INT NOT NULL,
             password VARCHAR NOT NULL
             
             );
            ''')

    conn.commit()

except Exception as err:
    print(f'Something went wrong {err}')