from rest_framework import serializers
from .models import ProductImage, Product, Category, Order


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image']

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        product_image = ProductImage.objects.create(**image_data)
        product = Product.objects.create(image=product_image, **validated_data)
        return product

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        if image_data:
            image_instance = instance.image
            image_instance.image = image_data.get('image', image_instance.image)
            image_instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'products']


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'product']

    def create(self, validated_data):
        product_data = validated_data.get('product')
        order = Order.objects.create(product=product_data)
        return order
