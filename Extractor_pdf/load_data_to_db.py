import csv
import os
from db_connection import get_db_connection


CSV_FILE_PATH = os.path.join("data", "employees.csv")
TABLE_NAME = "employees"


def load_csv_to_db():
    if not os.path.exists(CSV_FILE_PATH):
        print("❌ CSV file not found:", CSV_FILE_PATH)
        return

    conn = get_db_connection()
    if not conn:
        print("❌ Cannot load data without DB connection")
        return

    try:
        cursor = conn.cursor()

        with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cursor.execute(
                    f"""
                    INSERT INTO {TABLE_NAME} (
                        employee_id,
                        name,
                        department,
                        experience_years,
                        skills,
                        salary_inr
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (employee_id) DO NOTHING
                    """,
                    (
                        row["employee_id"],
                        row["name"],
                        row["department"],
                        int(row["experience_years"]),
                        row["skills"],
                        int(row["salary_inr"])
                    )
                )

        conn.commit()
        print("✅ CSV data successfully loaded into database")

    except Exception as error:
        conn.rollback()
        print("❌ Error inserting data:", error)

    finally:
        cursor.close()
        conn.close()


# ✅ Entry point
if __name__ == "__main__":
    load_csv_to_db()
