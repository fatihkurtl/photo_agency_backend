from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import ContactInformation, SocialMedia, WhyChooseUs, FrequentlyAskedQuestions
from .serializers import ContactFormSerializer, ContactInformationSerializer, SocialMediaSerializer, WhyChooseUsSerializer, FrequentlyAskedQuestionsSerializer


class ContactSaveView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Mesajınız alındı, En kısa sürede size geri dönüş yapacağız.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContactInformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer
    

class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    

class WhyChooseUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer
    

class FrequentlyAskedQuestionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
    