Backend API

Launch the backend app

Steps:  

1.  Install python 3.7
2.  Install pipenv
    > pip install pipenv or pip3 install pipenv in mac
3.  Run the following command in this directory to activate the virtual environtment
    > pipenv shell  
4.  Install the dependencies
    > pipenv install

5.  Run the app
    > pipenv run uvicorn main:app  --port 5000 --reload

    Or run the python file for debugging  
    > pipenv run python main.py
