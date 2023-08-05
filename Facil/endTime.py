""" 
The task is to prepare a simple code to evaluate or find the end time of a given time period, 
expressing it in hours and minutes. The start time is given as a pair of hours (0..23) and minutes 
(0..59). 

The result should be displayed in the console.

For example, if the event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

/--------------------------------------------------------------------------------------------------/

La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, 
expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). 

El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
"""

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')