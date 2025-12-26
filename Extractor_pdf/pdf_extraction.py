
import pdfplumber

PDF_PATH = "sample.pdf"


def fetch_users():
    users = []

    with pdfplumber.open(PDF_PATH) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            for line in text.split("\n"):
                if line.startswith("E00"):
                    parts = line.split()

                    employee_id = parts[0]
                    name = parts[1] + " " + parts[2]

                    exp_index = next(i for i, p in enumerate(parts) if p.isdigit())

                    department = " ".join(parts[3:exp_index])
                    experience = int(parts[exp_index])
                    skills = " ".join(parts[exp_index + 1:-1]).replace(",", "")
                    salary = int(parts[-1])

                    users.append(
                        (
                            employee_id,
                            name,
                            department,
                            experience,
                            skills,
                            salary
                        )
                    )

    return users


# ✅ Allows independent testing of this file
if __name__ == "__main__":
    data = fetch_users()
    for row in data:
        print(row)
