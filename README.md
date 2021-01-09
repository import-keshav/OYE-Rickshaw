# OYE-Rickshaw
Backend Assignment (Intern)

<h4> TechStack Used</h4>
1. Python (Programming Language)<br>
2. Django (Web Framework)<br>
3. Postgresql (Database)<br>


<h5> Entity–Relationship Model </h5>
<img src="https://user-images.githubusercontent.com/34139754/104079596-f6b3c980-5249-11eb-9012-f420b3cc9546.png" align="centre">


<h5> API's Postman ScreenShots</h5>
<h6> 1. Get TODO Tasks (GET Request)</h6>
Returns all the all todo tasks.
<img src="https://user-images.githubusercontent.com/34139754/104078989-d6ced680-5246-11eb-97fc-db147dd767cf.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 200 OK  |   20 ms |    543 B    |


<h6> 2. Create TODO Tasks (POST Request)</h6>
Create a todo task
<img src="https://user-images.githubusercontent.com/34139754/104078987-d6364000-5246-11eb-9c0b-5a75564f8b33.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 201 OK  |  428 ms |    358 B    |


<h6> 3. Update TODO Tasks (PUT Request)</h6>
Update a todo task
<img src="https://user-images.githubusercontent.com/34139754/104078985-d5051300-5246-11eb-99a3-bd62711834b4.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 201 OK  |  592 ms |    377 B    |


<h6> 4. Delete TODO Tasks (DELETE Request)</h6>
Delete a todo task
<img src="https://user-images.githubusercontent.com/34139754/104078983-d3d3e600-5246-11eb-8e73-8985e75dcf14.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 201 OK  |  428 ms |    358 B    |


<h6> 4. Search TODO Tasks (GET Request)</h6>
Search a todo task
<img src="https://user-images.githubusercontent.com/34139754/104078979-cf0f3200-5246-11eb-8b8f-9dd9e5ec130b.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 201 OK  |   16 ms |    525 B    |


<h5><a href="https://documenter.getpostman.com/view/6434629/TVzPnKH1"> Postman API's Documentation</a></h5>
<h5><a href="https://www.getpostman.com/collections/df0415ef583f88831d59"> Postman Collection</a></h5>


<h5> How to setup and run locally </h5>
<p>
  1. Clone the Repository <br>
  2. <a href="https://www.geeksforgeeks.org/python-virtual-environment/"> Create a Activate Python Virtual Environment </a></h5><br>
  3. After activating the virtual enviornment, redirect to project base directory. <br>
  4. Run the following command for installing dependencies.
</p>

    $ pip3 install -r requirements.txt

<br>
  5. Now direct to OYE_Rickshaw folder for starting the django server.

    $ cd OYE_Rickshaw

<br>
  6. Now before running the server, we have to setup database, so run.
 
    $ python3 manage.py migrate

<br>
  7. Now run the following command for starting the server

    $ python3 manage.py runserver

<br>

Now run the following apis described in the Postman collection for testing the project.
<br>

