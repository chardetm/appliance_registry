from rest_framework import serializers

from . import models


class ApplianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Appliance
        fields = '__all__'

    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Site
        fields = '__all__'