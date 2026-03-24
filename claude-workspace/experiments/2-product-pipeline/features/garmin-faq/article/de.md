# PeakWatch × Garmin FAQ

PeakWatch unterstützt jetzt die Verbindung mit Garmin-Geräten.
Aufgrund von Unterschieden in den Plattformfunktionen können einige Daten oder Funktionen geringfügig von dem abweichen, was in Garmin Connect angezeigt wird.

## 1. Warum werden einige Daten nicht angezeigt (z.B. Blutsauerstoff, Atemfrequenz usw.)?

Wenn bestimmte Metriken nicht angezeigt werden, versuchen Sie folgende Schritte zur Fehlerbehebung:

1. **Überprüfen Sie zuerst, ob die Daten in Garmin Connect vorhanden sind**. Wenn Garmin Connect diese Daten nicht aufgezeichnet hat, kann PeakWatch sie ebenfalls nicht abrufen.
2. **Überprüfen Sie, ob Ihr Gerät diese Metrik unterstützt**. Einige Garmin-Uhrenmodelle unterstützen keine Blutsauerstoff-, Atemfrequenz- oder andere Funktionen, daher werden keine entsprechenden Daten generiert.
3. **Überprüfen Sie, ob die Daten synchronisiert wurden**. Wenn die Daten in Garmin Connect vorhanden sind, aber nicht in PeakWatch angezeigt werden, wurden sie möglicherweise noch nicht synchronisiert. Versuchen Sie, Ihre Uhr manuell in Garmin Connect zu synchronisieren und dann in PeakWatch zum Aktualisieren zu ziehen.

## 2. Was tun, wenn PeakWatch keine Daten hat oder die Daten nicht mit Connect übereinstimmen?

**Schritte zur Fehlerbehebung:**

1. **Bestätigen Sie, ob die Garmin Connect App Daten hat**
   - Öffnen Sie die Garmin Connect App und stellen Sie sicher, dass Ihre Uhrendaten mit Connect synchronisiert wurden
   - **Grund**: Nur durch Öffnen der Connect App können Uhrendaten mit Connect synchronisiert werden, sodass PeakWatch sie abrufen kann

2. **Überprüfen Sie, ob Garmin Web (Cloud) Daten hat**
   - Garmin China: https://connect.garmin.cn
   - Garmin International: https://connect.garmin.com
   - Melden Sie sich an, um zu überprüfen, ob Sie vollständige historische Aufzeichnungen haben
   - **Grund**: Daten existieren möglicherweise lokal in der Connect App, aber nicht in der Cloud synchronisiert; PeakWatch ruft Daten aus der Cloud ab

3. **Erneut synchronisieren**
   - Wenn die Garmin Cloud Daten hat, PeakWatch aber keine anzeigt oder inkonsistent ist
   - Gehen Sie zu PeakWatch > Einstellungen > Datenquellen > Garmin
   - Tippen Sie auf "Erneut synchronisieren", um die neuesten Daten zu erhalten

Wenn Garmin Connect selbst keine Daten hat, können diese nicht über PeakWatch angezeigt werden.

## 3. Warum werden die heutigen Daten nicht aktualisiert?

Garmin-Daten müssen zuerst zu Garmin Connect synchronisiert werden, bevor PeakWatch darauf zugreifen kann.

Wenn die heutigen Daten nicht aktualisiert werden, versuchen Sie Folgendes:

1. Öffnen Sie die Garmin Connect App
2. Ziehen Sie zum Aktualisieren oder synchronisieren Sie die Uhr manuell
3. Ziehen Sie in PeakWatch zum Aktualisieren, um die aktualisierten Daten anzuzeigen

## 4. Warum sehe ich nach dem erfolgreichen Verbinden nicht viele historische Daten?

Die Garmin-API kann derzeit **nur die letzten 30 Tage an historischen Daten abrufen**.

Wenn Sie gerade Ihr Garmin-Konto verbunden haben, kann PeakWatch nur die Daten der letzten 30 Tage synchronisieren – ältere Daten können aufgrund der API-Einschränkungen der Garmin-Plattform nicht abgerufen werden.

Stellen Sie außerdem sicher, dass Sie die **Berechtigungen für historische Daten** aktiviert haben:

1. Öffnen Sie Garmin Connect
2. Gehen Sie zu Mehr > Einstellungen > Verbundene Apps
3. Finden Sie PeakWatch
4. Bestätigen Sie, dass die Berechtigungen für historische Daten aktiviert sind

## 5. Warum unterscheidet sich "Körperenergie" von Garmin "Body Battery"?

PeakWatch "Körperenergie" wird mit dem proprietären Algorithmus von PeakWatch berechnet.

Der Grund für dieses Design:

- Ermöglicht die einheitliche Verarbeitung von Daten von Garmin und Apple Watch
- Stellt sicher, dass Daten verschiedener Gerätequellen im selben System analysiert werden
- Bietet konsistentere und vollständigere Bewertungen des Erholungszustands

Daher können die Körperenergie-Werte von PeakWatch von Garmin's Body Battery abweichen – das ist normal.

## 6. Warum sehen einige Trainingsdetails nach der Synchronisierung mit Garmin anders aus?

Aufgrund von Unterschieden in den Plattformdatenstrukturen kann der Trainingsinhalt auf Garmin-Geräten geringfügig angepasst werden, z.B.:

- Einige Krafttrainings-Übungsnamen können unterschiedlich sein
- Einzelne Übungen können durch ähnliche ersetzt werden
- Aufwärm- oder Cool-Down-Dehnungen bei Lauftrainings werden möglicherweise nicht angezeigt

Diese Änderungen sind auf Plattform-Kompatibilitätsunterschiede zurückzuführen und beeinträchtigen nicht die Gesamtstruktur des Trainings.

## 7. Warum unterstützt das Synchronisieren von Trainingsplänen auf die Uhr nur Garmin-Internationalkonten?

Derzeit **unterstützt das Synchronisieren von Trainingsplänen auf die Uhr nur Garmin-Inlandskonten**.

Da Garmin-Internationalkonten uns noch keine entsprechenden API-Funktionen bereitgestellt haben, können wir die direkte Synchronisierung von Trainingsplänen auf die Uhr noch nicht implementieren.

Wir werden diese Funktion so bald wie möglich hinzufügen, wenn Garmin diese Funktionen freischaltet.

## 8. Wie startet man ein Training auf einer Garmin-Uhr?

Nach dem erfolgreichen Synchronisieren Ihres Trainingsplans mit Garmin können Sie folgende Schritte befolgen, um ein Training auf Ihrer Uhr zu starten:

1. Drücken Sie auf der Connect-Startseite die Trainingskurse auf Ihre Uhr. Wenn Sie die Kurse auf der Startseite nicht sehen, gehen Sie zu Mehr > Training & Pläne > Trainingskurse, um sie zu finden.
2. Drücken Sie auf dem Ziffernblatt die **START-Taste**
3. Wählen Sie den entsprechenden Aktivitätstyp (Laufen, Krafttraining usw.)
4. Halten Sie **MENU** lange gedrückt
5. Gehen Sie zu **Training > Workouts**
6. Wählen Sie das gewünschte Training aus
7. Tippen Sie auf **Training starten**
8. Drücken Sie erneut **START**, um die Aufzeichnung zu starten

Sobald das Training beginnt, führt Sie Ihre Uhr schrittweise durch jede Übung, zeigt Ziele oder Trainingsphasen an.

## 9. Wenn Sie gleichzeitig eine Garmin-Uhr und eine Apple Watch tragen, zeigt das Apple Watch-Widget falsche Werte an?

Die Apple Watch kann nur auf Apple Health-Daten zugreifen und nicht direkt auf Garmin Connect-Daten. Daher unterscheiden sich die angezeigten Daten von denen auf dem Telefon.

Allerdings stimmen die Desktop-Widgets mit den Daten auf dem Telefon überein.
