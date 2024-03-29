from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,filters
from profiles_api import serializers,models,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer



    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you most control over your application logic',
        'Is mapped mannually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):

        a_viewset=[
            'User actions (list,create,Retrive,update,partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new Hello Message"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'htttp_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'htttp_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of  an object"""
        return Response({'htttp_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle deleting an object by its ID"""
        return Response({'htttp_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginAPiView(ObtainAuthToken):
    """Handle creating User authentication tokens"""

    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    
