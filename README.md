# The Restaurateur
Restaurant focused CMS built using Wagtail/Django

## Requirements
- Python3

## Development Setup
Within 'restaurant' directory
```
$ pip install -r requirements.txt
$ pip install -r requirements-dep.txt
```

The latest version of pypugjs is required and is not available from pip directly, to install use the following git endpoint
`$ pip install git+https://github.com/matannoam/pypugjs.git`

## Deployment
### Dreamhost shared hosting
- Enable **Passenger** on the sub/domain
- Setup **virtualenv** to use Python3 and install all dependancies via **pip**.
- Run through standard inits, (including but not limited to)
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  $ ./manage.py collectstatic
  ```
- Goto **Panel > Domains > Remap Sub-Dir** then add a subdirectory /media to the sub/domain pointing it at Django's media folder
- Create `passenger_wsgi.py` in domain root (not in /public)

```bash
# Passenger WSGI config
# /env/ is where the virtualenv was setup
import sys, os
INTERP = "/home/giacomos/staging.giacomos.co.uk/env/bin/python3"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/restaurant-cms/restaurant')  # add project here

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "restaurant.settings.production"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
[Original instructions](https://help.dreamhost.com/hc/en-us/articles/215319648-How-to-create-a-Django-project-using-virtualenv)
