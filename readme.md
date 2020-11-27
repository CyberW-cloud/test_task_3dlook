# 3DLOOK Test task 
### Junior Python Developer
by Khmelenko Nikita

Project based on Django Rest Framework. It supplies management of Product objects via API.

Avaliable endpoints documentation in 
#### [Postman collection](https://documenter.getpostman.com/view/13254397/TVmHFg19)

## Installation:
1. Install [Python 3.6+](https://www.python.org/downloads/)
2. Make an empty folder for the project
3. Clone this git repository:
```
git clone https://github.com/CyberW-cloud/test_task_3dlook
```
4. Install the required libraries:
```
pip install -r requirements.txt
```
5. (For production) In ```wsgi.py``` and ```manage.py``` change:
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task_3dlook.settings.development')
```
to
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task_3dlook.settings.production')
```
Then in ```test_task_3dlook/settings/production.py``` change the host domain:
```
ALLOWED_HOSTS = ['%%host_domain%%']
```
6. To run project:
```
python3 manage.py runserver
```
