from rest_framework.serializers import ModelSerializer

from .models import Sample_post

class SamplePostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Sample_post
        fields = '__all__'

class SamplePostListModelSerializer(SamplePostBaseModelSerializer):
    class Meta(SamplePostBaseModelSerializer.Meta):
        fields =[
            'id',
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',]

class SamplePostUpdateContent(SamplePostBaseModelSerializer):
    class Meta(SamplePostBaseModelSerializer.Meta):
        fields =['content',]
        
class SamplePostRetrieveModelSerializer(SamplePostBaseModelSerializer):
    class Meta(SamplePostBaseModelSerializer.Meta):
        fields='__all__'
