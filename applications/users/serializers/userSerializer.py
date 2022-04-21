from applications.users.models.user    import User
from rest_framework       import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'password', 'name', 'email']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'name'    : user.name,
            'email'   : user.email,
        }