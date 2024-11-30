# Role Based Access Control 

## user
- url(local host) : http://127.0.0.1:8000/user/auth/
- code directory  : bugbounty/clients/views

- roles: can view the bug bounty program

## organization
- url(local host) : http://127.0.0.1:8000/organization/auth/
- code directory  : bugbounty/organization/views

- roles: can create new bug bounty program,update and delete bug bounty programs

## admin/company
- url(local host) : http://127.0.0.1:8000/admin/login/ 
- url(local host) : http://127.0.0.1:8000/admin/signup/ (temporary route will be deleted before production)
- code directory  : bugbounty/admin_app/views

- roles: can grant/decline permission for different organization to able to add or delete programs  and has all the control over live bug bounty program(create,update,delete)



# Install in local device

git clone https://github.com/HISHAN03/bugbounty.git

cd bugbounty.git

python -m venv venv

- On Windows: venv\Scripts\activate
- On macOS/Linux: source venv/bin/activate

Install dependencies:pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Access the application

# prerequisites

python3 and django should be installed in the local device
