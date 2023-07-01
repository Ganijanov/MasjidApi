from rest_framework import serializers
from main import models

class MasqueSer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = models.Masque
        fields = '__all__'


class ImageMasqueSer(serializers.ModelSerializer):
    masqueimg = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = models.ImageMasque
        fields = '__all__'


class PrayerTimeeSer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(read_only=True, slug_field='username')
    masquet = serializers.SlugRelatedField(read_only=True, slug_field='name')
 
    class Meta:
        model = models.PrayerTime
        fields = '__all__'
        

class StaffSer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(read_only=True, slug_field='username')
    masquet = serializers.SlugRelatedField(read_only=True, slug_field='name')
   
    class Meta:
        model = models.Staff
        fields = '__all__'
        