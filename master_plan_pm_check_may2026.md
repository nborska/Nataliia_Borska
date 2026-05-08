# AIR Music — Майстер-план оптимізації
## Personal Manager + Check My Track | Травень 2026

---

## ЧОМУ МИ ЦЕ РОБИМО (нагадування контексту)

При бюджеті $20/день на Meta алгоритмічна оптимізація математично неможлива (потрібно 50+ конверсій/тиждень/адсет, отримуємо 14-20). Тому стратегія — **ручна фільтрація** на 4 рівнях:

1. **Текст реклами** — фільтрує на рівні скролу
2. **Лендинг** — фільтрує перед формою
3. **Typebot** — фільтрує перед HubSpot
4. **Ключові слова Google** — фільтрує пошуковий intent

**Мета 4 тижнів:**
- % MQL з 42% → 65%+
- Lead → Opportunity з 3% → 12%+
- CPQL <$20

---

# ЧАСТИНА А — PERSONAL MANAGER

---

## A1. TYPEBOT — НОВА ВЕРСІЯ (з 9 → до 4 питань)

### Що міняємо

**Зараз у Typebot 9 кваліфікаційних питань** (бачила скріншоти):
1. Ім'я
2. Email
3. Monthly listeners
4. Genre
5. Tracks ready
6. Biggest frustration
7. Distributor status
8. Distributor name
9. Music ownership + ліцензії
+ Spotify/portfolio link
+ Social link

Це багато. На цьому етапі ми втрачаємо 30-40% людей.

**Стане:** 4 питання + автоматична дискваліфікація.

---

### Новий флоу Typebot

#### Group #1 — Welcome (без змін)
```
Hey 👋
I'm Alex — a manager at AIR Music Distribution.
Tired of chasing royalties, fixing release issues, or
getting zero response from your distributor?

Let's talk. I'll personally review your profile —
but only if you fit.

First — what should I call you?
[Set first_name]
```

---

#### Group #2 — Питання 1: Spotify URL
```
{first_name}, drop your Spotify artist link.
This is where I check if I can actually help you.
[Collect spotify_url]
```

**Логіка:**
- Якщо немає Spotify URL або текст не містить `spotify.com/artist` → DISQUALIFY → nurture
- Якщо є → далі

---

#### Group #3 — Питання 2: Monthly Listeners
```
How many monthly listeners do you have right now?

○ Under 500
○ 500–1,500
○ 1,500–5,000
○ 5,000–20,000
○ 20,000+
[Set monthly_listeners]
```

**Логіка:**
- `Under 500` → DISQUALIFY → nurture
- `500-1,500` → SOFT NO → nurture з offer повернутися
- `1,500-5,000` → MAIN FUNNEL
- `5,000-20,000` → MAIN FUNNEL (priority)
- `20,000+` → MAIN FUNNEL (high priority)

---

#### Group #4 — Питання 3: Активність релізів
```
How many releases have you put out in the last 12 months?

○ 0 — I haven't released yet
○ 1–2
○ 3–5
○ 6+
[Set releases_12m]
```

**Логіка:**
- `0` → DISQUALIFY → nurture
- `1-2` → MAIN FUNNEL
- `3-5` → MAIN FUNNEL (priority)
- `6+` → MAIN FUNNEL (high priority)

---

#### Group #5 — Питання 4: Email + WhatsApp
```
Almost done. What's the best way to reach you?

[Email — required]
[WhatsApp number — optional but recommended]
```

---

#### Group #6 — Кінець: Qualified
```
{first_name}, that's everything.

I'll personally review your profile within 24-48 hours.
If I see real potential — I'll reach out via WhatsApp or email.

We approve about 1 in 5 applications.
Be ready for a real conversation, not a sales pitch.
```
→ **Track event: TypebotCompleted** (тригер для Meta + HubSpot)

---

#### Group #DQ — Кінець: Дискваліфіковано (Under 500 OR 0 releases)
```
{first_name}, thanks for sharing.

Right now AIR Music is built for artists with 1+ release
on Spotify and 1,500+ monthly listeners.

You're not there yet — but you can get there.

We'll send you our free guide on how to grow
your first 1,500 listeners.
```
→ Email вже зібраний → trigger nurture sequence

---

#### Group #SOFT — Кінець: М'яка дискваліфікація (500-1,500)
```
{first_name}, you're close.

Right now AIR Music takes artists with 1,500+ monthly listeners —
because below that, our model doesn't move the needle for you.

Here's what we recommend in the next 3 months:
[link to free guide on growing to 1,500 MLs]

We'll keep your application on file.
When you cross 1,500 — write us back.
```

---

### Що ПРИБИРАЄМО і чому

| Питання | Чому прибираємо |
|---------|----------------|
| Genre | Менеджер дізнається при першому контакті |
| Tracks ready | Не впливає на кваліфікацію |
| Biggest frustration | Це для розмови з менеджером, не для бота |
| Distributor status + name | Не кваліфікаційне |
| Music ownership + license upload | Перенести на ПІСЛЯ approval — менеджер запитає документи перед distribution |
| Social/portfolio link | Spotify URL + monthly listeners достатньо для перевірки |

### Очікуваний ефект

| Метрика | Зараз | Після |
|---------|-------|-------|
| Час проходження | 4-5 хв | 1.5-2 хв |
| Drop-off rate | ~40% | ~15% |
| Авто-дискваліфікація | 0% | 35-45% |
| % MQL з тих хто завершив | 42% | 65-75% |

---

## A2. META КРЕАТИВИ — ВИБІР З 10 КОНЦЕПТІВ

### Що працює зараз
- **Карусель** з фото артистки → найкращий формат
- "WHAT IF SOMEONE ACTUALLY PICKED UP?" → стабільно
- "MID-TIER TRAP" → дуже добре

### Моя рекомендація: 4 креативи на старт

З 10 концептів обираю ті, що **найкраще фільтрують початківців**.

---

### CREATIVE 1 — Concept 8 "WHY ARTISTS GET STUCK"
**Формат:** Карусель 6 слайдів
**Чому обрала:** В hook одразу число "2-5K listeners" — найсильніший фільтр. Початківець з 200 listeners не впізнає себе. Mid-tier з 3K — впізнає миттєво.

**Primary Text (фінальна версія):**
> You're past the beginner stage. You have releases. People connect with your music. But growth stopped at 2-5K listeners. Same numbers month after month. Talent got you here. But talent alone doesn't scale a career. You need a personal manager — real person, real plan. Apply if you have 1+ release on Spotify and 1,500+ monthly listeners.

**Headline:** Stuck at 2-5K listeners?
**CTA:** Apply For A Personal Manager

---

### CREATIVE 2 — Concept 5 "THE EASY PART"
**Формат:** Карусель 6 слайдів
**Чому обрала:** "Getting on Spotify was the easy part" presupposes наявність релізу — beginner відсіюється сам.

**Primary Text:**
> You uploaded. You released. You thought something would happen. Playlist placements that never came. YouTube views that didn't move. Promo that disappeared. Getting on Spotify was step one — the real work starts after, and most artists do it alone. AIR Music gives you a personal manager who handles what comes after the upload. Apply if you have releases on Spotify and 1,500+ monthly listeners.

**Headline:** The hard part is what comes next.
**CTA:** Apply For A Personal Manager

---

### CREATIVE 3 — Existing "MID-TIER TRAP" (вже працює — посилити)
**Формат:** Карусель (вже існує)
**Чому залишити:** Вже виграє. Просто оновити текст щоб додати фільтр.

**Новий Primary Text:**
> 5-30 releases. 2K-50K monthly listeners. Still guessing every drop. That's the mid-tier trap. You don't need hype — you need structure. If approved, you get a manager who responds in hours, reviews your catalog, and builds a 90-day growth plan with you. Apply if you have at least 1 release and 1,500+ monthly listeners.

**Headline:** Stop releasing alone.
**CTA:** Apply For A Personal Manager

---

### CREATIVE 4 — Concept 6 "6 DAYS AGO"
**Формат:** Статика 1:1 + 4:5
**Чому обрала:** Дуже специфічний біль mid-tier — "релізу проблема не вирішується". Beginner ще не стикався з цим, бо ще не релізив.

**Primary Text:**
> Your release had a problem. A claim. A metadata error. A payout that didn't arrive. You contacted support — that was 6 days ago. Day 1, day 3, day 6. Automated reply. Ticket number. Silence. This is what DIY distribution looks like when something goes wrong. AIR Music gives you a personal manager who responds within 24 hours and actually fixes it. Apply if you have releases and 1,500+ monthly listeners.

**Headline:** Real support shouldn't feel like a miracle.
**CTA:** Apply For A Personal Manager

---

### Що ВИКЛЮЧАЮ з 10 концептів

| Concept | Чому НЕ беру |
|---------|-------------|
| 1 "Still at the beginning" | Звучить однаково з 7. Початківець теж думає "everything I did didn't work" — НЕ фільтрує. |
| 2 "Just stuck" | Дуже близьке до Concept 8 — не варто дублювати. |
| 4 "100 platforms" | Ширша аудиторія. Тестувати в Тиждень 2. |
| 7 "Nothing happens" | Дублює Concept 1 і 2. |
| 9 "Truly building" | Провокаційний кут. Тестувати в Тиждень 2 якщо буде бюджет. |
| 10 "Treated like a hobby" | Слабкий filter — beginner теж хоче partner not platform. |

---

### Запуск

**Тиждень 1:**
- 4 креативи в **одному ad set** (не дробити!)
- Бюджет: $20/день на весь ad set
- Meta сама перерозподілить на топ-2

**Тиждень 2:**
- Виключити 2 слабші креативи
- Додати Concept 4 або 9 на тест

---

## A3. ЗАВДАННЯ ДЛЯ АНДРІЯ (PPC)

### Контекст для Андрія
- Бюджет Meta — $20/день загальний
- Алгоритм Meta не вчиться при такому бюджеті
- Стратегія — ручна фільтрація через події і налаштування
- Google працює добре — не ламати, лише підсилити фільтр

---

### ✅ Завдання 1 — Створити подію `TypebotCompleted` (НАЙВИЩИЙ ПРИОРИТЕТ)

**Що зробити:**
1. Meta Events Manager → Custom Events → Create new
2. Назва події: **TypebotCompleted**
3. Trigger: коли Typebot досягає Group #6 (End: Qualified)
4. Дублювати трекінг на цій же точці у HubSpot як Lifecycle Stage = MQL

**Важливо:**
- НЕ використовувати подію `Lead` (вона спрацьовує на старті бота)
- Нова подія ТІЛЬКИ для тих хто пройшов всі 4 кваліфікаційні питання
- Налаштувати Conversions API (Pixel сам по собі втрачає 30-40% даних на iOS)
- Перевірити deduplication між Pixel і CAPI

---

### ✅ Завдання 2 — Перепідключити кампанію PM

**Action:** Optimization & Delivery → Conversion Event → **TypebotCompleted** (замість поточної події)

**Очікуваний ефект:** Meta почне шукати людей схожих на тих хто завершує бота, а не на тих хто просто клікнув.

---

### ✅ Завдання 3 — Структура кампанії

```
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
```

**Чому BROAD:** при $20/день і кваліфікованій події Meta краще знаходить аудиторію через event-optimization, ніж через interest targeting.

---

### ✅ Завдання 4 — Зупинити "Check My Track" на Meta

**Action:** зупинити кампанію Check My Track на Meta. Залишити тільки в Google.

**Чому:**
- Meta показує Check My Track тим самим людям що і PM (одна аудиторія)
- Це конкуренція двох наших же кампаній за бюджет
- Google інакше — там пошуковий intent, а не interrupt

---

### ✅ Завдання 5 — Google Ads — мінус-слова

Додати в обидві кампанії "SC_AIR_Music":
```
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
```

---

### ✅ Завдання 6 — Google Ads — нові заголовки і описи

Заголовки (додати до існуючих):
```
1. Music Distribution For Mid-Tier Artists
2. 1,500+ Monthly Listeners? Apply
3. Personal Manager + Real Strategy
4. For OPM Artists With Live Releases
5. 1 In 5 Applications Get Approved
6. Not For Beginners. For Serious Artists.
7. Spotify Catalog + Real Manager
8. Stop Uploading Alone — Apply Today
```

Description 1:
> AIR Music takes artists with 1,500+ monthly listeners and active release schedule. 5 spots per quarter. Apply with your Spotify link.

Description 2:
> Real personal manager. YouTube growth plan. Editorial pitching. Apply if you have 1+ release on Spotify and 1,500+ monthly listeners.

---

### ✅ Завдання 7 — Тижневий звіт від Андрія

Формат таблиці:

| Метрика | Минулий тиждень | Цей тиждень | Зміна |
|---------|----------------|-------------|-------|
| CPM | | | |
| CPC | | | |
| Meta Lead (старт бота) | | | |
| Meta TypebotCompleted | | | |
| CPL (cost per lead) | | | |
| **CPQL (cost per qualified lead)** | | | |
| Google Search Impressions | | | |
| Google Click-Through Rate | | | |
| Google Conversions | | | |

---

## A4. GOOGLE ADS — РОЗШИРЕНИЙ КОПІРАЙТ

### Заголовки (15 варіантів — Google ротує)
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

**D1:**
> AIR Music works only with artists who have 1+ release and 1,500+ monthly listeners. Personal manager. Real strategy. 5 spots per quarter. Apply with your Spotify link.

**D2:**
> Tired of distributors that don't reply? Get a personal manager who responds within 24 hours, reviews your catalog, and builds a 90-day growth plan. Apply today.

**D3:**
> Not a DIY platform. AIR Music is selected music distribution for serious OPM artists. 1 in 5 applications approved. Editorial pitching, YouTube setup, real growth.

**D4:**
> Stop guessing what to do next. Get a real manager who knows your music, your goals, your market. Apply if you have releases on Spotify and 1,500+ monthly listeners.

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

## Б1. СТРАТЕГІЯ — призначення лендингу artists-check

Сторінка має **ІНШИЙ кут продукту**, ніж PM. Це не дублікат:
- **PM лендинг** = "Get a personal manager" (комплексне рішення)
- **CMT лендинг** = "Check your track for technical issues" (точкова послуга)

CMT — це **хук-сервіс** який має конвертити в PM. Артист приходить за безкоштовною перевіркою → менеджер пише з результатом → пропонує підписатися.

### Що це означає для правок
- На лендингу CMT **фільтрація легша** (Google трафік — пошуковий intent)
- АЛЕ потрібно прибрати елементи які **навмисно приваблюють beginner**
- І додати чіткий шлях `Track Check → Personal Manager`

---

## Б2. Лендинг artists-check — детальні правки

**Сторінка:** https://air.io/en/artists-check
**Дата:** 2026-05-08

### СЕКЦІЯ 1 — HERO

**🔴 Залишити H1:** Don't Release Blind
*(Цей H1 непогано фільтрує — beginner ще не "релізить", тому ця фраза для нього не резонує.)*

**🔴 ЗАМІНИТИ підзаголовок:**
> GET YOUR FREE TRACK SAFETY REPORT IN 48H

**🟢 НА:**
> A REAL MANAGER REVIEWS YOUR TRACK. 48-HOUR TURNAROUND.

**Чому:** Слово "FREE" у головному екрані — головний магніт для beginner. Замінюємо на "Real Manager" — це фільтр (показує що це не автоматизовано).

**🔴 ЗАМІНИТИ body:**
> Rejected releases. Delayed royalties. Platform flags. We catch them first.

**🟢 НА:**
> Rejected releases. Delayed royalties. Content ID claims. Metadata errors. We catch them before your next release goes live.

**🟢 ДОДАТИ перед CTA:**
> *For artists with at least 1 release on Spotify or Apple Music.*

**CTA — залишити:** CHECK MY TRACK NOW

---

### СЕКЦІЯ 2 — "Is Something Breaking in Your Setup?"

**Картки болю — ЗАЛИШИТИ ПОВНІСТЮ БЕЗ ЗМІН.**

Чому: всі 6 болів **пресуппонують** наявність релізів:
- "Releases stuck in limbo" — у тебе вже є релізи
- "Content ID claims" — лише якщо в тебе є музика на платформах
- "Platform penalties" — те ж саме
- "Working money..." — вже отримав роялті
- Це секція сама по собі сильний фільтр.

---

### СЕКЦІЯ 3 — "What Happens When We Check Your Track"

**ЗАЛИШИТИ БЕЗ ЗМІН.** Технічна деталізація — добре. Кваліфіковано і професійно.

---

### СЕКЦІЯ 4 — Status outcomes (Safe / Fixable / High Risk)

**🟢 ДОДАТИ під трьома статусами додатковий рядок (під "You'll have your report in 24-48 hours"):**

> If we see real potential — your dedicated manager will personally reach out about the next step.

**Чому:** показує що Track Check — це двері до PM, а не окрема послуга.

CTA блок — залишити.

---

### СЕКЦІЯ 5 — "Trusted by Artists Worldwide"

**ЗАЛИШИТИ БЕЗ ЗМІН.** Цифри сильні (5,500+ / 100+ / 7 years / 105K+).

---

### СЕКЦІЯ 6 — "Hear from Artists Who Stopped Guessing"

**🚀 ВЕЛИКА НОВИНА:** На цьому лендингу ти вже маєш **реальні цифри** для Rian DTM:
> Rian DTM — 69,000 → 213,000 Monthly Listeners

**ВИКОРИСТАЙ ЦІ ЦИФРИ ТАКОЖ НА PM-ЛЕНДИНГУ** (оновити інструкцію розробника).

### Тестимоніал Rian DTM
**ЗАЛИШИТИ БЕЗ ЗМІН.** Підпис "Electronic Artist · 69,000 → 213,000 Monthly Listeners" — ідеальний.

### Тестимоніал Farhad (FH360)
**🔴 ЗАМІНИТИ підпис:**
> Farhad (FH360) · Independent Artist

**🟢 НА:**
> Farhad (FH360) · Electronic Artist

(Прибрати "Independent" — слово приваблює DIY-аудиторію)

### Тестимоніал Angga
**🔴 ЗАМІНИТИ підпис:**
> Angga · Independent Artist

**🟢 НА:**
> Angga · Electronic Artist · Indonesia

---

### СЕКЦІЯ 7 — "Get Your Free Track Safety Check Before It's Too Late"

**🔴 ЗАМІНИТИ заголовок:**
> Get Your Free Track Safety Check Before It's Too Late

**🟢 НА:**
> Get Your Track Safety Check Before It's Too Late

**Чому:** Прибираємо "Free" з заголовка великого блоку. Залишаємо це слово ТІЛЬКИ внизу як примітку.

**ЗАЛИШИТИ body** "One wrong sample. One metadata error. One Content ID flag — and your release is stuck. Don't wait until it happens." — добре, технічне.

**CTA — залишити:** CHECK MY TRACK NOW

---

### СЕКЦІЯ 8 — "How to Start" (3 кроки)

**Step 1 — Submit Your Track:**
**🔴 ЗАМІНИТИ:** Upload your link and answer questions about ownership and samples.
**🟢 НА:** Share your Spotify link, current monthly listeners, and the track you want checked.

**Step 2 — Get Your Safety Report (24-48h):**
**ЗАЛИШИТИ БЕЗ ЗМІН.**

**Step 3 — Know My Status:**
**🟢 ДОДАТИ четвертий пункт під 3-ма статусами:**
> If we see growth potential — your dedicated manager will reach out about the next step.

---

### 🚨 СЕКЦІЯ 9 — "Exclusive Perks for New Artists" — НАЙБІЛЬША ПРОБЛЕМА

**Цей блок ВЗАГАЛІ суперечить нашій стратегії!**

Зараз:
> Exclusive Perks for New Artists
> Artists who pass the Safety Check and join AIR Music this month receive:
> ONE GUARANTEED OFFICIAL EDITORIAL PITCH for their next single
> PRIORITY ONBOARDING with a dedicated manager
> Free · 24-48h · For independent artists only

**🔴 ПОВНІСТЮ ПЕРЕПИСАТИ цю секцію:**

**🟢 НА:**
> # What You Get After Approval
>
> Artists who pass the Safety Check and qualify for AIR Music receive:
>
> **ONE EDITORIAL PITCH FOR YOUR NEXT SINGLE** — submitted to platform curators
>
> **PRIORITY ONBOARDING WITH YOUR DEDICATED MANAGER** — real person, knows your catalog
>
> [CTA: CHECK MY TRACK NOW]
>
> *24-48h Safety Report. We approve about 1 in 5 applications.*

**Що ВИДАЛИТИ:**
- "Exclusive Perks for **New Artists**" → "What You Get **After Approval**"
- "**Free**" → видалити з підпису
- "**For independent artists only**" → видалити (звучить як для DIY)
- "**Guaranteed**" editorial pitch → "**An**" editorial pitch (Spotify забороняє слово guaranteed)
- "**Every day without a safety check is a day you're risking your release**" → **залишити**, це добре працює

---

### СЕКЦІЯ 10 — "Level Up Your Knowledge" (блог)

**🔴 ВИДАЛИТИ статтю:**
> "How to Distribute Your Music for Free in the Philippines"

**Чому:** Заголовок з "Free" і "Distribute" — прямий магніт для DIY-аудиторії. Ця стаття приведе на сайт людей які НЕ конвертяться у замовлення.

**🟢 ЗАМІНИТИ на статтю:**
> "Why Mid-Tier Artists Get Stuck at 5K Monthly Listeners (And How to Break Through)"
> або
> "5 Signs Your Distributor Is Holding You Back"

Якщо нової статті ще немає — просто прибрати цю.

**Інші 2 статті залишити:**
- "How Not to Lose Royalties Because of a Single Metadata Error" — фільтрує добре
- "How to Upload Music to All Major Platforms" — нейтрально

---

### СЕКЦІЯ 11 — FAQ

**ЗАЛИШИТИ БЕЗ ЗМІН.** Питання правильні, технічні, фільтруючі за замовчуванням.

---

### СЕКЦІЯ 12 — Фінальний блок "AIR Music works with artists who are ready to grow"

**🔴 ЗАМІНИТИ H2:**
> AIR Music works with artists who are ready to grow — is that you?

**🟢 НА:**
> AIR Music works with serious artists ready to grow past 5K listeners — is that you?

**ЗАЛИШИТИ Taglish frase:**
> Stop uploading and hoping for the best
> Kayang-kaya mo 'to! 🚀

---

### Підсумок змін на лендингу artists-check

**Заміна тексту:** 8 елементів
**Видалення:**
- Слово "Free" з 3 місць (hero subtitle, секція 7 H2, секція 9 perks)
- Стаття "Distribute for Free" з блогу
- "For New Artists" і "For independent artists only"
**Додавання:**
- Поріг 1+ release на головній
- Шлях "Manager will reach out" у двох місцях
- "Past 5K listeners" в фінальному блоці

**Без змін:** ~70% сторінки

---

## Б3. Check My Track — Meta креативи

### Стратегічне рішення: ВИМКНУТИ Check My Track на Meta

**Дані за 6-7 тижнів:**
| Канал | Lead | MQL | Opportunity | Lead→Opp |
|-------|------|-----|-------------|----------|
| FB Check My Track | 23 | 6 (26%) | 1 | **3%** |
| FB Personal Manager | 25 | 19 (76%) | 1 | 4% |
| Google #1 | 9 | 6 (67%) | 2 | 12% |
| Google #2 | 7 | 12 (171%) | 3 | 12.5% |

**Висновки:**
1. CMT на FB має найгіршу MQL conversion (26% vs 76% для PM)
2. CMT і PM на FB конкурують за одну й ту ж аудиторію
3. На бюджеті $20/день немає сенсу тримати 2 кампанії

**ACTION:** Зупинити Check My Track Meta. Залишити в Google.

### Якщо ВСЕ Ж вирішиш залишити CMT на Meta — топ-2 креативи з 6 концептів

#### CREATIVE 1 — "$800 vs $47" (Concept 1, карусель)
**Чому: ** Найсильніший фільтр через число. Beginner з 100 streams не впізнає $800 vs $47 — це для тих хто вже отримує роялті.

**Primary Text (фінальна версія):**
> Two artists. Same streams. Same platform. Same release week. One made $800. One made $47. The difference isn't talent — it's what's sitting behind the release. Rights registered. Content ID set up correctly. Metadata clean. One artist knew what to check. The other didn't. No platform sends you an error message. You just see the number. Find out which artist you are — before your next release. For artists with releases on Spotify.

**Headline:** Same streams. Different money.
**CTA:** Get A Track Safety Check

#### CREATIVE 2 — "STOP UPLOADING. START RELEASING." (Concept 6, карусель)
**Чому:** Identity-based фільтр. "Serious artists don't guess" — beginner не ідентифікує себе як serious yet.

**Primary Text:**
> Most artists hit 'Upload' and pray. Release it. Promote it. Hope for the best. But serious artists don't guess. They verify before they drop. One small technical issue — wrong metadata, a rights conflict, a hidden Content ID flag — can kill momentum before it even starts. You worked too hard on this track to leave it to chance. For artists with active release schedule.

**Headline:** Serious artists don't guess.
**CTA:** Get My Safety Check

### Що ВИКЛЮЧИТИ з 6 концептів CMT
- **Concept 2 "Someone is collecting your money"** — fearmongering, низька якість лідів
- **Concept 3 "47 views"** — занадто схоже на Concept 1
- **Concept 4 "Comparison with others"** — порівняння може демотивувати
- **Concept 5 "7-day window"** — урgency без фільтрації

### По існуючих креативах CMT (зі скріншотів)
- **"RELEASE STILL 'PROCESSING'?"** — добре, залишити
- **"100% ROYALTIES SOUNDS GREAT"** — добре, залишити
- **"BEFORE YOU DROP — CHECK YOUR TRACK"** — нейтрально, можна залишити
- **"RELEASE STUCK IN 'REVIEW'?"** — слабкіше, можна виключити

### Як адаптувати соц-медіа креативи (з твоїх 8 пунктів)
**Усі правки які ти описала — підтверджую. Але також:**

Замість generic "Free Track Safety Check" в CTA — використати варіанти що **ФІЛЬТРУЮТЬ**:
- "Track Safety Check For Active Releases"
- "Get a Pro Track Audit"
- "48h Track Audit by AIR Manager"

Слово "Free" у CTA знижує якість. Замінюємо на "48h" або "Pro".

---

## Б4. Check My Track — Google Ads (ЗАЛИШАЄМО, ПОСИЛЮЄМО)

### Чому залишаємо
Google Search працює — там прямий intent ("get my track reviewed", "submit track for feedback"). Це 12% Lead→Opportunity vs 3% на Meta.

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

### Descriptions (3 варіанти)

**D1:**
> Real AIR Music manager listens to your Spotify track and gives you honest feedback in 24-48 hours. Not a bot. For artists with 1+ release on Spotify.

**D2:**
> Stop wondering why your track isn't growing. A real music industry manager reviews your catalog, current numbers, and tells you exactly what to fix.

**D3:**
> Get an honest opinion from a music industry pro. Real listening, real feedback, real next steps. Submit your Spotify track today.

### Мінус-слова (Check My Track-специфічні)

Базовий список (як для PM) + додатково:
```
song lyrics, song meaning, song download
karaoke, instrumental, sing along
free music app, music player
free track download
```

---

# ЧАСТИНА В — ВПРОВАДЖЕННЯ

---

## Послідовність робіт

### Тиждень 1
**Day 1-2:**
- Андрій: створює подію `TypebotCompleted` у Meta + CAPI
- Маркетолог: збирає monthly listeners для тестимоніалів (Rian, Farhad, Angga)
- Розробник: вносить правки на лендинг artists-manager (за окремою інструкцією на Drive)

**Day 3-4:**
- Розробник: новий Typebot (4 питання)
- Дизайнер: 4 нові креативи (3 carousel + 1 static)

**Day 5-6:**
- Андрій: запускає нову кампанію PM з TypebotCompleted
- Андрій: зупиняє Check My Track на Meta
- Андрій: оновлює Google Ads (мінус-слова + нові headlines)
- Маркетолог: перевіряє наскрізну воронку (клік → лендинг → Typebot → HubSpot)

**Day 7:**
- Перший контрольний звіт. Перевірка що події приходять у Meta + HubSpot.

### Тиждень 2
- Збір даних. **Жодних змін** — даємо алгоритму час.
- Маркетолог: працює з Check My Track лендингом (надсилає скріншоти).

### Тиждень 3
- Аналіз: CPQL, % MQL, % дискваліфікації, Lead→Opportunity
- Виключити 2 слабкі креативи, додати 1-2 нові на тест
- Якщо CPQL < $20 → масштабувати до $30/день

### Тиждень 4
- Lookalike (якщо база > 100 якісних лідів)
- Оптимізація креативів — залишаємо top 2
- Звіт по 4-тижневих результатах

---

## Метрики (тижневий звіт)

| Метрика | Поточна | Ціль 4 тижні |
|---------|---------|--------------|
| CPL Meta | ~$5 | <$5 |
| **CPQL Meta** | не вимірюється | **<$20** |
| % дискваліфікації в Typebot | 0% | **>40%** |
| % MQL з кваліфікованих | 42% | **>65%** |
| **Lead → Opportunity** | 3% | **>12%** |
| Час у Typebot | 4-5 хв | <2 хв |
| Drop-off Typebot | ~40% | <15% |

---

## Чого НЕ робити (нагадування)

❌ Не дробити бюджет на багато кампаній
❌ Не запускати ретаргетинг (база <500 — Meta не запустить)
❌ Не робити lookalike до 100 якісних лідів
❌ Не повертати Check My Track на Meta до стабілізації PM
❌ Не міняти Typebot після запуску — мінімум 2 тижні зібрати дані
❌ Не міняти креативи кожні 3 дні — алгоритму потрібно 7 днів навчатися
❌ Не piднімати бюджет до стабілізації CPQL

---

## Контрольні точки

**📍 День 7:** Перевірка що всі події приходять. Якщо ні — стоп, фікс, перезапуск.

**📍 День 14:** Перший аналіз CPQL і % дискваліфікації. Якщо CPQL > $30 — переглянути таргетинг.

**📍 День 28:** Фінальна оцінка. Якщо метрики досягнуті — масштабувати. Якщо ні — зробити post-mortem і змінити підхід.

---

## Файли і документи на Google Drive

1. **Лендинг artists-manager — інструкція для розробника**
   https://docs.google.com/document/d/1ijEkZ_-Z7eLroeXCJdYX48gkzoV6YmhsAHgbuCL-eSA/edit

2. **Цей майстер-план** (поточний документ)

3. **Лендинг artists-check** — буде створений після отримання скріншотів

---

*Дата: 2026-05-08*
*Автор: AIR Music marketing team (Nataliia + Claude)*
