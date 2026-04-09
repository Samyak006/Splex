# Readme


# Splex

Splex is a FastAPI-based application designed to manage users, shares, transactions, and user-shared resources. It provides a RESTful API for creating, reading, updating, and deleting data related to users, transactions, and shares.

## Features

- **User Management**: Create, authenticate, and manage users.
- **Transaction Management**: Add, update, and retrieve user transactions.
- **Share Management**: Manage shared resources and their relationships with users.
- **User-Share Management**: Handle user-specific shared resources.

## Project Structure

Splex/ 

├── [main.py](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) # Entry point for the FastAPI application 

├── [config.py](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) # Application configuration settings 

├── database/ # Database connection and session management 

├── model/ # Pydantic and SQLModel models 

├── routing/ # API route definitions 

├── service/ # Business logic and service layer 

├── testing/ # Test utilities and functions 

├── utils/ # Utility functions (e.g., password hashing) 

├── [requirements.txt](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) # Python dependencies 

└── .env # Environment variables


## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Splex
   ```
2. Create and activate a virtual environment:

   ```python
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


3. 

```python-repl
pip install -r requirements.txt
```


3. Set up the [.env](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file with your database connection and other secrets:

   **SQLDB_URL="your-database-url"**

   **PLAID_CLIENT_ID="your-client-id"**

   **PLAID_SECRET="your-secret"**

## Usage

1. Start the FastAPI server:

   fastapi dev
2. Access the API documentation at:

   * Swagger UI: [http://127.0.0.1:8000/docs](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
   * ReDoc: [http://127.0.0.1:8000/redoc](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
3. Test the API using the provided [test.http](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file or any API client like Postman.

## ER-Diagram:


## Endpoints

### Users

* `POST /users/`: Create a new user.
* `POST /users/authenticate`: Authenticate a user.
* `GET /users/`: Retrieve user(s) by email or all users.

### Transactions

* `GET /transactions/`: Retrieve all transactions.
* `POST /transactions/{user_id}/add`: Add a transaction for a user.
* `GET /transactions/{user_id}/history`: Retrieve transaction history for a user.

### Shares

* `GET /shares/`: Retrieve all shares.
* `POST /shares/add`: Add a new share.
* `GET /shares/{share_id}`: Retrieve a specific share by ID.

### User Shares

* `GET /user-shares/`: Retrieve all user shares.
* `POST /user-shares/add`: Add a new user share.

## Testing

Run the test functions in the [testing](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) directory to validate the functionality of the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments

* [FastAPI](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
* [SQLModel](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
* [bcrypt](vscode-file://vscode-app/private/var/folders/nd/mxqd6hjj09x207tsmqznsdnc0000gn/T/AppTranslocation/5EE3C716-5736-49EB-B77D-A005874CDE99/d/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
