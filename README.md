<div align="center">

# WebSite

這是一個簡單的 `Django 3.2+` 項目範本，包含引入環境變數配置文件、多資料庫交互、多緩存資料庫交互。

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

</div>

- [WebSite](#website)
  - [Features](#features)
  - [專案目錄結構](#專案目錄結構)
    - [自定義錯誤頁面](#自定義錯誤頁面)
  - [建置](#建置)
    - [安裝環境](#安裝環境)
    - [初始化](#初始化)
    - [測試](#測試)
      - [設置環境變數](#設置環境變數)
      - [啟動](#啟動)

## Features

* `Django 3.2+`

* 使用 [`pdm`](https://github.com/pdm-project/pdm) 管理 `package`：一個現代的 `Python` 包管理器，支持 `PEP 582`。

* 使用 [`python-dotenv`](https://github.com/theskumar/python-dotenv) 引入環境變數：

   * 管理 `Development` 和 `Production` 設置。

   * 可以替換使用 [`django-environ`](https://github.com/joke2k/django-environ)來引入環境變數。

* `Database` 資料庫：

   * [`mssql-django`](https://github.com/microsoft/mssql-django)：作為替代 [`django-mssql-backend`](https://github.com/ESSolutions/django-mssql-backend) (項目已停止更新)。

   * [`mysqlclient`](https://github.com/PyMySQL/mysqlclient)

   * [`django-redis`](https://github.com/jazzband/django-redis)

## 專案目錄結構

```conf
Project Folder/
    ├── Documentation/
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── pdm.lock
    ├── pyproject.toml
    ├── requirements.txt
    └── project_name/
        ├── manage.py
        ├── media/
        ├── staticfiles/
        ├── project_name/
            ├── __init__.py
            ├── settings/
                ├── __init__.py
                ├── .env
                ├── base.py
                ├── database_router.py
                ├── development.py
                └── production.py
            ├── asgi.py
            ├── urls.py
            └── wsgi.py
        ├── app1/
            ├── static/
            ├── templates/
                └── app1/
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── test.py
            ├── urls.py
            └── views.py
        ├── app2/
            ├── static/
            ├── templates/
                └── app2/
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── urls.py
            └── views.py
        ├── app3/
            ├── static/
            ├── templates/
                └── app3/
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── urls.py
            └── views.py
```

### 自定義錯誤頁面

> [內置視圖](https://docs.djangoproject.com/zh-hans/3.2/ref/views/#module-django.views)

* 可以透過 `handler400` 、 `handler403` 、 `handler404` 、 `handler500` 自定義返回頁面。
```py
# project_name/ulrs.py
from django.contrib import admin
from django.urls import path, include

handler400 = 'project_name.views.error_400'
handler403 = 'project_name.views.error_403'
handler404 = 'project_name.views.error_404'
handler500 = 'project_name.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls'), name='app1'),
    path('app2/', include('app2.urls'), name='app2'),
    path('app3/', include('app3.urls'), name='app3'),
]
```

* 在 `view.py` 中新增指定路徑的 `html`：
```py
# project_name/views.py
from django.shortcuts import render

def error_400(request, exception):
    return render(request, 'errors/400.html')


def error_403(request, exception):
    return render(request, 'errors/403.html')


def error_404(request, exception):
    return render(request, 'errors/404.html')


def error_500(request, exception):
    return render(request, 'errors/500.html')


def csrf_failure(request, reason=''):
    return render(request, 'errors/403_csrf.html')
```

## 建置

### 安裝環境

* 建立虛擬環境(非必要)，並安裝 `pdm`：
```bash
(env) [website]$ pip install pdm
```

* 安裝專案的 `package`：
```bash
(env) [website]$ pdm install
```

* 也可以執行專案初始化：
```bash
(env) [website]$ pdm init
```

### 初始化

* 創建 `.env` (可修改 `env.example` 範本，檔名須修改為 `.env`)。

* 遷移：
```bash
# 創建遷移文件
(env) [website]$ pdm run python manage.py makemigrations app1 app2 app3
# 創建 default 遷移
(env) [website]$ pdm run python manage.py migrate
# 創建 app1 對應 primary database 遷移
(env) [website]$ pdm run python manage.py migrate app1 --database primary
# 創建 app2 對應 secondary database 遷移
(env) [website]$ pdm run python manage.py migrate app2 --database secondary
# 創建 app3 對應 third database 遷移
(env) [website]$ pdm run python manage.py migrate app3 --database third
```

* 創建緩存表：
```bash
(env) [website]$ pdm run python manage.py createcachetable
```

* 創建超級使用者：
```bash
(env) [website]$ pdm run python manage.py createsuperuser
```

* 收集靜態文件：
```bash
(env) [website]$ pdm run python manage.py collectstatic
```

### 測試

#### 設置環境變數

* 為當前 `shell` 設置環境變數 `DJANGO_SETTINGS_MODULE` 為 `development` ，進行測試：

   * `Linux`：
   ```bash
   $ export DJANGO_SETTINGS_MODULE=website.settings.development
   $ echo $DJANGO_SETTINGS_MODULE
   website.settings.development

   # unset DJANGO_SETTINGS_MODULE # 刪除當前 shell 的環境變數

   # export # 查看所有當前 shell 的環境變數
   ```

   * `Command Prompt`：
   ```bash
   > set DJANGO_SETTINGS_MODULE=website.settings.development
   > echo %DJANGO_SETTINGS_MODULE%
   website.settings.development
   ```

   * `PowerShell`：
   ```powershell
   > $Env:DJANGO_SETTINGS_MODULE="website.settings.development"
   > $Env:DJANGO_SETTINGS_MODULE
   website.settings.development
   ```

#### 啟動

* 啟動測試：
```bash
(env) [website]$ pdm run python manage.py runserver
```
