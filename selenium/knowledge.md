# selenium语法 #

## webdriver在python语言中定位元素的方法 ##

|webdriver 							|python|
|-----------------------------------|-------|
|id									|name|
|class name 						|tag name| 
|link text 							|partial link text|
|xpath								|css selector|
|find_element_by_id()				|find_element_by_name()|
|find_element_by_class_name() 		|find_element_by_tag_name()|
|find_element_by_link_text()		|find_element_by_partial_link_text()|
|find_element_by_xpath()			|find_element_by_css_selector()|

##css定位问题##

|选择器|例子|描述|
|-----|----|----|
|.class|.intro|class选择器，选择class="intro"的所有元素|
|#id|#firstname|id选择器，选择id="firstname"的所有原始|
|*|*|选择所有元素|
|element|p|元素所有<p>元素|
|element>element|div>input|选择父元素为<div>的所有<input>元素|
|element+element|div+input|选择同一级中紧接在<div>元素之后的所有<input>元素|
|[attribute=value]|[target=_blank]|选择target="_blank"的所有原始|