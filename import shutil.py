import shutil
total, usado, libre = shutil.disk_usage("/")
total_gb = total / (1024 ***3)
usado_gb = usado / (1024 ***3)
libre_gb = libre / (1024 ***3)

porcentaje_usado =(usado/total) * 100
porcentaje_libre =(libre/total) * 100

print("===============REPORTE DE ALMACENAMIENTO========")
print(f' Espacio total: {total_gb:.2f} GB')
print(f' Espacio total: {usado_gb:.2f} GB')
print(f' Espacio total: {libre_gb:.2f} GB')


