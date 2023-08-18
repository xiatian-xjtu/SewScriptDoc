人机界面API列表
=================

引用  #include"gui.h"

颜色表
~~~~~~~~~~~~~~~
=============================  ============
    宏定义                        颜色
=============================  ============
 C_BLACK                        黑色
 C_NAVY                         藏青
 C_DARKBLUE                     深蓝
 C_MEDIUMBLUE                   中蓝
 C_BLUE                         蓝色
 C_DARKGREEN                    深绿
 C_GREEN                        调和绿
 C_TEAL                         鸭翅绿
 C_DARKCYAN                     深青
 C_DEEPSKYBLUE                  深天蓝
 C_DARKTURQUOISE                深松石绿
 C_MEDIUMSPRINGGREEN            中嫩绿
 C_LIME                         绿色
 C_SPRINGGREEN                  春绿
 C_CYAN_AQUA                    青色
 C_MIDNIGHTBLUE                 午夜蓝
 C_DODGERBLUE                   湖蓝
 C_LIGHTSEAGREEN                浅海藻绿
 C_FORESTGREEN                  森林绿
 C_SEAGREEN                     海藻绿
 C_DARKSLATEGRAY                深岩灰
 C_LIMEGREEN                    青柠绿
 C_MEDIUMSEAGREEN               中海藻绿
 C_TURQUOISE                    松石绿
 C_ROYALBLUE                    品蓝
 C_STEELBLUE                    钢青
 C_DARKSLATEBLUE                深岩蓝
 C_MEDIUMTURQUOISE              中松石绿
 C_INDIGO                       靛蓝
 C_DARKOLIVEGREEN               深橄榄绿
 C_CADETBLUE                    军服蓝
 C_CORNFLOWERBLUE               矢车菊蓝
 C_MEDIUMAQUAMARINE             中碧绿
 C_DIMGRAY                      昏灰
 C_SLATEBLUE                    岩蓝
 C_OLIVEDRAB                    橄榄绿
 C_SLATEGRAY                    岩灰
 C_LIGHTSLATEGRAY               浅岩灰
 C_MEDIUMSLATEBLUE              中岩蓝
 C_LAWNGREEN                    草坪绿
 C_CHARTREUSE                   查特酒绿
 C_AQUAMARINE                   碧绿
 C_MAROON                       栗色
 C_PURPLE                       紫色
 C_OLIVE                        橄榄色
 C_GRAY                         灰色
 C_SKYBLUE                      天蓝
 C_LIGHTSKYBLUE                 浅天蓝
 C_BLUEVIOLET                   蓝紫色
 C_DARKRED                      深红
 C_DARKMAGENTA                  深品红
 C_SADDLEBROWN                  鞍褐
 C_DARKSEAGREEN                 深海藻绿
 C_LIGHTGREEN                   浅绿
 C_MEDIUMPURPLE                 中紫
 C_DARKVIOLET                   深紫
 C_PALEGREEN                    白绿色
 C_DARKORCHID                   深洋兰紫
 C_YELLOWGREEN                  暗黄绿色
 C_SIENNA                       土黄赭
 C_BROWN                        褐色
 C_DARKGRAY                     暗灰
 C_LIGHTBLUE                    浅蓝
 C_GREENYELLOW                  黄绿色
 C_PALETURQUOISE                白松石绿
 C_LIGHTSTEELBLUE               浅钢青
 C_POWDERBLUE                   粉末蓝
 C_FIREBRICK                    火砖红
 C_DARKGOLDENROD                深金菊黄
 C_MEDIUMORCHID                 中洋兰紫
 C_ROSYBROWN                    玫瑰褐
 C_DARKKHAKI                    深卡其色
 C_SILVER                       银色
 C_MEDIUMVIOLETRED              中紫红
 C_INDIANRED                    印度红
 C_PERU                         秘鲁红
 C_CHOCOLATE                    巧克力色
 C_TAN                          日晒褐
 C_LIGHTGRAY                    亮灰
 C_PALEVIOLETRED                白紫红
 C_THISTLE                      蓟紫
 C_ORCHID                       洋兰紫
 C_GOLDENROD                    金菊黄
 C_CRIMSON                      绯红
 C_GAINSBORO                    庚氏灰
 C_PLUM                         李紫
 C_BURLYWOOD                    硬木褐
 C_LIGHTCYAN                    浅青
 C_LAVENDER                     薰衣草紫
 C_DARKSALMON                   深鲑红
 C_VIOLET                       紫罗兰色
 C_PALEGOLDENROD                白金菊黄
 C_LIGHTCORAL                   浅珊瑚红
 C_KHAKI                        卡其色
 C_ALICEBLUE                    爱丽丝蓝
 C_HONEYDEW                     蜜瓜绿
 C_AZURE                        青白色
 C_SANDYBROWN                   沙褐
 C_WHEAT                        麦色
 C_BEIGE                        米色
 C_WHITESMOKE                   烟雾白
 C_MINTCREAM                    薄荷乳白
 C_GHOSTWHITE                   幽灵白
 C_SALMON                       鲑红
 C_ANTIQUEWHITE                 古董白
 C_LINEN                        亚麻色
 C_LIGHTGOLDENRODYELLOW         浅金菊黄
 C_OLDLACE                      旧蕾丝白
 C_RED                          红色
 C_MAGENTA_FUCHSIA              洋红
 C_DEEPPINK                     深粉
 C_ORANGERED                    橘红
 C_TOMATO                       番茄红
 C_HOTPINK                      艳粉
 C_CORAL                        珊瑚红
 C_DARKORANGE                   深橙
 C_LIGHTSALMON                  浅鲑红
 C_ORANGE                       橙色
 C_LIGHTPINK                    浅粉
 C_PINK                         粉色
 C_GOLD                         金色
 C_PEACHPUFF                    粉扑桃色
 C_NAVAJOWHITE                  土著白
 C_MOCCASIN                     鹿皮色
 C_BISQUE                       陶坯黄
 C_MISTYROSE                    雾玫瑰红
 C_BLANCHEDALMOND               杏仁白
 C_PAPAYAWHIP                   番木瓜橙
 C_LAVENDERBLUSH                薰衣草红
 C_SEASHELL                     贝壳白
 C_CORNSILK                     玉米穗黄
 C_LEMONCHIFFON                 柠檬绸黄
 C_FLORALWHITE                  花卉白
 C_SNOW                         雪白
 C_YELLOW                       黄色    
 C_LIGHTYELLOW                  浅黄
 C_IVORY                        象牙白
 C_WHITE                        白色
 C_CUSTOMER0                    激活
 C_CUSTOMER1                    编辑
 C_CUSTOMER2                    非激活
 C_CUSTOMER3                    深灰
 C_CUSTOMER4                    标题
 C_CUSTOMER5      
               待定
 C_CUSTOMER6                    待定
 C_CUSTOMER7                    待定
 C_CUSTOMER8                    待定
 C_CUSTOMER9                    待定     
=============================  ============

字体
~~~~~~~~~~~~~~~
.. code-block:: c

    enum font { 
        asc18,      //西文，18像素点
        asc26,      //西文，25像素点
        asc35,      //西文，35像素点
        zh24,       //西文，24像素点
        zh31,       //中文，31像素点
        zh44,       //中文，44像素点
        yahei52,    //雅黑数字及字母，52像素点
        yahei95,    //雅黑数字及字母，95像素点
        fontawesome32,  //谷歌图标字体，32像素点
        fontawesome52,  //谷歌图标字体，52像素点
        icon52,         //工缝图标字体，52像素点
        icon96,         //工缝图标字体，96像素点
        vetronlogo      //厂标
    };

|

结构体
~~~~~~~~~~~~~~~

.. declaration:: area

.. code-block:: c

    //矩形区域，(x1,y1)为左上角坐标，(x2,y2)为右下角坐标
    typedef struct AREA
    {
        short x1;
        short y1;
        short x2;
        short y2;
    }area;

.. declaration:: wnd_obj

.. code-block:: c

    //GUI的基础控件
    typedef struct OBJ
    {
        short state;        //状态，用于指示激活或禁止
        short id;           //用于表示控件的编号，在一个窗体里具有唯一性
        short type;         //类型，用于指示是按钮或标签等等
        short start_x;      //部件左上角x坐标
        short start_y;      //部件左上角y坐标
        short width;        //部件宽度
        short height;       //部件高度
        short bc;           //部件背景色
        short fc;           //部件绘图颜色
        short oc;           //部件边框颜色
        short owidth;       //部件边框宽度，为0无边框
        short font;         //部件字体
        char* text;         //部件文字
        void(*cb)();        //部件点击事件后回调处理函数指针
        short visible;      //部件是否可见
        short dirtflag;     //重绘标志，用户不可设定
        void(*draw_cb)();   //重绘函数指针，用户不可设定
    }wnd_obj;

.. declaration:: wnd

.. code-block:: c

    typedef struct WND
    {
        wnd_obj mywnd;
        //int cb_data[8];
        int obj_cnt;
        int heap;
        void(*click_cb)();
        wnd_obj* obj_list;
    }wnd;

.. declaration:: obj_button

.. code-block:: c

        typedef struct BUTTON
        {
            wnd_obj obj;
            short r;
            short padding;
            area touch;
        }obj_button;

.. declaration:: obj_key

.. code-block:: c

    typedef struct REALKEY
    {
        wnd_obj obj;
    }obj_key;

.. declaration:: obj_label

.. code-block:: c

    typedef struct LABEL
    {
        wnd_obj obj;
        short trans;
        short padding;
        area touch_area;
    }obj_label;

.. declaration:: obj_number

.. code-block:: c

    typedef struct NUMBER
    {
        wnd_obj obj;
        short selidx;
        short value;
        short max;
        short min;
        short sel_enable;
        short digi_num;
        area touch;
    }obj_number;

.. declaration:: obj_spinbox

.. code-block:: c

    typedef struct SPINBOX
    {
        wnd_obj obj;
        short selidx;
        short value;
        short max;
        short min;
        short scrollbar_size;
        short scrollbar_color;
        area touch1;
        area touch2;
        area touch3;
    }obj_spinbox;

.. declaration:: obj_led

.. code-block:: c

    typedef struct LED
    {
        wnd_obj obj;
        int status;
    }obj_led;

.. declaration:: obj_shape

.. code-block:: c

    typedef struct SHAPE
    {
        wnd_obj obj;
        short parent_start_x;
        short parent_start_y;
        short xcenter;
        short ycenter;
    }obj_shape;

.. declaration:: obj_qrcode

.. code-block:: c

    typedef struct QRCODE
    {
        wnd_obj obj;
    }obj_qrcode;

.. declaration:: obj_progressbar

.. code-block:: c

    typedef struct PROGRESSBAR
    {
        wnd_obj obj;
        int value;
    }obj_progressbar;

.. declaration:: obj_slider

.. code-block:: c

    typedef struct SLIDER
    {
        wnd_obj obj;
        short thumbwidth;
        short value;
        area touch_area;
    }obj_slider;

.. declaration:: obj_switch

.. code-block:: c
   
    typedef struct SWITCH
    {
        wnd_obj obj;
        int status;
        area touch;
    }obj_switch;

.. declaration:: listview_item

.. code-block:: c

    typedef struct LISTVIEW_ITEM
    {
        //wnd_obj obj;
        short item_data1;
        short item_data2;
        char* str_index;
        char* str_content;
        char* str_value;
        void* next;
    }listview_item;

.. declaration:: obj_listview

.. code-block:: c

    typedef struct LISTVIEW
    {
        wnd_obj obj;
        short item_cnt;
        short sel_index;
        short first_line;
        short last_line;
        short item_height;
        short scrollbar_size;
        short item_width1;
        short item_width2;
        short sel_color;
        short padding;
        area touch_up;
        area touch_down;
        area touch_list;
        void* obj_list;
    }obj_listview;

.. declaration:: iconview_item

.. code-block:: c

    typedef struct ICONVIEWITEM_ITEM
    {
        //obj_listview_item* obj_ptr;
        char* icon;
        char* text;
        void* next;
    }iconview_item;

.. declaration:: obj_iconview

.. code-block:: c

    typedef struct ICONVIEW
    {
        wnd_obj obj;
        short item_cnt;
        short item_width;
        short item_icon_height;
        short item_text_height;
        short item_space_x;
        short item_space_y;
        short bc;
        short fc;
        short sc;
        short icon_font;
        short text_font;
        short sel_index;
        short first_idx;
        short last_idx;
        short scrollbar_size;
        short padding;
        area touch_up;
        area touch_down;
        area touch_list;
        void* obj_list;
    }obj_iconview;


Widget类型
~~~~~~~~~~~~

.. declaration:: ObjectType

.. code-block:: c  

    enum ObjectType{
        OBJ_WINDOW,         //窗体
        OBJ_BUTTON,         //按钮
        OBJ_LABEL,          //标签
        OBJ_LISTVIEW,       //列表
        OBJ_LED,            //指示灯
        OBJ_QRCODE,         //二维码
        OBJ_PROGRESSBAR,    //进度条
        OBJ_SLIDER,         //滑动条
        OBJ_SWITCH,         //开关
        OBJ_SHAPE,          //画布
        OBJ_IMAGE,          //图片
        OBJ_NUMBER,         //数字
        OBJ_ICONVIEW,       //图标列表
        OBJECT_KEY,         //实体按键
        OBJ_SPINBOX         //数字加减器
    };

|

函数
~~~~~~

.. declaration:: void GUI_Init(short width,short height)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      GUI初始化         GUI初始化，指定屏幕宽度和高度
参数      width             屏幕宽度
参数      height            屏幕高度
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void ClearScreen(short c)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      清除屏幕          用某种颜色进行清屏
参数      c                 颜色值，RGB565格式
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetBeep(short option)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置蜂鸣器         
参数      option            为0禁止蜂鸣器，为1打开蜂鸣器
返回值    void              无返回值
======  ================  ========================================


.. declaration:: void SetBrightness(short c)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置屏幕亮度         
参数      c                 0-10级可调
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetColor(int color)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置绘图颜色         
参数      c                 颜色值，RGB565格式
返回值    void              无返回值
======  ================  ========================================


.. declaration:: void DrawLine(short x1,short y1,short x2,short y2)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      画直线         
参数      x1                 起点x坐标
参数      y1                 起点y坐标
参数      x2                 终点x坐标
参数      y2                 终点y坐标
返回值    void               无返回值
======  ================  ========================================


.. declaration:: void DrawRect(short x1,short y1,short x2,short y2)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      画矩形         
参数      x1                 左上角x坐标
参数      y1                 左上角y坐标
参数      x2                 右下角x坐标
参数      y2                 右下角y坐标
返回值    void               无返回值
======  ================  ========================================

.. declaration:: void DrawCircle(short x,short y,short r)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      画圆形         
参数      x                 中心点x坐标
参数      y                 中心点y坐标
参数      r                 半径
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void FillCircle(short x,short y,short r)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      填充圆形         
参数      x                 中心点x坐标
参数      y                 中心点y坐标
参数      r                 半径
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void FillFrame(short x1,short y1,short x2,short y2)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      填充矩形         
参数      x1                 左上角x坐标
参数      y1                 左上角y坐标
参数      x2                 右下角x坐标
参数      y2                 右下角y坐标
返回值    void               无返回值
======  ================  ========================================

.. declaration:: void FillRoundFrame(short x1,short y1,short x2,short y2,short r)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      填充圆角矩形         
参数      x1                 左上角x坐标
参数      y1                 左上角y坐标
参数      x2                 右下角x坐标
参数      y2                 右下角y坐标
参数      r                  圆角半径
返回值    void               无返回值
======  ================  ========================================

.. declaration:: void DrawString(char* s,short x,short y,short font,short bc,short fc,int width)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      绘制文字         
参数      s                 字符串
参数      x                 左上角x坐标
参数      y                 左上角y坐标
参数      font              字体
参数      bc                背景色
参数      fc                绘制颜色
参数      width             超过此宽度换行
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void DrawBMP(char* s,short x,short y)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      绘制位图         
参数      s                 图片内存指针
参数      x                 左上角x坐标
参数      y                 左上角y坐标
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void DrawPNG(char* filename, int xoffset, int yoffset)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      绘制PNG         
参数      s                 图片内存指针
参数      x                 左上角x坐标
参数      y                 左上角y坐标
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void DrawQRCode(char* s, int xoffset, int yoffset)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      绘制二维码         
参数      s                 二维码文字
参数      x                 左上角x坐标
参数      y                 左上角y坐标
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void DrawJPEG(char* s, int xoffset, int yoffset)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      绘制JPEG         
参数      s                 图片内存指针
参数      x                 左上角x坐标
参数      y                 左上角y坐标
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateWindow(wnd* ww)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建窗体         
参数      ww                窗体结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CloseWindow(wnd* ww)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      关闭窗体         
参数      ww                窗体结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateButton(wnd* ww,obj_button* btn)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建按钮         
参数      ww                窗体结构体指针
参数      btn               按钮结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateRealKey(wnd* ww,obj_key* key)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建实体按键         
参数      ww                窗体结构体指针
参数      btn               实体按键结构体指针
返回值    void              无返回值
======  ================  ========================================


.. declaration:: void SetWidgetText(wnd_obj* obj,char* s)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置部件的文字         
参数      obj               部件结构体指针
参数      s                 字符串指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetWidgetForeColor(wnd_obj* obj,int c)

======  =====================  ========================================
类型      项目                  描述
======  =====================  ========================================
说明      设置部件的绘制颜色         
参数      obj                   部件结构体指针
参数      c                     颜色，RGB565格式
返回值    void                  无返回值
======  =====================  ========================================

.. declaration:: void SetWidgetBkColor(wnd_obj* obj,int c)

======  =====================  ========================================
类型      项目                  描述
======  =====================  ========================================
说明      设置部件的背景颜色         
参数      obj                   部件结构体指针
参数      c                     颜色，RGB565格式
返回值    void                  无返回值
======  =====================  ========================================

.. declaration:: void SetWidgetFont(wnd_obj* obj,int c)

======  ===================  ========================================
类型      项目                  描述
======  ===================  ========================================
说明      设置部件的字体         
参数      obj                   部件结构体指针
参数      c                     字体，枚举索引
返回值    void                  无返回值
======  ===================  ========================================

.. declaration:: void SetWidgetVisible(wnd_obj* obj,int c)

======  ===================  ========================================
类型      项目                  描述
======  ===================  ========================================
说明      设置部件可见性         
参数      obj                   部件结构体指针
参数      c                     0为不可见，1为可见，2为边框颜色设置的颜色
返回值    void                  无返回值
======  ===================  ========================================

.. declaration:: void CreateLabel(wnd *ww,obj_label* lbl)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建标签         
参数      ww                窗体结构体指针
参数      lbl               标签结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateLed(wnd *ww,obj_led* led)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建Led         
参数      ww                窗体结构体指针
参数      led               led结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetLedStatus(obj_led* led,int value)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设定Led状态         
参数      led               led结构体指针
参数      value             0则LED灭，1则LED亮
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateQRcode(wnd* ww,obj_qrcode* qrcode)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建二维码         
参数      ww                窗体结构体指针
参数      qrcode            二维码结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateProgressbar(wnd* ww,obj_progressbar* prgbar)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建进度条        
参数      ww                窗体结构体指针
参数      prgbar            进度条结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetProgressbarValue(obj_progressbar* prgbar,int value)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设定进度条的值         
参数      prgbar            进度条结构体指针
参数      value             0-100
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateListView(wnd* ww,obj_listview* lstv)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建列表视图        
参数      ww                窗体结构体指针
参数      lstv              列表视图结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void ListViewAddItem(obj_listview* lstv,int data,char* s1,char* s2,char * s3)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      给列表增加行       一般用于参数设置
参数      lstv              列表视图结构体指针
参数      data              这一行关联的数据
参数      s1                第一列字符串
参数      s2                第二列字符串
参数      s3                第三列字符串
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void ListViewSetItem(obj_listview* lstv,int row,int colum,char * s)

======  ==================  ========================================
类型      项目                  描述
======  ==================  ========================================
说明      设置列表某个格子       一般用于参数设置
参数      lstv                 列表视图结构体指针
参数      row                  行，第一行为0
参数      colum                列，第一列为0
返回值    void                 无返回值
======  ==================  ========================================

.. declaration:: short ListViewGetItemData(obj_listview* lstv,int row)

======  ==================  ========================================
类型      项目                  描述
======  ==================  ========================================
说明      获取列表某行数值       一般用于参数设置
参数      lstv                 列表视图结构体指针
参数      row                  行，第一行为0
返回值    short                 
======  ==================  ========================================

.. declaration:: void CreateIconView(wnd* ww,obj_iconview* icon)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建图标视图         
参数      ww                窗体结构体指针
参数      icon              图标视图结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void IconViewAddItem(obj_iconview* icon,char* s1,char* s2)

======  ==================  ========================================
类型      项目                  描述
======  ==================  ========================================
说明      给图标视图增加项       一般用于参数设置
参数      lstv                 图标视图结构体指针
参数      s1                   图标指针，图标字体中的utf-8编码
参数      s2                   文字字符串指针
返回值    void                 无返回值
======  ==================  ========================================


.. declaration:: void CreateSwitch(wnd* ww,obj_switch* switch_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建开关         
参数      ww                窗体结构体指针
参数      switch_obj        开关结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: int GetSwitchStatus(obj_switch* switch_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      获取开关状态         
参数      switch_obj        窗体结构体指针
参数      led               开关结构体指针
返回值    int               0则开关滑至左侧，1为开关滑至右侧
======  ================  ========================================

.. declaration:: void CreateShape(wnd* ww,obj_shape* shape_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建画布        
参数      ww                窗体结构体指针
参数      shape_obj         画布结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void ShapeClear(obj_shape* shape_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      清除画布        
参数      shape_obj         画布结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void CreateNumber(wnd* ww,obj_number* number_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建数字显示         
参数      ww                窗体结构体指针
参数      led               数字显示结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetNumberValue(obj_number* number,int val)

======  ==================  ========================================
类型      项目                  描述
======  ==================  ========================================
说明      设定数字显示的值         
参数      number              数字显示结构体指针
参数      val                 0-65535
返回值    void                无返回值
======  ==================  ========================================

.. declaration:: void CreateSlider(wnd* ww,obj_slider* slider_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建滑动条         
参数      ww                窗体结构体指针
参数      slider_obj        滑动条结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: int GetSliderValue(obj_slider* slider_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      获取滑动条值         
参数      slider_obj        滑动条结构体指针
返回值    int              
======  ================  ========================================

.. declaration:: void CreateSpinbox(wnd* ww,obj_spinbox* spinbox_obj)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      创建Spinbox       一般用于调节参数
参数      ww                窗体结构体指针
参数      spinbox_obj       Spinbox结构体指针
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetSpinboxRange(obj_spinbox* spinbox_obj,int max,int min)

======  =====================  ========================================
类型      项目                  描述
======  =====================  ========================================
说明      设置Spinbox调节范围         
参数      spinbox_obj           Spinbox结构体指针
参数      max                   最大值
参数      min                   最小值
返回值    void                  无返回值
======  =====================  ========================================

.. declaration:: void SetSpinboxValue(obj_spinbox* spinbox_obj,int val)

======  =====================  ========================================
类型      项目                  描述
======  =====================  ========================================
说明      设置Spinbox值         
参数      spinbox_obj           Spinbox结构体指针
参数      val                   设定值
返回值    void                  无返回值
======  =====================  ========================================

.. declaration:: void SendUserMessage(int id,char* buf)

======  =========================  ========================================
类型      项目                       描述
======  =========================  ========================================
说明      设置窗体消息接收缓冲区         
参数      id                         窗体id
参数      buf                        缓冲区
返回值    void                       无返回值
======  =========================  ========================================

