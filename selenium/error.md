# 错误记录

## 1、'geckodriver' executable needs to be in PATH

描述：selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 
解决方式：
	需要安装浏览器的geckodriver驱动。在低版本浏览器中不需要，但是在Firefox 47版本上的需要下载该驱动。
	下载地址：http://docs.seleniumhq.org/download/
	下载后放到系统的path路径下面就可以了。

## 2、selenium.common.exceptions.ElementNotVisibleException

```
Traceback (most recent call last):
  File "/Users/mac/Documents/workspaces/github/python/selenium/moreWindowsTab.py", line 18, in <module>
    driver.find_element_by_link_text('登录').click()
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webelement.py", line 77, in click
    self._execute(Command.CLICK_ELEMENT)
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webelement.py", line 493, in _execute
    return self._parent.execute(command, params)
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 249, in execute
    self.error_handler.check_response(response)
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 193, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotVisibleException: Message: 

```
解决方式：
把  driver.find_element_by_link_text('登录').click()  改成该
```
logins = driver.find_elements_by_link_text('登录')
for login in logins:
	if login.is_displayed():
		login.click()
```

## 3、selenium.common.exceptions.WebDriverException: Message: TypeError: can't access dead object

使用`driver.switch_to_default_content()` 语句 返回到默认页。