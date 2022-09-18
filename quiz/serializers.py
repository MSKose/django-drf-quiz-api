from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    # answer = AnswerSerializer(many=True, read_only=True)
    answer = serializers.StringRelatedField(many=True)

    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]