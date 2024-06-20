from sqlalchemy import create_engine

# Replace with your actual database credentials
username = 'postgres'
password = 'I536ib9E6HVxgc'
hostname = 'localhost'
port = '5432'  # Default PostgreSQL port
database = 'app'

# Form the database URL
DATABASE_URL = f"postgresql+psycopg://{username}:{password}@{hostname}:{port}/{database}"

try:
    # Create an SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    # Connect to the database
    connection = engine.connect()

    print("Connection successful")

    # Close the connection
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")
