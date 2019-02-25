from celery import Celery

# 进行Celery允许配置
# 为celery使用django配置文件进行设置
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_meiduo.settings'

app = Celery('celery_tasks')

# 加载配置文件

app.config_from_object('celery_tasks.config')

# 自动加载任务
app.autodiscover_tasks(['celery_tasks.sms'])
