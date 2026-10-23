# Karakol Ski Transfer

Одностраничный сайт (landing page) зимнего трансфера с водителем на горнолыжные курорты Каракола.

## О проекте

Сайт представляет услугу трансфера на двух внедорожниках **Toyota Land Cruiser 100** (чёрный и серый) с автобоксом на крыше. Два направления:

- **Karakol Ski Resort & Kapriz**
- **Ala-Too Resort**

Форматы: **Private** (за машину) и **Shared** (за человека). Забор и развоз по адресам, ожидание до 4 часов, до 6 пассажиров.

Домен: `karakolskitransfer.com`. Летний сайт аренды (`kyrgyz4x4rentals.com`) — отдельный проект и работает независимо.

## Технологии

- **HTML5** — семантическая разметка
- **CSS3** — переменные, Grid, Flexbox, анимации
- **Vanilla JavaScript** — без фреймворков
- **Font Awesome 6.4** — иконки
- **Google Fonts** — Plus Jakarta Sans, Space Grotesk

## Структура проекта

```
karakolskitransfer/
├── index.html          # Рантайм сайта (HTML + CSS + JS, i18n-блок сгенерирован)
├── locales/
│   ├── ru.json         # Русские строки (источник правды)
│   └── en.json         # Английские строки (источник правды)
├── build.py            # Валидация ru/en + вшивание словаря (запуск перед пушем)
├── img/
│   ├── hero.jpg            # Фон hero (зимние горы)
│   ├── location-karakol.jpg # Фото Karakol Ski Resort / Kapriz
│   ├── location-alatoo.jpg  # Фото Ala-Too
│   ├── snow-forest.jpg      # Иллюстрация блока «Как проходит»
│   ├── lc100-1.jpg          # Toyota LC 100, чёрный (зима, автобокс)
│   ├── lc100-2.jpg          # Toyota LC 100, серый (зима, автобокс)
│   ├── autobox.png          # Автобокс (бейдж на фото машины)
│   └── roofbox.png          # Исходное фото автобокса
├── docs/               # Документация
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── IMPLEMENTATION_PLAN.md
│   ├── DEVELOPMENT_GUIDE.md
│   └── DEPLOYMENT.md
├── robots.txt
├── sitemap.xml
└── .opencode/          # Оркестрация сборки сайта (skill + 6 ролей)
```

Тексты интерфейса правятся только в `locales/*.json`, затем `python build.py`.

## Быстрый старт

1. Откройте `index.html` в любом современном браузере
2. Или запустите локальный сервер:
   ```bash
   python -m http.server 8000
   # или
   npx serve .
   ```

## Разделы документации

- [Архитектура](./ARCHITECTURE.md) — структура и устройство сайта
- [План реализации](./IMPLEMENTATION_PLAN.md) — статус и дорожная карта
- [Руководство по разработке](./DEVELOPMENT_GUIDE.md) — как вносить изменения
- [Деплой](./DEPLOYMENT.md) — как опубликовать сайт
