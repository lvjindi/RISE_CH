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
        document.getElementById("thirdTile").style.display = "none";
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
        document.getElementById("secondTile").style.display = "none";
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
    var domesticUrl = 'http://127.0.0.1:8000/api/admin/conference?type=domestic';
    var foreignUrl = 'http://127.0.0.1:8000/api/admin/conference?type=foreign';
    var allUrl = 'http://127.0.0.1:8000/api/admin/conference';
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
        table = ' <table class="tableStyle" id="tableStyle">' +
            '            <tr>' +
            '                <td>序号</td>' +
            '                <td>标题</td>' +
            '                <td>类别</td>' +
            '                <td>发布日期</td>' +
            '                <td>点击</td>' +
            '                <td>管理</td>' +
            '            </tr>' +
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
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].type + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#">编辑</a>&nbsp&nbsp<a href="#">删除</a>' + '</td>'
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

function showPeople(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    var staffUrl = 'http://127.0.0.1:8000/api/admin/people?type=staff';
    var studentUrl = 'http://127.0.0.1:8000/api/admin/people?type=student';
    var professorUrl = 'http://127.0.0.1:8000/api/admin/people?type=adjunctProfessor';
    var allUrl = 'http://127.0.0.1:8000/api/admin/people';
    var peopleUrl;
    if (option == '1') {
        peopleUrl = staffUrl;
    }
    if (option == '2') {
        peopleUrl = studentUrl;
    }
    if (option == '3') {
        peopleUrl = professorUrl;
    }
    if (option == '4') {
        peopleUrl = allUrl;
    }
    if (option != '5') {
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle">' +
            '            <tr>' +
            '                <td>序号</td>' +
            '                <td>姓名</td>' +
            '                <td>类别</td>' +
            '                <td>发布日期</td>' +
            '                <td>点击</td>' +
            '                <td>管理</td>' +
            '            </tr>' +
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
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].name + '</td>' + '<td>' + data[i].user_category + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#">编辑</a>&nbsp&nbsp<a href="#">删除</a>' + '</td>'
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

function showExchange(val) {
    var option = val;
    var obj = document.getElementById('MainRight');
    if (document.getElementById('tableStyle')) {
        obj.removeChild(document.getElementById('tableStyle'))
    }
    var missionUrl = 'http://127.0.0.1:8000/api/admin/exchange?type=mission';
    var visitorUrl = 'http://127.0.0.1:8000/api/admin/exchange?type=visitor';
    var allUrl = 'http://127.0.0.1:8000/api/admin/exchange';
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
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle">' +
            '            <tr>' +
            '                <td>序号</td>' +
            '                <td>标题</td>' +
            '                <td>类别</td>' +
            '                <td>发布日期</td>' +
            '                <td>点击</td>' +
            '                <td>管理</td>' +
            '            </tr>' +
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
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].type + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#">编辑</a>&nbsp&nbsp<a href="#">删除</a>' + '</td>'
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
    var introductionUrl = 'http://127.0.0.1:8000/api/admin/introduction';
    var projectUrl = 'http://127.0.0.1:8000/api/admin/project';
    var publicationUrl = 'http://127.0.0.1:8000/api/admin/publication';
    var reportUrl = 'http://127.0.0.1:8000/api/admin/report';
    var researchUrl;
    if (option == '1') {
        researchUrl = introductionUrl;
        var table = '';
        table = ' <table class="tableStyle" id="tableStyle">' +
            '            <tr>' +
            '                <td>序号</td>' +
            '                <td>标题</td>' +
            '                <td>发布日期</td>' +
            '                <td>点击</td>' +
            '                <td>管理</td>' +
            '            </tr>' +
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
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#">编辑</a>&nbsp&nbsp<a href="#">删除</a>' + '</td>'
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
        table = ' <table class="tableStyle" id="tableStyle">' +
            '            <tr>' +
            '                <td>序号</td>' +
            '                <td>标题</td>' +
            '                <td>作者</td>' +
            '                <td>发布日期</td>' +
            '                <td>点击</td>' +
            '                <td>管理</td>' +
            '            </tr>' +
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
                for (i = 0; i < data.length; i++) {
                    var tr;
                    tr = '<td>' + data[i].id + '</td>' + '<td>' + data[i].title + '</td>' + '<td>' + data[i].author + '</td>' + '<td>' + data[i].create_time + '</td>' + '<td>' + data[i].views_number + '</td>' + '<td>' + '<a href="#">编辑</a>&nbsp&nbsp<a href="#">删除</a>' + '</td>'
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
    var articleClass = val;
    var subclass = document.getElementById('articleSubClass');
    subclass.style.display = "none";   //先将子菜单关闭
    var childs = subclass.childNodes;  //删除原有的所有子节点
    for (var i = childs.length - 1; i >= 0; i--) {
        subclass.removeChild(childs[i]);
    }

    switch (articleClass) {
        case 'zxdt':
            //alert("进入我这个循环了"+ articleClass);
            //subclass.style.display="none";
            break;
        case 'xsbg':
            //alert("进入我这个循环了"+ articleClass);
            break;
        case 'xshy':
            subclass.style.display = "";
            subArry = ["国内会议", "国际会议"];
            subValue = ["gnhy", "gjhy"]
            for (i = 0; i < subArry.length; i++) {
                //alert("进入我这个循环了for"+ i);
                var option = document.createElement("option");
                var node = document.createTextNode(subArry[i]);
                option.appendChild(node);
                option.value = subValue[i];
                subclass.appendChild(option);
                //alert(subArry[i]);
            }
            break;
        case 'xsjl':
            subclass.style.display = "";
            subArry = ["出访", "来访"];
            subValue = ["cf", "lf"]
            for (i = 0; i < subArry.length; i++) {
                //alert("进入我这个循环了for"+ i);
                var option = document.createElement("option");
                var node = document.createTextNode(subArry[i]);
                option.appendChild(node);
                option.value = subValue[i];
                subclass.appendChild(option);

            }
            break;
        case 'kxyj':
            //alert("进入我这个循环了"+ articleClass);
            break;
        case 'znxs':
            //alert("进入我这个循环了"+ articleClass);
            subclass.style.display = "";
            subArry = ["博士生", "研究生", "教师"];
            subValue = ["bss", "yjs", "js"]
            for (i = 0; i < subArry.length; i++) {
                //alert("进入我这个循环了for"+ i);
                var option = document.createElement("option");
                var node = document.createTextNode(subArry[i]);
                option.appendChild(node);
                option.value = subValue[i];
                subclass.appendChild(option);

            }
            break;
        default:
        //alert("进入我这个循环了"+ articleClass);
    }

}


function xwfbSubmit() {

    var title = document.getElementById("title");
    var content = UE.getEditor('editor').getContent();
    //alert(content);
    if (title.value == "" || content == "") {
        if (title.value == "") {
            alert("请输入标题");
            return false;
        }
        else {
            alert("请输入内容");
            return false;
        }
    }
    else {
        return true;
    }
}


function NavLink() {
    //设置后台导航
    var title = document.getElementById("MainLeft").getElementsByTagName("li");//获取导航的DIV
    var LinkArry = ["htgl.php", "news_public", "#", "news_management", "seminar_management", "conference_management", "exchange_management", "research_management", "join_management", "xwgl.php?news=gywm", "people_management", "xzgl.php"]; //创建超链接数组
    var LinkNode = ["后台管理", "新闻发布", "新闻管理", "中心动态", "学术报告", "学术会议", "学术交流", "科学研究", "招纳贤士", "关于我们", "成员管理", "下载管理"]

    var n = title.length;

    for (i = 0; i < n; i++) {                                           //遍历添加超链接

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


}

function ShowFile() {
    var FileId = document.getElementById("file");
    var FileChange = document.getElementById("FileChange");
    FileId.style.display = "";
    FileChange.style.display = "none";
}