## What Are HRV and Stress?

- HRV (Heart Rate Variability) is objective physiological data that measures the subtle differences between heartbeat intervals. PeakWatch uses RMSSD as the default HRV calculation method, with units in ms (milliseconds). This differs from Apple Health's heart rate variability calculation, which uses SDNN, resulting in different values.
- Stress is a reference value derived by PeakWatch by combining heart rate and HRV historical distribution to help assess your body's stress state. The unit is %, ranging from 1% to 100%. Higher values indicate greater body stress.

## What Is the Relationship Between HRV and Stress?

HRV and Stress are unified. When HRV values are available, the HRV status corresponds to the Stress level.
During daytime, Stress score ranges are:
- Excellent: 1%-20%
- Normal: 20%-60%
- Elevated: 60%-80%
- Overload: 80%-100%

The standards during sleep differ.

## When Should You Use HRV vs Stress?

Under Apple Watch's default settings, HRV updates every 2-5 hours. In some countries and regions where Apple Watch's atrial fibrillation feature cannot be enabled, HRV update frequency is limited. Additionally, enabling the atrial fibrillation feature consumes more battery.
Therefore, we designed the Stress feature, which updates every 6 minutes. This compensates for HRV's slow update speed to some extent, and in most cases, Stress trends align with HRV trends.
