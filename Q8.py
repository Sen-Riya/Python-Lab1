# (8) Given a dictionary containing the following information about 10 different people:
# people = [
#     {"name": "John Doe", "age": 30, "bloodgroup": "A+"},
#     {"name": "Jane Smith", "age": 25, "bloodgroup": "B-"},
#     {"name": "Emily Davis", "age": 40, "bloodgroup": "O+"},
#     {"name": "Michael Brown", "age": 35, "bloodgroup": "AB-"},
#     {"name": "William Johnson", "age": 28, "bloodgroup": "A-"},
#     {"name": "Emma Wilson", "age": 22, "bloodgroup": "B+"},
#     {"name": "Oliver Martinez", "age": 33, "bloodgroup": "O-"},
#     {"name": "Sophia Anderson", "age": 27, "bloodgroup": "AB+"},
#     {"name": "James Thomas", "age": 45, "bloodgroup": "A+"},
#     {"name": "Isabella Lee", "age": 38, "bloodgroup": "B-"}
# ]
# Expected Output :
# Name : John Doe 
# Age : 30 
# Blood Group : A+
# -----------------------------
# Name : Jane Smith
# Age : 25
# Blood Group : B-

people = [
    {"name": "John Doe", "age": 30, "bloodgroup": "A+"},
    {"name": "Jane Smith", "age": 25, "bloodgroup": "B-"},
    {"name": "Emily Davis", "age": 40, "bloodgroup": "O+"},
    {"name": "Michael Brown", "age": 35, "bloodgroup": "AB-"},
    {"name": "William Johnson", "age": 28, "bloodgroup": "A-"},
    {"name": "Emma Wilson", "age": 22, "bloodgroup": "B+"},
    {"name": "Oliver Martinez", "age": 33, "bloodgroup": "O-"},
    {"name": "Sophia Anderson", "age": 27, "bloodgroup": "AB+"},
    {"name": "James Thomas", "age": 45, "bloodgroup": "A+"},
    {"name": "Isabella Lee", "age": 38, "bloodgroup": "B-"}
]

for record in people:
    print(f"Name : {record['name']}")
    print(f"Age : {record['age']}")
    print(f"Blood Group : {record['bloodgroup']}")
    print("-" * 30)  

