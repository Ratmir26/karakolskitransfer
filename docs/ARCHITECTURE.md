# Архитектура проекта

## Обзор

Karakol Ski Transfer — одностраничный статический сайт без серверной части. Рантайм — один файл `index.html` (вся разметка, стили и JS инлайн). Исходник текстов интерфейса — `locales/ru.json` + `locales/en.json`, словарь вшивается в `index.html` сборкой `python build.py`.

## Структура секций

```
┌─────────────────────────────────────┐
│  Header (фиксированная навигация)    │
│  - Логотип, меню, переключатель     │
│    языка (RU/EN), кнопка брони,     │
│    мобильное меню                    │
├─────────────────────────────────────┤
│  Hero (#hero)                        │
│  - Бейдж, заголовок, подзаголовок,   │
│    CTA, 3 показателя                 │
├─────────────────────────────────────┤
│  Locations (#locations)              │
│  - 2 карточки курортов с фото и      │
│    тарифами Private/Shared           │
├─────────────────────────────────────┤
│  Cars (#cars)                        │
│  - 2 карточки LC 100 с бейджем       │
│    автобокса и характеристиками      │
├─────────────────────────────────────┤
│  Prices (#prices)                    │
│  - Сводная таблица тарифов + 4       │
│    примечания (ожидание, shared,     │
│    забор по адресам, оплата)         │
├─────────────────────────────────────┤
│  How (#how)                          │
│  - 4 шага поездки + фото с заметкой  │
├─────────────────────────────────────┤
│  Booking (#booking)                  │
│  - Форма заявки → WhatsApp           │
│    с онлайн-оценкой стоимости        │
├─────────────────────────────────────┤
│  Contacts (#contacts)                │
│  - Телефон, WhatsApp, Telegram,      │
│    Instagram + быстрая бронь         │
├─────────────────────────────────────┤
│  Footer                              │
└─────────────────────────────────────┘
```

## Компоненты

### Карточка курорта (`.loc-card`)

```html
<article class="loc-card">
    <div class="loc-media">
        <img src="img/location-karakol.jpg" alt="...">
        <div class="loc-name" data-lang="loc1_name">...</div>
    </div>
    <div class="loc-body">
        <p data-lang="loc1_desc">...</p>
        <div class="rate-grid"> ... 3 тарифа ... </div>
        <ul class="loc-feats"> ... </ul>
        <a href="#booking" class="btn btn-primary" data-dest="karakol">...</a>
    </div>
</article>
```

Кнопка с `data-dest` при клике подставляет направление в форму брони.

### Карточка автомобиля (`.car-card`)

```html
<article class="car-card">
    <div class="car-media">
        <div class="car-box">
            <img src="img/autobox.png" alt="Roof box">
            <span data-lang="car_badge_box">Автобокс 420 л</span>
        </div>
        <img class="car-photo" src="img/lc100-1.jpg" alt="...">
    </div>
    <div class="car-body">
        <div class="car-title-row"> ... </div>
        <div class="specs"> ... 4 характеристики ... </div>
    </div>
</article>
```

Бейдж `.car-box` — автобокс на месте прежней плашки автомобиля.

### Форма брони (`#bookingForm`)

Поля: дата, количество пассажиров, адрес забора, курорт, тип трансфера. При изменении курорта/типа/пассажиров пересчитывается ориентировочная стоимость (`updateEstimate`). Отправка формирует текстовое сообщение и открывает `https://wa.me/996558130031?text=...`.

Логика цен продублирована в JS-объекте `prices` (см. `index.html`):

| Направление | private one-way | private round | shared / чел. | min shared |
|---|---|---|---|---|
| karakol | 3 000 | 8 000 | 1 500 | — |
| alatoo | 10 000 | 15 000 | 3 000 | 3 |

При изменении тарифов правьте **и** JSON/HTML, **и** объект `prices` в скрипте.

## Технические решения

### CSS-переменные

Все цвета, тени и радиусы вынесены в `:root`. Зимняя палитра: лёд/белый/синий, тёмно-синий текст.

### Адаптивность

- Desktop: 2 колонки для курортов и машин
- Tablet (< 980px): одна колонка, мобильное меню
- Mobile (< 640px): тарифы в столбик, форма в одну колонку, горизонтальный скролл таблицы

### Локализация

Источник правды — `locales/ru.json` + `locales/en.json` (паритет ключей обязателен). `python build.py` проверяет паритет ru/en и покрытие всех `data-lang`, затем вписывает объект `translations` в `index.html` между маркерами `/*__I18N_BEGIN__*/` / `/*__I18N_END__*/` (сгенерированный блок руками не правится).

Переключение языка заменяет содержимое элементов с `data-lang`; для `<meta>` обновляется `content`, для `<input>` — `placeholder`. Выбор сохраняется в `localStorage (kst-lang)`. Язык также можно задать ссылкой `?lang=ru|en` — используется в `hreflang` и sitemap.

Вайтлист (не переводится): имена Toyota/Land Cruiser/LC 100, бренд Karakol Ski Transfer, домен karakolskitransfer.com, единицы 4WD/420 л/KGS, мессенджеры WhatsApp/Telegram/Instagram, топонимы Karakol Ski Resort, Kapriz, Ala-Too, названия тарифов Private/Shared.

### Внешние зависимости

| Ресурс | Назначение |
|--------|-----------|
| Google Fonts | Шрифты Plus Jakarta Sans, Space Grotesk |
| Font Awesome 6.4 | Иконки (CDN cdnjs) |
| Unsplash | Фото hero и курортов (локальные копии в `img/`) |

## Файловая структура

```
karakolskitransfer/
├── index.html          # Рантайм сайта (HTML + CSS + JS, i18n-блок сгенерирован)
├── locales/
│   ├── ru.json         # Русские строки (источник правды)
│   └── en.json         # Английские строки (источник правды)
├── build.py            # Валидация ru/en + вшивание словаря в index.html
├── img/                # Локальные изображения
├── docs/               # Документация проекта
└── .opencode/          # Оркестрация: skill site-orchestrator + 6 ролей
```

## Производительность

- CSS и JS инлайн в рантайме (исходники текстов — `locales/*.json` + `build.py`)
- Изображения локальные, без внешних запросов к фотохостингам
- Иконки через CDN Font Awesome, шрифты с `preconnect`
- Минимум HTTP-запросов
