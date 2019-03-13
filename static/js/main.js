function DisplaySecond() {
    var x;
    var getLi;
    x = document.getElementById("secondTile");

    getLi = document.getElementById("secondTile").getElementsByTagName("li");
    for (i = 0; i < 5; i++) {
        getLi[i].style.background = "white";
    }
    if (x.style.display == "block") {

        x.style.display = "none";

    }
    else {
        x.style.background = "white";
        x.style.display = "block";
    }


};

function DisplayThird() {

    var x;
    var getLi;
    x = document.getElementById("thirdTile");
    getLi = document.getElementById("thirdTile").getElementsByTagName("li");
    for (i = 0; i < 2; i++) {
        getLi[i].style.background = "white";
    }
    if (x.style.display == "block") {

        x.style.display = "none";
    }
    else {
        x.style.background = "white";
        x.style.display = "block";
    }


};

function showConference(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    var domesticUrl = 'http://39.105.199.229:8000/api/admin/conference?type=domestic';
    var foreignUrl = 'http://39.105.199.229:8000/api/admin/conference?type=foreign';
    var allUrl = 'http://39.105.199.229:8000/api/admin/conference';
    var conferenceUrl;
    if (option == '1') {
        conferenceUrl = domesticUrl;
    }
    if (option == '2') {
        conferenceUrl = foreignUrl;
    }
    if (option == '3') {
        conferenceUrl = allUrl;
    }

    if (option != '4') {
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%"> ' +
            '<thead>' +
            '            <tr>' +
            '                <th>序号</th>' +
            '                <th>标题</th>' +
            '                <th>类别</th>' +
            '                <th>新闻ID</th>' +
            '                <th>发布日期</th>' +
            '                <th>点击</th>' +
            '                <th>管理</th>' +
            '            </tr>' +
            '</thead>' +
            '        </table>'
        $("#MainRight").append(table)
        $.ajax({
            type: 'GET',
            url: conferenceUrl,
            data: '',
            contentType: false,
            processData: false,
            //jsonpCallback: 'callback',
            success: function (data) {
                console.log(data)
                if (data.error) {
                    alert(data.error)
                }
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].type + '</td>' + '<td>' + data[i].news_id + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="news_edit(\'' + data[i].id + '\')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="news_delete(' + data[i].id + ')">删除</a>' + '</td>'
                    $("#tableStyle").append('<tr>' + tr + '</tr>')
                }
            },
            error: function (data) {
                alert(data)
            },
        })

    }
}

function peopleAdminCheck() {
    $.ajax({
        url: "http://39.105.199.229:8000/api/admin/checkAdmin",
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                str = '<select name="conferenceType" id="conferenceType" onchange="showPeopleAdmin(this.value)" style="margin-left: 30px">\n' +
                    '            <option value="7">请选择成员类别</option>\n' +
                    '            <option value="6">全部</option>\n' +
                    '            <option value="5">特聘教授</option>\n' +
                    '            <option value="4">科研人员</option>\n' +
                    '            <option value="3">本科生</option>\n' +
                    '            <option value="2">研究生</option>\n' +
                    '            <option value="1">博士生</option>\n' +
                    '        </select>';
                $('#MainRight').append(str)

            } else {

                $.ajax({
                    url: "http://39.105.199.229:8000/api/admin/people",
                    type: 'GET',
                    contentType: false,
                    processData: false,
                    success: function (data) {
                        console.log(data)
                        var table = '';
                        table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%">' +
                            '<thead>' +
                            '            <tr>' +
                            '                <th>序号</th>' +
                            '                <th>姓名</th>' +
                            '                <th>类别</th>' +
                            '                <th>发布日期</th>' +
                            '                <th>管理</th>' +
                            '            </tr>' +
                            '</thead>' +
                            '        </table>';
                        $("#MainRight").append(table);
                        for (i = 0; i < data.length; i++) {
                            var tr;
                            tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].name + '</td>' + '<td>' + data[i].user_category + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="people_edit(\'' + data[i].id + '\')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="news_delete(\'' + data[i].id + '\')">删除</a>' + '</td>'
                            $("#tableStyle").append('<tr>' + tr + '</tr>')
                        }


                    },
                    error: function (data) {
                        alert("获取数据失败！")

                    }


                })
            }
        }
    })

}

function showStudent(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    if (document.getElementById('studentType')) {
        obj.removeChild(document.getElementById('studentType'));
    }
    if (option == 'student') {
        str = '<select name="studentType" id="studentType"  style="margin-left: 30px">\n' +
            '            <option value="undergraduate">本科生</option>\n' +
            '            <option value="master">研究生</option>\n' +
            '            <option value="doctor">博士生</option>\n' +
            '        </select><br>' +
            '<span>入学时间</span><input type="date" name="enrollmentTime" id="enrollmentTime" style="margin-top: 20px" ><br>' +
            '<span>毕业时间</span><input type="date" name="graduationTime" id="graduationTime" style="margin-top: 20px"><br>';
        $('#selectPart').append(str)
    }

}


function showPeopleAdmin(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    if (document.getElementById('studentType')) {
        obj.removeChild(document.getElementById('studentType'));
    }
    var staffUrl = 'http://39.105.199.229:8000/api/admin/people?type=staff';
    var undergraduateUrl = 'http://39.105.199.229:8000/api/admin/people?type=undergraduate';
    var masterUrl = 'http://39.105.199.229:8000/api/admin/people?type=master';
    var doctorUrl = 'http://39.105.199.229:8000/api/admin/people?type=doctor';
    var professorUrl = 'http://39.105.199.229:8000/api/admin/people?type=adjunctProfessor';
    var allUrl = 'http://39.105.199.229:8000/api/admin/people';
    var peopleUrl;
    if (option == '1') {
        peopleUrl = doctorUrl;
    }
    if (option == '2') {
        peopleUrl = masterUrl;
    }
    if (option == '3') {
        peopleUrl = undergraduateUrl;
    }
    if (option == '4') {
        peopleUrl = staffUrl;
    }

    if (option == '5') {
        peopleUrl = professorUrl;
    }
    if (option == '6') {
        peopleUrl = allUrl;
    }
    if (option != '7') {
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%">' +
            '<thead>' +
            '            <tr>' +
            '                <th>序号</th>' +
            '                <th>姓名</th>' +
            '                <th>类别</th>' +
            '                <th>发布日期</th>' +
            '                <th>管理</th>' +
            '            </tr>' +
            '</thead>' +
            '        </table>'
        $("#MainRight").append(table)
        $.ajax({
            type: 'GET',
            url: peopleUrl,
            data: '',
            contentType: false,
            processData: false,
            //jsonpCallback: 'callback',
            success: function (data) {
                console.log(data)
                if (data.error) {
                    alert(data.error)
                }
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].name + '</td>' + '<td>' + data[i].user_category + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="people_edit(\'' + data[i].id + '\')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="news_delete(\'' + data[i].id + '\')">删除</a>' + '</td>'
                    $("#tableStyle").append('<tr>' + tr + '</tr>')
                }
            },
            error: function (data) {

                alert(data);
            },
        })

    }
}

function staffPublic() {
    var formData = new FormData();
    var url = 'http://39.105.199.229:8000/api/admin/people/staff';
    formData.append('name', $('#name').val());
    formData.append('img', document.getElementById('image').files[0]);
    formData.append('status', $('#status').val());
    formData.append('office', $('#office').val());
    formData.append('phone', $('#phone').val());
    formData.append('email', $('#email').val());
    formData.append('position', $('#position').val());
    formData.append('degree', $('#degree').val());
    formData.append('professionalTitle', $('#professionalTitle').val());
    formData.append('profession ', $('#profession ').val());
    formData.append('area', $('#area').val());
    formData.append('interesting', interesting.getContent());
    formData.append('biography', biography.getContent());
    formData.append('project', project.getContent());
    formData.append('achievement', achievement.getContent());
    formData.append('activity', activity.getContent());
    formData.append('publication', publication.getContent());
    formData.append('report', report.getContent());
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            location.reload("http://39.105.199.229:8000/api/admin/people/staff_management")
            if (data.error) {
                alert(data.error)
            }
            else {
                console.log(data)
                alert("发布成功")
            }

        },
        error: function (xhr, type) {
            alert("发布失败")
        }
    })

}

function leavePublic() {
    var formData = new FormData;
    var url = 'http://39.105.199.229:8000/api/admin/leave';
    formData.append('name', $('#name').val());
    formData.append('startTime', $('#startTime').val());
    formData.append('endTime', $('#endTime').val());
    formData.append('email', $('#email').val());
    formData.append('reason', reason.getContentTxt());

    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            alert("发送成功")
            console.log(data)

        },
        error: function () {
            alert("发送失败")
        }
    })


}

function adjunctProfessorPublic() {
    var formData = new FormData();
    var url = 'http://39.105.199.229:8000/api/admin/people/adjunctProfessor';
    formData.append('name', $('#name').val());
    formData.append('img', document.getElementById('image').files[0]);
    formData.append('email', $('#email').val());
    formData.append('position', $('#position').val());
    formData.append('degree', $('#degree').val());
    formData.append('professionalTitle', $('#professionalTitle').val());
    formData.append('area', $('#area').val());
    formData.append('link', $('#link').val());
    formData.append('biography', biography.getContent());
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            location.reload("http://39.105.199.229:8000/api/admin/people/adjunctProfessor_management")
            if (data.error) {
                alert(data.error)
            }
            else {
                console.log(data)
                alert("发布成功")
            }
        },
        error: function (xhr, type) {
            alert("发布失败")
        }
    })

}

function superiorInfo() {
    var result;
    $.ajax({
            type: 'GET',
            url: 'http://39.105.199.229:8000/api/admin/people/staff',
            async: false,
            success: function (data) {
                console.log(data)
                result = data
            },
            error: function () {
                console.log("获取导师首页连接失败")
            },

        }
    );
    return result;

}

function studentPublic() {
    var formData = new FormData();
    var url = 'http://39.105.199.229:8000/api/admin/people/student';
    var supervisorLinkUrl = 'http://39.105.199.229:8000/api/admin/people/staff';
    var supervisorLink;
    var superiorData;
    formData.append('name', $('#name').val());
    formData.append('img', document.getElementById('image').files[0]);
    formData.append('email', $('#email').val());
    formData.append('enrollmentTime', $('#enrollmentTime').val());
    formData.append('graduationTime', $('#graduationTime').val());
    formData.append('graduateStatus', $('#graduateStatus').val());
    formData.append('type', $('#type').val());
    formData.append('supervisor', $('#supervisor').val());
    if ($('#supervisor').val()) {
        superiorData = new superiorInfo();
        for (i = 0; i < superiorData.length; i++) {
            if (superiorData[i].name == $('#supervisor').val()) {
                supervisorLink = supervisorLinkUrl + "?id=" + superiorData[i].id;
                document.getElementById('supervisorLink').value = supervisorLinkUrl;
                break;
            }
            else {
                supervisorLink = ''
            }
        }
    }
    formData.append('area', $('#area').val());
    formData.append('supervisorLink', supervisorLink);
    formData.append('biography', biography.getContent());
    formData.append('project', project.getContent());
    formData.append('activity', activity.getContent());
    formData.append('publication', publication.getContent());
// setTimeout(formData.append('supervisorLink ', document.getElementById('supervisorLink ').value), 200)

    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            location.reload('http://39.105.199.229:8000/api/admin/people/student_management');
            console.log(data);
            alert("发布成功")

        },
        error: function () {
            alert("发布失败")
        }
    })

}

function sliderPublic() {
    var url = 'http://39.105.199.229:8000/api/admin/index/slider';
    var formData = new FormData();
    formData.append('image', document.getElementById('indexImage').files[0]);
    formData.append('articleId', $('#articleID').val());
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            if (data.error) {
                alert(data.error)
            }
            else {
                location.reload("http://39.105.199.229:8000/api/admin/index/slider_management");
                console.log(data);
                alert("发布成功");
            }
        },
        error: function (xhr, type) {
            alert("发布失败")
        }
    })
}

function messagePublic() {
    var url = 'http://39.105.199.229:8000/api/admin/index/message';
    var formData = new FormData();
    formData.append('image', document.getElementById('image').files[0]);
    formData.append('title', $('#articleTitle').val());
    formData.append('content', ue.getContent());
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            if (data.error) {
                alert(data.error)
            }
            else {
                location.reload("http://39.105.199.229:8000/api/admin/index/message_management")
                console.log(data)
                alert("发布成功")
            }
        },
        error: function (xhr, type) {
            alert("发布失败")
        }
    })
}

function newsPublic() {
    var url;
    var formData = new FormData();
    if (document.getElementById('type').value == 'news') {
        url = 'http://39.105.199.229:8000/api/admin/news';

        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'seminar') {
        url = 'http://39.105.199.229:8000/api/admin/seminar';
        formData.append('subType', $('#subSelect').val());
        formData.append('time', $('#time').val());
        formData.append('place', $('#place').val());
        formData.append('speaker', $('#speaker').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'conference') {
        url = 'http://39.105.199.229:8000/api/admin/conference';
        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'exchange') {
        url = 'http://39.105.199.229:8000/api/admin/exchange';
        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'research') {
        if ($('#subSelect').val() == 'introduction') {
            url = 'http://39.105.199.229:8000/api/admin/introduction';
            formData.append('subType', $('#subSelect').val());
            formData.append('title', $('#articleTitle').val());
            formData.append('content', ue.getContent());
        }
        if ($('#subSelect').val() == 'project') {
            url = 'http://39.105.199.229:8000/api/admin/project';
            formData.append('subType', $('#subSelect').val());
            formData.append('title', $('#articleTitle').val());
            formData.append('author', $('#author').val());
            formData.append('code', $('#code').val());
            formData.append('fund', $('#fund').val());
            formData.append('schedule', $('#schedule').val());
            formData.append('abstract', $('#abstract').val());
            formData.append('keywords', $('#keywords').val());
            formData.append('other', $('#other').val());
        }
        if ($('#subSelect').val() == 'publication') {
            url = 'http://39.105.199.229:8000/api/admin/publication';
            formData.append('subType', $('#subSelect').val());
            formData.append('title', $('#articleTitle').val());
            formData.append('author', $('#author').val());
            formData.append('place', $('#place').val());
            formData.append('year', $('#year').val());
            formData.append('other', $('#other').val());
        }
        if ($('#subSelect').val() == 'report') {
            url = 'http://39.105.199.229:8000/api/admin/report';
            formData.append('subType', $('#subSelect').val());
            formData.append('title', $('#articleTitle').val());
            formData.append('author', $('#author').val());
            formData.append('time', $('#time').val());
            formData.append('pdf', document.getElementById('pdf').files[0]);
            formData.append('place', $('#place').val());
            formData.append('year', $('#year').val());
            formData.append('other', $('#other').val());
        }

    }
    if (document.getElementById('type').value == 'join') {
        url = 'http://39.105.199.229:8000/api/admin/join';
        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'aboutUs') {
        url = 'http://39.105.199.229:8000/api/admin/aboutUs';
        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    if (document.getElementById('type').value == 'contact') {
        url = 'http://39.105.199.229:8000/api/admin/contact';
        formData.append('subType', $('#subSelect').val());
        formData.append('title', $('#articleTitle').val());
        formData.append('content', ue.getContent());
    }
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        // jsonpCallback: 'callback',
        success: function (data) {
            if (data.error) {
                alert(data.error)
            }
            else {
                console.log(data)
                location.replace(location.href);
                alert("发布成功")
            }
        },
        error: function (xhr, type) {
            alert("发布失败")
        }
    })


}

function showExchange(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    var missionUrl = 'http://39.105.199.229:8000/api/admin/exchange?type=mission';
    var visitorUrl = 'http://39.105.199.229:8000/api/admin/exchange?type=visitor';
    var allUrl = 'http://39.105.199.229:8000/api/admin/exchange';
    var exchangeUrl;
    if (option == '1') {
        exchangeUrl = visitorUrl;//来访
    }
    if (option == '2') {
        exchangeUrl = missionUrl;//出访
    }
    if (option == '3') {
        exchangeUrl = allUrl;
    }

    if (option != '4') {
        var table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%">' +
            '<thead>' +
            '            <tr>' +
            '                <th>序号</th>' +
            '                <th>标题</th>' +
            '                <th>类别</th>' +
            '                <th>新闻ID</th>' +
            '                <th>发布日期</th>' +
            '                <th>点击</th>' +
            '                <th>管理</th>' +
            '            </tr>' +
            '</thead>' +
            '        </table>'
        $("#MainRight").append(table)
        $.ajax({
            type: 'GET',
            url: exchangeUrl,
            data: '',
            contentType: false,
            processData: false,
            //jsonpCallback: 'callback',
            success: function (data) {
                console.log(data)
                if (data.error) {
                    alert(data.error)
                }
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].type + '</td>' + '<td>' + data[i].news_id + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="news_edit(\'' + data[i].id + ' \')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="news_delete(' + data[i].id + ')">删除</a>' + '</td>'
                    $("#tableStyle").append('<tr>' + tr + '</tr>')
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status);
                alert(XMLHttpRequest.readyState);
                alert(textStatus);
            },
        })

    }
}

function showResearch(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    var introductionUrl = 'http://39.105.199.229:8000/api/admin/introduction';
    var projectUrl = 'http://39.105.199.229:8000/api/admin/project';
    var publicationUrl = 'http://39.105.199.229:8000/api/admin/publication';
    var reportUrl = 'http://39.105.199.229:8000/api/admin/report';
    var researchUrl;
    if (option == '1') {
        researchUrl = introductionUrl;
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%">' +
            '<thead>' +
            '            <tr>' +
            '                <th>序号</th>' +
            '                <th>标题</th>' +
            '                <th>发布日期</th>' +
            '                <th>点击</th>' +
            '                <th>管理</th>' +
            '            </tr>' +
            '</thead>' +
            '        </table>'
        $("#MainRight").append(table)
        $.ajax({
            type: 'GET',
            url: researchUrl,
            data: '',
            contentType: false,
            processData: false,
            //jsonpCallback: 'callback',
            success: function (data) {
                console.log(data)
                if (data.error) {
                    alert(data.error)
                }
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="news_edit(\'' + data[i].id + '\')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="research_delete(\'' + researchUrl + '\',\'' + data[i].id + '\')">删除</a>' + '</td>'
                    $("#tableStyle").append('<tr>' + tr + '</tr>')
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status);
                alert(XMLHttpRequest.readyState);
                alert(textStatus);
            },
        })
    }
    if (option == '2') {
        researchUrl = projectUrl;
    }
    if (option == '3') {
        researchUrl = publicationUrl;
    }
    if (option == '4') {
        researchUrl = reportUrl;
    }
    if (option != '5' && option != '1') {
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle" style="margin: 20px 20px 0px 30px;width: 95%">' +
            '<thead>' +
            '            <tr>' +
            '                <th>序号</th>' +
            '                <th>标题</th>' +
            '                <th>作者</th>' +
            '                <th>发布日期</th>' +
            '                <th>管理</th>' +
            '            </tr>' +
            '</thead>' +
            '        </table>'
        $("#MainRight").append(table)
        $.ajax({
            type: 'GET',
            url: researchUrl,
            data: '',
            contentType: false,
            processData: false,
            //jsonpCallback: 'callback',
            success: function (data) {
                console.log(data)
                if (data.error) {
                    alert(data.error)
                }
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].author + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + '<a href="#" class="addUnderline" onclick="research_edit(\'' + researchUrl + '\',\'' + data[i].id + '\')">编辑</a>&nbsp&nbsp<a href="#" class="addUnderline" onclick="research_delete(\'' + researchUrl + '\',\' ' + data[i].id + '\')">删除</a>' + '</td>'
                    $("#tableStyle").append('<tr>' + tr + '</tr>')
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status);
                alert(XMLHttpRequest.readyState);
                alert(textStatus);
            },
        })

    }
}

function showSubclass(val) {

    var option = val;

    var obj = document.getElementById('selectPart')
    if (document.getElementById('subSelect')) {
        obj.removeChild(document.getElementById('subSelect'))
    }

    if (option == 'conference') {

        var subSelect = ' <select id="subSelect" name="subSelect">\n' +
            '                    <option value="domestic">国内会议</option>\n' +
            '                    <option value="foreign">国外会议</option>\n' +
            '                </select>';

        $("#selectPart").append(subSelect)

    }
    if (option == 'exchange') {
        var subSelect = ' <select id="subSelect" name="subSelect">\n' +
            '                    <option value="mission">出访</option>\n' +
            '                    <option value="visitor">来访</option>\n' +
            '                </select>';
        $("#selectPart").append(subSelect)
    }
    if (option == 'seminar') {
        if (document.getElementById('subForm')) {
            var par = document.getElementById('subForm').parentNode;
            par.removeChild(document.getElementById('subForm'));
        }
        var subformstr = ' <div id="subForm">\n' +
            '                    <span>时间</span><input type="date" name="time" id="time"><br>\n' +
            '                    <span>地点</span><input type="text" name="place" id="place"><br>\n' +
            '                    <span>讲者</span><input type="text" name="speaker" id="speaker"><br>\n' +
            '                </div>';
        $('#subform').append(subformstr)


    }
    if (option == 'research') {
        var subSelect = ' <select id="subSelect" name="subSelect" onchange="showResearchPart(this.value)">\n' +
            '                    <option value="introduction">研究介绍</option>\n' +
            '                    <option value="project">研究项目</option>\n' +
            '                    <option value="publication">研究论文</option>\n' +
            '                    <option value="report">研究报告</option>\n' +
            '                </select>';
        $("#selectPart").append(subSelect)

    }
}


function showResearchPart(val) {
    var option = val;
    if (document.getElementById('subForm')) {
        var par = document.getElementById('subForm').parentNode;
        par.removeChild(document.getElementById('subForm'))
    }
    if (document.getElementById('lable') && document.getElementById('editor')) {
        var obj = document.getElementById('lable').parentNode;
        obj.removeChild(document.getElementById('lable'));
        obj.removeChild(document.getElementById('editor'));
    }
    if (option == 'project') {

        var subformstr = ' <div id="subForm">\n' +
            '                    <span>作者</span><input type="text" name="author" id="author"><br>\n' +
            '                    <span>项目编码</span><input type="text" name="code" id="code"><br>\n' +
            '                    <span>项目基金</span><input type="text" name="fund" id="fund"><br>\n' +
            '                    <span>项目期限</span><input type="text" name="schedule" id="schedule"><br>\n' +
            '                    <span>摘要</span><input type="text" name="abstract" id="abstract"><br>\n' +
            '                    <span>关键字</span><input type="text" name="keywords" id="keywords"><br>\n' +
            '                    <span>其他</span><input type="text" name="other" id="other"><br>\n' +
            '                </div>';
        $('#subform').append(subformstr)
    }
    if (option == 'publication') {

        var subformstr = ' <div id="subForm">\n' +
            '                    <span>作者</span><input type="text" name="author" id="author"><br>\n' +
            '                    <span>详细期刊及事件</span><input type="text" name="place" id="place"><br>\n' +
            '                    <span>发表年限</span><input type="text" name="year" id="year"><br>\n' +
            '                    <span>其他</span><input type="text" name="other" id="other"><br>\n' +
            '                </div>';
        $('#subform').append(subformstr)
    }
    if (option == 'report') {

        var subformstr = ' <div id="subForm">\n' +
            '                    <span>作者</span><input type="text" name="author" id="author"><br>\n' +
            '                    <span>报告地点</span><input type="text" name="place" id="place"><br>\n' +
            '                    <span>报告时间</span><input type="text" name="time" id="time"><br>\n' +
            '                    <span>报告年限</span><input type="text" name="year" id="year"><br>\n' +
            '                    <span>相关文档</span><input type="file" name="pdf" id="pdf"><br>\n' +
            '                    <span>其他</span><input type="text" name="other" id="other"><br>\n' +
            '                </div>';
        $('#subform').append(subformstr)
    }
}

function news_delete(id) {
    var url = window.location.href;
    var managementIndex = url.indexOf('management');
    url = url.substr(0, managementIndex - 1);
    url = url + '?id=' + id;
    if (confirm("确定要删除吗？")) {
        $.ajax({
            url: url,
            type: 'DELETE',
            dataType: 'json',
            success: function (data) {
                alert('删除成功');
                location.reload()
            },
            error: function () {
                alert('删除失败')

            }
        });
    }

}

function user_delete(id) {
    var url = "http://39.105.199.229:8000/api/admin/change_role"
    url = url + '?id=' + id;
    if (confirm("确定要删除吗？")) {
        $.ajax({
            url: url,
            type: 'DELETE',
            dataType: 'json',
            success: function (data) {
                if (data.error) {
                    alert(data.error);
                }
                alert('删除成功');
                location.reload()
            },
            error: function () {
                alert('删除失败')

            }
        });
    }

}

function people_edit(id) {
    var str;
    var url = window.location.href;
    var urltype = url.split('/');
    var peopletype = urltype[urltype.length - 1]
    var managementIndex = url.indexOf('management');
    url = url.substr(0, managementIndex - 1);
    url = url + '?id=' + id;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            //删除展示数据的表格
            var tb = document.getElementById("tableStyle");
            var rowNum = tb.rows.length;
            for (i = 0; i < rowNum; i++) {
                tb.deleteRow(i);
                rowNum = rowNum - 1;
                i = i - 1;
            }
            if (peopletype.startsWith('staff')) {
                str = ' <form id="peopleForm" method="post" style="margin-left: 50px;margin-top: 20px">\n' +
                    '                <span>姓名</span><input type="text" name="name" id="name" value=\'' + data.name + '\'><br>\n' +
                    '                <span>状态</span>\n' +
                    '                <select id="status" name="status" >\n' +
                    '                    <option value="1">在职</option>\n' +
                    '                    <option value="0">不在职</option>\n' +
                    '                </select>\n' +
                    '<br>\n' +
                    '                <span>办公室</span><input type="text" name="office" id="office" style="margin-top: 20px" value=\'' + data.office + '\'><br>\n' +
                    '                <span>电话</span><input type="text" name="phone" id="phone" style="margin-top: 20px" value=\'' + data.phone + '\'><br>\n' +
                    '                <span>邮箱</span><input type="text" name="email" id="email" style="margin-top: 20px" value=\'' + data.email + '\'><br>\n' +
                    '                <span>职位</span><input type="text" name="position" id="position" style="margin-top: 20px" value=\'' + data.position + '\' placeholder="中心主任/助理教授/主任助理/博士后"><br>\n' +
                    '                <span>学位</span><input type="text" name="degree" id="degree" style="margin-top: 20px" value=\'' + data.degree + '\'  placeholder="本科/硕士/博士/FBCS(可多选)"><br>\n' +
                    '                <span>职称</span><input type="text" name="professionalTitle" id="professionalTitle" placeholder="教授/副教授/讲师"\n' +
                    '                                      style="margin-top: 20px" value=\'' + data.professionalTitle + '\'><br>\n' +
                    ' <span>导师类型</span><input type="text" id="profession" name="profession" style="margin-top: 20px"\n' +
                    '                                        placeholder="博士导师/硕士导师（可多选）" value=\'' + data.profession + '\' ><br>' +
                    '                <span>研究领域</span><input type="text" name="area" id="area" style="margin-top: 20px" value=\'' + data.area + '\'><br>\n' +
                    '                <div id="" style="margin-top: 20px" ></div>\n' +
                    '                <span>研究兴趣</span>\n' +
                    '                <div id="interesting" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="interesting">\n' +
                    '                </div>\n' +
                    '                <span>个人简介</span>\n' +
                    '                <div id="biography" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="biography">\n' +
                    '                </div>\n' +
                    '                <span>研究项目</span>\n' +
                    '                <div id="project" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="project">\n' +
                    '                </div>\n' +
                    '                <span>成就</span>\n' +
                    '                <div id="achievement" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="achievement">\n' +
                    '                </div>\n' +
                    '                <span>活动</span>\n' +
                    '                <div id="activity" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="activity">\n' +
                    '                </div>\n' +
                    '                <span>论文</span>\n' +
                    '                <div id="publication" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="publication">\n' +
                    '                </div>\n' +
                    '                <span>报告</span>\n' +
                    '                <div id="report" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="report">\n' +
                    '                </div>\n' +
                    '                <script type="text/javascript">\n' +

                    '                    var interestingUE = UE.getEditor(\'interesting\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            setTimeout(function () {\n' +
                    '                interestingUE.setContent(\'' + data.interesting + '\')\n' +
                    '            }, 300);' +
                    '                    var biographyUE = UE.getEditor(\'biography\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer2 = setTimeout(function () {\n' +
                    '                biographyUE.setContent(\'' + data.biography + '\');\n' +
                    '            }, 200);' +
                    '                    var projectUE = UE.getEditor(\'project\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer3 = setTimeout(function () {\n' +
                    '                projectUE.setContent(\'' + data.project + '\');\n' +
                    '            }, 200);' +
                    '                    var achievementUE = UE.getEditor(\'achievement\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer4 = setTimeout(function () {\n' +
                    '                achievementUE.setContent(\'' + data.achievement + '\');\n' +
                    '            }, 200);' +
                    '                    var activityUE = UE.getEditor(\'activity\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer5 = setTimeout(function () {\n' +
                    '                activityUE.setContent(\'' + data.activity + '\');\n' +
                    '            }, 200);' +
                    '                    var publicationUE = UE.getEditor(\'publication\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer6 = setTimeout(function () {\n' +
                    '                publicationUE.setContent(\'' + data.publication + '\');\n' +
                    '            }, 200);' +
                    '                    var reportUE = UE.getEditor(\'report\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer7 = setTimeout(function () {\n' +
                    '                reportUE.setContent(\'' + data.report + '\');\n' +
                    '            }, 200);' +
                    '                </script>\n' +

                    '\n' +
                    '\n' +
                    '                <div id="subform"></div>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="staffEditSubmit( \'' + url + '\',\'' + id + '\')">\n' +
                    '\n' +
                    '            </form>';
            }
            if (peopletype.startsWith('student')) {
                str = ' <form id="peopleForm" method="post" action="/"  style="margin-left: 50px;margin-top: 20px">\n' +
                    '                <span>姓名</span><input type="text" name="name" id="name" value=\'' + data.name + '\'><br>\n' +
                    '                <span>邮箱</span><input type="text" name="email" id="email" style="margin-top: 20px" value=\'' + data.email + '\'><br>\n' +
                    '                <span>学生状态</span>\n' +
                    '                <select id="graduateStatus" name="graduateStatus">\n' +
                    '                    <option value="postgraduate" selected="selected">在读</option>\n' +
                    '                    <option value="graduate">毕业</option>\n' +
                    '                </select>\n' +
                    '                <br>\n' +
                    '                <span>研究领域</span><input type="text" name="area" id="area" style="margin-top: 20px" value=\'' + data.area + '\'><br>\n' +
                    '                <div id="" style="margin-top: 20px"></div>\n' +
                    '                <span>个人简介</span>\n' +
                    '                <div id="biography" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="biography">\n' +
                    '                </div>\n' +
                    '                <span>研究项目</span>\n' +
                    '                <div id="project" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="project">\n' +
                    '                </div>\n' +
                    '\n' +
                    '                <span>活动</span>\n' +
                    '                <div id="activity" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="activity">\n' +
                    '                </div>\n' +
                    '                <span>论文</span>\n' +
                    '                <div id="publication" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="publication">\n' +
                    '                </div>\n' +
                    '\n' +
                    '                <script type="text/javascript">\n' +

                    '                    var biographyUE = UE.getEditor(\'biography\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer2 = setTimeout(function () {\n' +
                    '                biographyUE.setContent(\'' + data.biography + '\');\n' +
                    '            }, 200);' +
                    '                    var projectUE = UE.getEditor(\'project\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer3 = setTimeout(function () {\n' +
                    '                projectUE.setContent(\'' + data.project + '\');\n' +
                    '            }, 200);' +

                    '                    var activityUE = UE.getEditor(\'activity\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer5 = setTimeout(function () {\n' +
                    '                activityUE.setContent(\'' + data.activity + '\');\n' +
                    '            }, 200);' +
                    '                    var publicationUE = UE.getEditor(\'publication\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '            var timer6 = setTimeout(function () {\n' +
                    '                publicationUE.setContent(\'' + data.publication + '\');\n' +
                    '            }, 200);' +

                    '                </script>\n' +

                    '\n' +
                    '\n' +
                    '                <div id="subform"></div>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="studentEditSubmit( \'' + url + '\',\'' + id + '\')">\n' +
                    '\n' +
                    '            </form>';
            }
            if (peopletype.startsWith('adjunctProfessor')) {
                str = ' <form id="peopleForm" method="post" action="/" style="margin-left: 50px;margin-top: 20px">\n' +
                    '                <span>姓名</span><input type="text" name="name" id="name" value=\'' + data.name + '\'><br>\n' +
                    '                <span>邮箱</span><input type="text" name="email" id="email" style="margin-top: 20px" value=\'' + data.email + '\'><br>\n' +
                    '                <span>学位</span><input type="text" name="degree" id="degree" style="margin-top: 20px"\n' +
                    '                                      placeholder="本科/硕士/博士/FBCS(可多选)" value=\'' + data.degree + '\'/><br>\n' +
                    '                <span>职称</span><input type="text" name="professionalTitle" id="professionalTitle"\n' +
                    '                                      style="margin-top: 20px" placeholder="教授/副教授/讲师" value=\'' + data.professionalTitle + '\'><br>\n' +
                    '                <span>主页链接</span>\n' +
                    '                <input type="text" name="link" id="link" style="margin-top: 20px" placeholder="http://..." value=\'' + data.link + '\'><br>\n' +
                    '                <span>研究领域</span><input type="text" name="area" id="area" style="margin-top: 20px" value=\'' + data.area + '\'><br><br>\n' +
                    '                <span>个人简介</span>\n' +
                    '                <div id="biography" type="text/plain"\n' +
                    '                     style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                    '                     name="biography">\n' +
                    '                </div>\n' +
                    '\n' +
                    '\n' +
                    '                <script type="text/javascript">\n' +
                    '                var biographyUE = UE.getEditor(\'biography\', {\n' +
                    '                        serverUrl: "/api/controller/"\n' +
                    '                    });//实例化编辑\n' +
                    '                var timer2 = setTimeout(function () {\n' +
                    '                biographyUE.setContent(\'' + data.biography + '\');\n' +
                    '            }, 200);' +
                    '                </script>\n' +
                    '                <div id="subform"></div>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="adjunctProfessorEditSubmit( \'' + url + '\',\'' + id + '\')">\n' +
                    '\n' +
                    '            </form>';
            }
            $('#MainRight').html(str)
        }

    })
}

function user_edit(id) {

    var str;
    var url = "http://39.105.199.229:8000/api/admin/change_role";
    url = url + '?id=' + id;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            //删除展示数据的表格
            if (data.error) {
                alert(data.error)
            }
            var tb = document.getElementById("tableStyle");
            var rowNum = tb.rows.length;
            for (i = 0; i < rowNum; i++) {
                tb.deleteRow(i);
                rowNum = rowNum - 1;
                i = i - 1;
            }
            str = '<form name="userEditForm" method="post" style="margin-left: 50px;margin-top: 20px">\n' +
                '        <p>\n' +
                '            <label for="id_email">邮箱：</label>\n' +
                '            <input type="text" id="email" placeholder="邮箱" name="email" value=\'' + data.email + '\'>\n' +
                '        </p>\n' +
                '        <br>\n' +
                '        <p>\n' +
                '            <label for="id_real_name">真实姓名：</label>\n' +
                '            <input type="text" id="real_name" placeholder="真实姓名" name="real_name" value=\'' + data.real_name + '\'>\n' +
                '        </p>\n' +
                '        <br>\n' +
                '        <p>\n' +
                '            <label for="id_user_category">身份：</label>\n' +
                '            <select id="user_category" name="user_category">\n' +
                '                <option value="staff">工作人员</option>\n' +
                '                <option value="student" selected="selected">学生</option>\n' +
                '                <option value="adjunctProfessor">兼职教授</option>\n' +
                '            </select>\n' +
                '        </p>\n' +
                '        <br>\n' +
                '        <p>\n' +
                '            <label for="id_role_type">角色：</label>\n' +
                '            <select id="role_type" name="role_type">\n' +
                '                <option value="Super Admin">超级管理员</option>\n' +
                '                <option value="Regular User" selected="selected">普通用户</option>\n' +
                '            </select>\n' +
                '        </p>\n' +
                '\n' +
                '\n' +
                '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                '                       onclick="userEditSubmit(\'' + url + '\',\'' + id + '\' )">\n' +
                '    </form>'
            $('#MainRight').html(str);
        },
        error: function () {
            alert('修改失败')

        }
    })
}

function message_edit(id) {
    var str;
    var url = window.location.href;
    var managementIndex = url.indexOf('management');
    url = url.substr(0, managementIndex - 1);
    url = url + '?id=' + id;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            //删除展示数据的表格
            if (data.error) {
                alert(data.error)
            }
            var tb = document.getElementById("tableStyle");
            var rowNum = tb.rows.length;
            for (i = 0; i < rowNum; i++) {
                tb.deleteRow(i);
                rowNum = rowNum - 1;
                i = i - 1;
            }
            str = ' <form id="newsForm" method="post" action="/" enctype="multipart/form-data" style="margin-left: 30px;margin-top: 20px">\n' +
                '                <span>标题</span><input type="text" name="articleTitle" id="articleTitle" value=\'' + data.title + '\'><br>\n' +
                '                <div id="lable" style="margin-top: 20px">新闻内容</div>\n' +
                '                <div id="editor" type="text/plain" style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                '                     name="myeditor"></div>\n' +
                '                <script type="text/javascript">\n' +
                '                    var ue = UE.getEditor(\'editor\', {\n' +
                '                        serverUrl: "/api/controller/"\n' +
                '                    });//实例化编辑\n' +
                '            var timer = setTimeout(function () {\n' +
                '                ue.setContent(\'' + data.content + '\');\n' +
                '            }, 100);' +
                '\n' +
                '                </script>\n' +
                '                <div id="subform"></div>\n' +
                '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                '                       onclick="messageEditSubmit(\'' + url + '\',\'' + id + '\' )">\n' +
                '\n' +
                '            </form>';
            $('#MainRight').html(str);
        },
        error: function () {
            alert('修改失败')

        }
    })
}

function news_edit(id) {
    var str;
    var url = window.location.href;
    var urltype = url.split('/');
    var newstype = urltype[urltype.length - 1]
    var managementIndex = url.indexOf('management');
    url = url.substr(0, managementIndex - 1);
    url = url + '?id=' + id;
    if (newstype.startsWith('research')) {
        url = url.replace('research', 'introduction')
    }
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            //删除展示数据的表格
            if (data.error) {
                alert(data.error)
            }
            var tb = document.getElementById("tableStyle");
            var rowNum = tb.rows.length;
            for (i = 0; i < rowNum; i++) {
                tb.deleteRow(i);
                rowNum = rowNum - 1;
                i = i - 1;
            }
            //   添加编辑内容
            var strfont = ' <form id="newsForm" method="put" action="/" enctype="multipart/form-data" style="margin-left: 30px;margin-top: 20px">\n' +
                '                <span>标题</span><input type="text" name="articleTitle" id="articleTitle" ><br>\n' +
                '\n' +
                '                \n' +
                '                <br>\n';
            var strend = '                <div id="lable" style="margin-top: 20px">新闻内容</div>\n' +
                '                <div id="editor" type="text/plain" style="margin-left:110px;width:90%;height:400px;margin-top: -13px"\n' +
                '                     name="myeditor"></div>\n' +
                '                <script type="text/javascript">\n' +
                '                    var ue = UE.getEditor(\'editor\', {\n' +
                '                        serverUrl: "/api/controller/"\n' +
                '                    });//实例化编辑\n' +
                '  document.getElementById(\'articleTitle\').value = \'' + data.title + '\';\n' +
                '            var timer = setTimeout(function () {\n' +
                '                ue.setContent(\'' + data.content + '\');\n' +
                '            }, 100);' +
                '\n' +
                '                </script>\n' +
                '                <div id="subform"></div>\n' +
                '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                '                       onclick="newsEditSubmit(\'' + url + '\',\'' + id + '\')">\n' +
                '\n' +
                '            </form>';
            if (newstype.startsWith('news') || newstype.startsWith('research') || newstype.startsWith('join') || newstype.startsWith('aboutUs') || newstype.startsWith('contact')) {
                str = strfont + strend;
            }
            if (newstype.startsWith('seminar')) {
                var strmiddle = ' <div id="subForm">\n' +
                    '                    <span>地点</span><input type="text" name="place" id="place" value=\'' + data.place + '\'><br>\n' +
                    '                    <span>讲者</span><input type="text" name="speaker" id="speaker" value=\'' + data.speaker + '\'><br>\n' +
                    '                </div>';
                str = strfont + strmiddle + strend
            }
            if (newstype.startsWith('conference')) {
                var strmiddle = '<span>标题</span>' + ' <select id="subSelect" name="subSelect">\n' +
                    '                    <option value="domestic">国内会议</option>\n' +
                    '                    <option value="foregin">国外会议</option>\n' +
                    '                </select>';
                str = strfont + strmiddle + strend
            }
            if (newstype.startsWith('exchange')) {
                var strmiddle = '<span>标题</span>' + ' <select id="subSelect" name="subSelect">\n' +
                    '                    <option value="mission">出访</option>\n' +
                    '                    <option value="visitor">来访</option>\n' +
                    '                </select>';
                str = strfont + strmiddle + strend
            }
            $('#MainRight').html(str)


        },
        error: function () {
            alert('修改失败')

        }
    });
}


function research_edit(url, id) {
    var urltype = url.split('/');
    var newstype = urltype[urltype.length - 1]
    var researchurl = url + '?id=' + id;
    $.ajax({
        url: researchurl,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data.error) {
                alert(data.error)
            }
            //删除展示数据的表格
            var tb = document.getElementById("tableStyle");
            var rowNum = tb.rows.length;
            for (i = 0; i < rowNum; i++) {
                tb.deleteRow(i);
                rowNum = rowNum - 1;
                i = i - 1;
            }

            //   添加编辑内容
            var str = '';
            if (newstype == 'project') {
                str = ' <div id="subForm" style="margin-left: 10%;margin-top: 30px">\n' +
                    '<form id="researchEditForm" method="put" style="margin-left: 30px;margin-top: 20px">\n' +
                    '<span>题目</span><input type="text" name="researchtitle" id="researchtitle" value=\'' + data.title + '\'><br>\n' +
                    '                    <span>作者</span><input type="text" name="author" id="author" value=\'' + data.author + '\'><br>\n' +
                    '                    <span>项目编码</span><input type="text" name="code" id="code" value=\'' + data.project_code + '\'><br>\n' +
                    '                    <span>项目基金</span><input type="text" name="fund" id="fund" value=\'' + data.project_fund + '\'><br>\n' +
                    '                    <span>项目期限</span><input type="text" name="schedule" id="schedule" value=\'' + data.project_schedule + '\'><br>\n' +
                    '                    <span>摘要</span><input type="text" name="abstract" id="abstract" value=\'' + data.abstract + '\'><br>\n' +
                    '                    <span>关键字</span><input type="text" name="keywords" id="keywords" value="\'' + data.keywords + '\'"><br>\n' +
                    '                    <span>其他</span><input type="text" name="other" id="other" value=\'' + data.other + '\'><br>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="researchEditSubmit(\'' + url + '\',\'' + id + '\')">\n' +
                    '</form>\n' +
                    '                </div>';
                $('#MainRight').html(str)
                // document.getElementById('author').value = data.author
                // document.getElementById('code').value = data.code


            }
            if (newstype == 'publication') {
                str = ' <div id="subForm">\n' +
                    '<form id="researchEditForm" method="put" style="margin-left: 30px;margin-top: 20px">\n' +
                    '<span>题目</span><input type="text" name="researchtitle" id="researchtitle" value=\'' + data.title + '\'><br>\n' +
                    '                    <span>作者</span><input type="text" name="author" id="author" value=\'' + data.author + '\'><br>\n' +
                    '                    <span>详细期刊及事件</span><input type="text" name="place" id="place" value=\'' + data.place + '\'><br>\n' +
                    '                    <span>发表年限</span><input type="text" name="year" id="year" value=\'' + data.year + '\'><br>\n' +
                    '                    <span>其他</span><input type="text" name="other" id="other" value=\'' + data.other + '\'><br>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="researchEditSubmit(\'' + url + '\',\'' + id + '\')">\n' +
                    '</form>\n' +
                    '                </div>';
                $('#MainRight').html(str)
            }
            if (newstype == 'report') {
                str = ' <div id="subForm">\n' +
                    '<form id="researchEditForm" method="put" style="margin-left: 30px;margin-top: 20px">\n' +
                    '<span>题目</span><input type="text" name="researchtitle" id="researchtitle" value=\'' + data.title + '\'><br>\n' +
                    '                    <span>作者</span><input type="text" name="author" id="author" value=\'' + data.author + '\'><br>\n' +
                    '                    <span>报告地点</span><input type="text" name="place" id="place" value=\'' + data.place + '\'><br>\n' +
                    '                    <span>报告时间</span><input type="text" name="time" id="time" value=\'' + data.time + '\'><br>\n' +
                    '                    <span>报告年限</span><input type="text" name="year" id="year" value=\'' + data.year + '\'><br>\n' +
                    '                    <span>相关文档</span><input type="file" name="pdf" id="pdf" value=\'' + data.pdf_path + '\'><br>\n' +
                    '                    <span>其他</span><input type="text" name="other" id="other" value=\'' + data.other + '\'><br>\n' +
                    '                <input type="button" class="submit" style="margin-left: 190px;margin-top: 35px;" value="提交"\n' +
                    '                       onclick="researchEditSubmit(\'' + url + '\',\'' + id + '\')">\n' +
                    '</form>\n' +
                    '                </div>';
                $('#MainRight').html(str)
            }


        },
        error: function () {
            alert('修改失败')

        }
    });
}

function researchEditSubmit(url, id) {
    var urltype = url.split('/');
    var newstype = urltype[urltype.length - 1]
    var data;
    var type;
    if (newstype.startsWith("report")) {
        data = {
            'id': id,
            'title': $('#researchtitle').val(),
            'author': $('#author').val(),
            'place': $('#place').val(),
            'time': $('#time').val(),
            'year': $('#year').val(),
            'pdf': $('#pdf').val(),
            'other': $('#other').val()
        }
    }
    if (newstype.startsWith("publication")) {
        data = {
            'id': id,
            'title': $('#researchtitle').val(),
            'author': $('#author').val(),
            'place': $('#place').val(),
            'year': $('#year').val(),
            'other': $('#other').val()
        }
    }
    if (newstype.startsWith("project")) {
        data = {
            'id': id,
            'title': $('#researchtitle').val(),
            'author': $('#author').val(),
            'code': $('#code').val(),
            'fund': $('#fund').val(),
            'schedule': $('#schedule').val(),
            'abstract': $('#abstract').val(),
            'keywords': $('#keywords').val(),
            'other': $('#other').val()
        }
    }
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {
            if (data.error) {
                alert(data.error)
            } else {
                alert('修改成功')
            }

        },
        error: function () {
            alert('修改失败')

        }
    });

}

function staffEditSubmit(url, id) {
    var name = $('#name').val();
    var status = $('#status').val();
    var office = $('#office').val();
    var phone = $('#phone').val();
    var email = $('#email').val();
    var position = $('#position').val();
    var degree = $('#degree').val();
    var professionalTitle = $('#professionalTitle').val();
    var profession = $('#profession').val();
    var area = $('#area').val();
    var interesting = interestingUE.getContent();
    var biography = biographyUE.getContent();
    var project = projectUE.getContent();
    var achievement = achievementUE.getContent();
    var activity = activityUE.getContent();
    var publication = publicationUE.getContent();
    var report = reportUE.getContent();
    var data;
    var type;
    data = {
        'id': id,
        'name': name,
        'status': status,
        'profession': profession,
        'office': office,
        'phone': phone,
        'email': email,
        'position': position,
        'degree': degree,
        'professionalTitle': professionalTitle,
        'area': area,
        'interesting': interesting,
        'biography': biography,
        'project': project,
        'achievement': achievement,
        'activity': activity,
        'publication': publication,
        'report': report

    };
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {
            location.reload('http://39.105.199.229:8000/api/admin/people/staff_management')
            alert('修改成功')
        },
        error: function () {
            alert('修改失败')

        }
    });

}

function adjunctProfessorEditSubmit(url, id) {
    var name = $('#name').val();
    var email = $('#email').val();
    var degree = $('#degree').val();
    var professionalTitle = $('#professionalTitle').val();
    var area = $('#area').val();
    var link = $('#link').val();
    var biography = biographyUE.getContent();
    var data;
    data = {
        'id': id,
        'name': name,
        'degree': degree,
        'email': email,
        'area': area,
        'biography': biography,
        'professionalTitle': professionalTitle,
        'link': link,

    };
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {
            location.reload('http://39.105.199.229:8000/api/admin/people/adjunctProfessor_management')
            alert('修改成功')


        },
        error: function () {
            alert('修改失败')

        }
    });

}

function studentEditSubmit(url, id) {
    var name = $('#name').val();
    var graduateStatus = $('#graduateStatus ').val();
    var email = $('#email').val();
    var area = $('#area').val();
    var biography = biographyUE.getContent();
    var project = projectUE.getContent();
    var activity = activityUE.getContent();
    var publication = publicationUE.getContent();
    var data;
    data = {
        'id': id,
        'name': name,
        'graduateStatus': graduateStatus,
        'email': email,
        'area': area,
        'biography': biography,
        'project': project,
        'activity': activity,
        'publication': publication,
    };
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {
            location.reload('http://39.105.199.229:8000/api/admin/people/student_management')
            alert('修改成功')


        },
        error: function () {
            alert('修改失败')

        }
    });

}

function messageEditSubmit(url, id) {
    var title = $('#articleTitle').val();
    var content = ue.getContent();
    var data;
    var type;
    data = {'id': id, 'title': title, 'content': content};
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {

            if (data.error) {
                alert(data.error)
            } else {
                alert('修改成功')
            }
        },
        error: function () {
            alert('修改失败')

        }
    });

}

function userEditSubmit(url, id) {

    var email = $('#email').val();
    var real_name = $('#real_name').val();
    var user_category = $('#user_category').val();
    var role_type = $('#role_type').val();
    data = {'id': id, 'email': email, 'real_name': real_name, 'user_category': user_category, 'role_type': role_type};
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {

            if (data.error) {
                alert(data.error)
            } else {
                alert('修改成功')
            }
        },
        error: function () {
            alert('修改失败')

        }
    });

}

function newsEditSubmit(url, id) {

    var urltype = url.split('/');
    var newstype = urltype[urltype.length - 1]
    var title = $('#articleTitle').val();
    var content = ue.getContent();
    var data;
    var type;
    if (newstype.startsWith('seminar')) {
        var place = $('#place').val();
        var speaker = $('#speaker').val();
        data = {'id': id, 'title': title, 'content': content, 'place': place, 'speaker': speaker};
    }
    if (newstype.startsWith('news') || newstype.startsWith('introduction') || newstype.startsWith('join') || newstype.startsWith('aboutUs') || newstype.startsWith('contact')) {
        data = {'id': id, 'title': title, 'content': content};
    }
    if (newstype.startsWith('conference') || newstype.startsWith('exchange')) {
        type = $('#subSelect').val()
        data = {'id': id, 'title': title, 'content': content, 'type': type};
    }
    $.ajax({
        url: url,
        type: 'PUT',
        dataType: 'json',
        data: data,
        success: function (data) {
            if (data.error) {
                alert(data.error)
            } else {
                alert('修改成功')
            }
        },
        error: function () {
            alert('修改失败')

        }
    });

}

function research_delete(url, id) {
    url = url + '?id=' + id;
    if (confirm("确定要删除吗？")) {
        $.ajax({
            url: url,
            type: 'DELETE',
            dataType: 'json',
            success: function (data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('删除成功');
                    location.reload();
                }
            },
            error: function () {
                alert('删除失败')

            }
        });
    }
}

function logout() {
    if (confirm("确定要退出吗？")) {
        $.ajax({
            url: 'http://39.105.199.229:8000/api/admin/logout',
            type: 'GET',
            dataType: 'json',
            success: function () {
                alert('退出登陆成功')
                window.location.href = "http://39.105.199.229:8000/api/admin/index";
            },
            error: function () {
                alert('退出登陆失败')

            }
        });
    }
}

function checkLogin() {
    $.ajax({
        url: "http://39.105.199.229:8000/api/admin/checkLogin",
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (!data.error) {
                document.getElementById('login').append(data + ",欢迎您！")
            } else {
                str = '<a href="http://39.105.199.229:8000/api/admin/login">登录</a>'
                $('#login').html(str)
            }
        },
        error: function (data) {
            alert(data)
        }

    })
}

function PeoplePublicPermission() {
    var url = window.location.href;
    var urltype = url.split('/');
    var peopletype = urltype[urltype.length - 1]
    var managementIndex = url.indexOf('management');
    //设置后台导航
    $.ajax({
        url: 'http://39.105.199.229:8000/api/admin/checkAdmin',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                if (peopletype.startsWith('adjunctProfessor')) {
                    str = '<img\n' +
                        '                src="/static/images/add_lable.jpg" style="height: 15px;width: 15px;margin-right: 5px">\n' +
                        '            <a href="adjunctProfessor_public">添加</a>';
                    $('#peoplePublic').html(str)
                }
                if (peopletype.startsWith('staff')) {
                    str = '<img\n' +
                        '                src="/static/images/add_lable.jpg" style="height: 15px;width: 15px;margin-right: 5px">\n' +
                        '            <a href="staff_public">添加</a>';
                    $('#peoplePublic').html(str)

                }
                if (peopletype.startsWith('student')) {
                    str = '<img\n' +
                        '                src="/static/images/add_lable.jpg" style="height: 15px;width: 15px;margin-right: 5px">\n' +
                        '            <a href="student_public">添加</a>';
                    $('#peoplePublic').html(str)

                }


            }
        },
        error: function () {
            alert('验证失败')
        }

    })
}

function NavLink() {
    //设置后台导航
    $.ajax({
        url: 'http://39.105.199.229:8000/api/admin/checkAdmin',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                str = ' <ul>\n' +
                    '            <li></li>\n' +
                    '            <li></li>\n' +
                    '            <li></li>\n' +
                    '            <li></li>\n' +
                    '            <li onclick="DisplaySecond()"></li>\n' +
                    '            <ul id="secondTile">\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '                <li></li>\n' +
                    '            </ul>\n' +
                    '            <li onclick="DisplayThird()"></li>\n' +
                    '            <ul id="thirdTile">\n' +
                    '                <li></li>' +
                    '               <li></li>' +
                    '               <li></li>' +
                    '            </ul>\n' +
                    '            <li></li>\n' +
                    '            <li></li>\n' +
                    '        </ul>';

                $('#MainLeft').html(str);
                var title = document.getElementById("MainLeft").getElementsByTagName("li");//获取导航的DIV
                var LinkArry = ["http://39.105.199.229:8000/api/admin/userManagement", "http://39.105.199.229:8000/api/admin/index/slider_management", "http://39.105.199.229:8000/api/admin/index/message_management", "http://39.105.199.229:8000/api/admin/news_public", "#", "http://39.105.199.229:8000/api/admin/news_management", "http://39.105.199.229:8000/api/admin/seminar_management", "http://39.105.199.229:8000/api/admin/conference_management", "http://39.105.199.229:8000/api/admin/exchange_management", "http://39.105.199.229:8000/api/admin/research_management", "http://39.105.199.229:8000/api/admin/join_management", "http://39.105.199.229:8000/api/admin/aboutUs_management", "http://39.105.199.229:8000/api/admin/contact_management", "#", "http://39.105.199.229:8000/api/admin/people/staff_management", "http://39.105.199.229:8000/api/admin/people/student_management", "http://39.105.199.229:8000/api/admin/people/adjunctProfessor_management", "http://39.105.199.229:8000/api/admin/leave_public", "http://39.105.199.229:8000/api/admin/leave_management"]; //创建超链接数组
                var LinkNode = ["用户管理", "轮播图管理", "内容管理", "新闻发布", "新闻管理", "中心动态", "学术报告", "学术会议", "学术交流", "科学研究", "招纳贤士", "关于我们", "联系我们", "成员管理", "职工管理", "学生管理", "兼职教授管理", "请假发布", "请假管理"]
                var n = title.length;

            } else {
                str = ' <ul>\n' +
                    '            <li onclick="DisplayThird()"></li>\n' +
                    '            <ul id="thirdTile">\n' +
                    '                <li></li>' +
                    '               <li></li>' +
                    '               <li></li>' +
                    '            </ul>\n' +
                    '            <li></li>\n' +
                    '        </ul>';
                $('#MainLeft').html(str);
                var title = document.getElementById("MainLeft").getElementsByTagName("li");//获取导航的DIV
                var LinkArry = ["#", "http://39.105.199.229:8000/api/admin/people/staff_management", "http://39.105.199.229:8000/api/admin/people/student_management", "http://39.105.199.229:8000/api/admin/people/adjunctProfessor_management", "http://39.105.199.229:8000/api/admin/leave_public"]; //创建超链接数组
                var LinkNode = ["成员管理", "职工管理", "学生管理", "兼职教授管理", "请假发布"]
                var n = title.length;
                if (document.getElementById('conferenceTypeId')) {
                    $('#MainRight').removeChild(document.getElementById('conferenceTypeId'))

                }
            }
            for (i = 0; i < n; i++) {                                           //遍历添加超链接s

                var a = document.createElement("a");
                var node = document.createTextNode(LinkNode[i]);
                a.appendChild(node);
                a.href = LinkArry[i];
                title[i].appendChild(a);
            }
            ;

            var getLi, getAllLi;
            getLi = document.getElementById("secondTile").getElementsByTagName("li");
            getAllLi = document.getElementById("MainLeft").getElementsByTagName("li");
            for (i = 0; i < 6; i++) {
                getLi[i].onclick = function () {
                    for (i = 0; i < 6; i++) {
                        getLi[i].style.background = "white";
                    }
                    this.style.background = "#c5eaf3";
                }
            }
            ;

            var getLiThird;
            getLiThird = document.getElementById("thirdTile").getElementsByTagName("li");
            for (i = 0; i < 2; i++) {
                getLiThird[i].onclick = function () {
                    for (i = 0; i < 2; i++) {
                        getLiThird[i].style.background = "white";
                    }
                    this.style.background = "#c5eaf3";
                }
            }
            ;
        },
        error: function () {
            alert('菜单栏渲染失败')

        }
    });


}

function ShowFile() {
    var FileId = document.getElementById("file");
    var FileChange = document.getElementById("FileChange");
    FileId.style.display = "";
    FileChange.style.display = "none";
}
