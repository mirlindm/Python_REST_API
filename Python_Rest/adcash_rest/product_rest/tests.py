import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from . models import Category, Product
from . serializers import CategorySerializer, ProductSerializer


class ProductTestCase(APITestCase):

    # 1. Testing the retrieval of the categories
    def test_categoryRetrieval(self):
        response = self.client.get("/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 2. Testing the retrieval of the categories
    def test_productRetrieval(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 3. Testing the successful creation of a category
    def test_categoryRegistration(self):
        data = { "category_id": 1,
                 "category_name": "Beauty Products",
                 "category_description": "All beauty items",
                
                }
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # 4. Testing the creation of a category with a missing field, which should fail.
    def test_categoryRegistrationWithMissingColumn(self):
        data = { "category_id": 1,
                 "category_name": "Beauty Products"
                 #"category_description": "All beauty items",    -- this row is missing in this case!
                 
                }
        response = self.client.post("/categories/", data)
        self.assertContains(response, "This field is required", status_code=400)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

    # 5. testing the successful creation of a product along with the creation of its category
    def test_categoryAndProductRegistration(self):
        data = { "category_id": 1,
                 "category_name": "Beauty Products",
                 "category_description": "All beauty items"
                 
                }

        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 1 
                }
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)


    # 6. testing the creation of a product and its category, with a missing field in the product model, which should fail
    def test_categoryAndProductRegistrationWithFailure(self):
        data = { "category_id": 1,
                 "category_name": "Beauty Products",
                 "category_description": "All beauty items"
                 
                }

        data1 = { 
                    "product_name": "Samsung",
                    #"product_amount": 25,      --> This field is missing in this case, to check if the product won't be created!
                    "category": 1 
                }
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response1, "This field is required", status_code=400)
        

    # 7. Creating a category with ID = 1 and creating a product which belongs to Category with ID = 2.
    # The creation of the product should fail, because we do not have the Category with ID = 2, yet.  
    def test_categoryAndProductRegistrationForNonexistingCategory(self):
        data = { "category_id": 1,
                 "category_name": "Beauty Products",
                 "category_description": "All beauty items"
                 
                }

        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 2 
                }
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
    


    # 8. Testing the creation of a category and its product in one go, 
    # product creation should fail, as it needs to be created separately
    def test_categoryAndProductRegistrationTogether(self):
        
        data = {
                "category_id": 1,
                "category_name": "Test",
                "category_description": "Test Test",
                "products": [
                    {
                        "id": 20,
                        "product_name": "Highlighters",
                        "product_amount": 50
                    }
          
                    ]
                }  

        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    # 9. Update Category
    def test_updateCategory(self):
        
        data = {
                "category_id": 1,
                "category_name": "Category 1",
                "category_description": "Items of Category 1"
                } 
        data1 = {
                "category_id": 1,
                "category_name": "Category1 is updated",
                "category_description": "Items of Category 1"
                }   

        #updated_data = {"category_name": "Category1 is updated"}
                     

        response = self.client.post("/categories/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.put("/categories/1/", data=data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertContains(response1, "Category1 is updated")



    
    
     # 10. Delete Category
    def test_deleteCategory(self):
        
        data = {
                "category_id": 1,
                "category_name": "Category 1",
                "category_description": "Items of Category 1"     
                }

        response = self.client.post("/categories/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.delete("/categories/1/", data)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        


     # 11. Update Product By ID
    def test_updateProductByID(self):
        
        data = {
                "category_id": 1,
                "category_name": "Category 1",
                "category_description": "Items of Category 1"
                } 
        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 1 
                }
        data2 = { 
                    "product_name": "iPhone",
                    "product_amount": 20, 
                    "category": 1 
                }

        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.client.put("/products/1/", data2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertContains(response2, "iPhone")


    # 12. Delete Product By ID
    def test_deleteProductByID(self):
        
        data = {
                "category_id": 1,
                "category_name": "Category 1",
                "category_description": "Items of Category 1"
                } 

        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 1 
                }

        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response1 = self.client.delete("/products/1/", data)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)


    # 13. Category Description Field exceeds limit of characters
    def test_categoryDescriptionLessThanFiftyChars(self):
        
        data = {
                "category_id": 1,
                "category_name": "Category 1",
                "category_description": "This is a random text used to make a category description more than fifty characters, which will be used for validation and testing purposes"
                } 

        response = self.client.post("/categories/", data)
        self.assertContains(response,"Ensure this field has no more than 50 characters.", status_code=400)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

    # 14. Testing the successful retrieval of products of the correct category
    def test_categoryRegistrationAndProductRetrieval(self):
        data = { "category_id": 1,
                 "category_name": "Elecronics",
                 "category_description": "All Phones",
                }
        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 1 
                }
        data2 = { 
                    "product_name": "iPhone",
                    "product_amount": 25, 
                    "category": 1 
                }                
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED) 
        response2 = self.client.post("/products/", data2)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        response3 = self.client.get("/categories/1/")
        self.assertEqual(response3.status_code, status.HTTP_200_OK)   
        self.assertContains(response3,"iPhone", status_code=200)



    # 15. Testing the successful retrieval of a single prodct by ID
    def test_categoryRegistrationAndProductRetrievalByID(self):
        data = { "category_id": 1,
                 "category_name": "Elecronics",
                 "category_description": "All Phones",
                }
        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": 1 
                }              
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED) 
        response3 = self.client.get("/products/1/")
        self.assertEqual(response3.status_code, status.HTTP_200_OK)   
        self.assertContains(response3,"Samsung", status_code=200)     
     


    # 16. Testing product creation with a string amount value instead of Integer
    def test_createProductWithInvalidAmount(self):
        data = { "category_id": 1,
                 "category_name": "Elecronics",
                 "category_description": "All Phones",
                }
        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": "Twenty Five", 
                    "category": 1 
                }              
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)   
        self.assertContains(response1,"A valid integer is required.", status_code=400)   

        
    # 17. Testing product creation with a string Category value instead of Primary Key
    def test_createProductWithInvalidCategory(self):
        data = { "category_id": 1,
                 "category_name": "Elecronics",
                 "category_description": "All Phones",
                }
        data1 = { 
                    "product_name": "Samsung",
                    "product_amount": 25, 
                    "category": "One" 
                }              
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)   
        self.assertContains(response1,"Incorrect type. Expected pk value, received str.", status_code=400)


    # 18. Testing access to an uncreted category, which should fail
    def test_retrieveNonExistingCategory(self):
              
        response = self.client.get("/categories/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertContains(response,"Not found.", status_code=404)

    # 19. Testing access to a created and uncreated product, which should pass and fail, respectively
    def test_retrieveNonExistingProduct(self):
        data = { "category_id": 1,
                 "category_name": "Elecronics",
                 "category_description": "All Phones",
                }
        data1 = { 
                    "product_name": "Huawei",
                    "product_amount": 25, 
                    "category": 1
                }          
              
        response = self.client.post("/categories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response1 = self.client.post("/products/", data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED) 
        response3 = self.client.get("/products/1/")   
        self.assertEqual(response3.status_code, status.HTTP_200_OK) 
        self.assertContains(response3,"Huawei", status_code=200)
        response4 = self.client.get("/products/2/")   
        self.assertEqual(response4.status_code, status.HTTP_404_NOT_FOUND) 
        self.assertContains(response4,"Not found.", status_code=404)