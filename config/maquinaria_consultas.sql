# query para obtener la maquinaria
SELECT * FROM maquinaria

# query para obteenr total de horas trabajadas por maquinaria
SELECT maquinaria_id, SUM(horas_maquina) AS total_horas FROM registro_horas GROUP BY maquinaria_id

