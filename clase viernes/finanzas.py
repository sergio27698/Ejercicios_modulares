def precio_con_descuento(precio,porcentaje_descuento):
    descuento=precio*(porcentaje_descuento/100)
    return precio - descuento
def calcular_iva(precio):
    return precio * 0.13