# SuggestionSystem
<p align="center">
  <p align="center">
    </br>
    <a href="https://dialogflow.cloud.google.com/#/" target="_blank">
     <img src="https://upload.wikimedia.org/wikipedia/en/c/c7/Dialogflow_logo.svg"  height="64">
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
      <a href="https://www.python.org/" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"  height="64">
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
      <a href="https://www.djangoproject.com/" target="_blank">
      <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg"  height="64">
    </a>
  </p>
</p>

## About
It's a utility service for suggesting response using DialogFlow for a provided sentence.

## DialogFlow
Dialogflow is a natural language understanding platform used to design and integrate a conversational user interface into mobile apps, web applications, devices, bots, interactive voice response systems and related uses.

## Getting Stared
To get this project up and running you should start by having [Python](https://www.python.org/) installed on your computer. It's advised you create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to store your projects dependencies separately. You can install virtualenv with

```cmd
py -m pip install --user virtualenv
```

Clone or download this repository and open it in your editor of choice. In a windows terminal, run the following command in the base directory of this project

```cmd
py -m venv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on windows:

```cmd
.\env\Scripts\activate
```

Then install the project dependencies with

``` cmd
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
**Note** Project won't start until you provide *SECRET_KEY*, *PROJECT_ID*(Get it from dialog flow project) and *GOOGLE_APPLICATION_CREDENTIALS* (Get it from creating service account in google cloud console).

## Usage
As of now, it has only one end point
- ***{url}/get_suggestions*** : Only [HTTP Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) **GET** is allowed. User should sent text in body with the parameter name as note and it will return a [JSON](https://www.json.org/json-en.html) Object as response. Given below an example for better understading
</br>

![Image](https://github.com/Avish34/Playgroung/blob/master/Screenshot%20(377).png)

</br> In the above image, we have used Postman for testing API.

## Tech Stack
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [DialogFlow](https://dialogflow.cloud.google.com/#)

## Software Used
- [VS Code](https://code.visualstudio.com/)
- [Postman](https://www.postman.com/)

## References
- https://docs.djangoproject.com/en/3.2/
- https://cloud.google.com/dialogflow/es/docs/reference
