import json
from pydantic import ValidationError
from alien_contact import AlienContact  # Ձեր ստեղծած մոդելը
from generated_data.alien_contacts import ALIEN_CONTACTS
# Բեռնում ենք գեներացված տվյալները


# Փորձում ենք վալիդացնել յուրաքանչյուրը
for data in ALIEN_CONTACTS:
    try:
        report = AlienContact(**data)
        print(f"✅ Հաջողվեց վալիդացնել՝ {report.contact_id}")
    except ValidationError as e:
        print(f"❌ Սխալ {data.get('contact_id')}-ի համար՝ {e.errors()[0]['msg']}")