# 
Загрузка и обработка файлов
# **Picasso**

### **Стек**
![python version](https://img.shields.io/badge/Python-3.9.6-green)
![django version](https://img.shields.io/badge/Django-4.2.7-blue)
![celery version](https://img.shields.io/badge/Celery-4.2.7-blue)
![redis version](https://img.shields.io/badge/Redis-4.2.7-blue)
![docker version](https://img.shields.io/badge/Docker-4.2.7-blue)

### **Запуск проекта с помощью Docker**

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:VugarIbragimov/test_picasso.git
```

2. Перейдите в директорию с файлом docker-compose.yml:
```
cd file_upload_project
``` 

3. Выполните команду docker-compose up:
```
docker-compose up --build
```

4. Откройте страницу по адресу http://localhost:8000/


### Примеры запросов к API:

## Post-запрос на загрузку файла (Postman):
```
![p_1](/img/p_1.jpeg)

```
### Ответ:
```
![p_2](/img/p_2.jpeg)
```
## Get-запрос на получение файлов (Postman):
```
![p_3](/img/g_1.jpeg)
```

### Ответ:
```
![p_4](/img/g_2.jpeg)
```