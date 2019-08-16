# insights-host-delete
Kafka listener app for Red Hat Insights.  Listens for delete events in current namespace
and sends delete HTTPS call to classic to limit inconsistencies.

## Getting Started
This application uses pipenv to manage the deployment enviroments.  To set the project up for
development do the following:
```
pipenv install --dev
```
Afterwards you can activate the virtual enviroment by running:
```
pipenv shell
```

## Running the App
This application relies on kafka to be running in order to function.

Running the app itself is quite simple:
```
pipenv run python app.py
```