from rest_framework import serializers

from core.models import  CallInitial, CallEnd


class CallInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallInitial
        fields = ('id','time','call_id','source','destination')

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        :param validated_data:
        """
        return CallInitial.objects.create(**validated_data)
class CallEndSerializer(serializers.Serializer):
    class Meta:
        model = CallEnd
        fields = ('id','time','call_id')
    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        :param validated_data:
        """
        return CallEnd.objects.create(**validated_data)
