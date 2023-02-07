# Enterprise Directory - Departement and Employee Class Documentation
## _Departement Class_

This class represents a department in an enterprise. It contains information about the department name and the list of staff members in the department.

## Properties

- _name_ (str): Name of the department
- _staff_ (List): List of staff members in the department
- _DB_ (TinyDB): Database connection instance
- _dir_ (Path): Directory of the database

## Methods

 - _add_staff_member_ (**member: dict**) -> **int**: Adds a new staff member to the department. The information of the staff member is passed as an argument. Returns the number of staff members in the department after the operation.

 - _remove_staff_member_ (**id: str**) -> **bool**: Removes a staff member from the department. The ID of the staff member to remove is passed as an argument. Returns True if the staff member was removed, False otherwise.

 - _exist_in_db_() -> **bool**: Checks if the instance of the Departement class exists in the database. Returns True if it is in the database, False otherwise.

 - _save_() -> **bool**: Saves the instance of the Departement class in the database or updates it if it already exists. Returns True if the instance was saved, False otherwise.

 - _delete_() -> **bool**: Deletes the instance of the Departement class from the database. Returns True if the instance was deleted, False otherwise.

 - _get_all_department_() -> **List**: Returns a list of all departments in the database.

 - _get_department_(name) -> **table.Document**: Returns a specific department based on its name.

 - _count_department_() -> **int**: Returns the number of departments in the database.


## _Employee Class_

This class represents an employee in an enterprise. It contains information about the employee's first name, last name, phone number, and ID.

## Properties
- _id_ (str): ID of the employee
- _first_name_ (str): First name of the employee
- _last_name_ (str): Last name of the employee
- _phone_number_ (str): Phone number of the employee

## Methods
generate_id() -> str: Generates a unique ID for the employee.

check_name(name: str) -> str: Checks if the name passed as an argument is valid. Returns the name if it is valid, raises an error otherwise.

check_phone_number(number: str) -> str: Checks if the phone number passed as an argument is valid. Returns the phone number if it is valid, raises an error otherwise.

__str__(self) -> str: Returns a string representation of the Employee class instance.

save() -> None: Saves the instance of the Employee class in the department staff list.
