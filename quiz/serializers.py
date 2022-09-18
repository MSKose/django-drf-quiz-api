from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    #! this would only get the answer_text to the front-end, but defining a custom relational field below in line 32 we'd get all: the id, answer_text, and is_right
    #! also, this is named "answer" because "Question" object has an attribute answer (see their fk relationship in models.py)
    # answer = serializers.StringRelatedField(many=True)

    #! this is called custom relational field: https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
    #! this way, the fields in AnswerSerializer will be serialized and brought into the variable "answer" here to be used in fields
    answer = AnswerSerializer(many=True, read_only=True) 

    class Meta:
    
        model = Question
        fields = [
            'title',
            'answer',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True) #! we're not putting many=True for this one since we're not returning more than one item

    class Meta:
    
        model = Question
        fields = [
            'quiz',
            'title',
            'answer',
        ]