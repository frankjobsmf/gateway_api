#rest_framework
from rest_framework import serializers

#add
class AddNoteSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

#update
class UpdateNoteSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()