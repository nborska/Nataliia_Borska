# Зовнішні скіли Claude Code — AIR Music Distribution

> Документ містить: що робить кожен скіл, як встановити, і готові промпти для AIR Music.

---

## Як встановити скіли

Є два способи:

**Спосіб 1 — через Claude Code Marketplace:**
```
/plugin install <назва-скіла>
```

**Спосіб 2 — вручну (git clone):**
```bash
git clone <url-репозиторію> ~/.claude/plugins/<назва>
```

Після встановлення — перезапустіть Claude Code.

---

## 1. OpenClaudia — Marketing Automation Toolkit
**Репо:** https://github.com/OpenClaudia/openclaudia-skills
**Що робить:** 63+ скіли для автоматизації маркетингу — публікація контенту, email-кампанії, реклама, SEO, аналітика, CRM-інтеграція (HubSpot і GA4 вже є у вашому стеку).

**Встановлення:**
```bash
npx openclaudia install --all
```

**Промпти для AIR Music:**

```
/openclaudia
Продукт: AIR Music Distribution. Бриф: [вставити brief.md секції 1-6].
Задача: запустити email-кампанію для re-engagement холодних лідів з HubSpot.
ЦА: indie artists Philippines, вже заповнили форму але не відповіли на менеджера.
TOV: людяний, pain-first. Без хайпу.
Склади серію з 3 листів з темами, текстами і CTA.
```

```
/openclaudia
Задача: аналіз GA4 за минулий тиждень для AIR Music Distribution.
Ключові метрики: конверсії по каналах, CPA, bounce rate на лендінгах Check і Manager.
Виведи: що спрацювало → що не спрацювало → 3 конкретні дії.
```

---

## 2. Claude SEO — SEO Audit Tool
**Репо:** https://github.com/AgriciDaniel/claude-seo
**Що робить:** 25 SEO-скілів — технічний аудит сайту, аналіз контенту E-E-A-T, schema markup, оптимізація для AI-пошуку (Google Overviews, ChatGPT), локальне SEO, інтеграція з Google Search Console і GA4.

**Встановлення:**
```bash
git clone https://github.com/AgriciDaniel/claude-seo ~/.claude/plugins/claude-seo
```

**Промпти для AIR Music:**

```
/seo-audit
URL: https://air.io/en/music-distribution
Задача: повний SEO аудит сторінки. Ринок: Філіппіни.
Ключові слова: music distribution Philippines, indie artist distribution SEA.
Виведи: технічні проблеми → on-page оптимізація → рекомендації по контенту.
```

```
/seo-content
Задача: написати SEO-оптимізовану статтю для блогу AIR Music.
Тема: "Why your royalties don't add up — and what your distributor isn't telling you"
ЦА: mid-tier Filipino artists, 1.5K–500K monthly listeners.
Ключові слова: music royalties Philippines, spotify royalty calculator.
E-E-A-T: expertise через конкретні цифри і кейси.
Обсяг: 1,500–2,000 слів.
```

```
/ai-search-optimize
Задача: оптимізувати контент air.io для Google AI Overviews і ChatGPT.
Питання цільової аудиторії: "best music distributor Philippines", "is distrokid safe", "how to get on spotify playlists".
Виведи: які фрагменти з сайту потрібно переписати щоб вони з'явились у AI-відповідях.
```

---

## 3. Video Toolkit — AI Video Production
**Репо:** https://github.com/digitalsamba/claude-code-video-toolkit
**Що робить:** Повний цикл відеовиробництва — скрипти, voiceover, монтаж, AI-генерація зображень, публікація. Підтримує Remotion, MoviePy, Modal GPU.

**Встановлення:**
```bash
git clone https://github.com/digitalsamba/claude-code-video-toolkit ~/.claude/plugins/video-toolkit
python3 -m pip install -r tools/requirements.txt
```

**Промпти для AIR Music:**

```
/video
Задача: створити скрипт для 30-секундного Reels для Instagram AIR Music Distribution.
ЦА: Filipino indie artists, вже мають дистрибуцію але застрягли.
Хук (перші 3 сек): біль — "Your release dropped 3 weeks ago. Nothing happened."
Структура: хук → проблема → рішення → CTA "Comment CHECK below".
TOV: спокійний, людяний. Без хайпу.
```

```
/video
Задача: ТЗ для відео-кейсу про артиста AIR Music Distribution.
Формат: YouTube/Facebook video, 2-3 хвилини.
Структура: до AIR (проблема) → рішення → результати → CTA.
Ключові меседжі: personalized manager, transparent royalties, real support.
```

---

## 4. AI Marketing Skills — Strategy & Conversion
**Репо:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Що робить:** 23 безкоштовних скіли — позиціонування, LinkedIn стратегія, контент, cold outreach, homepage audit, case studies, щоденне планування. Підтримує режими quick/standard/deep.

**Встановлення:**
```bash
git clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills ~/.claude/plugins/marketing-skills
```

**Промпти для AIR Music:**

```
/positioning deep
Продукт: AIR Music Distribution.
УТП: "AIR — не платформа. Це команда." Revenue share 70/30, персональний менеджер, відповідь до 4 годин.
Конкуренти: DistroKid, TuneCore, CD Baby, SoundOn.
ЦА: mid-tier Filipino artists + indie labels.
Задача: перевірити позиціонування — чи достатньо диференційовані, де слабкі місця.
```

```
/cold-outreach standard
Продукт: AIR Music Distribution.
ЦА: Filipino indie artists в Instagram, 2K–50K Spotify listeners.
Вже мають дистриб'ютора але незадоволені підтримкою.
TOV: Taglish hook + англійська тіло. Не продажний, людяний.
Склади: 3 варіанти першого DM + follow-up послідовність.
```

```
/homepage-audit
URL: https://air.io/en/music-distribution
Задача: аудит лендінгу Check My Track. Поточна конверсія 38.9%.
Що перевірити: hero section, CTA розміщення, trust signals, mobile UX.
Виведи: що можна покращити щоб конверсія зросла до 45%+.
```

---

## 5. Social Media Skills — Multi-Platform Management
**Репо:** https://github.com/charlie947/social-media-skills
**Що робить:** Система для ведення Instagram, LinkedIn, Substack, X, YouTube через єдиний голос бренду. Центр — voice-builder, від якого залежать всі інші скіли.

**Встановлення:**
```bash
git clone https://github.com/charlie947/social-media-skills ~/.claude/plugins/social-media-skills
```

**Промпти для AIR Music:**

```
/voice-builder
Продукт: AIR Music Distribution.
TOV: calm, clear, human, pain-first. Без хайпу.
Заборонено: "best", "all-in-one", "grow fast", агресивний sales.
ЦА: Filipino indie artists + indie labels.
Мовні якорі: "real manager", "we help fix it", "you're not alone with this".
Створи voice.md і about-me.md для всіх соцмереж.
```

```
/post-writer
Платформа: Instagram.
Тема: "Your distributor went silent for 3 weeks — here's what that costs you"
TOV: [використати voice.md що створили вище]
CTA: "Comment CHECK below"
Формат: карусель, 5 слайдів. Перший рядок — хук.
```

```
/content-matrix
Продукт: AIR Music Distribution.
Платформи: Instagram, Facebook, TikTok.
5 контентних пілонів: біль/криза, пояснення дистрибуції, соціальний доказ, стратегія зростання, mindset.
Склади матрицю контенту на місяць: теми × формати × платформи.
```

---

## 6. Claude Skills (alirezarezvani) — 313 Modular Skills
**Репо:** https://github.com/alirezarezvani/claude-skills
**Що робить:** 313 скілів у 12 доменах — маркетинг (45), інжиніринг (45), продакт (13), C-level advisory (28), дослідження (8), compliance (14) тощо.

**Встановлення:**
```bash
/plugin install marketing@claude-code-skills
/plugin install cmo@claude-code-skills
/plugin install product-manager@claude-code-skills
```

**Промпти для AIR Music:**

```
/cmo
Продукт: AIR Music Distribution. Фаза: Ф1 Стабілізація Філіппіни.
Бюджет: $1,500/міс реклама. Ціль: 6-8 клієнтів/міс, CAC ≤$380.
Поточна проблема: Meta дає початківців та AI-генераторів, не mid-tier.
Як CMO — дай стратегічне рішення: що змінити в таргетингу і каналах.
```

```
/marketing content-strategy
Продукт: AIR Music Distribution. Ринок: Philippines.
Бюджет на контент: $5,000/рік.
Цілі: ліди з блогу, awareness у нової ЦА, SEO.
Склади контент-стратегію на квартал: типи контенту, теми, частота, канали.
```

---

## 7. Creatomate — Video Generation via API
**Репо:** https://github.com/Sara-Saraireh/claude-code-skill-creatomate
**Що робить:** Генерація відео через Creatomate API — соціальний контент для TikTok, Instagram, YouTube. Шаблони, анімовані субтитри, AI-озвучка, монтаж.

**Вимоги:** Creatomate API key (безкоштовний тариф є), Node.js 16+

**Встановлення:**
```bash
git clone https://github.com/Sara-Saraireh/claude-code-skill-creatomate ~/.claude/plugins/creatomate
```

**Промпти для AIR Music:**

```
/creatomate
Задача: створити серію з 5 відео-постів для Instagram Reels AIR Music Distribution.
Шаблон: текст на фоні + music waveform анімація + субтитри.
Теми: 5 болів mid-tier артистів (stuck release, silent support, royalty confusion, content ID, playlist rejection).
Тривалість: 15-20 секунд кожне.
CTA наприкінці: "Comment CHECK below".
Брендові кольори: [вказати].
```

```
/creatomate
Задача: відео-анонс для кейсу артиста AIR Music.
Формат: before/after — до і після роботи з AIR.
Метрики: streams growth, royalty clarity, response time.
Тривалість: 30 секунд. Платформа: Facebook + Instagram.
```

---

## 8. SEO & GEO Skills — Search + AI Engine Optimization
**Репо:** https://github.com/aaron-he-zhu/seo-geo-claude-skills
**Що робить:** 20 скілів для SEO і GEO (Generative Engine Optimization) — ключові слова, аудит контенту, schema, backlinks, rank tracking, оптимізація для AI-пошуку. Benchmark: 80-item CORE-EEAT.

**Встановлення:**
```bash
/plugin install seo-geo-bundle@aaron-seo-skills
```

**Промпти для AIR Music:**

```
/aaron:auto keyword-research
Домен: air.io
Ринок: Philippines
Ніша: music distribution, artist services
Seed keywords: music distribution, indie artist Philippines, spotify royalties, content ID
Ціль: знайти low-competition, high-intent keywords для блогу і Google Ads.
```

```
/aaron:max content-audit
URL: https://air.io/en/music-distribution
EEAT перевірка: expertise (музична дистрибуція), authority (14 років, офіційний партнер YouTube), trust (відгуки, кейси).
Що покращити щоб сторінка ранжувалась по "music distribution Philippines".
```

```
/aaron:auto geo-optimize
Задача: оптимізувати контент air.io для генеративних пошуковців.
Цільові запити: "best music distributor in Philippines", "how to distribute music in SEA", "distrokid vs air music".
Виведи: які структурні зміни зроблять сайт джерелом для AI-відповідей.
```

---

## 9. Marketing Skills (coreyhaines31) — Full-Stack Marketing
**Репо:** https://github.com/coreyhaines31/marketingskills
**Що робить:** 40+ скілів — CRO, копірайтинг, Google Ads, Meta Ads, LinkedIn, SEO, аналітика, revenue operations. Базовий скіл `product-marketing` об'єднує всі інші.

**Встановлення:**
```bash
npx skills install coreyhaines31/marketingskills
```

**Промпти для AIR Music:**

```
/product-marketing
Бриф: [вставити brief.md секції 1-6].
Задача: запустити новий рекламний цикл для Meta Ads.
Проблема: зараз приходять початківці та AI-генератори, не mid-tier.
Дай: нові аудиторії для таргетингу + 5 варіантів ad copy + рекомендації по creative.
```

```
/google-ads
Кампанія: Personal Manager — AIR Music Distribution. Ринок: Philippines.
Поточний стан: royalty_issues (CTR 10.1%, CPA $3.4) — золота група.
Проблема: howto_keywords (CPA $18, дають початківців).
Задача: розширити royalty_issues + мінус-слова для howto + нові ad groups.
```

```
/cro
Лендінг: Personal Manager — https://air.io (apply page).
Поточна конверсія: 15.8% (ціль: 25%+).
Порівняння: Check лендінг конвертує 38.9%.
Аналіз: де втрачаємо людей, що змінити в першому екрані, де поставити CTA.
```

---

## ШВИДКИЙ ДОВІДНИК — який скіл для якої задачі

| Задача | Скіл |
|--------|------|
| Email кампанія, HubSpot автоматизація | OpenClaudia |
| SEO аудит сторінок air.io | Claude SEO |
| SEO для AI-пошуку (Google Overviews) | SEO & GEO Skills |
| Ключові слова для блогу і Google Ads | SEO & GEO Skills |
| Скрипти для Reels/TikTok | Video Toolkit |
| Генерація відео-постів | Creatomate |
| Позиціонування, холодний аутріч | AI Marketing Skills |
| Контент-план для Instagram | Social Media Skills |
| Стратегія CMO-рівня | Claude Skills |
| Google Ads оптимізація | Marketing Skills |
| Meta Ads таргетинг | Marketing Skills |
| Аудит лендінгу (CRO) | Marketing Skills / AI Marketing Skills |
