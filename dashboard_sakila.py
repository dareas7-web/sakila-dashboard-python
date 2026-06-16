import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
	host="localhost",
	user="root",
	password="123qwasZ@",
	database="sakila"
)	

q1= "SELECT title, length,rating FROM film ORDER BY length DESC LIMIT 10;"
df1= pd.read_sql(q1,conn)

q2= """ 
SELECT c.name as categoria, SUM(p.amount) as ingresos_usd
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name ORDER BY ingresos_usd DESC;
"""
df2 = pd.read_sql(q2, conn)
conn.close()

with pd.ExcelWriter("dashboard_sakila.xlsx", engine="openpyxl")as writer:
    df1.to_excel(writer, sheet_name="Top Peliculas", index=False)
    df2.to_excel(writer, sheet_name="Ganancias", index=False)

print("Excel generado: dashboard_sakila.xlsx")
	




