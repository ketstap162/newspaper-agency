![Logo of the project](https://i.ibb.co/4FxS3nG/github.png)

# 3rAgency
> Newspaper Agency

A site that allows you to manage newspapers and editors, having an appropriate database.

## Check it out!

<a href="https://threeragency.onrender.com" target="_blank">3rAgency project deployed to render.com</a>

Test user (is staff):  
login: `test.redactor`  
password: `redtest123`

## Installing / Getting started

Python3 must be already installed.

Clone the [repository](https://github.com/ketstap162/newspaper-agency) and run the commands:

```shell
cd newspaper-agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

After cloning the repository, you need to go to the root of the project, create and activate the virtual environment, and install the elements necessary for the project. And then start the server.

## Features

What's all the bells and whistles this project can perform?
* Authentication functionality for Redactor/User.
* Managing books, redactors & topics directly from website interface.
* Powerful admin panel for advanced managing.

## Group of users:
* `superuser`: This is the `admin` (Chief Redactor). 
All actions on the site are available to him, and he also 
has access to the `admin page`.
* `staff`: This is an agency employee who has access 
to editing newspapers, topics, as well as user experience.
* `user`: This is a registered user who must receive 
confirmation from the administrator in order to become a `staff`.
* `anon`: This is an unauthorized user 
who has access only to view the site.

## Demo
![image](https://user-images.githubusercontent.com/72568844/204335794-56fe003a-7d42-48de-86f7-bfba940b84ec.png)
