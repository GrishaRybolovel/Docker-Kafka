# Docker-Kafka
Проект имеет такую логику работы:
  Пользователь отправляет сообщение телеграм боту(https://t.me/TestingTaskBBot)(В проекте: Web.py)
  
  Сразу же после этого сообщение отправляется в базу данных со статусом 'на проверке', сообщение отправляется на http://localhost:3000/api/v1/message/
  P.s. в Requests.py создан локальный сервер для реализации REST API
  
  P.s. кафка(развернута локально на докере, конфиги есть в docker-composer.yml)
  
  Далее кафка продюсер(producer.py) читает сообщения из http://localhost:3000/api/v1/message/ и отправляет их кафка консюмеру(consumer.py)
  
  Кафка консюмер проверяет сообщения на корректность и отправляет на http://localhost:3000/api/v1/message_confirmation/ с соответствующим статусом
  
  Requests.py к тому же еще и проверяет http://localhost:3000/api/v1/message_confirmation/ и меняет статус сообщения в БД
  
  
  
  Что нужно для запуска:
    1)Requests.py
    2)Web.py
    3)Consumer.py
    4)Producer.py
    Все! Можно отправлять сообщения боту.
