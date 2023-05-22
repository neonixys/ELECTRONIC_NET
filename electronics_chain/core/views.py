from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from electronics_chain.core.serializers import CoreSerializer


class UserCreateView(CreateAPIView):
    serializer_class = CoreSerializer
    permission_classes = [AllowAny]