# About this project
This project uses [django_tenants](https://django-tenants.readthedocs.io/en/latest/) and uses **shared schema** approach.

## .env file 

Change value of each variable according to your setup

DB_NAME="django_tenants_db"
DB_USER="dev_user"
DB_PASSWORD="adminadminadmin"
DB_HOST="localhost"
DB_PORT="5432"


## Migrate schemas
```bash
python manage.py migrate_schemas
```

## First thing to do after setup: Creating a Tenant

Creating a tenant works just like any other model in django. The first thing we should do is to create the `public` tenant to make our main website available

```bash
# open python shell
python manage.py shell

```

```python
tenant = Client(schema_name="public", name="thepgwolf") # schema_name should be public
tenant.save()

domain = Domain()
domain.domain = "localhost"
domain.tenant = tenant
domain.is_primary = True # it will be true by default
domain.save()

```

## Create tenant using command
```bash
python manage.py create_tenant
```


## To query data in database
Use schema_name and dot followed by table name to look at data
```sql
select * from mclaren.tasks_task;  -- here, schema_name is mclaren
select * from ferrari.tasks_task;  -- here, schema_name is ferrari

-- OR 

set search_path to mclaren; -- change schema to search for
select * from tasks_task;

set search_path to mclaren, public; -- can add many schemas to search

```


## Adding data to each tenants

To add elements to each tenants go to tenant.localhost:8000/admin


## Tutorial source
[YouTube BugBtyes](https://www.youtube.com/watch?v=seTUY18ge38&t=222s)