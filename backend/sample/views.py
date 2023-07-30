from django.shortcuts import render

from .models import Sample_post
from sample import serializers as SR

from rest_framework import generics

# 게시글 목록 
class SamplePostListView(generics.ListAPIView):
    queryset = Sample_post.objects.all()
    serializer_class = SR.SamplePostListModelSerializer

# 게시글 생성
class SamplePostCreateView( generics.CreateAPIView):
    queryset = Sample_post.objects.all()
    serializer_class = SR.SamplePostBaseModelSerializer

# 게시글 상세
class SamplePostRetrieveModelSerializer(generics.RetrieveAPIView):
    queryset = Sample_post.objects.all()
    serializer_class = SR.SamplePostRetrieveModelSerializer

# 게시글 수정, 삭제 
class SamplePostUpdateContent(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Sample_post.objects.all()
    serializer_class = SR.SamplePostUpdateContent
