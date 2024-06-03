from rest_framework.serializers import Serializer, FileField

class MergeRequestSerializer(Serializer):
    original_file = FileField()
    a_file = FileField()
    b_file = FileField()
    class Meta:
        fields = ["original_file", "a_file", "b_file"]