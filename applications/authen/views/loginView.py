from applications.authen.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework                  import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class LoginView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer

    def post(self, request, *args,**kwargs):
        serializers = self.serializer_class(
            data=request.data,
            context={'request':request}
        )
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token, __ = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)