from rest_framework import viewsets

from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()