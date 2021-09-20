import pandas as pd

filename = "2018-07-10-pure_param_stats_driver1.csv"
csv = pd.read_csv(filename, error_bad_lines=False, sep=';')

time = csv["Date/Time"].tolist()
speed = csv["Speed(km/h)"].tolist()
light = csv["LightLevel(Lux)"].tolist()
pitch = csv["IsHeadRotatedPitch"].tolist()
yawn = csv["IsHeadRotatedYaw"].tolist()

speedsum = 0.0
speedcount = 0.0
lightsum = 0.0
dangersum = 0.0

count = len(time)
for i in range(count):
    speedsum += float(speed[i].replace(",", "."))
    if(float(speed[i].replace(",", ".")) != 0):
        speedcount += 1
    lightsum += float(light[i].replace(",", "."))
    if(pitch[i] or yawn[i]):
        dangersum += 1

deltatime = 0.2

speedavg = speedsum * deltatime / speedcount
lightavg = lightsum / count
dangeravg = dangersum / count

print(len(time))
print(speedsum)
print(speedcount)
print(lightsum)
print(dangersum)

print(speedavg)
print(lightavg)
print(dangeravg)