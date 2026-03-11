	

chromecast
Initial chromecast testing has revealed that it is a DIAL device and sniffing shows several interesting commands that can be sent to it.

The chromecast dongle is apparently listening on http port 8008. (Also port 9080 while Netflix app is running)

Some control can be established by sending simple HTTP GET’s, POST’s and DELETE’s.

** For these examples the youtube app is running, also available are Netflix, ChromeCast, and GoogleMusic.

get device information xml:
```bash
curl http://10.0.1.2:8008/ssdp/device-desc.xml
```

get detailed device information json:
```bash
curl http://10.0.1.2:8008/setup/eureka_info?options=detail
```

scan for available wifi:
```bash
curl http://10.0.1.2:8008/setup/scan_results
```

get supported time zones:
```bash
curl http://10.0.1.2:8008/setup/supported_timezones
```

get info about current app:
```bash
curl -H “Content-Type: application/json” http://10.0.1.2:8008/apps/YouTube -X GET
```

send youtube video to chromecast:
```bash
curl -H “Content-Type: application/json” http://10.0.1.2:8008/apps/YouTube -X POST -d ‘v=oHg5SJYRHA0’
```

kill current running app:
```bash
curl -H “Content-Type: application/json” http://10.0.1.2:8008/apps/YouTube -X DELETE
```

reboot the chromecast dongle:
```bash
curl -H “Content-Type: application/json” http://10.0.1.2:8008/setup/reboot -d ‘{“params”:”now”}’ -X POST
```

factory default reset the chromecast dongle:
```bash
curl -H “Content-Type: application/json” http://10.0.1.2:8008/setup/reboot -d ‘{“params”:”fdr”}’ -X POST
```
