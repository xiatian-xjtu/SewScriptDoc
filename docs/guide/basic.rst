基本例程
==============

Hello wolrd!
~~~~~~~~~~~~~~~~~~~
点击菜单项目->新建

.. image::  /.//image//new-project.png
   :align: center
   :width: 400px
   :alt: new project

|

输入工程名和一个工程文件夹目录。

点击工具栏新建，在源代码编辑区域输入代码

.. code-block:: c

   #include "device.h"

   void main()
   {
      printf("Hello world!\n");
      printf("SewScript is comming!\n");
   }

点击工具栏保存文件。右键点击项目管理窗口的人机界面，点击弹出菜单的添加，将刚才保存的文件添加进去。

点击菜单项目->选项，一般缺省设置就行。

.. image::  /.//image//menubar.png
   :align: center
   :width: 600px
   :alt: menu bar

|

返回主界面，点击工具栏编译，没有错误后点击工具栏运行，最下方信息输出会显示"Hello world!"。

可以看出语法与标准C完全一致, 只不过头文件由"stdio.h"变为了"device.h", "device.h"中包含了通用的一些API函数，可参考API列表说明。

.. image::  /.//image//debug.png
   :align: center
   :width: 600px
   :alt: debug

|

如果需要调试，在编译后可以打断点，可以单步调试。编译之前，打断点是无效的。

Fibonacci 递归算法
~~~~~~~~~~~~~~~~~~~

.. code-block:: c

   #include "device.h"
   int fib(int n)
   {
      if(n<=2)
      {
         return 1;
      }
      else
      {
         return fib(n - 1) + fib(n -2);
      }
   }
   int Fibonacci_bottom_up(int n)//自底向上算法
   {
      int result[2] = {0, 1};
      int i;
      if(n < 2)
         return result[n];

      int  fibNMinusN_1 = 1;
      int  fibNMinusN_2 = 0;
      int  fibN = 0;
      for( i = 2; i <= n;  i++)   //从底到上逐次计算出数列值
      {
         fibN = fibNMinusN_1 + fibNMinusN_2;

         fibNMinusN_2 = fibNMinusN_1;
         fibNMinusN_1 = fibN;
      }

      return fibN;//返回数组值
   }
   void main()
   {
      int cc;
      int start_time,end_time;
      start_time = get_ticks();
      printf("Start:\n");
      cc = fib(35);
      end_time = get_ticks();
      printf("fib(35)= %d\n",cc);
      printf("Consume time:%dms\n",end_time - start_time);
   }

|

Callback 回调函数
~~~~~~~~~~~~~~~~~~~

.. code-block:: c

   #include<device.h>

   void Callback_1(int x) // Callback Function 1
   {
      printf("Hello, this is Callback_1: x = %d\n", x);
   }

   void Callback_2(int x) // Callback Function 2
   {
      printf("Hello, this is Callback_2: x = %d\n", x);
   }

   void Callback_3(int x) // Callback Function 3
   {
      printf("Hello, this is Callback_3: x = %d\n", x);
   }

   void Handle(int y,void (*Callback)(int c),)
   {
      printf("Entering Handle Function.\n");
      Callback(y);
      printf("Leaving Handle Function.\n");
   }

   void main()
   {
      int a = 2;
      int b = 4;
      int c = 6;
      printf("Entering Main Function.\n");
      Handle(a,Callback_1);
      Handle(b,Callback_2);
      Handle(c,Callback_3);
      printf("Leaving Main Function.\n");
   }

class
~~~~~~~~~~

.. code-block:: c

   #include "device.h"

   class Led
   {
      short chanel;
      short state;
      point pt;
      void on()
      {
         gpio_out(chanel,1);
         //printf("Led%d is on\n",chanel);

      }
      void off()
      {
         gpio_out(chanel,0);
         //printf("Led%d is off\n",chanel);
      }
      void toggle()
      {
         gpio_out(chanel,2);
         printf("Led%d is toggled\n",chanel);
      }
      void print()
      {
         printf("%d\n",chanel);
         printf("%d\n",pt.x-2*pt.y);
      }
      void add(int a,int b)
      {
         printf("%d\n",a-b);
      }
   };

   Led led1 = {0,1,{1,20}};
   int timer1;
   void timer1_update();

   int add(int a,int b)
   {
      int c;
      c = a+b;
      printf("%d\n",c);
      return c;
   }

   void main()
   {
      int c = 100;
      printf("Hello!\n");
      led1.print();
      led1.add(1,2);
      c = add(1,2);
      timer1 = CreateTimer(2000,0,timer1_update);
      StartTimer(timer1);
      while (1)
      {
         eventHandler();
      }
   }

   void timer1_update()
   {
      led1.toggle();
   }

从以上例子看，除了class以外，SewScript有着和标准C相同的语法，因此对于有C语言经验的开发人员来说，可以直接上手。class这个还有待进一步完善。
