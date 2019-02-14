<!DOCTYPE>
<html>
<head>
	
	 <link rel="stylesheet" type="text/css" href="css/css.css" />
	 <script src="js/main.js"></script>
	 <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
         <script type="text/javascript" charset="utf-8" src="ueditor.config.js"></script>
        <script type="text/javascript" charset="utf-8" src="ueditor.all.min.js"> </script>
        <!--建议手动加在语言，避免在ie下有时因为加载语言失败导致编辑器加载失败-->
         <!--这里加载的语言文件会覆盖你在配置项目里添加的语言类型，比如你在配置项目里配置的是英文，这里加载的中文，那最后就是中文-->
         <script type="text/javascript" charset="utf-8" src="lang/zh-cn/zh-cn.js"></script>


</head>

<body>
<!--HeadBegin-->
	<div id="Head">            
		<div id="Title"><img src="images/logo.png" />RISE网站后台管理系统</div>
		<div id="exit"><img src="images/exit.png" />退出</div>
		<div id="Banner"><img src="images/index.png" />首页预览</div>
	</div>

<!--HeadEnd-->

<!--MainBegin-->
	<div id="Main">
		<div  id="MainLeft">
			<ul >
				<li>后台管理</li>
				<li>新闻发布</li>
				<li onclick="DisplaySecond()"><a href="#">新闻管理</a></li>
					<ul id="secondTile">
						<li>中心动态</li>
						<li>学术报告</li>
						<li>学术交流</li>
						<li>科学研究</li>
						<li>招纳贤士</li>
					</ul>
				<li onclick="DisplayThird()">成员管理</li>
					<ul id="thirdTile">
						<li>科研人员</li>
						<li>中心学生</li>
						<li>特聘教授</li>
					</ul>
				<li>下载管理</li>
			</ul>
		
		
		</div>
		<div  id="MainRight">
    
   <h1>完整demo</h1>
    <script id="editor" type="text/plain" style="width:1024px;height:500px;"></script>

		</div>
	
	</div>

<!--MainEnd-->

<!--Begin-->
<div id="bottom">
	
</div>

<!--End-->
<script src="js/admin.js"></script>
</body>


</html>