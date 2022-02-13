# telegram bot

a telegram bot run on python

# Using VirtualEnv
```
# install virtualenv
pip install virtualenv
pip install virtualenvwrapper-win
cd my_project

# init virtualenv
virtualenv env
\env\Scripts\activate.bat

# backup all requirement
pip freeze > requirements.txt

# install in requirement
pip install -r requirements.txt

# uninstall all
pip freeze | xargs pip uninstall -y
```