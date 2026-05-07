# AIR Music Distribution — маркетинговий контекст

> Робочий файл для Наталії. Зберігає весь контекст по рекламним кампаніям AIR Music щоб не втрачати при нових сесіях.
> Дата створення: 2026-05-07

---

## 1. Продукт

**AIR Music Distribution** — частина AIR Media-Tech (10+ років на ринку, 5,500+ артистів).

Дистрибуція музики для електронних/OPM артистів з персональним менеджером.

**Ключові переваги:**
- Персональний менеджер (відповідь до 24 год)
- Revenue split 70/30 (артисту/AIR), $0 setup fee
- YouTube Content ID — головна сильна сторона
- 100% rights retention
- Дистрибуція на 100+ платформ (Spotify, Apple Music, TikTok, YouTube Music, Amazon)
- Перші виплати — 3-4 міс, далі щомісяця

**Чого не робить:** не гарантує результати, не приймає масовий AI-контент, не масова дистрибуція.

---

## 2. Ринки і аудиторія

### Ринки
- **Електронна музика:** DE, NL, UK, FR, ES, IT, US, BR, MX, CA
- **SEA (стратегічний фокус):** Філіппіни, Малайзія, Індонезія
- **Поточні рекламні кампанії:** Філіппіни (Meta + Google)

### Цільова аудиторія
**Основна:**
- Mid-tier артисти: 1,500–500K monthly listeners на Spotify, активний графік релізів
- Indie лейбли: 5–20 артистів у каталозі

**Друга (lower priority):** початківці 0-50K — освітня воронка, не основний продукт

### Жанри (Tier 1)
Tech House, Melodic Techno (для електронної ніші)
OPM, Pop, R&B (для PH ринку)

---

## 3. Конкуренти

| Конкурент | Ціна | Підтримка | Позиція |
|-----------|------|-----------|---------|
| DistroKid | $22-36/рік | Майже відсутня | Масовий DIY |
| Ditto Music | $19-99/рік | Слабка | Середній DIY |
| TuneCore | $15-50/реліз | Повільна | Втрачає частку |
| CD Baby | $50 + 9% | Занепадає | Преміум |
| Symphonic | Корпоративна | Висока | Закриті двері |

**Позиція AIR:** human-first сервіс з персональним менеджером — між дешевим DIY і закритим преміумом.

---

## 4. Поточний стан реклами (станом на травень 2026)

### Платформи
- **Meta (Facebook/Instagram):** $20/день загальний бюджет
- **Google Ads:** ~$10/день на кампанію

### Кампанії на Meta
**1. Personal Manager** — 4 креативи:
- Carousel Stop, Carousel, Another Distributor, DIY

**2. Artist Check (Check My Track)** — 6 креативів:
- video technical safety, royalties carousel/static, release stuck static/carousel, video not beginner anymore

### Кампанії в Google
- 2 кампанії "SC_AIR_Music" (Personal Manager + Check My Track)

### Воронка
Реклама → Лендинг → Typebot → HubSpot → Менеджер у WhatsApp

**Лендинги:**
- https://air.io/en/artists-manager (для Personal Manager)
- https://air.io/en/artists-check (для Check My Track)

**Typebot:**
- Check My Track: 3 питання (OK)
- Personal Manager: 8 питань (ЗАБАГАТО — треба до 4)

---

## 5. Результати за 6-7 тижнів (з 23.03.26)

**Загалом: 113 контактів**

| Кампанія | Lead | MQL | Opportunity | Bad |
|----------|------|-----|-------------|-----|
| FB Check My Track | 23 | 6 (20%) | 1 (3%) | — |
| FB Personal Manager | 25 | 19 (42%) | 1 (2%) | — |
| Google #1 | 9 | 6 (35%) | 2 (12%) | — |
| Google #2 | 7 | 12 (50%) | 3 (12.5%) | 2 |

### Ключовий висновок
- **Google конвертує в Opportunity у 4-6 разів краще за Facebook** (12% vs 2-3%)
- Facebook генерує лідів, але майже всі — початківці (не цільова аудиторія)
- Більшість креативів на Meta показують "Недостатньо результатів" — фрагментація бюджету

---

## 6. Головна проблема

**Приходять початківці, а не mid-tier артисти.**

### 3 кореневі причини
1. **Математика Meta:** при $20/день і ~10 кампаніях алгоритм ніколи не вчиться (потрібно 50 конверсій/тиждень/адсет)
2. **Копірайт не фільтрує** — "Check My Track" і "Personal Manager" звучать для всіх
3. **Невірна подія конверсії** — Meta оптимізує під клік/заповнену форму, а не під якісного ліда

---

## 7. План оптимізації (4 тижні)

### Стратегічний зсув
**Не покладатися на алгоритм Meta** (бюджет занадто малий) → **фільтрувати руками** через копірайт + Typebot + ключові слова.

### Тиждень 1
1. Зупинити "Check My Track" на Meta (залишити тільки в Google)
2. Скоротити Typebot Personal Manager з 8 до 4 питань:
   - Spotify URL
   - Monthly listeners (<500 / 500-1.5K / 1.5K-10K / 10K+)
   - Релізи за 12 міс (0 / 1-2 / 3-5 / 6+)
   - Email + WhatsApp
3. Якщо <500 listeners АБО 0 релізів → дискваліфікація + nurture email
4. 3 варіанти копірайту з фільтром у першому реченні (Taglish + English + дискваліфікуючий)

### Тиждень 2 (завдання Андрію — PPC спеціаліст)
**Meta:**
- Створити кастомну подію `TypebotCompleted` (не на старті, а на завершенні)
- Перепідключити кампанію на цю подію в Optimization & Delivery

**Google:**
- Search Terms Report → додати мінус-слова: free, download, beginner, first, how to record, tutorial, lyrics, karaoke, mp3
- Заголовки: додати "For artists with Spotify releases" / "1,500+ monthly listeners"

### Тиждень 3 — структура
**Meta:**
```
Кампанія: PM_Philippines_Qualified
└── Адсет: PH_Mid-Tier ($20/день)
    ├── Гео: Філіппіни
    ├── Вік: 22-42
    ├── Інтереси: BROAD
    ├── Виключення: music tutorial, how to make beats, FL Studio beginner
    └── Конверсія: TypebotCompleted
```

### Тиждень 4 — заміри
- **CPQL** (cost per qualified lead) → ціль <$20
- % дискваліфікації в Typebot → ціль >40%
- Lead → Opportunity → ціль >15%

---

## 8. Бюджетні обмеження

- **Meta:** $20/день загалом ($600/міс) — вже тестували $40, гірше працювало
- **Google:** $10/день на кампанію (можна підвищити)
- **Загальна логіка:** при таких бюджетах алгоритмічна оптимізація не працює — треба ручна фільтрація

---

## 9. Команда

- **Наталія Борська** — маркетолог (мова комунікації — українська)
- **Андрій** — PPC спеціаліст (відповідає за технічні налаштування Meta + Google)

---

## 10. Ключові файли на Google Drive

| Файл | ID | Що містить |
|------|-----|-----------|
| `AIR_Music_Electronic_Artists` | 1sHgOlHowospp1LhZnCtunEn95s08HeN44iI_UEASk4E | Пітч-дек для електронних артистів |
| `AIR_Music_Electronic_Artists_v2` | 1PWcTPCzjCtNb-GzrKeODhsyEk4g8-Pi4Hs2_mWPFP4s | Оновлена версія пітч-деку |
| `AIR_Music Marketing_Strategy_2026/2027` | 1Q-JiaMjN_eFM-4Bk4-m7kVhTqva6YoGJ | Стратегія SEA (PH/MY/ID) |
| `air_lead_quality_ua` | 1LYUNQU06VeL478DnU4U22zGF7V9QhMjuVxzfnd0efSM | **Ключове дослідження по якості лідів** |
| `AIR_Electronic_Research` | 1zBTKdXbPernjtkMLv16o4jy0u3V_69O4g7IsmN0GI5g | Дослідження electronic music ринку |

**Spreadsheets:**
- https://docs.google.com/spreadsheets/d/1Bim98Z-HOEQVEe6HA-3KvaQhZaGyyC65prhXXofodYo
- https://docs.google.com/spreadsheets/d/1zZYYJU1kmIiXMryC6-4FfNV9SOv4Nb9n

---

## 11. Ринкові інсайти PH

- **Spotify:** 71% APAC-стримерів сидять у PH, 75% Топ-50 — місцева OPM
- **TikTok:** двигун відкриття музики, mid-tier OPM артисти релізять у TikTok-friendly форматах
- **Платежі:** GCash, Maya, e-гаманці — стандарт (низьке проникнення кредиток)
- **CPM/CPC:** медіанний CPM ~$1.00-1.33, CPC ~$0.05-0.27 (дуже дешевий ринок)
- **Mobile-first** аудиторія
- **Taglish** (суміш тагальської + англ) працює краще за чисту англ для хуків

### Поведінкові сигнали для таргету
**OPM-артисти:** Bini, SB19, Ben&Ben, Moira dela Torre, Zack Tabudlo, Lola Amour, Maki, Denise Julia
**Лейбли/дистрибутори:** Underdog Music, Offshore Music, Viva Records
**Плейлисти:** Tatak Pinoy

---

## 12. Шаблони готового копірайту

### Meta — варіант A (Taglish)
> May 1,500+ monthly listeners ka na sa Spotify? We're taking 5 OPM artists this quarter for managed distribution. Real Pinoy manager. GCash payouts. Apply if you have at least 1 release.

### Meta — варіант B (English прямий)
> Not a beginner platform. AIR Music takes OPM artists with 1,500+ monthly listeners and an active release schedule. 5 spots per quarter. Apply with your Spotify link.

### Meta — варіант C (дискваліфікуючий)
> If your last release got under 500 streams — this isn't for you yet. AIR Music works with mid-tier OPM artists ready to scale from 2K to 10K listeners. Spots are limited.

---

## 13. Що НЕ робити зараз

- Не запускати ретаргетинг (аудиторії <500 — Meta не запустить)
- Не робити lookalike (потрібно 100+ якісних лідів в базі)
- Не підіймати бюджет на Meta поки не виправлена конверсійна подія
- Не дробити бюджет на багато кампаній

---

## 14. Майбутні етапи (після стабілізації якості)

1. **Lookalike 1-2%** — на основі поточних артистів AIR з PH (email-list)
2. **Ретаргетинг** — 3 аудиторії: Spotify URL ввели / Typebot почали / 75%+ відео переглянули
3. **Chartmetric/SongStats інтеграція** — менеджер бачить статистику артиста до першого контакту
4. **Офлайн-конверсії** — передача статусу "Accepted by Manager" / "Client" назад у Meta та Google
5. **Масштабування** до $30-40/день коли CPQL <$20 і Lead→Opportunity >15%
