硬件平台
============

.. image::  /.//image//hardware.svg
   :align: center
   :width: 400px
   :alt: hardware

|

如上图所示，硬件平台与市面上电控并无太大区别，分为主轴控制器以及HMI，如果有送布或其他需求，可选配步进电机。HMI可以为触摸屏或其他类型如数码管显示。

主轴是一块单板，步进电机通过CAN总线接收命令，完成送布等动作。

.. image::  /.//image//develop.svg
   :align: center
   :width: 500px
   :alt: develop

|

HMI与主轴控制器之间采用串口通信。开发调试时将串口断开，分别接入以太网或WIFI转换器，通过网络连接到IDE的Socket server。

IDE通过Socket连接对HMI和控制器进行程序下载和运行调试等操作, 并通过转发实现二者通信调试。

关于MCU的存储问题，建议存储为主轴控制板为大于32kbytes SRAM，HMI为大于128kbytes SRAM。程序存储在扩展的SPI flash里。
