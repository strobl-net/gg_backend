from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, data):
        if data.get('survey_id') is None:
            raise serializers.ValidationError('survey_id is not supplied')
        if data.get('user_id') is None:
            raise serializers.ValidationError('user_id is not supplied')
        if data.get('answers') is None:
            raise serializers.ValidationError('No answer is given')
        return data

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

