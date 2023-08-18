控制器API列表
===============

引用  #include"sewcontrol.h"

结构体
~~~~~~~~~~~~~~~

.. declaration:: DRIVE_PARA

.. code-block:: c

    //驱动参数表
    typedef struct DRIVE_PARA
    {
        uint16_t sole01_enable;
        uint16_t sole01_auto_off;
        uint16_t sole01_start_duty;
        uint16_t sole01_start_time;
        uint16_t sole01_hold_duty;
        uint16_t sole01_hold_time;

        uint16_t sole02_enable;
        uint16_t sole02_auto_off;
        uint16_t sole02_start_duty;
        uint16_t sole02_start_time;
        uint16_t sole02_hold_duty;
        uint16_t sole02_hold_time;

        uint16_t sole03_enable;
        uint16_t sole03_auto_off;
        uint16_t sole03_start_duty;
        uint16_t sole03_start_time;
        uint16_t sole03_hold_duty;
        uint16_t sole03_hold_time;

        uint16_t sole04_enable;
        uint16_t sole04_auto_off;
        uint16_t sole04_start_duty;
        uint16_t sole04_start_time;
        uint16_t sole04_hold_duty;
        uint16_t sole04_hold_time;

        uint16_t sole05_enable;
        uint16_t sole05_auto_off;
        uint16_t sole05_start_duty;
        uint16_t sole05_start_time;
        uint16_t sole05_hold_duty;
        uint16_t sole05_hold_time;

        uint16_t sole06_enable;
        uint16_t sole06_auto_off;
        uint16_t sole06_start_duty;
        uint16_t sole06_start_time;
        uint16_t sole06_hold_duty;
        uint16_t sole06_hold_time;

        uint16_t sole07_enable;
        uint16_t sole07_auto_off;
        uint16_t sole07_start_duty;
        uint16_t sole07_start_time;
        uint16_t sole07_hold_duty;
        uint16_t sole07_hold_time;

        uint16_t sole08_enable;
        uint16_t sole08_auto_off;
        uint16_t sole08_start_duty;
        uint16_t sole08_start_time;
        uint16_t sole08_hold_duty;
        uint16_t sole08_hold_time;

        uint16_t sole09_enable;
        uint16_t sole09_auto_off;
        uint16_t sole09_start_duty;
        uint16_t sole09_start_time;
        uint16_t sole09_hold_duty;
        uint16_t sole09_hold_time;

        uint16_t sole10_enable;
        uint16_t sole10_auto_off;
        uint16_t sole10_start_duty;
        uint16_t sole10_start_time;
        uint16_t sole10_hold_duty;
        uint16_t sole10_hold_time;


        uint16_t pmsm_acc;
        uint16_t pmsm_max_speed;
        uint16_t pmsm_elecangle_offset;
        uint16_t pmsm_belt_ratio;
        uint16_t pmsm_stop_entry_speed;
        uint16_t pmsm_position_loop_angle;
        uint16_t pmsm_hold_enable;
        uint16_t pmsm_hold_torque;
        uint16_t pmsm_normal_interia;

        uint16_t pmsm_id_kp;
        uint16_t pmsm_id_ki;
        uint16_t pmsm_id_limit;

        uint16_t pmsm_iq_kp;
        uint16_t pmsm_iq_ki;
        uint16_t pmsm_iq_limit;

        uint16_t pmsm_speed_kp;
        uint16_t pmsm_speed_ki;
        uint16_t pmsm_speed_limit;

        uint16_t pmsm_position_kp;
        uint16_t pmsm_position_kd;
        uint16_t pmsm_position_limit;
    }DRIVE_PARA;

.. declaration:: sew_para

.. code-block:: c

    //功能参数
    typedef struct SEW_PARA
    {
        short id;
        short cate;
        char* name;
        short val;
        short max;
        short min;
        short def;
        char* title;
        char* comment;
    }sew_para;

.. declaration:: seam_mode

.. code-block:: c

    //工作模式
    enum seam_mode
    {
        seam_mode_action,       //动作，无电机旋转，一般用于停车后的过渡环节
        seam_make_stitches,     //缝制，电机正常速度旋转
        seam_jogging            //调整电机位置，电机以较低速度旋转
    };

.. declaration:: seg_event

.. code-block:: c

    //事件，一般用于伴随主轴电机旋转经过某些特定位置时发生事件
    typedef struct EventTypedef
    {
        char action;            //0表示无action,不为0则有动作
        char action_type;       //0表示经过位置检查点IO输出,1表示经过位置检查点执行_cb_action所定义的动作,2表示每针经过位置检查点执行_cb_action所定义的动作(位置小于1针)
        char out_chanel;        //输出通道
        char out_level;         //输出电平
        int check_point;        //检查点，启动位置为0
        void* _cb_action;       //经过检查点触发事件的处理回调函数
    } seg_event;

.. declaration:: seam_seg

.. code-block:: c

    //运动控制节段，一个完整的运动由多个节段组成，这是运动规划时的最小单位
    typedef struct SeamSegTypedef
    {
        char mode;	            //工作模式
        char enable;	        //使能
        char auto_enter_next;	//如果启动条件仍存在，直接进入下一seg
        char auto_running;		//如果启动条件不存在，则暂停
        char auto_attach;	    //和下一seg连接起来，不判断启动条件
        char start_event_id;    //触发事件
        char pause_event_id;    //暂停事件,0表示无法暂停
        char end_event;	        //结束事件
        short maxspeed;	        //最高转速
        short degree;	        //目标位置，调度，与stitches合用
        int stitches;           //目标位置，整针数
        void* _cb_prepare_job;	//启动前的处理回调函数
        seg_event* event[16];	//基于位置的事件组
    } seam_seg;

函数
~~~~~~~~~~~~~~~

.. declaration:: void SewControlInit()

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      初始化运动控制        
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void GetDriverParameters(char* buf,int cate)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      获取驱动参数       获取全部参数值到缓冲区
参数      buf               缓冲区
参数      cate              0为参数最大值，1为参数最小值，2为参数缺省值，3为参数当前值
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetGlobalSpeedLimit(short speed)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置最大速度        
参数      speed             速度值，rpm
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetAccel(short acc,short de_acc)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置加速度        
参数      acc               加速时加速度，120 0->4500rpm in 150ms
参数      de_acc            减速时加速度
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void EnqueueSeamSeg(seam_seg* seg)

======  ===========================  ========================================
类型      项目                          描述
======  ===========================  ========================================
说明      向运动规划器加入一个节段        
参数      seg                          节段结构体指针 
返回值    void                         无返回值
======  ===========================  ========================================

.. declaration:: void LoadSeamSegs()

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      重新装载节段        
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void NextSeg()

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      进入下一个节段        
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void SetSeg(int idx)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      跳至设定节段        
参数      idx               设定节段索引 
返回值    void               无返回值
======  ================  ========================================

.. declaration:: void EnqueueGlobalEvent(seg_event* seg)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      设置全局事件        
参数      seg               全局事件结构体指针 
返回值    void              无返回值
======  ================  ========================================

.. declaration:: int StartMotion()

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      开始电机旋转        
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void FeedStitch(short x,short y,short theta)

======  ================  ========================================
类型      项目                  描述
======  ================  ========================================
说明      发送送布指令        一般用于送布框动作的机型
参数      x                  
参数      y                  
参数      theta              
返回值    void              无返回值
======  ================  ========================================

.. declaration:: void StartJogging(short speed,short target)

======  ===================  ========================================
类型      项目                  描述
======  ===================  ========================================
说明      开始一个调整运动 
参数      speed                调整时的转速
参数      target               设定的目标位置
返回值    void                 无返回值
======  ===================  ========================================

.. declaration:: void SetRunLimit(int val)

======  =====================  ========================================
类型      项目                    描述
======  =====================  ========================================
说明      禁止或使能电机旋转       一般用于界面操作调整时，禁止控制器电机动作     
参数      val                    为0禁止旋转，为1恢复正常
返回值    void                   无返回值
======  =====================  ========================================
