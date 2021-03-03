# Todo
Fractal Assignment

Running the backend code-

Open command prompt and give the path till BackendCode
Activate the virtual environment- venv\Scripts\activate
Run the server- python manage.py runserver -> It will run the backend code in the port 8000
Go to path "localhost:8000/admin" and use the login credential as "Ruchika9/Ruchika9" or else to create new user you can use- python manage.py creatsuperuser
After successful login, it will display Items model where you can add any todo with the titile and category. Also you can give the complete status(True/False). 
You can also view the details in json format in the url- localhost:8000/tasks/task-list/
