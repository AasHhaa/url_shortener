# Start project:
- pip install -r requirements.txt
- flask run

# API description:
After starting the project, head to the page http://127.0.0.1:5000/. 
On the page you can fill in the "Url field" and "Lifetime field". 
The default value for the Lifetime field is 90 days, so this field is optional.

# Endpoints:
- http://127.0.0.1:5000/ - Directs to the form page.
- http://127.0.0.1:5000/add_link - Support only POST method. Adds a link.
- http://127.0.0.1:5000/<short_url> - Redirect endpoint. 
  Provide your short link after the \ and if there is one in the database, 
  and its lifetime has not expired, you will be redirected to the original link.