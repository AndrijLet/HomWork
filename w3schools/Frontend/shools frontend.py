
# a = 3
#
#
# for i in range(10):
#     print(i)
#     if i == 5:
#         break

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def start_phone_traced(target):
    print("[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print("[*] Initiating trace...")

    # Парсимо номер
    p = phonenumbers.parse(target)

    # Локація
    location = geocoder.description_for_number(p, "uk")
    print(f"[+] Location: {location if location else 'Невідомо'}")

    # Оператор
    operator = carrier.name_for_number(p, "uk")
    print(f"[+] Carrier: {operator if operator else 'Невідомо'}")

    # Часові зони
    zones = timezone.time_zones_for_number(p)
    print(f"[+] Timezones: {', '.join(zones) if zones else 'Невідомо'}")

start_phone_traced("+1-553-7683")