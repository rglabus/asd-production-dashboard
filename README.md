# 📊 ASD Production Dashboard

Interaktywny panel analityczny czasu produkcji oparty na danych z systemu Redmine. Aplikacja umożliwia monitorowanie wskaźników KPI, weryfikację wydajności procesów oraz filtrowanie kaskadowe z wbudowaną bramką jakościową walidującą strukturę plików CSV. 
ps. aplikacja jest aplikacją z przetwarzaniem wsadowym (Batch Processing Application). Oznacza, że dane nie są strumieniowane na żywo, lecz przetwarzane w gotowych pakietach (zrzutach CSV). Aplikacja sterowana API (API-Driven / API-Integrated Application) z danymi np Redmine do ewentualnego wykonania...

---

### 🚀 Dostęp do Aplikacji
👉 **[Otwórz ASD Production Dashboard](https://asd-appuction-dashboard-m884wzqztd4kscjyozb5ub.streamlit.app/)**

### 📁 Dane Testowe
Ze względów bezpieczeństwa dane produkcyjne nie są przechowywane w repozytorium, dodatkowo zmieniono w nim nazwiska osób opracujących na produkcji. Do przetestowania działania panelu pobierz przygotowany plik testowy:
📥 **[Pobierz plik testowy CSV (Google Drive)](https://drive.google.com/file/d/1t7SrsDdKAat916rTEx-8NZGSANT0u6g1/view?usp=sharing)**
---

### 🛠️ Stos Technologiczny
* **Python 3.11+**
* **Streamlit** – interfejs użytkownika i wdrożenie w chmurze
* **Pandas** – transformacja i czyszczenie struktur danych
* **Plotly Express** – dynamiczne wykresy i wskaźniki KPI