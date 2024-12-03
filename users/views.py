from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer
from users.services import (create_stripe_product, create_stripe_price,
                            create_stripe_session, get_stripe_session_retrieve)

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.set_password(new_user.password)
        new_user.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class PaymentListApiView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']


class PaymentCreateApiView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        success_url = "http://127.0.0.1:8000/" + reverse_lazy('users:payment_list')

        payment = serializer.save()
        payment.owner = self.request.user
        stripe_product = create_stripe_product(payment)
        stripe_price = create_stripe_price(stripe_product, payment.value)
        stripe_session = create_stripe_session(stripe_price, success_url)  # "http://127.0.0.1:8000/users/payments"

        payment.payment_link = stripe_session.get("url")
        payment.session_id = stripe_session.get("id")

        payment.save()


class PaymentRetrieveApiView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, *args, **kwargs):

        payment_id = self.kwargs['pk']
        payment = get_object_or_404(Payment, pk=payment_id)

        if payment is not None and payment.session_id is not None:
            status = get_stripe_session_retrieve(payment.session_id)
        else:
            status = '_нет данных_'
        return Response({"status": status})
