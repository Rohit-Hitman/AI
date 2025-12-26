import csv
import os
from pdf_extraction import fetch_users


def export_users_to_csv(filename="employees.csv"):
    users = fetch_users()

    if not users:
        print("❌ No data found to export")
        return

    data_dir = "data"

    if not os.path.exists(data_dir):
        print(f"🔹 Directory '{data_dir}' does not exist. Creating now...")
        os.makedirs(data_dir)
    else:
        print(f"🔹 Directory '{data_dir}' already exists. Using it.")

    file_path = os.path.join(data_dir, filename)

    headers = [
        "employee_id",
        "name",
        "department",
        "experience_years",
        "skills",
        "salary_inr"
    ]

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(users)

        print(f"✅ Data exported successfully to {file_path}")

    except Exception as error:
        print("❌ Error while writing CSV:", error)


# ✅ Entry point for CSV export
if __name__ == "__main__":
    export_users_to_csv()
