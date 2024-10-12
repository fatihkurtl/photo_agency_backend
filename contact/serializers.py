from rest_framework import serializers
from .models import ContactForm, ContactInformation, SocialMedia, WhyChooseUs, FrequentlyAskedQuestions


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        exclude = ['id', 'created_at', 'updated_at']

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'created_at', 'updated_at']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        exclude = ['id', 'created_at', 'updated_at']

class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        exclude = ['id', 'created_at', 'updated_at']

class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        exclude = ['id', 'created_at', 'updated_at']
