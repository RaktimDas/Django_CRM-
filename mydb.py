import psycopg2

try:
    # Eastablish the connection
    connection = psycopg2.connect(
        dbname="crm_db", user="postgres", password="9854", host="localhost", port="5432"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Fetch one result
    record = cursor.fetchone()
    print(f"Connected to - {record}")
except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

# finally:
#     # Close the connection
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection closed")
