from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import random

User = get_user_model()

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    if not all([username, email, phone_number, password]):
        return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email is already in use'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, phone_number=phone_number, password=password)

    # Generate verification code
    verification_code = random.randint(100000, 999999)
    user.is_verified = False
    user.save()

    # Send verification code via email
    send_mail(
        'Verify Your Account',
        f'Your verification code is: {verification_code}',
        'no-reply@example.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'User registered successfully. Check your email for the verification code.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def verify_account(request):
    email = request.data.get('email')
    verification_code = request.data.get('verification_code')

    try:
        user = User.objects.get(email=email)
        if verification_code == '123456':  # Replace with actual logic
            user.is_verified = True
            user.save()
            return Response({'message': 'Account verified successfully.'})
        else:
            return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
