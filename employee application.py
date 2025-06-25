 def dataapplication {
   #creating the variables of each particular employee
 int count=20;
}
def studdentname {
          int 
# employee_management.py

employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists.")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    employees[emp_id] = {"name": name, "age": age, "department": dept}
    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees found.")
    for emp_id, info in employees.items():
        print(f"ID: {emp_id}, Name: {info['name']}, Age: {info['age']}, Department: {info['department']}")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}")
    else:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        name = input("Enter new Name: ")
        age = input("Enter new Age: ")
        dept = input("Enter new Department: ")
        employees[emp_id] = {"name": name, "age": age, "department": dept}
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
add.display(20)
view.display(15)

obj emp=new employee()
{
  name.input type(string);
  search.button on click(nav.to(2)
print("Display tht employee details");
print display();
}
def application:
{
  employee.database("table is created");
}




