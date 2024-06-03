from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import FileResponse
from .serializers import MergeRequestSerializer
import io
from .merge import MergeResult

# Create your views here.
class MergeViewSet(ViewSet):
    serializer_class = MergeRequestSerializer

    def create(self, request):
        with request.FILES.get('original_file').open('r') as original_file, request.FILES.get('a_file').open('r') as a_file, request.FILES.get('b_file').open('r') as b_file:
            buffer = io.BytesIO()
            merge = MergeResult.merge(original_file.readlines(), a_file.readlines(), b_file.readlines())
            merge.write_to_byte_buffer(buffer)
            buffer.seek(0)

            return FileResponse(buffer, as_attachment=True, filename="merged.txt")


