# PeakWatch × Garmin FAQ

PeakWatch now supports connecting to Garmin devices.
Due to differences in platform capabilities, some data or features may differ slightly from what's shown in Garmin Connect.

## 1. Why aren't some metrics showing (like blood oxygen, breathing rate, etc.)?

If certain metrics aren't displaying, try troubleshooting as follows:

1. **Check if the data exists in Garmin Connect first**. If Garmin Connect doesn't have the data recorded, PeakWatch won't be able to retrieve it either.
2. **Verify if your device supports that metric**. Some Garmin watch models don't support blood oxygen, breathing rate, or other features, so they won't generate corresponding data.
3. **Check if data has synced**. If the data exists in Garmin Connect but doesn't show in PeakWatch, it may not have synced yet. Try manually syncing your watch in Garmin Connect, then pull to refresh in PeakWatch.

## 2. What should I do if PeakWatch has no data or data doesn't match Connect?

**Troubleshooting steps:**

1. **Confirm if Garmin Connect app has data**
   - Open the Garmin Connect app and ensure your watch data has synced to Connect
   - **Reason**: Only by opening the Connect app can watch data sync to Connect, allowing PeakWatch to retrieve it

2. **Check if Garmin web (cloud) has data**
   - Garmin China: https://connect.garmin.cn
   - Garmin International: https://connect.garmin.com
   - Log in to check if you have complete historical records
   - **Reason**: Data may exist locally in the Connect app but not synced to the cloud; PeakWatch retrieves data from the cloud

3. **Re-sync**
   - If Garmin cloud has data but PeakWatch still shows none or inconsistent data
   - Go to PeakWatch > Settings > Data Sources > Garmin
   - Tap "Re-sync" to get the latest data

If Garmin Connect itself has no data, it cannot be viewed through PeakWatch.

## 3. Why isn't today's data updating?

Garmin data needs to sync to Garmin Connect first before PeakWatch can access it.

If today's data isn't updating, try:

1. Open the Garmin Connect app
2. Pull to refresh or manually sync your watch
3. Pull to refresh in PeakWatch to view updated data

## 4. Why don't I see much historical data after connecting successfully?

The Garmin API currently **can only retrieve the most recent 30 days of historical data**.

If you just connected your Garmin account, PeakWatch can only sync the last 30 days of data—earlier data cannot be retrieved due to Garmin's platform API limitations.

Also make sure you've enabled **Historical Data Permissions**:

1. Open Garmin Connect
2. Go to More > Settings > Connected Apps
3. Find PeakWatch
4. Confirm Historical Data Permissions is enabled

## 5. Why is "Body Energy" different from Garmin's "Body Battery"?

PeakWatch's "Body Energy" uses PeakWatch's proprietary algorithm for calculation.

The reason for this design:

- Allows unified processing of data from both Garmin and Apple Watch
- Ensures data from different device sources is analyzed within the same system
- Provides more consistent and complete recovery status assessments

Therefore, PeakWatch's Body Energy values may differ from Garmin's Body Battery—this is normal.

## 6. Why do some workout details look different after syncing to Garmin?

Due to differences in platform data structures, workout content may have some adjustments on Garmin devices, such as:

- Some strength training exercise names may differ
- Individual exercises may be replaced with similar ones
- Warm-up or cool-down stretches in running workouts may not display

These changes are due to platform compatibility differences and don't affect the overall workout structure.

## 7. Why does syncing training plans to the watch only support Garmin international accounts?

Currently **syncing training plans to the watch only supports Garmin domestic accounts**.

Since Garmin international accounts haven't provided us with the relevant API capabilities yet, we can't implement direct training plan syncing to the watch yet.

We'll add support as soon as Garmin opens up these capabilities.

## 8. How to start a workout on a Garmin watch?

After successfully syncing your training plan to Garmin, follow these steps to start a workout on your watch:

1. On the Connect home page, push the training course to your watch. If you don't see the course on the home page, go to More > Training & Plans > Training Courses to find it.
2. On the watch face, press the **START** button
3. Select the corresponding activity type (running, strength training, etc.)
4. Long press **MENU**
5. Go to **Training > Workouts**
6. Select the workout you want to do
7. Click **Do Workout**
8. Press **START** again to start recording the workout

Once the workout starts, your watch will guide you through each step, showing the current exercise, goals, or training phases.

## 9. Apple Watch widget shows incorrect values when using both Garmin and Apple Watch?

Apple Watch can only access Apple Health data and cannot directly retrieve data from Garmin Connect. Therefore, the data displayed differs from what's shown in the app.

However, desktop widgets will display the same data as the app.

## 10. Can I view Garmin training plans in PeakWatch?

Currently **Garmin training plans cannot be viewed in PeakWatch**.

This is because Garmin has not opened up API access for training plan data, so PeakWatch cannot retrieve users' Garmin training plans.

To use training plan features, please manage them through the Garmin Connect App or Garmin watch.

## 11. Why does Garmin show Heart Rate Recovery values but PeakWatch doesn't?

Some users can see Heart Rate Recovery values in Garmin Connect, but PeakWatch doesn't display them.

**Explanation:**

Garmin does **not directly provide Heart Rate Recovery values**—PeakWatch needs to calculate them from raw heart rate data. When heart rate signal quality is poor (e.g., measuring immediately after activity, poor contact between skin and watch), the system cannot accurately calculate recovery heart rate, so it chooses not to display any value.

This is to avoid providing potentially inaccurate recovery data that could affect users' judgment of their recovery status.
