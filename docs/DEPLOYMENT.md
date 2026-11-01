# Деплой

## Локальный просмотр

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

## Перед публикацией (обязательно)

```bash
python build.py
# должен вывести: OK: N keys per language, M data-lang usages covered
# без FAIL — иначе в деплой уйдёт index.html со старым словарём
```

## Публикация: GitHub → Vercel

1. Создать новый репозиторий, например `karakolskitransfer`.
2. Инициализировать git и запушить:
   ```bash
   git init
   git add .
   git commit -m "Initial Karakol Ski Transfer site"
   git branch -M main
   git remote add origin https://github.com/USER/karakolskitransfer.git
   git push -u origin main
   ```
3. В [Vercel](https://vercel.com) → **Add New → Project** → импортировать репозиторий.
4. Framework Preset: **Other** (статика). Build Command — пусто, Output Directory — `.` (корень).
5. Deploy. Проверить выданный `*.vercel.app` адрес.

## Домен karakolskitransfer.com

1. Купить домен (оплачивает владелец по команде Ratmir).
2. Vercel → Project → **Settings → Domains** → добавить `karakolskitransfer.com` и `www.karakolskitransfer.com`.
3. У регистратора прописать DNS-записи, которые покажет Vercel (A/AAAA для apex, CNAME для www).
4. Дождаться выпуска HTTPS-сертификата (обычно автоматически).
5. Проверить:
   - `https://karakolskitransfer.com/` открывается с замком;
   - `.../robots.txt` и `.../sitemap.xml` отдаются;
   - `?lang=ru` и `?lang=en` переключают язык.

## SEO после привязки домена

- Google Search Console: подтвердить владение, загрузить `sitemap.xml`, запросить обход.
- Проверить canonical и hreflang после смены домена (сейчас в коде `https://karakolskitransfer.com/`).
- OG/Twitter-картинки заработают только после привязки домена (до этого абсолютные URL ведут на несуществующий домен — ожидаемо).

## Google Ads (после запуска)

1. Исследовать актуальные ставки Google Ads по Кыргызстану (KGS) для запросов «трансфер Каракол», «Karakol ski transfer», «такси Каракол курорт».
2. Выбрать самый экономичный формат (Search с точным соответствием + гео Бишкек/Каракол).
3. Посадочные — секции `#booking` и `#prices`.
4. Бюджет согласует владелец.

## Чек-лист перед запуском

- [ ] `python build.py` без ошибок
- [ ] RU/EN переключаются, форма не сбрасывается
- [ ] Оценка стоимости совпадает с таблицей
- [ ] WhatsApp-ссылки открывают чат с готовым сообщением
- [ ] Все фото загружаются
- [ ] Нет ошибок в консоли браузера
- [ ] Мобильная вёрстка 390px
