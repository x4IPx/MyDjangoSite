# MyDjangoSite
Быстрый запуск:
docker-compose -f docker-compose.prod.yml down -v && sleep 1 && docker-compose -f docker-compose.prod.yml up -d --build && sleep 15 && docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput && sleep 1 && docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear && sleep 1 && echo http://192.168.77.32/
