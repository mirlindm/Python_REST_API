# Python_REST_API
A simple REST API for a catalog of products. Technology used: Python Django REST API

I have used Visual Code IDE for developing this REST API. The data format is JSON!

Instructions on how to deploy and run it:

Clone the repo: git clone https://github.com/mirlindm/Python_REST_API.git

1. Open the project in the preferred IDE:

2. Navigate to the folder: < cd adcash_rest >

3. On a terminal, run: < pip install djangorestframework > - if not installed before. 

4. Run: < python manage.py makemigrations > - in order to make the migrations in the project

5. Run: < python manage.py migrate > - in order to migrate the models created in the project

6. Create a super user for Django Rest Framework: < python manage.py createsuperuser > 

7. Create a username and password (email can be blank)

8. Run: < python manage.py runserver > 

9. Open browser and go to: http://localhost:8000/ - this is the main endpoint of our application.

10. Navigate to: http://localhost:8000/admin - here you can manually create some categories and products through the interface

11. Later, navigate to: http://localhost:8000/categories - to:
		11.1. (GET) see all the categories in a JSON format
		11.2. (POST) create a new category in a JSON format by inputting the necessary fields
		
12. Later, navigate to: http://localhost:8000/products - to:
		12.1. (GET) see all the products in a JSON format
		12.2. (POST) create a new product in a JSON format by inputting the necessary fields
		
13. Navigate to: http://localhost:8000/categories/1/ - to:
		13.1. (GET) see the category with id = 1 (first category), and all of the products that belong to it
		13.2. (PUT) update the category with id = 1 (first category)
		13.3  (DELETE) delete the category based on its id
		
		
14. Navigate to: http://localhost:8000/products/1/ - to:
		14.1. (GET) see all the details of the product with id = 1 (first product)
		14.2. (PUT) update the product with id = 1 (first product)
		14.3  (DELETE) delete the product based on its id
		
15. Run: < python manage.py test > - to run the unit tests which are located in < product_rest > folder, and in the < tests.py > file	


**************************************************************************

** I have used Postman to test the APIS **

** Category APIs: **

1. GET - Retrieve All Categories - http://localhost:8000/categories/

2. GET - Retrieve List of Products of Concrete Category - http://localhost:8000/categories/1/

3. POST - Create New Category - http://localhost:8000/categories/

	3.1 Request Body (example):  
	
							{
								"category_id": 1,
								 "category_name": "Electronis",
								"category_description": "Mobile Phones, Laptops, Other  Devices"
							}

4. PUT  - Update Category By ID - http://localhost:8000/categories/1/

	4.1 Request Body (example):
	
							{
							"category_id": 1,
							"category_name": "All Electronics",
							"category_description": "All Mobile Phones, Laptops, Other  Devices",
							"products": [
								{
									"id": 1,
									"product_name": "All Mobile Phones",
									"product_amount": 40,
									"category": 1
								}
										]
							}

5. DELETE - Delete Category By ID - http://localhost:8000/categories/1/   



**************************************************************************

**Product APIs:**

1. GET - Retrieve All Products - http://localhost:8000/products/

2. GET - Retrieve Single Product - http://localhost:8000/products/1/

3. POST - Create New Product - http://localhost:8000/products/

	3.1 Request Body (example):
	
								{
								"id": 1,
								"product_name": "iPhone 11",
								"product_amount": 25,
								"category": 1
								}
	

4. PUT  - Update Product By ID - http://localhost:8000/products/1/

	4.1 Request Body (example):
	
								{
								"id": 1,
								"product_name": "Apple Phone", 
								"product_amount": 40,
								"category": 1
								}


5. DELETE - Delete Product By ID - http://localhost:8000/products/1/  

**************************************************************************





