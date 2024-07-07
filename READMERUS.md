# AR_headset
## Разработчик - [Zernov](https://www.youtube.com/@zernovtech)
[README.md on english](./README.md)

## Предисловие
Хэй! Это мой код для создания AR/MR шлема (дополненная реальность) на базе Python и Linux. В Python используется MediaPipe (трекинг рук) и OpenCV для видеопотоков.
Разработку я начал около двух месяцев назад, так что эта штуковина ещё не идеальна.
БОльший FPS, который Вы можете получить - около 30-ти. Хотя при этом Вы должны использовать суперкомпьютер NASA, наверное.

# Начнём!

(Проверьте свою версию Python, я рекомендую 3.11)
Перед запуском кода нужно установить зависимости. Вы можете использовать [requirements](requirements.txt) для этого:

```console
pip install -r requirements.txt
```

## Конфигурация

После установки зависимостей, вы можете настроить программу.

В файле [config.ini](./config.ini) вы можете найти немного конфигурационных линий:
```ini
[Camera]
mode=ps5camera
# 1camera, 2camera, ps4camera (2560x800), ps5camera (3840x1080), camera_off
resolution_w=1280
resolution_h=720
first_camera_id=0
second_camera_id=1
ps5camera_id=0
ps4camera_id=0
rotate_image=False
...
```

Здесь устанавливается тип камеры. 
1camera - 1 USB UVC камера.\
2camera - 2 разных USB UVC камеры. Просто камеры, ничего интересного.\
ps4camera - HD (720p) стерео камера, разработанная для PS4. Работает со специальным кабелем и драйвером, который можно найти [тут](https://github.com/Hackinside/PS4-CAMERA-DRIVERS)\
ps5camera - Full HD (1080p) стерео камера для PS5. Не требует переходника, но требует [драйвера](https://github.com/Hackinside/PS5_camera_files)
camera_off - работа без камеры. Черный экран.

В конце конфигурационного кода вы можете найти строки отключения/включения видеозаписи, barrel distiortion, трекинга, GUI (интерфейса) и веб интерфейс:
```python
[Options]
active_interface=True
video_recording=False
tracking_active=True
webserver_active=True
barrel_distortion=False
```
Это всё. 

## ЗАПУСК

После установки всех конфигурационных переменных вы можете проверить свою вебкамеру и запустить код:
```console
python3.11 AR_HeadSet.py
```
или
```console
python3 AR_HeadSet.py
```

## Check the video

После запуска кода вы можете убедиться в его работе:
```http
вашIP:5000
```
например:
```http
localhost:5000
```
Затем вы должны увидеть стрим с вебкамеры и интерфейс очков.
## The end 
