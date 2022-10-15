# LAB - Class 06

## Project: Seabed | Password Keeper CLI Application

## Author(s): Yazan Alfarra & Razan Alowedat

## Project Description

Seabed is a CLI application, where a user can add his/her social media accounts user names and passwords for instance. It is basically a password keeper, where a user can choose to view all his/her accounts or view a spicific account, add a new one with the option of auto generating password, edit an account info or perhaps deleting an account.

Seabed uses sheety API, where sheety is a google sheet API, where you can request to get, add, edit, or delete data. We decided to go with sheety as a part for practicing dealing with APIs and not to increase the program desk storage by dealing with local storage such as JSON or CSV files.

Downside of using sheety; sheety is a free API, hence, it has a limit of 200 requests per month. In addition that it is not appropriate to be used by multiple users as all the information is stored at the same sheet. To make the program more effecient the use of a local csv file generated for each instance makes the application scalable, however, for the particular reason of practising dealing with APIs, we choose to favor enhancing our capabilities in working with APIs rather than dealing with files at this moment. 

## How to initialize/run the application

**Install the project dependencies:**
```
pip install -r requirements.txt
```

**To run the application:**
```
python oop_project.main.py
```

or

```
python -m oop_project.main
```

**To run the tests:**

```
pytest
```

or

```
pytest -v
```

or

```
pytest -vv
```

Note that some of the tests will work only once as the data will be updated in the google sheet making the overall data different from the original data that the those tests are built upon. 
