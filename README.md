# Django API Challenge #

## Task: ##

Build a CRUD API with basic functionality for restaurant management.
* A customer should be able to order an item from a menu (Retrieved from [this menu](https://api.myjson.com/bins/19vode). Hint: the food menu is listed under "categories").
* Kitchen should be able to read the customers order with a table number. When they’ve done cooking the meal, they should be able to update the customer that their meal is ready
* Manager should be able to delete the order upon a customers request.

Build unit tests to ensure the endpoints are functioning, and protect the API with some sort of authorization header.

## How To Use: ##

* Download repo
* Connect to your local db
* get into your virtual env
* cd into "restaurant"
* run `python setup.py install` to get necessary packages
* `python manage.py runserver` to start the server

## End Points ##

* `http://127.0.0.1:8000/orders/` to list all/ post
* `http://127.0.0.1:8000/orders/1` to get/ delete/ update order with id 1

## Approach ##

As this was my first time using Django, I began by building a full MVC web application. I chose to do this to really familiarise myself with the tools available, the documentation and to better understand how the framework functions. The full site including templates can be seen in previous commits.

After this I streamlined my already built MVC into a much cleaner API. I did this by using djang-rest-framework as this allowed me to DRY up the code in my views and url confs.

Testing was done using unnitest and Django's test framework. They are simple test to check that each of the endpoints works correctly to manipulate data in the database as expected.

The API was protected by incorporating django-rest-auth into the project. Resultantly, some endpoints are protected with an Auth Token that is only attainable by logging in.

## Areas For Improvement ##

Unfortunately, I did not find as much time as I had hoped to spend on this challenge. As such there are various areas that could be further developed.

Security:
    * Build custom Users to allow only customer/chef/manager to access various end points
    * Check the item being created against the items in the menu to allow/ deny orders

Message queing:
    * Incoporate a message queueing system
