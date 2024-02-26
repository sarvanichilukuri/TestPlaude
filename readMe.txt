To set up the environment:

Create a virtual environment: 
python -m venev testPlaude

Activate the virtual environment:
testPlaude\Scripts\activate

Now inside the virtual environment do the following:

Install all the dependencies:
pip install -r requirements.txt


Now migrate all the models to your database:
python manage.py makemigrations
python manage.py migrate


Commands to run the project:

Start the server:
python manage.py runserver 8080

http://localhost:8080/posts/Pages/ - displays a button 
Upon clicking on the button "Fetch Data", it fetches 1 random post from the endpoint, between 1 to 100, saves it and redirects to a Success page("/success") 
which consists of all the posts fetched till date along with the newly fetched post
