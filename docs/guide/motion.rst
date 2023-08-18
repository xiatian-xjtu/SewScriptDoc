运动控制
==============

运动控制虚拟机运行机制
~~~~~~~~~~~~~~~~~~~~~~~

.. image::  /.//image//motion-mechanism.svg
   :align: center
   :width: 800px
   :alt: motion-mechanism

| 


如上图所示，虚拟机通过API函数创建了运动Segment数组，每一个Segment由一个规定了如下参数：

.. code-block:: c

   typedef struct SeamSegTypedef
   {
      char mode;              // 固定针数，自由针数, 延时，等待事件，做一个动作(无电机运转)
      char enable;            //使能
      char auto_enter_next;   //如果启动条件仍存在，直接进入下一seg
      char auto_running;      //如果启动条件不存在，则暂停
      char auto_attach;	      //和下一seg连接起来，不判断启动条件
      char start_event_id;    // 触发事件
      char pause_event_id;    // 暂停事件,0表示无法暂停
      char end_event;         // 结束事件
      short maxspeed;         // 最高转速
      short degree;           //目标位置，调度，与stitches合用
      int stitches;           // 目标位置，整针数
      void* _cb_prepare_job;  // action回调
      seg_event* event[16];   //基于位置的事件action回调
   } seam_seg;

转速、针数、停车角度等选项以及一个位置检查事件数组。

虚拟机捕捉位置检查事件、定时器事件以及通信消息等等加入到事件队列。

虚拟机通过用户定义的回调函数或底层驱动来进行处理事件队列，并处理电机静止状态时的缝前准备回调函数。

一个简化的平缝机运动过程
~~~~~~~~~~~~~~~~~~~~~~~~~

下面以一个简化的平缝机运动控制来7示例。

平缝一般由前加固、中间段、后加固以及剪线组成。这四段均对应着主轴电机旋转。

三自动分别是指倒缝、抬压脚以及剪线。这对应着三路电磁铁/阀输出。虚拟机分配0，1，2三个通道给这3路输出。

需要处理的输入为启动、抬压脚、剪线。一般分别对应调速器输入的3个区间段，示例简化为三联踏板的3个数字量输入。虚拟机分配0，1，2三个通道给这3路输入。

倒缝在加固时动作，剪线在后加固或者无加固时动作，抬压脚则在缝制中间段或结束后动作。

首先建立一个空白工程

工程管理区，右键点击公共模型，菜单弹出后再点击新建。

.. image::  /.//image//motion-eg1.png
   :align: center
   :width: 800px
   :alt: motion-eg1

|  

弹出的窗口为运动控制设计器，可点击右键，添加Segment或Event，还可添加参数。保存为model.smd。

如默认窗口设置为800*480，这个可与实际屏幕硬件进行匹配。

.. image::  /.//image//motion-eg2.png
   :align: center
   :width: 800px
   :alt: motion-eg2

| 

如图所示，添加了前加固、中间段以及后加固，再加上剪线4个Segment，并添加了倒缝动作事件，剪线事件。事件的检查位置都是以本Segment初始位置来算针数的。

.. image::  /.//image//motion-eg3.png
   :align: center
   :width: 800px
   :alt: motion-eg3

| 

如图所示，将各事件添加到各Segment中。

.. image::  /.//image//menubar.png
   :align: center
   :width: 800px
   :alt: menubar

| 

点击菜单栏中自动生成代码，会生成和模型同名的初始化文件以及头文件。

.. code-block:: C

   //parameters macro declaration
   #include "sewcontrol.h"
   #include "parameter.h"
   seam_seg p_starttack = 
   {
      .mode = 1,
      .enable = 1,
      .auto_running = 1,
      .auto_attach = 0,
      .auto_enter_next = 0,
      .start_event_id = 0
   };
   seam_seg p_middle = 
   {
      .mode = 1,
      .enable = 1,
      .auto_running = 0,
      .auto_attach = 0,
      .auto_enter_next = 0,
      .start_event_id = 0
   };
   seam_seg p_endtack = 
   {
      .mode = 1,
      .enable = 1,
      .auto_running = 1,
      .auto_attach = 1,
      .auto_enter_next = 0,
      .start_event_id = 0
   };
   seam_seg p_trimm = 
   {
      .mode = 1,
      .enable = 1,
      .auto_running = 0,
      .auto_attach = 0,
      .auto_enter_next = 0,
      .start_event_id = 0
   };

   seg_event ev_statck_on = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 0,
      .out_level = 1
   };
   seg_event ev_statck_off = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 0,
      .out_level = 0
   };
   seg_event ev_endtack_on = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 0,
      .out_level = 1
   };
   seg_event ev_endtack_off = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 0,
      .out_level = 0
   };
   seg_event ev_trimm_on = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 1,
      .out_level = 1
   };
   seg_event ev_trimmoff = 
   {
      .action = 1,
      .action_type = 0,
      .out_chanel = 1,
      .out_level = 0
   };

   short control_para[1] = 
   {
   2500,
   };
   void CreateSeam()
   {
      p_starttack.stitches = 6;
      p_starttack.degree = 220;
      p_starttack.maxspeed = 900;
      p_starttack.event[0] = &ev_statck_on;
      p_starttack.event[1] = &ev_statck_off;
      p_middle.stitches = INF_STITCHES;
      p_middle.degree = 220;
      p_middle.maxspeed = 3000;
      p_endtack.stitches = 6;
      p_endtack.degree = 220;
      p_endtack.maxspeed = 900;
      p_endtack.event[0] = &ev_endtack_on;
      p_endtack.event[1] = &ev_endtack_off;
      p_trimm.stitches = 0;
      p_trimm.degree = 60;
      p_trimm.maxspeed = 200;
      p_trimm.event[0] = &ev_trimm_on;
      p_trimm.event[1] = &ev_trimmoff;
      ev_statck_on.check_point = (3) * 1440 + 10 * 4;
      ev_statck_off.check_point = (6) * 1440 + 200 * 4;
      ev_endtack_on.check_point = (0) * 1440 + 10 * 4;
      ev_endtack_off.check_point = (3) * 1440 + 200 * 4;
      ev_trimm_on.check_point = (0) * 1440 + 220 * 4;
      ev_trimmoff.check_point = (1) * 1440 + 60 * 4;
   }
   /*void AssignJobAndEvent()
   {
      p_starttack._cb_prepare_job = p_starttack_prepare_job;
      p_middle._cb_prepare_job = p_middle_prepare_job;
      p_endtack._cb_prepare_job = p_endtack_prepare_job;
      p_trimm._cb_prepare_job = p_trimm_prepare_job;
      EnqueueSeamSeg(&p_starttack);
      EnqueueSeamSeg(&p_middle);
      EnqueueSeamSeg(&p_endtack);
      EnqueueSeamSeg(&p_trimm);
   }*/


可以看出，自动生成的代码对各Segment以及Event做了初始化，这部分可以与人机界面公用。

对于Segment数组代表的运动模型，人机界面可对器进行修改，如速度，针数，使能以及接续性等。

运动控制器则根据一数组来完成整个缝制过程。

新建seam.c, 输入以下代码。并将seam.c及model.c添加到项目管理区运动控制分支下。

.. code-block:: c

   #include "device.h"
   #include "sewcontrol.h"
   #include "model.h"

   void p_starttack_prepare_job()
   {
      if(GetInputStatus(0) == 1)
      {
         StartMotion();
      }
   }
   static void p_middle_prepare_job()
   {
      if(GetInputStatus(0) == 1)
      {
         StartMotion();
      }
      else if(GetInputStatus(2) == 1)
      {
         NextSeg();
      }
   }
   static void p_endtack_prepare_job()
   {
      if(GetInputStatus(2) == 1)
      {
         StartMotion();
      }
   }
   static void p_trimm_prepare_job()
   {
      if(GetInputStatus(2) == 1)
      {
         StartMotion();
      }
   }
   void AssignJobAndEvent()
   {
      p_starttack._cb_prepare_job = p_starttack_prepare_job;
      p_middle._cb_prepare_job = p_middle_prepare_job;
      p_endtack._cb_prepare_job = p_endtack_prepare_job;
      p_trimm._cb_prepare_job = p_trimm_prepare_job;
      EnqueueSeamSeg(&p_starttack);
      EnqueueSeamSeg(&p_middle);
      EnqueueSeamSeg(&p_endtack);
      EnqueueSeamSeg(&p_trimm);
   }

   void main()
   {
      SewControlInit();
      SetGlobalSpeedLimit(2500);
      SetAccel(60,60);
      CreateSeam();
      AssignJobAndEvent();
      LoadSeamSegs();
      SetRunLimit(1);
      while(1)
      {
         eventHandler();
      }
   }

   以上代码可以看出，程序初始化了运动控制虚拟机，设置了加速度以及最大速度。创建了一个运动Segment数组，创建了一个Event事件数组，并将Event关联到相应的Segment。

   程序还关联了各个Segment启动前的准备回调函数，最后是将Segment加载到虚拟机。打开运行使能。最后是死循环，处理事件队列。

   编译后运行。

.. image::  /.//image//motion-eg4.png
   :align: center
   :width: 800px
   :alt: motion-eg4

| 

由上图可知，模拟器展示了一段完整的线迹，由前加固、中间段、后加固以及剪线组成。x轴水平线以上是电机的运行速度曲线以及角度值，水平线以下是各电磁铁/阀的输出。
最右边是线迹模拟效果。