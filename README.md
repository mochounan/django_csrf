# django_csrf

将csrf_文件放入app文件夹下
然后在settings中间件里添加如下：

MIDDLEWARE_CLASSES = [
    'api.csrf_.DisableCSRF',  # 添加这行 app文件夹/文件/类
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

主要是解决django自带登录认证之后获取用户名为匿名用户