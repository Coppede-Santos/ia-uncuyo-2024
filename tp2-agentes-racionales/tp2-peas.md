| Tipo de agente               | Medida de desempeño                                                        | Entorno                          | Actuadores                                | Sensores                                      |
|------------------------------|---------------------------------------------------------------------------|----------------------------------|-------------------------------------------|----------------------------------------------|
| Jugador de CS.               | Muertes, partidas ganadas, disparos acertados, daño recibido.              | Mapa, jugadores, objetos del mapa. | Movimiento, disparar, cambiar de arma.     | Cámara del avatar, barra de vida, minimapa.   |
| Explorador de océano.        | Superficie recorrida, choques.                                             | Océano, peces, rocas.            | Acelerador, freno, luces, lastres, timón.  | Sonar, cámaras, sensores del motor.           |
| Trader de tokens crypto.     | Ganancias netas.                                                           | Web de compra venta.             | Compra y venta de crypto.                  | Precio.                                       |
| Tenista.                     | Cantidad de pelotas que se devolvió, velocidad de la pelota.               | Cancha, red, pared, pelota.      | Brazos, piernas.                           | Cámara.                                       |
| Saltador.                    | Altura, tiempo en el aire.                                                 |                                  | Piernas, brazos, torso.                    | Cámara.                                       |
| Subastador.                  | Artículos comprados, precio, ganancias.                                    | Subasta, subastadores, objetos en venta. | Parlante.                                   | Ofertas, detalle del objeto a subastar.       |

- **Jugar al CS**:  
  - **Tipo**: Parcialmente observable  
  - **Agentes**: Multiagente   
  - **Dinámicas**: Dinámico  
  - **Espacio**: Continuo 

- **Explorar los océanos**:  
  - **Tipo**: Parcialmente observable  
  - **Agentes**: Multiagente  
  - **Dinámicas**: Dinámico  
  - **Espacio**: Continuo  

- **Comprar y vender tokens crypto**:  
  - **Tipo**: Parcialmente observable  
  - **Agentes**: Multiagente  
  - **Dinámicas**: Dinámico  
  - **Espacio**: Discreto  

- **Practicar tenis contra una pared**:  
  - **Tipo**: Parcialmente observable  
  - **Agentes**: Un solo agente  
  - **Dinámicas**: Estático  
  - **Espacio**: Continuo  

- **Realizar un salto de altura**:  
  - **Tipo**: Totalmente observable  
  - **Agentes**: Un solo agente  
  - **Dinámicas**: Estático  
  - **Espacio**: Continuo  

- **Pujar por un artículo en una subasta**:  
  - **Tipo**: Totalmente observable  
  - **Agentes**: Multiagente  
  - **Dinámicas**: Dinámico  
  - **Espacio**: Continuo  
