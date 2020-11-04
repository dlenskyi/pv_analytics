# PV Analytics
To run this project locally, you will need to perform the following steps.

1. Install virtualenv
```
$> sudo pip install virtualenv
```
2. Copy `.env_example` to `.env`
```
$> cp .env_example .env
```
3. Copy `pv_analytics/settings/local.py_example` to `pv_analytics/settings/local.py`
```
$> cp pv_analytics/settings/local.py_example pv_analytics/settings/local.py
```
4. Either put your PostgreSQL database credentials in `.env` or edit local settings.
5. Initialize the project with the setup script. It will also create a superuser with credentials username `admin` and password `admin` (you can change these credentials in `.env` if you want).
```
$> ./setup.sh
```
6. Open another terminal and build the frontend part of the project in `/<root>/frontend`

   6.1. Go to the `frontend` directory
   ```
   cd frontend
   ```
   6.2. Copy content from `.env_example` to `.env`
   ```
   $> cp .env_example .env
   ```
   6.3. Install npm dependencies
   ```
   $> npm install
   ```
   6.4. Build the frontend and make it watch for your local changes
   ```
   $> npm run watch
   ```
7. Run dev server in project root (e.g. pv_analytics) in another terminal:
```
$> python manage.py runserver
```

This is it. You can now open your browser and visit `localhost:8000`.

## ENV

Server has 3 types:
SERVER TYPES: `DEV`, `STAGING`, `PRODUCTION`
## SECURITY WARNING: don't run with STAGING or DEV, and DEBUG=True on in production!
example:
`SERVER_TYPE=DEV` from development
`DEBUG=True`

Also in STAGING, PRODUCTION servers DEBUG mode must be False
