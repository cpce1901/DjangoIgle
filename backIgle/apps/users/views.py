import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.sessions.models import Session
from .serializer import UserTokenSerializer
from .authorization_mixin import Authentication

class UserTokenRefresh(Authentication, APIView):
    def get(self, request, *args, **kargs):
        try:
            user_token, _ = Token.objects.get_or_create(user=self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token': user_token.key,
                'user': user.data
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'error', 'Credenciales enviadas incorrectas'
                }, status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kargs):
        login_serializer = self.serializer_class(data= request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de secion existoso'
                        }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de secion existoso'
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Este usuario no puede iniciar seción'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
           return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

 
class Logout(APIView):


    def post(self, request, *args, **kwargs):
        try:
            token_value = request.POST.get('token')
            token = Token.objects.filter(key=token_value).first()

            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.datetime.now())
                
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()

                token.delete()

                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({
                    'token_message': token_message,
                    'session_message': session_message
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'No se ha encontrado un usuario con estas credenciales'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Error en el proceso de cierre de sesión: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)