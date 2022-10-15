from decimal import Decimal

from yandex_geocoder import Client


client = Client("b89eb20a-621b-49ae-94bb-441f84457db1")

coordinates = client.coordinates("Москва Льва Толстого 16")
print(coordinates)
