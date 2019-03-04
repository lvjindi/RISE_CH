from aboutUs.models import AboutUs

from contact.models import Contact
from contact.serializers import ContactSerializer
from utils.api.api import APIView


class ContactDetailAPI(APIView):
    def get(self, request):
        data = request.data
        try:
            contact = Contact.objects.get(id=data['id'])
            views_number = contact.views_number + 1
            setattr(contact, 'views_number', views_number)
            contact.save()
            return self.success(ContactSerializer(contact).data)
        except Contact.DoesNotExist:
            return self.error('Contact does not exist')
