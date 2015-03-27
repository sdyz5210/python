# -*- coding: utf-8 -*-  

import easygui as g
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

while 1:
	g.msgbox('hi，欢迎进入第一个界面小游戏')

	msg = "请问你希望学到什么指示"
	title = "问卷调查"
	choices = ["谈恋爱","编程","OOXX","琴棋书画"]

	choice = g.choicebox(msg,title,choices)

	g.msgbox('您的选择是'+str(choice))

	msg = "你希望重新开始小游戏吗？"
	title = "请选择"

	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)