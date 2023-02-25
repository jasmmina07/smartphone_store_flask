# smartphone_store_flask

## objective

This project is a simple web application that show the list of smartphones and their details. The application is built using Flask framework and tinydb database.

## virtual environment

To create a virtual environment, run the following command:

```bash
python3 -m venv venv
```

To activate the virtual environment, run the following command:

```bash
source venv/bin/activate
```

To deactivate the virtual environment, run the following command:

```bash
deactivate
```

## install dependencies

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## run the application

To run the application, run the following command:

```bash
python app.py
```

## SmartphoneDB

The SmartphoneDB class is a wrapper class for the tinydb database. It provides the following methods:

- get_all_smartphones()
- get_smartphone_by_id(id)

