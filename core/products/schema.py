import graphene 
from graphene_django import DjangoObjectType
from .models import (
    Category, 
    SubCategory, 
    Product, 
    ProductImage, 
    Rating, 
    Comment,
)

class ProductType(DjangoObjectType): 
    class Meta: 
        model = Product
class Query(graphene.ObjectType): 
    all_products = graphene.List(ProductType)
    def resolve_all_products(root, info): 
        return Product.objects.all()

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class SubCategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        fields = ('id','image')

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image

class RatingType(DjangoObjectType):
    class Meta:
        model = Rating
        fields = ('id','note')

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int(required=True))
    category = graphene.Field(CategoryType, id = graphene.Int(), name=graphene.String())
    subCategory = graphene.Field(SubCategoryType, id=graphene.Int(), name = graphene.String())

    def resolve_all_products(root,info):
        return Product.objects.all()

    def resolve_product(root, info, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None

    def resolve_category(root, info, id=None, name=None):
        try:
            if(id):
                return Category.objects.get(pk=id)
            if (name):
                return Category.objects.get(name=name)
            else:
                return None
        except Category.DoesNotExist:
            return None
    
    def resolve_subCategory(root, info, id=None, name = None):
        try:
            if(id):
                return SubCategory.objects.get(pk=id)
            if (name):
                return SubCategory.objects.get(name = name)
            else:
                return None
        except SubCategory.DoesNotExist:
            return None