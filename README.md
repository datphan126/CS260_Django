# CS260 - Full-stack Web Development - DJango
This repository contains 10 modules about DJango development for 2019 AWS Apprenticeship Program. The modules were completed by **Dat Phan**.

DJango was the framework used for the development. For database engines, there are four database engines used, including SQLite, Oracle Cloud, Azure SQL, and AWS MySQL.

# How to setup - Django + AWS MySQL database
1) Install **Python3** to your machine
2) Create a file named requirement.txt and add the following contents to the file:
```
Django==2.2.6
django-debug-toolbar==2.0
django-environ==0.4.5
```
3) Run this command to install the dependencies specified in the requirements.txt: `pip install -r requirements.txt`
4) Make a copy of `dotenv_template.txt` and rename the copy to `.env`
5) Update the `.env` to use the MySQL DB
6) Start your server: `python manage.py runserver`
7) Access your server via this link: [http://localhost:8000](http://localhost:8000)

