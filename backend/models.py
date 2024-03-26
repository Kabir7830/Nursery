from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Users(AbstractUser):
    username = None  # Remove the username field

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,null=True,blank=True)

    # Add your additional fields here
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']  # Add any other required fields

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Company(models.Model):
    class Meta:
        db_table = "company"

    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    email = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 14)
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
    favicon = models.ImageField(upload_to='favicon/',null=True,blank=True)
    address = models.CharField(max_length = 255,null=True,blank=True)
    currency_symbol = models.TextField(blank=True,default="₹")


class ProductCategory(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/',blank=True,default='/categories/default-image.png')
    show_on_home = models.BooleanField(default=False,blank=True)


class Products(models.Model):

    def __str__(self):
        self.name

    class Meta:
        db_table = 'products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory,on_delete=models.PROTECT,null=True,blank=True)
    cost_price = models.CharField(max_length=255)
    selling_price = models.CharField(max_length=255)
    rating = models.CharField(max_length=255,null=True,blank=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length = 255,null=True,blank=True)
    is_published = models.BooleanField(default=True,null=True,blank=True)
    is_new_arrival = models.BooleanField(default=True,null=True,blank=True)
    is_best_selling = models.BooleanField(default=True,null=True,blank=True)

class Images(models.Model):
    class Meta:
        db_table = 'images'
        managed = True
        verbose_name = 'image'
        verbose_name_plural = 'images'
    
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Products,on_delete=models.CASCADE)

class ProductCollections(models.Model):

    def __str__(self):
        self.name

    class Meta:
        db_table = 'product_collections'
        managed = True
        verbose_name = 'ProductCollection'
        verbose_name_plural = 'ProductCollections'

    name = models.CharField(max_length=255,unique=True)
    product_ids = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)


class HomepageCollection(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = 'homepage_collection'
        managed = True
        verbose_name = 'HomepageCollection'
        verbose_name_plural = 'HomepageCollections'

    collection = models.ForeignKey(ProductCollections,on_delete=models.PROTECT)


class Banner(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = 'banners'
        managed = True
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    image = models.ImageField(upload_to='banners/')
    heading = models.CharField(max_length=255,null=True,blank=True)
    sub_heading = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)



class ShopByCategory(models.Model):
    class Meta:
        db_table = "shop_by_category"
        managed = True

    product = models.ForeignKey(Products,on_delete=models.CASCADE)


class Cart(models.Model):
    class Meta:
        db_table = "cart"

    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.CharField(max_length = 255,default=1,blank=True)
    total = models.CharField(max_length = 255,null=True,blank=True)
    # discount = models.CharField(max_length = 255,null=True,blank=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)


class UserAddress(models.Model):
    class Meta:
        db_table = "UserAddress"

    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255,null=True,blank=True)
    email = models.EmailField()
    company_name = models.CharField(max_length= 255,null=True,blank=True)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length=255)
    order_notes = models.TextField(null=True,blank=True)
    country = models.CharField(max_length = 255)
    pin_code = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 255)


class Orders(models.Model):
    class Meta:
        db_table = "orders"

    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress,on_delete = models.CASCADE)
    products = models.TextField()
    total_price = models.CharField(max_length = 255)
    # discount = models.CharField(max_length = 255,default="0",blank=True,null=True)
    # discounted_price = models.CharField(max_length = 255,null=True,blank=True)
    date_time = models.CharField(max_length = 255)
    is_completed = models.BooleanField(default=False,null=True,blank=True) 



class Newsletters(models.Model):
    class Meta:
        db_table = 'newsletters'

    email = models.EmailField()
    date_time = models.CharField(max_length = 255,blank=True,null=True)
    is_approved = models.BooleanField(default=False,null=True,blank=True)



class Contact(models.Model):
    class Meta:
        db_table = "contact"

    name = models.CharField(max_length= 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    date_time = models.CharField(max_length = 255,null=True,blank=True)
    is_read = models.BooleanField(default = False,null=True,blank=True)



class Reviews(models.Model):
    class Meta:
        db_table = "reviews"
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True)
    nickname = models.CharField(max_length = 255)
    reason = models.CharField(max_length = 255)
    comments = models.TextField()
    rating = models.CharField(max_length = 255)
    date_time = models.CharField(max_length = 255)
    is_read = models.BooleanField(default=False,null=True,blank=True)


class Blogs(models.Model):
    class Meta:
        db_table = "blogs"

    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    publish_date = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_published = models.BooleanField(default = True,blank=True,null=True)


class BlogComments(models.Model):
    class Meta:
        db_table = "blog_comments"

    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    comment = models.TextField()
    tags = models.CharField(max_length = 255,null=True,blank=True)
    is_approved = models.BooleanField(default = False,blank=True,null=True)
