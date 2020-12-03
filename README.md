# Arduino Gesture Control

> Arduino Nano BLE 33 sensor 板支持手势传感器，于是我想是否可能通过它来在我的 Mac 上进行控制。

## 环境准备

- Sensor + MicroUSB
- Arduino IDE
- Python 

## 基本思路

通过 MicroUSB 线连接 sensor 板

![select-sensor-board](./imgs/select-sensor-board.png)

![select-serial-port](./imgs/select-serial-port.png)

为 Arduino 烧录实例项目中的代码

![gesture-sample](./imgs/gesture-sample.png)

现在在 sensor 传感器一侧挥舞手势，查看串口输出

![gestrue-detect](./imgs/gestrue-detect.png)

编写 Python 脚本

## 实际效果

// 插入gif