from django.shortcuts import render

from account.decorators import super_admin_required, login_required
from contact.models import Contact
from contact.serializers import ContactSerializer
from utils.api.api import APIView


class ContactAdminAPI(APIView):
    # @validate_serializer(CreateConferenceSerializer)
    # @validate_serializer(CreateNewsSerializer)
    @super_admin_required
    def post(self, request):
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            contact = Contact.objects.create(title=title, content=content)
            contact.save()
            return self.success(ContactSerializer(contact).data)
        except Exception:
            return self.error("Error")

    # @validate_serializer(CreateConferenceSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            contact = Contact.objects.get(id=data['id'])
            setattr(contact, 'content', data['content'])
            setattr(contact, 'title', data['title'])

            contact.save()

            return self.success(ContactSerializer(contact).data)
        except Contact.DoesNotExist:
            return self.error("Contact does not exist")
        except Exception:
            return self.error("Error")

    @login_required
    def get(self, request):
        contact_id = request.GET.get('id')
        if contact_id:
            try:
                contact = Contact.objects.get(id=contact_id)
                return self.success(ContactSerializer(contact).data)
            except Contact.DoesNotExist:
                return self.error("Contact does not exist")
        else:
            contact = Contact.objects.all()
            return self.success(self.paginate_data(request, contact, ContactSerializer))

    @super_admin_required
    def delete(self, request):
        contact_id = request.GET.get('id')
        if contact_id:
            contact = Contact.objects.get(id=contact_id)
            contact.delete()
            return self.success()


class ContactManageAdminAPI(APIView):
    def get(self, request):
        return render(request, 'contactManagement.html')
