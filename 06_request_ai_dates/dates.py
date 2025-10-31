# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale # para manejar localizacion de fechas
import os
os.system("cls")

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # para que las fechas salgan en español

now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora específica
specific_date = datetime(2025,12,25,0,0,0)
print(f"Fecha específica: {specific_date}")

# 3. Formatear fechas y horas. metodo strftime(), le pasas el objeto datetime y el formato especificado. EL formato lo puedes sacar de la documentacion oficial de python
format_date = now.strftime("%A/%B/%Y %H:%M:%S") # si pones la Y minusculas, el año te saldra con dos digitos
print(f"Fecha formateada: {format_date}")

# 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)

yesterday = datetime.now() - timedelta(days=1) # se puede hacer con 0.5 que es medio dia
print(f"Ayer fue: {yesterday.strftime('%d/%m/%Y %H:%M:%S')}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana será: {tomorrow.strftime('%d/%m/%Y %H:%M:%S')}")

one_hour_later = datetime.now() + timedelta(hours=1)
print(f"Dentro de una hora será: {one_hour_later.strftime('%d/%m/%Y %H:%M:%S')}")

# 5. Obtener componentes individuales de una fecha
year = now.year
print(f"Año actual: {year}")

month = now.month
print(f"Mes actual: {month}")

# 6. Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2024,1,1,0,0,0)
difference = date2 - date1
print(f"Diferencia: {difference}")

