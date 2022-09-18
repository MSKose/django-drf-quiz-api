from django.shortcuts import render
from rest_framework import generics
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        '''
        #! the double underscore here basically means WHERE in SQL. See: https://docs.djangoproject.com/en/dev/topics/db/queries/#field-lookups
        #! here, in our case, because Question model is related to Quizzes model with a fk, we access the title attribute of the Quizzes with 
        #! double underscore.
        #! the order_by('?')[:1] part randomizes and selects one item from it
        '''
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)