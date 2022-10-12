### FastAPI research

1. Clone this project
2. Enter to project

3. Create Virtualenv

```sh
virtualenv venv
```

4. Install dependencies

```sh
pip install -r requirements.txt
```

5. Initiate migrations

```sh
aerich init -t project.database.TORTOISE_ORM
```

6. Initialize db

```sh
aerich init-db
```

7. Update if any changes in model

```sh
aerich migrate
aerich upgrade
```

8. Runserver

```sh
uvicorn asgi:app --reload
```

9. GraphQL playground [link](http://localhost:8000/graphql)
