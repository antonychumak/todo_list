# todo_list

A Django project's to-do list consists of the tasks you plan to do.
So you will always know what you need to do and mark the completed task.

# Installation

Python3 must be already installed

```shell
git clone https://github.com/anton-chumak-main/todo_list.git
cd todo_list
python3 -m venv venv
source venv/bin/activate
export SECRET_KEY=<your DJANGO_SECRET_KEY>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
 - You can use the following superuser (or create another user one yourself):
    - Login: user
    - Password: User12345

## Feature

* Your tasks are always ordered from failed to completed and newest to oldest
* You always see which task is completed and which is not.
* You can easily manage your tasks, update or delete
