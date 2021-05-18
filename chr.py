from selenium import webdriver

# 谷歌浏览启动配置
option = webdriver.ChromeOptions()
# 配置参数 禁止 Chrome 正在受到自动化软件控制
option.add_argument('disable-infobars')
# 配置参数禁止data;的出现
option.add_argument('user-data-dir=C:\python27\profile')


# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.baidu.com")