# sber-competences
Решение на хакатон Цифрового Прорыва от команды [CLS][UNK][PAD][PAD]

Демонстрационная версия доступна [здесь](http://vlakoresker.pythonanywhere.com/)  
Видео с демонстрацией доступно [здесь]https://youtu.be/E1u9hT5UtGg

## How to run
1. Склонировать этот репозиторий

```bash
git clone https://github.com/omega1996/sber-competences
cd sber-competences
```
2. Собрать docker-образ приложения
```bash
docker build -t sber-competences .
```
3. Запустить приложение
```bash
docker run -p 8000:8000 -d --rm sber-competences
```
4. Открыть в браузере [сайт](http://localhost:8000)
