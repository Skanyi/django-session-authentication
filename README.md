### How to set up the project locally

## Open your terminal

# Create a virtual enviroment with
```mkvirtualenv --python=/usr/local/bin/python3 myenv```

## Change to the project directory

## Install the project dependancies
```pip install -r requirement.txt```

## Run the migrations
```python manage.py makemigrations```

then

``` python manage.py migrate ```

## Start the server 

``` python manage.py runserver ```

## Test Register user endpoint - POST METHOD
`http://127.0.0.1:8000/api/v1/auth/register/`

You can use postman for this, 

``{
	"email": "example@gmail.com",
	"username": "example1",
	"firstname": "example",
	"lastname": "exampleone",
	"password": "my_password",
	"confirm_password": "my_password"
}```

## Succesful Response

## Failure Response


## Test login user endpoint - POST METHOD
`http://127.0.0.1:8000/api/v1/auth/login/`

You can use postman for this, 

```{
	"email": "example@gmail.com",
	"password": "example1",
}```

## Succesful Response

## Failure Response