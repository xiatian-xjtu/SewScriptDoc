实现原理
=================================

1. 虚拟机的运行原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
我们以一个最简单的“Hello world”来介绍一下SewScript的运行原理。

源代码

.. code-block:: c

   #include "device.h"
   void main()
   {
      printf("Hello world!\n");
   }

经过IDE的编译后，产生字节码即汇编指令序列。

汇编指令

.. code-block:: c

         3:void main()
   0x10002000	ENT	0

         5:printf("Hello world!\n");
   0x10002008	IMM	0x10000000
   0x10002010	PUSH
   0x10002014	SYSCALL(printf)	;$1001
   0x1000201c	ADJ	1

可以看到，字节码是由 ENT, IMM, PUSH, SYSCALL, ADJ等指令构成。

下面是虚拟机的程序片段:

.. code-block:: C

   while(1)
   {
      if (virtual_machine_status == kVM_Running)
      {
         vm_cycle++;
         op = *pc++;
         switch (op)
         {
            case IMM:
               ax = *pc++;
               break;
            case PUSH:
               *--sp = ax;
               break;
            case ENT:
               *--sp = (int)bp;
               bp = sp;
               sp = sp - *pc++;
               break;
            case ADJ:
               sp = sp + *pc++;
               break;
            case SYSCALL:
               syscall_temp = *pc++;
               rt_function_id = (syscall_temp >> 16) - 1001;
               size = syscall_temp & 0xffff;
               tmp = sp + size;
               for (i = 0; i < size; i++)
               {
                  para[i] = tmp[-1 - i];
               }
               ax = rt[rt_function_id].exec(para);
               break;
            
            ......
      
            default:
               virtual_machine_status = kVM_UnknownInstruction;
               break;
         }
      }
   }

可以看出虚拟机模拟了通用处理器的行为，从程序存储单元取出指令，然后分析指令并运行指令，在处理多个操作数时，会将操作数压入堆栈。

SewScript的虚拟机设计为一种栈式虚拟机，这是最常用的虚拟机。

 - ENT 为函数局部变量开辟栈空间
 - IMM 装载立即数到寄存器AX
 - PUSH 将AX压入栈内
 - SYSCALL 调用运行时库里的API函数
 - ADJ 恢复函数调用前的栈顶

 解释再详细一点，“Hello world”字符串存储在0x10000000这个地址，将此地址压栈，调用运行时函数printf，将字符串打印出来。rt就是运行时的API函数数组。

2. 模拟仿真原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image::  /.//image//how-simulate.svg
   :align: center
   :width: 600px
   :alt: how-simulate

| 

集成环境IDE提供了模拟仿真器，可在无实体机器的情况下进行仿真验证，可针对屏幕及主轴运动控制进行仿真模拟。由于无需实体机器，可快速反复的进行调试，因此大大提高了开发效率。仿真完成后，再转入实体机器验证。

仿真是如何做到和实体机器效果一致的呢？

 - 首先，PC模拟器使用的程序和实体电控是一样的，也就是完全相同的字节码序列。
 - 再次，PC模拟器使用了和实体机器完全一致的虚拟机（代码完全一致）。
 - 最后，虽然二者在底层驱动上是不一样的，例如PC上使用了SDL2进行屏幕打点，而实体机器是单片机屏幕打点。但由于使用了同样的API，因此可以做到完全的模拟。

后面我们可以在程序示例中来进行演示。

3. 辅助设计器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image::  /.//image//gui-design.png
   :align: center
   :width: 800px
   :alt: gui-design

|

人机界面设计器。可像visual studio一样来进行窗体设计和编写事件响应，并支持控件事件跳转，可自动生成初始化代码，开发者只需要填入各控件的点击事件即可。

.. image::  /.//image//motion-design.png
   :align: center
   :width: 800px
   :alt: motion-design

|

运动控制设计器。可根据机器功能，设计运动控制序列。如平缝机的工作流程就是前加固、中间段、后加固及剪线。

集成环境IDE提供了辅助设计器，可帮助开发者快速的自动生成代码，提高效率。