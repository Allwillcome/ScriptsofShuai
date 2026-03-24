## ¿Qué son HRV y Estrés?

- HRV (Variabilidad de la Frecuencia Cardíaca) son datos fisiológicos objetivos que miden las diferencias sutiles entre los intervalos de latidos. PeakWatch utiliza RMSSD como método de cálculo de HRV predeterminado, con unidades en ms (milisegundos). Esto difiere del cálculo de variabilidad de frecuencia cardíaca de Apple Health, que utiliza SDNN, resultando en valores diferentes.
- Estrés es un valor de referencia derivado por PeakWatch al combinar la frecuencia cardíaca y la distribución histórica de HRV para ayudar a evaluar el estado de estrés de su cuerpo. La unidad es %, que va del 1% al 100%. Valores más altos indican mayor estrés corporal.

## ¿Cuál es la relación entre HRV y Estrés?

HRV y Estrés están unificados. Cuando los valores de HRV están disponibles, el estado de HRV corresponde al nivel de Estrés.
Durante el día, los rangos de puntuación de Estrés son:
- Excelente: 1%-20%
- Normal: 20%-60%
- Elevado: 60%-80%
- Sobrecarga: 80%-100%

Los estándares durante el sueño difieren.

## ¿Cuándo debe usar HRV vs Estrés?

Bajo la configuración predeterminada de Apple Watch, HRV se actualiza cada 2-5 horas. En algunos países y regiones donde la función de fibrilación auricular de Apple Watch no se puede habilitar, la frecuencia de actualización de HRV está limitada. Además, habilitar la función de fibrilación auricular consume más batería.
Por lo tanto, diseñamos la función de Estrés, que se actualiza cada 6 minutos. Esto compensa la lenta velocidad de actualización de HRV hasta cierto punto, y en la mayoría de los casos, las tendencias de Estrés se alinean con las tendencias de HRV.
