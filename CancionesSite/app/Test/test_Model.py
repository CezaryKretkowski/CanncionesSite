from django.test import TestCase
from django.urls import reverse
from ..Entities.Dictionary.Category import Category
from ..Entities.Dictionary.SubCategory import SubCategory
from ..Entities.Dictionary.ProductDetails.Brand import Brand
from ..Entities.Dictionary.ProductDetails.BodyMaterial import BodyMaterial
from ..Entities.Dictionary.ProductDetails.TopMaterial import TopMaterial
from ..Entities.Dictionary.ProductDetails.Pickups import Pickups
from ..Entities.Product.Product import Product
from ..Entities.Product.Customization import Customization


class TestCategoryModel(TestCase):
    
    def setUp(self):
        self.data = Category.objects.create(name='django', image='django') 
       
    def test_category_model_entry(self):
        data = self.data
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):

        data = self.data
        response = self.client.post(
            reverse('app:SubCategoryView', args=[data.id]))
        self.assertEqual(response.status_code, 200)
  
  
class TestSubCategory(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='django', image='django') 
        self.subCat=SubCategory.objects.create(name='django_restFramewroek',category=self.category,image='django_restFramewroek')
       
    def test_subCategory_model_entry(self):
        data = self.subCat
        self.assertTrue(isinstance(data, SubCategory))
        self.assertEqual(str(data), 'django_restFramewroek')
  
    def test_subCategory_url(self):
        data = self.subCat
        response = self.client.get(
            reverse('app:ProductList', args=[data.id]))
        self.assertEqual(response.status_code, 200) 
        
        
class TestBrand(TestCase):
    
    def setUp(self):
        self.brand=Brand.objects.create(name="new_Brand")
        
    def test_Brand_model_entry(self):
        data = self.brand
        self.assertTrue(isinstance(data, Brand))
        self.assertEqual(str(data), 'new_Brand')


class TestCustomizationData(TestCase):
    
    def setUp(self):
        self.pickups=Pickups.objects.create(name="HHS")
        self.body=BodyMaterial.objects.create(name="oak")
        self.top=TopMaterial.objects.create(name="machogany")
        self.customization = Customization.objects.create(color="#FFFFFF"
                                                          ,topMaterial=self.top
                                                          ,bodyMaterial=self.body
                                                          ,pickups=self.pickups)
        
    def test_CustomizationData_model_entry(self):
        self.assertTrue(isinstance(self.pickups, Pickups))
        self.assertTrue(isinstance(self.body, BodyMaterial))
        self.assertTrue(isinstance(self.top, TopMaterial))
        self.assertTrue(isinstance(self.customization, Customization))
        self.assertEqual(str(self.pickups), 'HHS')
        self.assertEqual(str(self.body), 'oak')
        self.assertEqual(str(self.top), 'machogany')
                
        
        
class TestProduct(TestCase):
    
    def setUpCustomization(self):
        self.pickups=Pickups.objects.create(name="HHS")
        self.body=BodyMaterial.objects.create(name="oak")
        self.top=TopMaterial.objects.create(name="machogany")
        self.customization = Customization.objects.create(color="#FFFFFF"
                                                          ,topMaterial=self.top
                                                          ,bodyMaterial=self.body
                                                          ,pickups=self.pickups)
    
    def setUp(self):
        self.setUpCustomization()
        self.category = Category.objects.create(name='django', image='django') 
        self.subCat = SubCategory.objects.create(name='django_restFramewroek',category=self.category,image='django_restFramewroek')
        self.brand = Brand.objects.create(name="new_Brand")
        self.product = Product.objects.create(name='djangoBook',brand = self.brand,subCategory = self.subCat,
                                              price=145.67,description="testowyOpis",rating=1,available=True,specialOffer=False,specialPrice=130.99,customization=None,image='django')
        self.productWithCustomization = Product.objects.create(name='djangoBook',brand = self.brand,subCategory = self.subCat,
                                              price=145.67,description="testowyOpis",rating=1,available=True,specialOffer=False,specialPrice=130.99,customization=None,image='django')
        
    def test_Product_model_entry(self):
        self.assertTrue(isinstance(self.product,Product))
        self.assertTrue(isinstance(self.productWithCustomization,Product))
        self.assertEquals(str(self.product),'djangoBook')
        
    def test_get_sbsolut_url(self):
        data=self.product
        response = self.client.get(
            reverse("app:ProductDetails", args=[data.id]))
        self.assertEqual(response.status_code, 200) 
        
    def test_add_To_Cart(self):
        data=self.product
        response = self.client.get(
            reverse("app:Cart/add", args=[data.id]))
        self.assertEqual(response.status_code, 302) 
    
    def test_Customization(self):
        data=self.product
        response = self.client.get(
            reverse("app:Cart/add", args=[data.id]))
        self.assertEqual(response.status_code, 302) 
        