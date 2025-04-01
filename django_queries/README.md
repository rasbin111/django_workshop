# About
This django project demonstrates use of prefetch_related() and select_related() to speed up fetching data 


# To run this code

**Steps:** 
Clone the project locally and follow these steps: 

1. Install Requirements
```bash
pip install -r requirements.txt
```

2. Migrate 
```bash
python manage.py migrate
```

3. Populate dummy data
```bash
python manage.py loaddata data/initial_data_1000.json
```

4. Run the server
```bash
python manage.py runserver
```

# urls

Here are urls you can try and check the Console of `python manage.py runserver` to see time taken by each urls

- http://localhost:8000/creator/slow
- http://localhost:8000/creator/fast
- http://localhost:8000/students/slow
- http://localhost:8000/students/fast
- http://localhost:8000/students/faster