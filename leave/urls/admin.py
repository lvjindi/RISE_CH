from django.conf.urls import url

from leave.views.admin import LeaveAdmin, LeavePublic, LeaveManagement, AgreeReplyAdmin, DisAgreeReplyAdmin

urlpatterns = [

    url(r"^leave/?$", LeaveAdmin.as_view(), name="leave_admin_api"),
    url(r"^leave/agree/?$", AgreeReplyAdmin.as_view(), name="leave_agree_admin_api"),
    url(r"^leave/disagree/?$", DisAgreeReplyAdmin.as_view(), name="leave_disagree_admin_api"),
    url(r"^leave_public/?$", LeavePublic.as_view(), name="leave_public_api"),
    url(r"^leave_management/?$", LeaveManagement.as_view(), name="leave_management_api"),

]
