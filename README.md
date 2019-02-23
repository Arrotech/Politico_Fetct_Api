[![Build Status](https://travis-ci.org/Arrotech/Politico_Api.svg?branch=develop)](https://travis-ci.org/Arrotech/Politico_Api) [![Coverage Status](https://coveralls.io/repos/github/Arrotech/Politico_Api/badge.svg?branch=develop)](https://coveralls.io/github/Arrotech/Politico_Api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/e4c6a7d21481978d93b4/maintainability)](https://codeclimate.com/github/Arrotech/Politico_Api/maintainability)



# Politico API's

This project i am to create a set of API endpoints defined in the API Endpoints Specification
section and use database to store data.

Below are the Endpoints that have been created.

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v2/auth/signup | Create user| POST |
| api/v2/auth/login | Login to account |GET|
| api/v2/offices | Create Office | POST |
| api/v2/offices | Fetch all office | GET |
| api/v2/offices/<int:office_id> | Fetch one office | GET |
| api/v2/offices/<int:office_id>/edit | Edit an office | PUT |
| api/v2/offices/<int:office_id>/delete | Delete an office | DELETE |
| api/v2/parties | Create Party | POST |
| api/v2/parties | Fetch all parties | GET |
| api/v2/parties/<int:party_id> | Fetch one party | GET |
| api/v2/parties/<int:party_id>/edit | Edit a Party | PUT |
| api/v2/parties/<int:party_id>/delete | Delete a Party | DELETE |
| api/v2/petitions | Create Petition | POST |
| api/v2/voters | Cast vote | POST |



**TOOLS TO BE USED IN THE CHALLENGE**
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)
6. Testing Framework:[Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)


 
**Requirements**

		Install python

		Install pip

		virtualenv

		Postgres


**How to run the application**
 1. Make a new directory on your computer
 2. `git clone` this  <code>[repo](https://github.com/Arrotech/Politico_Api/)</code>
 3. Create virtual environment by typing this in the terminal - virtualenv -p python3 venv
 4. run `pip install -r requirements.txt` on the terminal to install the dependencies
 5. Create a .env file on the root folder of the project. Add the following  environmental variables.


 		
 		source venv/bin/activate

		export FLASK_APP=run.py

		export FLASK_DEBUG=1

		export APP_SETTINGS="testing"

		export FLASK_ENV=development

		export DB_NAME="electoral_system"

		export DB_USER="postgres"

		export DB_HOST="localhost"

		export DB_PASSWORD="postgres"

		export SECRET_KEY="thisisarrotech"

		export DB_TEST_NAME="test_politico"

 6. Then type on the terminal ```source .env``` to activate the environment and also to export all the environment variables.
 7. Then type on the terminal ```flask run``` to start and run the server
 8. Then on [postman](https://www.getpostman.com/), use the above url's



**Heroku link**

This is the heroku link [Heroku](https://politico-api-database.herokuapp.com/)



**Author**

     Harun Gachanja Gitundu



**Contributors to the project**

     Abraham Ogol.

     Brian.

     wilson.

     Mark.