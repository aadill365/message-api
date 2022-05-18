from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone



# Create your views here.
class RegisterUserAPIView(generics.CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = RegisterSerializer

class MessagesAPI(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):
		time_limit = timezone.now() - timezone.timedelta(hours=1)
		filtered = Message.objects.filter(user=request.user,created_at__gte=time_limit)
		if filtered.count()<10:
			try:
				data = request.data
				message = Message.objects.create(user=request.user,message=data.get('message'))
				response = {
							'id':message.id,
				 			'message':message.message,
				 			'created_at':message.created_at,
				 			'created_by':{
				 				'id':request.user.id,
				 				'email': request.user.email,
				 				'username':request.user.username

				 			}
				 		}

				return Response(response)
			except Exception as e:
				return Response({'response':e.args})
		else:
			return Response({'response':'You have exhausted the quota of 10 messages per hour.'})


