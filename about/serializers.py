from rest_framework import serializers
from .models import AboutUsContent, OurApproach, BusinessCard, SkilsAndExperience, Achievements


class AboutUsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsContent
        exclude = ('id', 'created_at', 'updated_at')


class OurApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurApproach
        exclude = ('id', 'created_at', 'updated_at')


class BusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        exclude = ('id', 'created_at', 'updated_at')


class SkilsAndExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkilsAndExperience
        exclude = ('id', 'created_at', 'updated_at')


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        exclude = ('id', 'created_at', 'updated_at')
