from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from account.decorators import super_admin_required
from index.models import SliderPicture, MessageFromDirector
from index.serializers import CreateSliderSerializer, SliderSerializer, EditSliderSerializer, CreateMessageSerializer, \
    MessageFromDrSerializer
from utils.api.api import APIView, validate_serializer


class SlideAdminAPI(APIView):
    # @validate_serializer(CreateSliderSerializer)
    @super_admin_required
    def post(self, request):
        "publish slide picture"
        data = request.data
        slide_picture = SliderPicture.objects.create(flag=data['flag'],
                                                     articleId=data['articleId'],
                                                     image=data['image'])
        return self.success(SliderSerializer(slide_picture).data)

    # @validate_serializer(EditSliderSerializer)
    @super_admin_required
    def put(self, request):
        "edit slider"
        data = request.data
        try:
            slider_pricture = SliderPicture.objects.get(id=data.pop['id'])
        except SliderPicture.DoesNotExist:
            return self.error("SliderPicture does not exist")
        for k, v in data.items():
            setattr(slider_pricture, k, v)
        slider_pricture.save()
        return self.success(SliderSerializer(slider_pricture).data)

    @super_admin_required
    def get(self, request):
        "get slider picture list"
        slider_id = request.Get.get('id')
        if slider_id:
            try:
                slider_picture = SliderPicture.objects.get(id=slider_id)
                return self.success(SliderPicture(slider_picture).data)
            except SliderPicture.DoesNotExist:
                return self.error("slider picture does not exist")
        slider_picture = SliderPicture.objects.all().order_by('-create_time')
        return self.success(self.paginate_data(request, slider_picture, SliderSerializer))

    # @super_admin_required
    def delete(self, request):
        if request.GET.get('id'):
            SliderPicture.objects.filter(id=request.GET['id']).delete()
        return self.success()


class DrMessageAdminAPI(APIView):
    # @validate_serializer(CreateMessageSerializer)
    @super_admin_required
    def post(self, request):
        "create message"
        data = request.data
        message = MessageFromDirector.objects.create(content=data['content'],
                                                     title=data['title'],
                                                     image=data['image'])
        return self.success(MessageFromDrSerializer(message).data)

    # @validate_serializer(MessageFromDrSerializer)
    @super_admin_required
    def put(self, request):
        "edit message"
        data = request.data
        try:
            message = MessageFromDirector.objects.get(id=data.pop['id'])
        except MessageFromDirector.DoesNotExist:
            return self.error('Message does not exits')
        for k, v in data.items:
            setattr(message, k, v)
        message.save()
        return self.success(MessageFromDrSerializer(message).data)

    @super_admin_required
    def get(self, request):
        message_id = request.GET.get('id')
        if message_id:
            try:
                message = MessageFromDirector.objects.get(id=message_id)
                return self.success(MessageFromDrSerializer(message).data)
            except MessageFromDirector.DoesNotExist:
                return self.error('Message does not exist')
        message = MessageFromDirector.objects.all()
        return self.success(self.paginate_data(request, message, MessageFromDrSerializer))

    @super_admin_required
    def delete(self, request):
        if request.GET.get('id'):
            MessageFromDirector.objects.filter(id=request.GET.get('id')).delete()
        return self.success()


class IndexAdminAPI(APIView):
    def get(self, request):
        return render(request, 'index.html')
