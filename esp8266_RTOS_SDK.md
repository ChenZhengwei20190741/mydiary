# ESP8266 RTOS SDK 技术总结

## 这是关于个人对 ESP8266 RTOS SDK 的技术总结

---

### RTOS_SDK

部分需频繁调用的函数定义在 RAM 中,需在函数前面添加宏`IRAM_ATTR`,
如:

```c
void IRAM_ATTR function(void)
```

#### RTOS 优先级

> watchdog task 优先级 14,
> pp task 优先级 13,
> 高精度 timer (ms) 线程优先级 12,
> TCP/IP task 优先级 10,
> freeRTOS timer 优先级 2,
> Wi-Fi event 优先级为 2,
> idle task 优先级为 0;

用户可用的优先级为 1~9

---

### esp8266 wifi 工作模式

#### 1.作为 Station 连接路由

1. 设置 ESP8266 为 Station 模式,或者 Station+SoftAP 共存模式。
   `wifi_set_opmode(STATION_MODE);`
2. 设置连接 AP 的信息。

```c
#define DEMO_AP_SSID "DEMO_AP"

#define DEMO_AP_PASSWORD "1234"
```

wifi_station_set_config 设置 ESP8266 Station 连接 AP 的信息。请注意将
station_config 中的 bssid_set 初始化为 0,除非非需要指定 AP MAC 地址的情况才设
置为 1。
wifi_station_connect 设置连接路路由。

```c
struct	station_config* config = (struct station_config *)zalloc(sizeof(struct station_config));

sprintf(config->ssid, DEMO_AP_SSID);

sprintf(config->password, DEMO_AP_PASSWORD);

wifi_station_set_config(config);

free(config);

wifi_station_connect();

```
