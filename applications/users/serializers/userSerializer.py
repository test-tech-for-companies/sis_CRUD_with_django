from applications.users.models.user    import User
from rest_framework       import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'password', 'name', 'email']
        extra_kwargs = {'password':{'write_only':True,'min_length':8}}
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'name'    : user.name,
            'email'   : user.email,
        }