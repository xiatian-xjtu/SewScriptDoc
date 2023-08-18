人机界面+运动控制
=======================

人机界面以及运动控制加上通信就可以实现一个完整的工缝电控了。

以运动控制示例中的平缝为基础，再加入一个人机界面，实现最简单的转速调节。

新建人机界面工程，新建设计资源panel.sfd, 添加一个数字显示以及加减按钮。

.. image:: /.//image//sew-eg0.png
   :align: center
   :width: 600px
   :alt: sew-eg0

|

新建panel.c, 自动生成如下代码。

.. code-block:: C

    #include "device.h"
    #include "gui.h"
    /*widgetinfo start*/
    #define AUTO_GEN
    #ifdef AUTO_GEN
    static void button0_click();
    static void button1_click();
    static void number0_click();
    static void shape0_redraw();
    static wnd mywnd= {
        .mywnd.id = 1000,
        .mywnd.type = OBJ_WINDOW,
        .mywnd.start_x = 0,
        .mywnd.start_y = 0,
        .mywnd.width = 800,
        .mywnd.height = 480,
        .mywnd.bc = C_BLACK,
        .mywnd.fc = C_WHITE,
        .mywnd.oc = C_BLACK,
        .mywnd.owidth = 0,
        .mywnd.font = asc35,
        .mywnd.text = "",
        .mywnd.visible = 0,
    };
    static obj_button button0 = {
        .obj.id = 1001,
        .obj.type = OBJ_BUTTON,
        .obj.start_x = 258,
        .obj.start_y = 100,
        .obj.width = 80,
        .obj.height = 60,
        .obj.bc = C_BLUE,
        .obj.fc = C_GRAY,
        .obj.oc = C_GRAY,
        .obj.owidth = 4,
        .obj.font = fontawesome32,
        .obj.text = "\uf077",
        .obj.visible = 1,
        .obj.cb = button0_click,
        .r = 15,
    };
    static obj_button button1 = {
        .obj.id = 1002,
        .obj.type = OBJ_BUTTON,
        .obj.start_x = 260,
        .obj.start_y = 170,
        .obj.width = 80,
        .obj.height = 60,
        .obj.bc = C_GREEN,
        .obj.fc = C_GRAY,
        .obj.oc = C_GRAY,
        .obj.owidth = 4,
        .obj.font = fontawesome32,
        .obj.text = "\uf078",
        .obj.visible = 1,
        .obj.cb = button1_click,
        .r = 15,
    };
    static obj_number number0 = {
        .obj.id = 1003,
        .obj.type = OBJ_NUMBER,
        .obj.start_x = 72,
        .obj.start_y = 131,
        .obj.width = 160,
        .obj.height = 60,
        .obj.bc = C_DARKGRAY,
        .obj.fc = C_CRIMSON,
        .obj.oc = C_BLACK,
        .obj.owidth = 0,
        .obj.font = yahei52,
        .obj.text = "0000",
        .obj.visible = 1,
        .obj.cb = number0_click,
        .value = 0,
    };
    static obj_shape shape0 = {
        .obj.id = 1004,
        .obj.type = OBJ_SHAPE,
        .obj.start_x = 57,
        .obj.start_y = 77,
        .obj.width = 309,
        .obj.height = 169,
        .obj.bc = C_BLACK,
        .obj.fc = C_WHITE,
        .obj.oc = C_WHITE,
        .obj.owidth = 2,
        .obj.font = asc18,
        .obj.text = "",
        .obj.visible = 1,
        .obj.cb = shape0_redraw,
    };
    static obj_label label0 = {
        .obj.id = 1006,
        .obj.type = OBJ_LABEL,
        .obj.start_x = 29,
        .obj.start_y = 17,
        .obj.width = 183,
        .obj.height = 39,
        .obj.bc = C_BLACK,
        .obj.fc = C_GRAY,
        .obj.oc = C_BLACK,
        .obj.owidth = 0,
        .obj.font = zh44,
        .obj.text = "转速调节",
        .obj.visible = 1,
        .trans = 0,
    };
    /*
    static void button0_click()
    {	
    }
    static void button1_click()
    {	
    }
    static void number0_click()
    {	
    }
    static void shape0_redraw()
    {	
    }
    */
    static void Createmywnd()
    {
        CreateWindow(&mywnd);
        CreateShape(&mywnd,&shape0);
        CreateButton(&mywnd,&button0);
        CreateButton(&mywnd,&button1);
        CreateNumber(&mywnd,&number0);
        CreateLabel(&mywnd,&label0);
    }
    #endif
    /*widgetinfo end*/
    static void button0_click()
    {	
        printf("Inc speed\n");
    }
    static void button1_click()
    {	
        printf("Dec speed\n");
    }
    static void number0_click()
    {	
    }
    static void shape0_redraw()
    {	
    }
    void main()
    {
        GUI_Init(800,480);
        Createmywnd();
        while(1)
        {
            eventHandler();
        }
    }

编译运行后如下图所示。

.. image:: /.//image//sew-eg1.png
   :align: center
   :width: 600px
   :alt: sew-eg1

|

在panel.c程序中添加通信的处理

.. code-block::

    int max_speed;
    char send_buf[32];
    char rec_buf[32];
    short rec_status;
    enum REC_STATUS{WAIT_HAND_SHAKE, RECIEVE_PAR};
    static void SendPara();

    static void button0_click()
    {	
        printf("Inc speed\n");
        max_speed = max_speed + 100;
        SetNumberValue(&number0,max_speed);
        SendPara();
    }
    static void button1_click()
    {	
        printf("Dec speed\n");
        max_speed = max_speed - 100;
        SetNumberValue(&number0,max_speed);
        SendPara();
    }
    static void number0_click()
    {	
    }
    static void shape0_redraw()
    {	
    }

    static void SendAck()
    {
        send_buf[0] = 1;
        send_buf[1] = 2;
        SendUartMessage(send_buf,2);
    }
    static void SendPara()
    {
        send_buf[0] = 1;
        send_buf[1] = max_speed >> 8;
        send_buf[2] = max_speed & 0xff;
        SendUartMessage(send_buf,3);
    }
    static void MessageHandler()
    {
        if(rec_status == WAIT_HAND_SHAKE)
        {
            if(rec_buf[0] == 0x1)
            {
                printf("Recieved handshake!\n");
                max_speed = rec_buf[1] * 256 + rec_buf[2];
                SetNumberValue(&number0,max_speed);
                SendAck();
            }
        }
        else if(rec_status == RECIEVE_PAR)
        {
        }
    }

    void main()
    {
        GUI_Init(800,480);
        Createmywnd();
        SetMessageHandler(MessageHandler,rec_buf);
        rec_status = WAIT_HAND_SHAKE;
        while(1)
        {
            eventHandler();
        }
    }

如程序所示， SetMessageHandler(MessageHandler,rec_buf)语句制定了串口消息处理回调函数以及串口接收数据缓冲区。在收到运动控制器握手消息后，通过人机界面加减按钮进行速度调节。

在运动控制seam.c里也同样添加通信有关代码。

.. code-block:: C

    char send_buf[32];
    char rec_buf[32];
    short rec_status;
    enum REC_STATUS{WAIT_HANDSHAKE_ACK, RECIEVE_PAR};

    void SendHandshake()
    {
        int val;
        val = control_para[0];
        send_buf[0] = 1;
        send_buf[1] = val >> 8;
        send_buf[2] = val & 0xff;
        SendUartMessage(send_buf,3);
    }

    static void MessageHandler()
    {
        if(rec_status == WAIT_HANDSHAKE_ACK)
        {
            if(rec_buf[0] == 0x1)
            {
                printf("Recieved handshake ack!\n");
                rec_status = RECIEVE_PAR;
            }
        }
        else if(rec_status == RECIEVE_PAR)
        {
            control_para[0] = (short)(rec_buf[1] * 256 + rec_buf[2]);
            p_middle.maxspeed = control_para[0];
            LoadSeamSegs();
        }
    }

    void main()
    {
        printf("Sew control init!\n");
        SewControlInit();
        SetGlobalSpeedLimit(3500);
        SetAccel(60,60);
        CreateSeam();
        AssignJobAndEvent();
        LoadSeamSegs();
        SetRunLimit(1);
        SendHandshake();
        SetMessageHandler(MessageHandler,rec_buf);
        while(1)
        {
            eventHandler();
        }
    }

如程序所示，运动控制器发起了握手，握手完成后接收速度调节，并刷新Segment队列数据。

编译无误后运行，模拟器可处理人机界面于运动控制器之间的交互。

.. image:: /.//image//sew-eg2.png
   :align: center
   :width: 600px
   :alt: sew-eg2

|

人机界面与运动控制器由于是两个程序，实现起来有些麻烦。但通过模拟仿真，不用实体机器调试，可大幅度提高调试效率。

由于模拟器和实体机器通信口都虚拟化成为Socket接口，因此集成开发平台还可以支持模拟器与实体机器之间通信。可以在全虚拟模拟仿真后，再换成实体HMI或运动控制与模拟仿真HMI或运动控制调试，
最终过渡到全实体机器调试。

