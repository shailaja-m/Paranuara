Steps to setup and run the project
1) install pip3 on your machine(compatible with python3 and python3.6 or later is required for this project)
2) install virtualenv using pip on your machine
In command line
3) cd <folder, where you wan to clone project>
4) git clone <git url>   (name it as eg. paranura)
5) virtualenv <use any name>   (eg. pyenv)
6) cd pyenv
7) pip install -r paranura/requirements.txt
8) cd ../paranura
9) source ../pyenv/bin/activate
10) python manage.py runserver
11) Question1-
    open http://127.0.0.1:8000/api/company/ROCKABYE/ in browser and change ROCKABYE to any comapny name you want to see results of

    Question2-
    open http://127.0.0.1:8000/api/friends?guid1=5e71dc5d-61c0-4f3b-8b92-d77310c7fa43&guid2=b057bb65-e335-450e-b6d2-d4cc859ff6cc
    in browser and change guid1 and guid2 values to any guid values in people.json

    Question3-
    open http://127.0.0.1:8000/api/employeeinformation/Conway Charles/ in browser change 'Conway Charles' to any name  
