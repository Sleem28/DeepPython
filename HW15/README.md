# ДЗ15

Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.

### Приблизимся ближе к реальности.
Подключимся к криптобирже Binance через библиотеку python-bynance.
Установка: pip install pithon-binance. Данные обработаем через pandas.

Будем читать текущие котировки по всем фьючерсам USDT и искать крупные установленные ордера. От них
можно искать сделки на отбой. Сделаем скринер плотностей на коленке за который просят обычно денег))).
Минимальный размер для крупных ордеров в USDT будем передавать через аргументы при вызове.
Интервал проверки на крупные ордера также передадим в аргументы.

Поиск будем производить асинхронно по всем фьючерсам одновременно. Найденные заявки слогируем в файл с ордерами.
Ошибки при работе с сервером также слогируем в файл с ошибками.

Сделан параметрический запуск для файла main.py

Логи лежат в ./logs/