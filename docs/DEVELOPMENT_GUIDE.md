# Руководство по разработке

## Изменение текстов (i18n)

Переводы живут в JSON-файлах — это источник правды:
- `locales/ru.json` — русские строки
- `locales/en.json` — английские строки

Элементы для локализации имеют атрибут `data-lang="ключ"`. Ключи в ru и en обязаны совпадать.

После любых правок JSON обязательно пересобери словарь в `index.html`:
```bash
python build.py
```
Скрипт проверит паритет ключей ru/en и покрытие всех `data-lang`, затем впишет словарь в `index.html`. Без этого сайт будет использовать старый текст.

Вайтлист (не переводится): имена Toyota/Land Cruiser/LC 100, бренд Karakol Ski Transfer, домен, единицы 4WD/420 л/KGS, мессенджеры WhatsApp/Telegram/Instagram, топонимы Karakol Ski Resort/Kapriz/Ala-Too, названия тарифов Private/Shared.

## Добавление / изменение тарифа

Тарифы заданы в трёх местах, менять нужно согласованно:

1. **Карточка курорта** — блок `.rate-grid` в `#locations`.
2. **Сводная таблица** — `#prices` (строки `tbody`).
3. **Логика оценки** — объект `prices` в `<script>`:

```js
const prices = {
    karakol: { private_one: 3000, private_round: 8000, shared: 1500, minShared: 0 },
    alatoo:  { private_one: 10000, private_round: 15000, shared: 3000, minShared: 3 }
};
```

`minShared` — минимум пассажиров для shared (0 = без минимума). Если меняете сумму, обновите и видимый текст, и число в `prices`.

## Добавление нового курорта

1. Скопируйте `<article class="loc-card">` в `#locations` и замените фото, тексты, тарифы.
2. Добавьте строку в таблицу `#prices`.
3. Добавьте `<option>` в `#destSelect`:
   ```html
   <option value="newkey" data-lang="dest3">Название</option>
   ```
4. Добавьте направление в объект `prices` и ключи `locN_*`/`destN` в оба JSON.
5. Запустите `python build.py`.

## Замена фотографии

Поместите файл в `img/` и обновите `src`. Фото машин используют `object-fit: cover` в контейнере высотой 290px — рекомендуемое соотношение 320×240 или шире.

### Автобокс (бейдж на фото машины)

Бейдж — блок `.car-box` с картинкой `img/autobox.png`. Чтобы заменить картинку, положите новый файл и обновите `src` в обеих карточках. Прозрачный фон или светлый — предпочтительно.

## Изменение стилей

CSS-переменные находятся в `:root` (цвета, тени, радиусы). Основные блоки: `.hero`, `.loc-card`, `.car-card`, `.rates`, `.booking-card`, `.quick-card`.

Зимняя палитра: `--ink` (тёмно-синий текст), `--blue`/`--blue-d` (акцент), `--ice`/`--surface-2` (светлый лёд), `--bg` (фон страницы).

## Форма брони

Поля и ids:
- `#dateInput` — дата (min = сегодня)
- `#paxInput` — пассажиры (1–6)
- `#pickupInput` — адрес забора
- `#destSelect` — курорт
- `#typeSelect` — тип трансфера
- `#estimateVal` — ориентировочная стоимость

Обработчики — в IIFE в конце `index.html`. Телефон WhatsApp задан константой `PHONE`.

## Локальная проверка

```bash
python build.py
python -m http.server 8000
# открыть http://localhost:8000/?lang=ru и ?lang=en
```
