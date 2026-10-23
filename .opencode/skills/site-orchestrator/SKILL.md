---
name: site-orchestrator
description: Orchestrate site builds for Kyrgyz4x4rentals via Architect->Designer->Frontend->Tester->Reviewer->Security pipeline with playwright-mcp verification.
---

# Site Orchestrator

Маршрут сборки сайта `Kyrgyz4x4rentals` (статический одностраничник, весь код в `index.html`).

## Когда использовать

Используй этот скилл для любого изменения сайта: новая секция, правка карточек,
калькулятора, темизации, i18n, стилей, контактов.

## Маршрут (строго по порядку)

1. **Архитектор** (`@architect`) — спроектирует:
   - Читает `docs/ARCHITECTURE.md`, `docs/IMPLEMENTATION_PLAN.md`, структуру `index.html`.
   - Выдаёт план: какие секции/ключи `data-lang`/`locales/ru.json`+`en.json` затронуты, риски.
   - Без правок кода.
2. **Дизайнер** (`@designer`) — нарисует:
   - Решение в терминах существующих CSS-переменных (`:root`, `data-theme`), сеток, брейкпоинтов 992/768px.
   - Без правок кода, только спецификация.
3. **Frontend** (`@frontend`) — сверстает:
   - Правит только `index.html` + `locales/*.json`, затем запускает `python build.py`.
   - Соблюдает `data-lang` покрытие и паритет ключей ru/en.
4. **Тестировщик** (`@tester`) — проверит:
   - Запускает `python build.py`, открывает страницу через playwright-mcp
     (`browser_snapshot`, `browser_console_messages`, `browser_network_requests`),
     проверяет обе темы и оба языка, мобильный viewport 390px.
5. **Reviewer** (`@reviewer`) — вычитает код:
   - Читает дифф, ищет мёртвый CSS/JS, дубли `data-lang`, сломанные селекторы.
   - Правок не вносит, только вердикт fix/approve.
6. **Security** (`@security`) — пропустит в прод:
   - Финальный гейт: XSS/`innerHTML`, `target=_blank`+`noopener`, mixed-content,
     внешние CDN (fonts, font-awesome, unsplash), WhatsApp-ссылки, `img/` пути.
   - Только approve/block.

## Параллельные суб-агенты внутри этапа

- Внутри одного этапа можно запускать несколько суб-агентов параллельно одним блоком Task-вызовов.
- Встроенных `@explore` (быстрый read-only поиск по коду) и `@general` (многозадачный исследователь/исполнитель) можно вызывать по 3 и больше одновременно.
- Типовой веер перед архитектором: 3x `@explore` параллельно — первый читает `docs/`, второй — секции `index.html`, третий — `locales/` и покрытие `data-lang`.
- Типовой веер для независимых проверок: 2x `@general` параллельно — например, один смотрит темы/брейкпоинты, второй — i18n-паритет и внешние ссылки.
- Это не ломает маршрут 1→6: параллельность разрешена только внутри текущего этапа, перепрыгивать этапы нельзя.
- Код по-прежнему правит только `@frontend`; `@explore`/`@general` в этом маршруте — read-only.
- Пример веера: `Task(@explore: секции index.html) + Task(@explore: ключи locales/) + Task(@explore: ограничения из docs/)` — все три вызова в одном блоке.

## Правила оркестрации

- Веди маршрут через `todowrite`: один `in_progress` за раз.
- Не пропускай этапы и не меняй порядок. Если этап нашёл блокер — вернись на предыдущий, не иди вперёд.
- `frontend` — единственный, кто правит код. Остальные — read-only.
- Проект однофайловый: не создавать новые `.css`/`.js` файлы без требования архитектора.
- I18n-инвариант: каждый `data-lang` в HTML обязан существовать в обоих `locales/*.json`; `python build.py` обязан дать `OK`.
- Каждая задача заканчивается отчётом: что сделано, чем проверено (build.py + playwright), вердикты reviewer/security.
