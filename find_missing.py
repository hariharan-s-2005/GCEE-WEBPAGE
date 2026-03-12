import os
from bs4 import BeautifulSoup

html_file = r'c:\GCEE-WEBPAGE\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

panels = soup.find_all(class_='dept-panel')
for panel in panels:
    dept_id = panel.get('id')
    staff_cards = panel.find_all(class_='scard')
    for card in staff_cards:
        avatar = card.find(class_='savatar')
        if avatar and not avatar.find('img'):
            print(f"Missing in {dept_id}:")
            print(card.prettify())
            print("-" * 40)
