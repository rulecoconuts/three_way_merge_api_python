# three_way_merge_api_python
 An API to automatically merge changes two changed versions of an orignal file usng a three-way merge algorithm

How to use

To use this api, simply setup your virtual environment and install Django:
```shell
python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
```

Run the API

```shell
python manage.py runserver
```

Then send a POST request with file form data with the following names:
original_file, a_file, b_file
