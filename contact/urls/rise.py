from django.conf.urls import url


from contact.views.rise import ContactDetailAPI

urlpatterns = [
    url(r"^contact/?$", ContactDetailAPI.as_view(), name="contact_detail_list_api"),


]