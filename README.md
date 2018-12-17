**SureEdu Record Service**
=====================================

A Backend RespAPI build with **Django and Django_Rest_Framework.**

**Requirements**
-----------------
1. Python3
2. Django
3. Django_rest_framework library
4. MySql setup in your Server Environment

**How To Setup And Run**
-----------------------
1. Clone this repo to your system
2. Make a virtual environment [it's not a must but wud be great if you do]
3. Open up the project directory in your terminal/Command Prompt and run this command below to install all required packages including django
    
      **For Linux where no virtual environment is setup**

    `sudo python3 -m pip install --user -r requirements.txt`

    **IF You set up a virtual environment just activate it in this folder and run this command** 
 `pip install -r requirements.txt`
 
 4. Rename the .env.sample file to .env and edit the **DATABASE_URL** with your database details
 
 5. Go back to your command prompt and run this command from within the project directory to make migrations to database

    **For Linux where no virtual environment is setup**

    `python3 manage.py migrate`

    **IF You set up a virtual environment just activate it in this folder and run this command** 
 `./manage.py migrate `
 
 6. Finally run the server to test the application ``./manage.py runserver 0.0.0.0:8000``
    Go to your browser and open **127.0.0.1:8000** to access the root page of the api and carry on your test from there.
    