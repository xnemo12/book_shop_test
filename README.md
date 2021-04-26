# INSTALL & SETUP INSTRUCTIONS

to clone project open terminal & write: git clone https://github.com/xnemo12/book_shop_test.git,
then: cd book_shop_test,

#### 1. Create a virtual environment to isolate our package dependencies locally
pip install virtualenv  
python -m venv env 
 
source env/bin/activate for Linux/MacOS  
env\Scripts\activate.bat for Windows
  
#### 2. Install requirements
pip install -r requirements.txt

#### 3. Migrate
python manage.py makemigrations
python manage.py migrate

#### 4. Create superuser
python manage.py createsuperuser  

#### 5. Load fixtures
python manage.py loaddata apps/store/fixtures/\*.yaml 

#### 6. Run server
python manage.py runserver

#### 7. Enjoy
http://localhost:8000/api/v1/  
http://localhost:8000/admin/  