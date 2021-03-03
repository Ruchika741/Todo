# Todo
Fractal Assignment

Running the backend code-

Open command prompt and give the path till BackendCode Activate the virtual environment- venv\Scripts\activate 
Run the server- python manage.py runserver -> It will run the backend code in the port 8000 
Go to path "localhost:8000/admin" and use the login credential as "Ruchika9/Ruchika9" or else to create new user you can use- python manage.py creatsuperuser 
After successful login, it will display Items model where you can add any todo with the titile and category. 
Also you can give the complete status(True/False). 
You can also view the details in json format in the url- localhost:8000/tasks/task-list/

DDL Queries-

Here I have used Django ORM which uses default Database Sqlite3 and written below queries-

-python manage.py shell ( to enter django interactive console) -from tasks.models import Task

t1= Task(title="Electricity bill", category="Monthly update")
t1.save()
t2= Task(title="Grocery", category="Weekly update")
t2.save()
Task.objects.all()
Task.objects.filter(category__endswith = "ate")
First-entry = Task.objects.get(pk=1)
