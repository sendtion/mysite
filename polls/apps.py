from django.apps import AppConfig


# 投票应用的配置文件，默认配置了投票app的名称
# 需要在设置中加入已安装app列表时使用

class PollsConfig(AppConfig):
    name = 'polls'
