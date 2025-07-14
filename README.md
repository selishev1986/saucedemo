# 🧪 SauceDemo UI Test Automation Framework

Dieses Projekt automatisiert UI-Tests für die [SauceDemo-Webanwendung](https://www.saucedemo.com/) mit **Playwright** und **Python**. Es verwendet das **Page Object Model (POM)**, um die Testlogik sauber zu strukturieren und die Wartbarkeit zu verbessern.
Für Reports zu erstellen können, nutzt es pytest-html.

---

## 📦 Projektstruktur

```plaintext
sauce/
├── test_data/              # Ein Ordner für zukunftige APIs Tests
│
├── test_data/              # Zugangsdaten für verschiedene Nutzertypen
│   └── access_data.py
│
├── ui/
│── constants/
│        ├── constants.py    # Constants wie urls usw.
│
│── pages/                   # Page Objects für Login, Produkte, Warenkorb, Checkout und etc.
│       ├── cart_page.py
│       ├── checkout_complete_page.py
│       ├── checkout_step_one_page.py
│       ├── checkout_step_two_page.py
│       ├── login_page.py
│       ├── product_page.py
│       ├── products_page.py
│
├── tests/                   # Testfälle für verschiedene Szenarien
│   ├── test_add_to_cart_from_all_products_page_different_users.py
│   ├── test_add_to_cart_from_product_card_different_users.py
│   ├── test_cancel_checkout_from_step_one_different_users.py
│   ├── test_cancel_checkout_from_step_two_different_users.py
│   ├── test_checkout_different_users.py
│   ├── test_continue_shopping_different_users.py
│   ├── test_login_different_users.py
│   ├── test_logout_different_users.py
│   ├── test_remove_product_from_all_products_page_different_users.py
│   ├── test_remove_product_from_cart_different_users.py
│   ├── test_remove_product_from_product_card_different_users.py
│
├── utils/                  # Ein Ordner für zukunftige utils
│
│── conftest.py             # Pytest-Fixture für Browser-Setup
│
│── report.html             # Pyreporst - Report von letzte alle Tests Durchführung
```

---

## 🚀 Features

- Login/Logout-Tests für verschiedene Nutzertypen (Standard, Problem, Performance)
- Produktseite: Hinzufügen und Entfernen von Artikeln
- Warenkorb-Validierung
- Checkout-Prozess mit Adressdaten
- Nutzung von `pytest.mark.parametrize` für datengesteuerte Tests
- Modularer Aufbau mit Page Object Pattern
- HTML-Testreport mit `pytest-html`

---

## 🛠️ Installation

```bash
# Repository klonen
git clone https://github.com/selishev1986/Sauce.git
cd Sauce

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

---

## ▶️ Tests ausführen

```bash
# Alle Tests ausführen
pytest sauce/ui/tests/  --template=html1/index.html --report=report.html

# Einzelnen Test ausführen
pytest sauce/ui/tests/test_login_different_users  --template=html1/index.html --report=report.html
```

---

## 📚 Technologien

- [Playwright](https://playwright.dev/python/)
- Python 3.11+
- Pytest
- Page Object Model (POM)
- HTML-Reporting mit `pytest-html`

---

## 👨‍💻 Autor

**Vadim Selishchev**  
Senior Test Automation Engineer  
📍 Erlangen, Deutschland  

---

## 📄 Lizenz

Dieses Projekt steht unter keiner expliziten Lizenz.

```
