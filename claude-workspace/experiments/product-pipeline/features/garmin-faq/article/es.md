# PeakWatch × Garmin Preguntas Frecuentes

PeakWatch ahora es compatible con la conexión de dispositivos Garmin.
Debido a diferencias en las capacidades de la plataforma, algunos datos o funciones pueden diferir ligeramente de lo que se muestra en Garmin Connect.

## 1. ¿Por qué no se muestran algunos datos (como oxígeno en sangre, frecuencia respiratoria, etc.)?

Si ciertas métricas no se muestran, prueba los siguientes pasos para solucionar problemas:

1. **Primero verifica si los datos existen en Garmin Connect**. Si Garmin Connect no tiene los datos registrados, PeakWatch tampoco podrá recuperarlos.
2. **Verifica si tu dispositivo es compatible con esa métrica**. Algunos modelos de relojes Garmin no admiten oxígeno en sangre, frecuencia respiratoria u otras funciones, por lo que no generarán datos correspondientes.
3. **Verifica si los datos se han sincronizado**. Si los datos existen en Garmin Connect pero no se muestran en PeakWatch, puede que aún no se hayan sincronizado. Intenta sincronizar manualmente tu reloj en Garmin Connect, luego desliza hacia abajo para actualizar en PeakWatch.

## 2. ¿Qué hacer si PeakWatch no tiene datos o los datos no coinciden con Connect?

**Pasos para solucionar problemas:**

1. **Confirma si la aplicación Garmin Connect tiene datos**
   - Abre la aplicación Garmin Connect y asegúrate de que los datos de tu reloj se hayan sincronizado con Connect
   - **Razón**: Solo al abrir la aplicación Connect, los datos del reloj pueden sincronizarse con Connect, permitiendo que PeakWatch los recupere

2. **Verifica si Garmin Web (nube) tiene datos**
   - Garmin China: https://connect.garmin.cn
   - Garmin Internacional: https://connect.garmin.com
   - Inicia sesión para verificar si tienes registros históricos completos
   - **Razón**: Los datos pueden existir localmente en la aplicación Connect pero no sincronizados en la nube; PeakWatch recupera datos de la nube

3. **Volver a sincronizar**
   - Si la nube de Garmin tiene datos pero PeakWatch no muestra ninguno o es inconsistente
   - Ve a PeakWatch > Configuración > Fuentes de datos > Garmin
   - Toca "Volver a sincronizar" para obtener los datos más recientes

Si Garmin Connect mismo no tiene datos, no se pueden ver a través de PeakWatch.

## 3. ¿Por qué los datos de hoy no se actualizan?

Los datos de Garmin necesitan sincronizarse primero con Garmin Connect antes de que PeakWatch pueda acceder a ellos.

Si los datos de hoy no se actualizan, prueba lo siguiente:

1. Abre la aplicación Garmin Connect
2. Desliza hacia abajo para actualizar o sincroniza tu reloj manualmente
3. Desliza hacia abajo en PeakWatch para ver los datos actualizados

## 4. ¿Por qué no veo muchos datos históricos después de conectar exitosamente?

La API de Garmin actualmente **solo puede recuperar los últimos 30 días de datos históricos**.

Si acabas de conectar tu cuenta de Garmin, PeakWatch solo puede sincronizar los datos de los últimos 30 días; los datos anteriores no se pueden recuperar debido a las limitaciones de la API de la plataforma de Garmin.

También asegúrate de haber habilitado los **Permisos de Datos Históricos**:

1. Abre Garmin Connect
2. Ve a Más > Configuración > Aplicaciones Conectadas
3. Encuentra PeakWatch
4. Confirma que los Permisos de Datos Históricos estén habilitados

## 5. ¿Por qué "Energía corporal" es diferente de "Body Battery" de Garmin?

El "Energía corporal" de PeakWatch utiliza el algoritmo propietario de PeakWatch para el cálculo.

La razón de este diseño:

- Permite el procesamiento unificado de datos de Garmin y Apple Watch
- Garantiza que los datos de diferentes fuentes de dispositivos se analicen en el mismo sistema
- Proporciona evaluaciones más consistentes y completas del estado de recuperación

Por lo tanto, los valores de Energía corporal de PeakWatch pueden diferir de los de Body Battery de Garmin; esto es normal.

## 6. ¿Por qué algunos detalles del entrenamiento se ven diferentes después de sincronizar con Garmin?

Debido a diferencias en las estructuras de datos de la plataforma, el contenido del entrenamiento puede tener algunos ajustes en los dispositivos Garmin, como:

- Algunos nombres de ejercicios de entrenamiento de fuerza pueden diferir
- Ejercicios individuales pueden ser reemplazados por otros similares
- Los estiramientos de calentamiento o enfriamiento en los entrenamientos de carrera pueden no mostrarse

Estos cambios se deben a diferencias de compatibilidad de la plataforma y no afectan la estructura general del entrenamiento.

## 7. ¿Por qué sincronizar planes de entrenamiento al reloj solo es compatible con cuentas internacionales de Garmin?

Actualmente **la función de sincronizar planes de entrenamiento al reloj solo es compatible con cuentas nacionales de Garmin**.

Dado que las cuentas internacionales de Garmin aún no nos han proporcionado las capacidades de API relevantes, actualmente no podemos implementar la sincronización directa de planes de entrenamiento al reloj.

Agregaremos soporte tan pronto como Garmin habilite estas capacidades.

## 8. ¿Cómo iniciar un entrenamiento en un reloj Garmin?

Después de sincronizar exitosamente tu plan de entrenamiento con Garmin, sigue estos pasos para iniciar un entrenamiento en tu reloj:

1. En la página de inicio de Connect, envía el curso de entrenamiento a tu reloj. Si no ves el curso en la página de inicio, ve a Más > Entrenamiento y Planes > Cursos de Entrenamiento para encontrarlo.
2. En la esfera del reloj, presiona el botón **START**
3. Selecciona el tipo de actividad correspondiente (carrera, entrenamiento de fuerza, etc.)
4. Mantén presionado **MENU**
5. Ve a **Training > Workouts**
6. Selecciona el entrenamiento que deseas hacer
7. Haz clic en **Do Workout**
8. Presiona **START** nuevamente para comenzar a registrar el entrenamiento

Una vez que comience el entrenamiento, tu reloj te guiará a través de cada paso, mostrando el ejercicio actual, objetivos o fases del entrenamiento.

## 9. Al usar un Garmin y un Apple Watch al mismo tiempo, ¿por qué los valores del widget de Apple Watch no son correctos?

Apple Watch solo puede acceder a datos de Apple Health y no puede obtener directamente datos de Garmin Connect. Por lo tanto, los datos que se muestran difieren de los del teléfono.

Sin embargo, los widgets de escritorio serán iguales a los del teléfono.
