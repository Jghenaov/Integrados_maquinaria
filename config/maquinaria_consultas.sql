# query para obtener la maquinaria
SELECT * FROM maquinaria

# query para obteenr total de horas trabajadas por maquinaria
SELECT maquinaria_id, SUM(horas_maquina) AS total_horas FROM registro_horas GROUP BY maquinaria_id

# Obtener maquiaria y mantenimientos
CREATE OR REPLACE VIEW vista_maquinaria_mantenimiento AS
SELECT 
    maq.id AS maquinaria_id,
    maq.nombre,
    maq.tipo,
    maq.modelo,
    maq.serie,
    maq.ubicacion,
    maq.fecha_adquisicion,
    maq.estado,
    m.tipo_mantenimiento,
    m.descripcion
FROM 
    maquinaria maq
LEFT JOIN 
    mantenimiento m ON maq.id = m.maquinaria_id;


	
SELECT * FROM vista_maquinaria_mantenimiento;
