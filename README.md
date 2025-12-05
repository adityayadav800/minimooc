## Setup & run
1. Create virtualenv:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip3 install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Run dev server:
   ```bash
   python manage.py runserver
   ```

## Notes
- Requires running postgres using default credentials in settings.py
