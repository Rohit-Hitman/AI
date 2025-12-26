import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    """
    Creates and returns a PostgreSQL database connection
    """
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="employee",      # database name
            user="postgres",
            password="pgadmin",   # your password
            port=5432
        )
        return connection

    except Exception as error:
        print("❌ Database connection failed:", error)
        return None


# 🔽 THIS IS REQUIRED TO SEE OUTPUT
if __name__ == "__main__":
    print("🔹 Testing database connection...")
    conn = get_db_connection()

    if conn:
        print("✅ Database connection successful")
        conn.close()
    else:
        print("❌ Database connection failed")
