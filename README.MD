## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
```shell
$ git clone https://github.com/raslon1/backend_test.git
$ cd backend_test/
```

### Develop using virtual environment
```shell
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py createsuperuser
$ ./manage.py runserver
```
Need to add workers and retail outlets


### Develop using Docker

```shell
$ docker-compose up --build
```
