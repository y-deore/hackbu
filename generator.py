from faker import Faker
from random import choice, uniform
import csv

# Initialize Faker generator
fake = Faker()

# Define the number of records you want to generate
num_records = 10000

# Define the fields you want to include in your dataset
fields = ['ID', 'Name', 'Major', 'Level', 'Email', 'Phone Number', 'Date of Birth', 'GPA']

# Generate data and write to CSV file
with open('student_info_dataset.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for _ in range(num_records):
        writer.writerow({
            'ID': fake.numerify(text='B0%%%%%%%'),
            'Name': fake.name(),
            'Major': choice(['Computer Science', 'Biology', 'Finance', 'History']),
            'Level': choice(['Under Graduate', 'Graduate', 'Doctrate']),
            'Email': fake.email(),
            'Phone Number': fake.phone_number(),
            'Date of Birth': fake.date_of_birth(minimum_age=18, maximum_age=30).strftime('%Y-%m-%d'),
            'GPA': round(uniform(2.5, 4.0), 2)  # Generating a random GPA between 2.5 and 4.0
        })

print("Dataset generation completed.")
