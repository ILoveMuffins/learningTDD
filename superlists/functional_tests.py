#!/usr/bin/env python3.4

from selenium import webdriver

browser = webdriver.Firefox()

# Edyta dowiedziala sie o nowej, wspanialej aplikacji w postaci listy rzeczy do zrobienia.
# Postanowila wiec przejsc na strone glowna tej aplikacji
browser.get('http://localhost:8000')

# Zwrocila uwage, ze tytul strony i naglowek zawieraja slowo "Listy".
assert 'Listy' in browser.title, "Tytuł okna przeglądarki: " + browser.title

# Od razu zostaje zachęcona, aby wpisać rzecz do zrobienia.

# W polu tekstowym wpisała "Kupić pawie pióra" (hobby Edyty
# polega na tworzeniu ozdobnych przynęt).

# Po naciśnięciu klawisza Enter strona została uaktualniona i wyświetla
# "1: Kupić pawie pióra" jako element listy rzeczy do zrobienia.

# Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania.
# Edyta wpisała "Użyć pawich piór do zrobienia przynęty" (Edyta jest niezwykle skrupulatna).

# Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia.

# Edyta była ciekawa, czy witryna zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej
# unikatowy adres URL, obok którego znajduje się pewien tekst z wyjaśnieniem

# Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy do zrobienia.

# Usatysfakcjonowana kładzie się spać.
browser.quit()

