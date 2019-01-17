from django.http import HttpResponse
from django.shortcuts import render

from utils.api.api import APIView


class UploadAdminAPI(APIView ):
    def post(self, request):
        # File=request.data['myfile']
        File = request.FILES['myfile']
        if File is None:
            return self.error("没有需要上传的文件")
        else:
            with open("./upload/temp_file/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
                f.close()
            return self.success("Upload over!")

    def get(self, request):
        return render(request, 'upload.html')
