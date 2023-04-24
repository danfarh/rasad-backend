from rest_framework import serializers
from .models import CustomUser as User, Company
from rest_framework.validators import UniqueValidator
from category.serializers import CategorySerializer
from category.models import Category


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=60,
        required=True,
    )
    last_name = serializers.CharField(
        max_length=60,
        required=True
    )
    email = serializers.EmailField(
        max_length=100,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=20,
        required=True,
    )
    user_type = serializers.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'password', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=20,
        required=True,
    )
    phone_number = serializers.CharField(
        max_length=15,
        required=True
    )

    class Meta:
        model = User
        fields = ['password', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CompanySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Company
        fields = ['id', 'name', 'image', 'category']


class CreateCompanySerializer(serializers.ModelSerializer):
    #category = serializers.SerializerMethodField()
    category = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ['name', 'image', 'category']

    # def get_category(self, obj):
    #     category = Category.objects.filter(id=obj)
    #     return CategorySerializer(instance=category).data


class VisitorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=60,
        required=True,
    )
    last_name = serializers.CharField(
        max_length=60,
        required=True
    )
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=20,
        required=True,
    )
    center_x = serializers.FloatField(required=True)
    center_y = serializers.FloatField(required=True)
    radius = serializers.FloatField(required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','phone_number', 'password', 'center_x', 'center_y', 'radius']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ReportVisitorsActivitySerializer(serializers.Serializer):
    hours_of_work = serializers.FloatField()
    sales_amount = serializers.FloatField()
    num_out_of_limit = serializers.IntegerField()


class VisitorCoordinatesSerializer(serializers.Serializer):
    center_x = serializers.FloatField(required=True)
    center_y = serializers.FloatField(required=True)
    radius = serializers.FloatField(required=True)
