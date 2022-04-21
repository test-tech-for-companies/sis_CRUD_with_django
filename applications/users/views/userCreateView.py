from rest_framework                            import generics
from applications.users.serializers.userSerializer   import UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer