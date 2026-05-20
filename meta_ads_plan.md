# AIR MUSIC — Майстер-план оптимізації
## Personal Manager + Check My Track | Травень 2026

---

## ЧОМУ МИ ЦЕ РОБИМО

При бюджеті $20/день на Meta алгоритмічна оптимізація математично неможлива (потрібно 50+ конверсій/тиждень/адсет, отримуємо 14-20). Тому стратегія — РУЧНА ФІЛЬТРАЦІЯ на 4 рівнях:

1. Текст реклами — фільтрує на рівні скролу
2. Лендинг — фільтрує перед формою
3. Typebot — фільтрує перед HubSpot
4. Ключові слова Google — фільтрує пошуковий intent

ЦІЛІ 4 ТИЖНІВ:
- % MQL з 42% → 65%+
- Lead → Opportunity з 3% → 12%+
- CPQL < $20

---

# ЧАСТИНА А — PERSONAL MANAGER

---

## A1. TYPEBOT — НОВА ВЕРСІЯ (з 9 → до 4 питань)

### Що міняємо

ЗАРАЗ у Typebot 9 кваліфікаційних питань. На цьому етапі ми втрачаємо 30-40% людей.

СТАНЕ: 4 питання + автоматична дискваліфікація.

---

### Новий флоу Typebot

#### Group #1 — Welcome (без змін)

Hey 👋
I'm Alex — a manager at AIR Music Distribution.
Tired of chasing royalties, fixing release issues, or
getting zero response from your distributor?

Let's talk. I'll personally review your profile —
but only if you fit.

First — what should I call you?
[Set first_name]

---

#### Group #2 — Питання 1: Spotify URL

{first_name}, drop your Spotify artist link.
This is where I check if I can actually help you.
[Collect spotify_url]

ЛОГІКА:
- Якщо немає Spotify URL або текст не містить spotify.com/artist → DISQUALIFY → nurture
- Якщо є → далі

---

#### Group #3 — Питання 2: Monthly Listeners

How many monthly listeners do you have right now?

○ Under 500
○ 500–1,500
○ 1,500–5,000
○ 5,000–20,000
○ 20,000+
[Set monthly_listeners]

ЛОГІКА:
- Under 500 → DISQUALIFY → nurture
- 500-1,500 → SOFT NO → nurture з offer повернутися
- 1,500-5,000 → MAIN FUNNEL
- 5,000-20,000 → MAIN FUNNEL (priority)
- 20,000+ → MAIN FUNNEL (high priority)

---

#### Group #4 — Питання 3: Активність релізів

How many releases have you put out in the last 12 months?

○ 0 — I haven't released yet
○ 1–2
○ 3–5
○ 6+
[Set releases_12m]

ЛОГІКА:
- 0 → DISQUALIFY → nurture
- 1-2 → MAIN FUNNEL
- 3-5 → MAIN FUNNEL (priority)
- 6+ → MAIN FUNNEL (high priority)

---

#### Group #5 — Питання 4: Email + WhatsApp

Almost done. What's the best way to reach you?

[Email — required]
[WhatsApp number — optional but recommended]

---

#### Group #6 — Кінець: Qualified

{first_name}, that's everything.

I'll personally review your profile within 24-48 hours.
If I see real potential — I'll reach out via WhatsApp or email.

We approve about 1 in 5 applications.
Be ready for a real conversation, not a sales pitch.

→ Track event: TypebotCompleted (тригер для Meta + HubSpot)

---

#### Group #DQ — Дискваліфіковано (Under 500 OR 0 releases)

{first_name}, thanks for sharing.

Right now AIR Music is built for artists with 1+ release
on Spotify and 1,500+ monthly listeners.

You're not there yet — but you can get there.

We'll send you our free guide on how to grow
your first 1,500 listeners.

→ Email вже зібраний → trigger nurture sequence

---

#### Group #SOFT — М'яка дискваліфікація (500-1,500)

{first_name}, you're close.

Right now AIR Music takes artists with 1,500+ monthly listeners —
because below that, our model doesn't move the needle for you.

Here's what we recommend in the next 3 months:
[link to free guide on growing to 1,500 MLs]

We'll keep your application on file.
When you cross 1,500 — write us back.

---

### Що ПРИБИРАЄМО

| Питання | Чому прибираємо |
|---------|----------------|
| Genre | Менеджер дізнається при першому контакті |
| Tracks ready | Не впливає на кваліфікацію |
| Biggest frustration | Це для розмови з менеджером, не для бота |
| Distributor status + name | Не кваліфікаційне |
| Music ownership + license upload | Перенести на ПІСЛЯ approval |
| Social/portfolio link | Spotify URL + monthly listeners достатньо |

### Очікуваний ефект

| Метрика | Зараз | Після |
|---------|-------|-------|
| Час проходження | 4-5 хв | 1.5-2 хв |
| Drop-off rate | ~40% | ~15% |
| Авто-дискваліфікація | 0% | 35-45% |
| % MQL з тих хто завершив | 42% | 65-75% |

---

## A2. META КРЕАТИВИ — 4 ОБРАНІ З 10 КОНЦЕПТІВ

### Що працює зараз
- Карусель з фото артистки → найкращий формат
- "WHAT IF SOMEONE ACTUALLY PICKED UP?" → стабільно
- "MID-TIER TRAP" → дуже добре

---

### CREATIVE 1 — Concept 8 "WHY ARTISTS GET STUCK"
ФОРМАТ: Карусель 6 слайдів

Primary Text:
You're past the beginner stage. You have releases. People connect with your music. But growth stopped at 2-5K listeners. Same numbers month after month. Talent got you here. But talent alone doesn't scale a career. You need a personal manager — real person, real plan. Apply if you have 1+ release on Spotify and 1,500+ monthly listeners.

Headline: Stuck at 2-5K listeners?
CTA: Apply For A Personal Manager

---

### CREATIVE 2 — Concept 5 "THE EASY PART"
ФОРМАТ: Карусель 6 слайдів

Primary Text:
You uploaded. You released. You thought something would happen. Playlist placements that never came. YouTube views that didn't move. Promo that disappeared. Getting on Spotify was step one — the real work starts after, and most artists do it alone. AIR Music gives you a personal manager who handles what comes after the upload. Apply if you have releases on Spotify and 1,500+ monthly listeners.

Headline: The hard part is what comes next.
CTA: Apply For A Personal Manager

---

### CREATIVE 3 — Existing "MID-TIER TRAP" (вже працює)
ФОРМАТ: Карусель (вже існує)

Новий Primary Text:
5-30 releases. 2K-50K monthly listeners. Still guessing every drop. That's the mid-tier trap. You don't need hype — you need structure. If approved, you get a manager who responds in hours, reviews your catalog, and builds a 90-day growth plan with you. Apply if you have at least 1 release and 1,500+ monthly listeners.

Headline: Stop releasing alone.
CTA: Apply For A Personal Manager

---

### CREATIVE 4 — Concept 6 "6 DAYS AGO"
ФОРМАТ: Статика 1:1 + 4:5

Primary Text:
Your release had a problem. A claim. A metadata error. A payout that didn't arrive. You contacted support — that was 6 days ago. Day 1, day 3, day 6. Automated reply. Ticket number. Silence. This is what DIY distribution looks like when something goes wrong. AIR Music gives you a personal manager who responds within 24 hours and actually fixes it. Apply if you have releases and 1,500+ monthly listeners.

Headline: Real support shouldn't feel like a miracle.
CTA: Apply For A Personal Manager

---

### Запуск
ТИЖДЕНЬ 1: 4 креативи в одному ad set, бюджет $20/день
ТИЖДЕНЬ 2: виключити 2 слабкі, додати Concept 4 або 9 на тест

---

## A3. ЗАВДАННЯ ДЛЯ АНДРІЯ (PPC)

### КОНТЕКСТ ДЛЯ АНДРІЯ
- Бюджет Meta — $20/день загальний
- Алгоритм Meta не вчиться при такому бюджеті
- Стратегія — ручна фільтрація через події і налаштування
- Google працює добре — не ламати, лише підсилити фільтр

---

### Завдання 1 — TypebotCompleted event (НАЙВИЩИЙ ПРИОРИТЕТ)

ЩО ЗРОБИТИ:
1. Meta Events Manager → Custom Events → Create new
2. Назва: TypebotCompleted
3. Trigger: коли Typebot досягає Group #6 (End: Qualified)
4. Дублювати у HubSpot як Lifecycle Stage = MQL

ВАЖЛИВО:
- НЕ використовувати подію Lead (вона на старті бота)
- Налаштувати Conversions API (Pixel втрачає 30-40% даних на iOS)
- Перевірити deduplication між Pixel і CAPI

---

### Завдання 2 — Перепідключити кампанію PM

Optimization & Delivery → Conversion Event → TypebotCompleted

---

### Завдання 3 — Структура кампанії

Кампанія: PM_Philippines_Qualified
└── Ad set: PH_Mid-Tier ($20/день)
    ├── Geo: Philippines
    ├── Age: 22-42
    ├── Interests: BROAD (нічого не вказувати)
    ├── Detailed targeting expansion: OFF
    ├── Виключення інтересів:
    │   ├── "music tutorial"
    │   ├── "how to make beats"
    │   ├── "FL Studio beginner"
    │   ├── "music production for beginners"
    │   └── "free music distribution"
    ├── Conversion event: TypebotCompleted
    └── 4 креативи (3 carousel + 1 static)

---

### Завдання 4 — Зупинити Check My Track на Meta

Зупинити кампанію Check My Track на Meta. Залишити тільки в Google.

---

### Завдання 5 — Google Ads — мінус-слова

Додати в обидві кампанії "SC_AIR_Music":

free, free music, free distribution, free download
download, mp3, mp3 download, lyrics, karaoke
beginner, first track, first release, my first song
how to upload, how to record, how to make
tutorial, guide, learn, course, tips
fl studio, ableton free, free vst, free beats
piano lesson, guitar lesson, learn guitar
remix free, sample pack, beat maker
upload music free, distribute music free
song lyrics, song meaning

---

### Завдання 6 — Google Ads — нові заголовки

1. Music Distribution For Mid-Tier Artists
2. 1,500+ Monthly Listeners? Apply
3. Personal Manager + Real Strategy
4. For OPM Artists With Live Releases
5. 1 In 5 Applications Get Approved
6. Not For Beginners. For Serious Artists.
7. Spotify Catalog + Real Manager
8. Stop Uploading Alone — Apply Today

DESCRIPTION 1:
AIR Music takes artists with 1,500+ monthly listeners and active release schedule. 5 spots per quarter. Apply with your Spotify link.

DESCRIPTION 2:
Real personal manager. YouTube growth plan. Editorial pitching. Apply if you have 1+ release on Spotify and 1,500+ monthly listeners.

---

### Завдання 7 — Тижневий звіт від Андрія

| Метрика | Минулий тиждень | Цей тиждень | Зміна |
|---------|----------------|-------------|-------|
| CPM | | | |
| CPC | | | |
| Meta Lead (старт бота) | | | |
| Meta TypebotCompleted | | | |
| CPL (cost per lead) | | | |
| CPQL (cost per qualified lead) | | | |
| Google Search Impressions | | | |
| Google CTR | | | |
| Google Conversions | | | |

---

## A4. GOOGLE ADS — РОЗШИРЕНИЙ КОПІРАЙТ ДЛЯ PM

### Заголовки (15 варіантів)
1. Music Distribution For Mid-Tier Artists
2. 1,500+ Monthly Listeners? Apply
3. Personal Manager + Real Strategy
4. Not For Beginners. For Serious Artists.
5. Stop Releasing Alone — Apply Today
6. Spotify Catalog + Real Manager
7. 1 In 5 Applications Get Approved
8. AIR Music — For OPM Artists
9. Real Manager Replies in 24 Hours
10. From 5K to 50K Monthly Listeners
11. Your Distributor Won't Reply? We Will.
12. Real Person. Real Plan. Real Growth.
13. Editorial Pitching For Your Next Single
14. YouTube Growth + Distribution Combined
15. Built For Artists Who've Outgrown DIY

### Descriptions (4 варіанти)

D1: AIR Music works only with artists who have 1+ release and 1,500+ monthly listeners. Personal manager. Real strategy. 5 spots per quarter. Apply with your Spotify link.

D2: Tired of distributors that don't reply? Get a personal manager who responds within 24 hours, reviews your catalog, and builds a 90-day growth plan. Apply today.

D3: Not a DIY platform. AIR Music is selected music distribution for serious OPM artists. 1 in 5 applications approved. Editorial pitching, YouTube setup, real growth.

D4: Stop guessing what to do next. Get a real manager who knows your music, your goals, your market. Apply if you have releases on Spotify and 1,500+ monthly listeners.

### Sitelink Extensions
- "How To Apply" → лендинг ↓ How to Start
- "Who We Take" → лендинг ↓ Who This Is For
- "Real Artists" → лендинг ↓ Testimonials
- "FAQ" → лендинг ↓ FAQ

### Callout Extensions
- 70/30 Revenue Split
- $0 Setup Fee
- 100+ Platforms
- 24-Hour Manager Response
- 1 In 5 Approval Rate
- For Mid-Tier Artists Only

---

# ЧАСТИНА Б — CHECK MY TRACK

---

## Б1. СТРАТЕГІЯ

CMT — це ХУК-СЕРВІС який має конвертити в PM. Артист приходить за безкоштовною перевіркою → менеджер пише з результатом → пропонує підписатися.

---

## Б2. Лендинг artists-check — детальні правки

### СЕКЦІЯ 1 — HERO

ЗАЛИШИТИ H1: Don't Release Blind

ЗАМІНИТИ підзаголовок:
GET YOUR FREE TRACK SAFETY REPORT IN 48H
→ A REAL MANAGER REVIEWS YOUR TRACK. 48-HOUR TURNAROUND.

ЗАМІНИТИ body:
→ Rejected releases. Delayed royalties. Content ID claims. Metadata errors. We catch them before your next release goes live.

ДОДАТИ перед CTA: For artists with at least 1 release on Spotify or Apple Music.

### СЕКЦІЯ 9 — "Exclusive Perks" — ПЕРЕПИСАТИ

Зараз: "Exclusive Perks for New Artists"
Стане: "What You Get After Approval"

Зараз: "ONE GUARANTEED OFFICIAL EDITORIAL PITCH"
Стане: "ONE EDITORIAL PITCH FOR YOUR NEXT SINGLE — submitted to platform curators"

Зараз внизу: "Free · 24-48h · For independent artists only"
Стане: "24-48h Safety Report. We approve about 1 in 5 applications."

### СЕКЦІЯ 10 — блог

ВИДАЛИТИ статтю: "How to Distribute Your Music for Free in the Philippines"

ЗАМІНИТИ на: "Why Mid-Tier Artists Get Stuck at 5K Monthly Listeners"

### СЕКЦІЯ 12 — Фінальний блок

ЗАМІНИТИ:
→ AIR Music works with serious artists ready to grow past 5K listeners — is that you?

---

## Б3. Check My Track — Meta

### Рішення: ВИМКНУТИ Check My Track на Meta

Дані за 6-7 тижнів:
| Канал | Lead | MQL | Opportunity | Lead→Opp |
|-------|------|-----|-------------|----------|
| FB Check My Track | 23 | 6 (26%) | 1 | 3% |
| FB Personal Manager | 25 | 19 (76%) | 1 | 4% |
| Google #1 | 9 | 6 (67%) | 2 | 12% |
| Google #2 | 7 | 12 | 3 | 12.5% |

ACTION: Зупинити Check My Track Meta. Залишити в Google.

---

## Б4. Check My Track — Google Ads (ЗАЛИШАЄМО)

### Заголовки (15 варіантів)
1. Real Manager Reviews Your Track
2. Honest Track Review By AIR Music
3. Not A Bot. Real Music Industry Pro.
4. Get Pro Feedback On Your Spotify Track
5. Track Review For Independent Artists
6. Honest Review By Music Manager
7. AIR Music — Track Review In 48h
8. Real Person Listens. Real Feedback.
9. Submit Your Track For Pro Review
10. For Artists With Releases on Spotify
11. Track Review By Real Music Manager
12. What's Stopping Your Track From Growing
13. Stop Guessing — Get Pro Feedback
14. AIR Music Listens. Honestly.
15. Track Feedback That Actually Helps

### Descriptions

D1: Real AIR Music manager listens to your Spotify track and gives you honest feedback in 24-48 hours. Not a bot. For artists with 1+ release on Spotify.

D2: Stop wondering why your track isn't growing. A real music industry manager reviews your catalog, current numbers, and tells you exactly what to fix.

D3: Get an honest opinion from a music industry pro. Real listening, real feedback, real next steps. Submit your Spotify track today.

### Мінус-слова CMT (додатково до базового списку)
song lyrics, song meaning, song download
karaoke, instrumental, sing along
free music app, music player
free track download

---

# ЧАСТИНА В — ВПРОВАДЖЕННЯ

---

## Послідовність робіт

### ТИЖДЕНЬ 1
Day 1-2:
- Андрій: створює подію TypebotCompleted у Meta + CAPI
- Розробник: правки лендинга artists-manager

Day 3-4:
- Розробник: новий Typebot (4 питання)
- Розробник: правки лендинга artists-check
- Дизайнер: 4 нові креативи PM

Day 5-6:
- Андрій: запускає нову кампанію PM з TypebotCompleted
- Андрій: зупиняє Check My Track на Meta
- Андрій: оновлює Google Ads (мінус-слова + headlines)

Day 7: Перший контрольний звіт. Перевірка що події приходять.

### ТИЖДЕНЬ 2
Збір даних. ЖОДНИХ ЗМІН.

### ТИЖДЕНЬ 3
- Аналіз: CPQL, % MQL, % дискваліфікації, Lead→Opportunity
- Виключити 2 слабкі креативи
- Якщо CPQL < $20 → масштабувати до $30/день

### ТИЖДЕНЬ 4
- Lookalike (якщо база > 100 якісних лідів)
- Звіт по 4-тижневих результатах

---

## Метрики (тижневий звіт)

| Метрика | Поточна | Ціль 4 тижні |
|---------|---------|--------------|
| CPL Meta | ~$5 | <$5 |
| CPQL Meta | не вимірюється | <$20 |
| % дискваліфікації в Typebot | 0% | >40% |
| % MQL з кваліфікованих | 42% | >65% |
| Lead → Opportunity | 3% | >12% |
| Час у Typebot | 4-5 хв | <2 хв |
| Drop-off Typebot | ~40% | <15% |

---

## Чого НЕ робити

- Не дробити бюджет на багато кампаній
- Не запускати ретаргетинг (база <500)
- Не робити lookalike до 100 якісних лідів
- Не повертати Check My Track на Meta до стабілізації PM
- Не міняти Typebot після запуску — мінімум 2 тижні
- Не міняти креативи кожні 3 дні — алгоритму потрібно 7 днів
- Не піднімати бюджет до стабілізації CPQL

---

## Контрольні точки

- ДЕНЬ 7: Перевірка що всі події приходять. Якщо ні — стоп, фікс, перезапуск.
- ДЕНЬ 14: Перший аналіз CPQL і % дискваліфікації.
- ДЕНЬ 28: Фінальна оцінка. Якщо метрики досягнуті — масштабувати.

---

Дата: 2026-05-08
Автор: AIR Music marketing team (Nataliia + Claude)
