from rest_framework                   import generics
from rest_framework.permissions                    import IsAuthenticated
from applications.users.models.user                import User
from applications.users.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        ''' 
        Retrieves an user 
        '''
        return super().get(request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        '''
        Updates a user
        '''
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    '''
    Deletes a user
    '''
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)