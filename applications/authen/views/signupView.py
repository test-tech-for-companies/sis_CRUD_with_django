from rest_framework.response            import Response
from rest_framework                     import status, views
from rest_framework.authtoken.models    import Token
from applications.users.serializers     import UserSerializer

class SignUpView(views.APIView):

    def post(self, request, *args, **kwargs):
        '''
        Creates a new user (admin/customer)
        '''
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, __ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)