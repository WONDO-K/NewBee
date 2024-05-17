from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer


@method_decorator(csrf_exempt, name='dispatch')
# 게시글 작성 및 목록
class ArticleListCreateAPIView(APIView): 
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = (JSONRenderer,)

    # 게시글 작성
    @swagger_auto_schema(tags=['게시판'], request_body=ArticleSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data) # request.data에는 게시글 정보가 담겨있음
        if serializer.is_valid(raise_exception=True): # raise_exception=True로 설정하면 유효성 검사에 실패하면 400 Bad Request 응답을 반환
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 게시글 목록
    @swagger_auto_schema(tags=['게시판'])
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
# 게시글 조회, 수정, 삭제
class ArticleRetrieveAPIView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = (JSONRenderer,)

    # 게시글 조회
    @swagger_auto_schema(tags=['게시판'])
    def get(self, request, pk=None, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk) # pk에 해당하는 게시글이 없으면 404 Not Found 응답을 반환
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 수정
    @swagger_auto_schema(tags=['게시판'], request_body=ArticleSerializer)
    def put(self, request, pk=None, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data) # request.data에는 수정할 게시글 정보가 담겨있음
        if serializer.is_valid(raise_exception=True): # raise_exception=True로 설정하면 유효성 검사에 실패하면 400 Bad Request 응답을 반환
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


    # 게시글 삭제
    @swagger_auto_schema(tags=['게시판'])
    def delete(self, request, pk=None, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 댓글 작성
@method_decorator(csrf_exempt, name='dispatch')
class CommentCreateAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = (JSONRenderer,)

    # 댓글 작성
    @swagger_auto_schema(tags=['댓글'], request_body=CommentSerializer)
    def post(self, request, article_pk=None, *args, **kwargs):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # raise_exception=True로 설정하면 유효성 검사에 실패하면 400 Bad Request 응답을 반환
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 댓글 조회, 수정, 삭제
@method_decorator(csrf_exempt, name='dispatch')
class CommentRetrieveAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = (JSONRenderer,)

    # 댓글 조회
    @swagger_auto_schema(tags=['댓글'])
    def get(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # 댓글 수정
    @swagger_auto_schema(tags=['댓글'], request_body=CommentSerializer)
    def put(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk) 
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True): # raise_exception=True로 설정하면 유효성 검사에 실패하면 400 Bad Request 응답을 반환
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 댓글 삭제
    @swagger_auto_schema(tags=['댓글'])
    def delete(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)