lineas
linea1= c.create_line(0,0,BASE, ALTURA, fill="IndianRed2")
linea2= c.create_line(0,ALTURA, BASE,0, fill="IndianRed2")
linea3= c.create_line(BASE/2,0 , BASE/2,ALTURA, fill="blue")
linea4= c.create_line(0,ALTURA/2 , BASE,ALTURA/2, fill="blue")
for i in range(11):
   linea= c.create_line(0,ALTURA , BASE, 36*i, fill=["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])])
cuadrado y rectangulos
rect1 = c.create_rectangle(10,10,BASE/2-10,ALTURA/2-10, fill="pink",outline="red")
rect2=c.create_rectangle(10,10,110,110, fill="green")
poligonos
poli1=c.create_polygon(BASE/2,0, 0,ALTURA/2, BASE/2, ALTURA, BASE,ALTURA/2,fill="green", outline="red", width=5)