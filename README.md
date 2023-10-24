# Test Project

## Introduction

The purpose of this project is to test the functionalities of the API provided by https://reqres.in/api/users. The project includes automated tests that cover various use cases such as retrieving users, creating new users, updating user data, and deleting users.

## Technologies

The project is written in Python and utilizes the following technologies:

- `requests` - a library for making HTTP requests.
- `json` - a library for handling JSON data.
- `logging` - a module for handling application logs.

## Running the Tests
1. Clone the repository to your local machine.
```bash
git clone https://github.com/kbart93/pytest-api
```
2. Navigate to the project directory.
```bash
cd pytest-api
```
3. Run the Python script.
```bash
python test_api_crud.py
```

To run the tests, make sure you have the `requests` library installed. If you haven't installed it yet, you can do so using `pip`:

```bash
pip install requests
```
## Tests
The project includes the following tests:

1. Get Users Test
Checks if the API returns the expected user data.

2. Check Response Status Test
Verifies if the API response status is 200, indicating success.

3. Create Users Test
Tests the ability to add new users to the system.

4. Create User from File Test
Tests the ability to add a user based on data from a JSON file.

5. Update User Data Test
Tests the ability to update existing user data.

6. Delete User Test
Tests the ability to delete a user from the system.