import logging
import os
from email.mime.image import MIMEImage
from os import path

from django.core import mail
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.template.loader import get_template

from Rise_CH import settings
from account.decorators import login_required, super_admin_required, auto_log
from leave.models import Leave
from leave.serializers import LeaveSerializer
from utils.api.api import APIView

logg = logging.getLogger('django')


def add_img(src, img_id):
    """
    在富文本邮件模板里添加图片
    :param src:
    :param img_id:
    :return:
    """
    fp = open(src, 'rb')
    msg_image = MIMEImage(fp.read())
    fp.close()
    msg_image.add_header('Content-ID', '<' + img_id + '>')
    return msg_image


class LeaveAdmin(APIView):
    @login_required
    def post(self, request):

        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            startTime = request.POST.get('startTime')
            endTime = request.POST.get('endTime')
            reason = request.POST.get('reason')
            leave = Leave.objects.create(name=name, email=email, startTime=startTime, endTime=endTime, reason=reason)
            emailTemplate = get_template('EmailTemplate.html')
            context = {
                'reason': reason,
                'startTime': startTime.replace('T', ' '),
                'endTime': endTime.replace('T', ' '),
                'id': leave.id,
            }
            path = os.getcwd()
            path_use = path.replace('\\', '/')
            title = name + " Ask For Leave"
            from_mail = settings.EMAIL_HOST_USER
            recipient_list = []
            recipient_list.extend(settings.EMAIL_RECEIVE_LEAVE_USER)
            html_content = emailTemplate.render(context)
            msg = mail.EmailMessage(title, html_content, from_mail, recipient_list)
            # image_agree = add_img(path_use + '/static/images/agree.png', 'test_cid1')
            # image_disagree = add_img(path_use + '/static/images/disagree.png', 'test_cid2')
            msg.content_subtype = 'html'
            msg.encoding = 'utf-8'
            # msg.attach(image_agree)
            # msg.attach(image_disagree)
            msg.send()
            return self.success("发送成功，请注意查收邮件回复")
        except ValidationError as e:
            logg.error('提交请假失败：' + str(e))
            return self.error(msg=str(e))
        except Exception as e:
            logg.error('提交请假失败：' + str(e))
            return self.error(msg=str(e))

    def get(self, request):
        leave_id = request.GET.get('id')
        if leave_id:
            try:
                leave = Leave.objects.get(id=leave_id)
                leave.status = leave.get_status_display()
                return self.success(LeaveSerializer(leave).data)
            except Leave.DoesNotExist:
                return self.error("Leave does not exist")
        else:
            leave = Leave.objects.all().order_by('id')
            for item in leave:
                item.status = item.get_status_display()
            return self.success(self.paginate_data(request, leave, LeaveSerializer))

    @super_admin_required
    def delete(self, request):
        leave_id = request.GET.get('id')
        if leave_id:
            leave = Leave.objects.get(id=leave_id)
            leave.delete()
            return self.success()


class ReplyAdmin(APIView):
    def post(self, request):
        leave_id = request.POST.get('id')
        status = request.POST.get('status')
        reply = request.POST.get('reply')
        title = "The Reply Of Asking For Leave"
        from_mail = settings.EMAIL_HOST_USER
        try:
            recipient = Leave.objects.get(id=leave_id)
            if recipient.status == 'agree' or recipient.status == 'disagree' or recipient.reply:
                return self.error("The request has been replied!")
            else:
                setattr(recipient, 'status', status)
                setattr(recipient, 'reply', reply)
                recipient.save()
                emailReplyTemplate = get_template('EmailReply.html')
                context = {
                    'name': recipient.name,
                    'time': recipient.create_time,
                    'status': status,
                    'reply': recipient.reply,
                }
                recipient_list = []
                recipient_list.extend(settings.EMAIL_RECEIVE_LEAVE_USER)
                recipient_list.append(recipient.email)
                html_content = emailReplyTemplate.render(context)
                msg = mail.EmailMessage(title, html_content, from_mail, recipient_list)
                msg.content_subtype = 'html'
                msg.encoding = 'utf-8'
                msg.send()
                return self.success("Send reply email successfully!")
        except Leave.DoesNotExist:
            return self.error("Leave does not exist")
        except Exception as e:
            logg.error("审批失败：" + str(e))


# class DisAgreeReplyAdmin(APIView):
#     def get(self, request):
#         leave_id = request.GET.get('id')
#         title = "The reply of asking for leave"
#         from_mail = settings.EMAIL_HOST_USER
#         try:
#             recipient = Leave.objects.get(id=leave_id)
#             setattr(recipient, 'status', '拒绝')
#             recipient.save()
#             recipient_email = recipient.email
#         except Leave.DoesNotExist:
#             return self.error("Leave does not exist")
#         content = 'Dear ' + recipient.name + ', your request for leave on ' + str(
#             recipient.create_time).replace('T', ' ') + ' has been rejected!'
#         recipient_list = settings.EMAIL_RECEIVE_REPLY_USER
#         recipient_list.append(recipient_email)
#         send_mail(title, content, from_mail, recipient_list, fail_silently=False)
#         return self.success("Send disagreed email successfully!")


class LeavePublic(APIView):
    def get(self, request):
        return render(request, 'leavePublic.html')


class LeaveManagement(APIView):
    def get(self, request):
        return render(request, 'leaveManagement.html')


class LeaveReply(APIView):
    def get(self, request):
        return render(request, 'leaveReply.html')
