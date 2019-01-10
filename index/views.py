# # -*-coding:utf-8 -*-
# from index.models import SliderPicture, MessageFromDirector
# from index.serializers import SliderSerializer, MessageFromDrSerializer
# from utils.api.api import APIView
#
#
# class SliderImageAPI(APIView):
#     def get(self, request):
#         slider_image = SliderPicture.objects.all()
#         return self.success(self.paginate_data(request, slider_image, SliderSerializer))
#
#
# class MessageFromDrAPI(APIView):
#     def get(self, request):
#         message = MessageFromDirector.objects.all()
#         return self.success(self.paginate_data(request, message, MessageFromDrSerializer))
