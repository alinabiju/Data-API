# API
This is a simple Fast api which retrieves from a local postgres database. The api has two endpoints:
        - GET - retrieves all objects from the database
        * POST - updates the status of an object in the database

# Simulator
The program that randomly selects an object every 60 seconds and updates it's status in the database.

### Environment Setup
To setup the environment:
``` 
     py -m venv .venv
     .venv/Scripts/activate
     pip install -r requirements. txt
```

To start the api:
```
    py api.py
```

To run the Simulator:
```
    py simulator.py
```
