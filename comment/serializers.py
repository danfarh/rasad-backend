from rest_framework import serializers
from .models import Question,Answer
from users.serializers import RegisterSerializer
from product.serializers import ProductSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    product = ProductSerializer()
    class Meta:
        model = Question
        fields = ['text','title','user','product']        


class CreateQuestionSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    product = serializers.IntegerField()
    title = serializers.CharField(required=True)
    class Meta:
        model = Question
        fields = ['text','title','user','product']  


class AnswerSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = ['text','user','question']    


class CreateAnswerSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    question = serializers.IntegerField()
    class Meta:
        model = Answer
        fields = ['text','user','question']         