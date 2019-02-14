//设置后台导航
var title = document.getElementById("MainLeft").getElementsByTagName("li");//获取导航的DIV
var LinkArry = ["htgl.php", "news_public", "#", "news_management'", "seminar_management'", "conference_management", "exchange_management", "xwgl.php?news='kxyj'", "xwgl.php?news='znxs'", "#", "xwgl.php", "xwgl.php", "xwgl.php", "xzgl.php"]; //创建超链接数组
var LinkNode = ["后台管理", "新闻发布", "新闻管理", "中心动态", "学术报告", "学术会议", "学术交流", "科学研究", "招纳贤士", "成员管理", "科研人员", "中心学生", "特聘教授", "下载管理"]

var n = title.length;

for (i = 0; i < n; i++) {                                           //遍历添加超链接

    var a = document.createElement("a");
    var node = document.createTextNode(LinkNode[i]);
    a.appendChild(node);
    a.href = LinkArry[i];
    title[i].appendChild(a);
}
;
	
