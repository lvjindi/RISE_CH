var title=document.getElementById("Title");//��ȡ�����DIV
var LinkArry=["SETSS2017.html","Menu/Lecturers.html","Menu/Courses.html","Menu/Seminar.html","Menu/Program.html","Menu/Organisation.html","Menu/Registered.html","Menu/News.html"]; //��������������

var titleArry=["Home","Lecturers","Courses","Seminar","Program","Organisation","Registration","News"];//��������������

var a=document.createElement("ul");     //���UL
	title.appendChild(a);

a.innerHTML="<li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li>";



var Link=document.getElementById("Title").getElementsByTagName("li");
var n=Link.length;
//title.innerHTML=title.innerHTML+n;

for(i=0;i<n;i++){                                           //������ӳ�����
	
        var a=document.createElement("a");
	var b=document.createTextNode(titleArry[i]);
	a.appendChild(b);
	a.href=LinkArry[i];
	Link[i].appendChild(a);
	//title.innerHTML=title.innerHTML+i;

};


//var addUl=document.createElement("li");
//var Node=document.createTextNode("1234");
//addUl.appendChild(Node);
//title.appendChild(addUl);
//addUl.innerHTML="<p>��ҳ</p>";


