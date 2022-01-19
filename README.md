# Salesforce OAuth App
Salesforce integration which includes fetching user token from salesforce using  OAuth2 and then fetch the list of Users, Accounts, and Contacts from salesforce and store it in the database


## Built With

- [Django REST Framework](https://www.django-rest-framework.org)

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)

- [docker-compose](https://docs.docker.com/compose/install/)

## Installation and Usage

1. Clone this repository and change directory.

```bash
git clone https://github.com/Rugz007/Convin-Task.git
cd Convin-Task
```
2. Rename .env.dev to .env and add your client_id and client_secret of salesforce app.
3. Run the following command to **build** all the containers
```bash
docker-compose build
```
4. Run the following command to **run** all the containers 

```bash
docker-compose up
```

 5. Visit `localhost:8000/salesforce/authorize` to fetch authorize
    token and then go to callback URL to fetch access token and
    necessary data.
 6. Visit django-admin at ```localhost:8000/admin/```, login using credentials below.
## Note
Admin user with username as *admin* and password as *admin* is created.
