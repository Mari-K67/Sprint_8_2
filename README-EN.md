# Sprint_8
Task 2: API
Task: test the API endpoints for [Stellar Burgers](https://qa-stellarburgers.education-services.ru) ([API documentation](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-Stelar_Burger_10.25.pdf?etag=3584917d935c90b69cb3ffaff58d4f34)).

## User creation:
* create a unique user;
* create a user who is already registered;
* create a user and do not fill in one of the required fields.

## User login:
* login as an existing user,
* login with an incorrect login and password.

## User data modification:
* with authorization,
* without authorization,

For both situations, you need to check that any field can be changed. For an unauthorized user — also that the system will return an error.

## Order creation:
* with authorization,
* without authorization,
* with ingredients,
* without ingredients,
* with incorrect ingredient hash.

## Getting orders for a specific user:
* authorized user,
* unauthorized user.

**What you need to do:**
- Create a separate repository for API tests.
- Connect libraries: pytest, requests and allure-pytest.
- Write tests.
- Create a report in Allure.
