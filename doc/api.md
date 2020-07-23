## mvs api文档

[TOC]

### 约定
1. <mark>**所有请求参数，以json形式发送**</mark>
2. <mark>**返回参数中包含ret和msg,ret非0则为失败，msg记录失败信息。失败时，http状态码为非200的值**</mark>
3. <mark>**所有的时间以秒级的时间戳形式传递**</mark>

### host(测试)
http://ip/mvs/api

### 接口详细


#### 登陆

- **请求URL**
> [auth/login](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| username|  String | 是 | 用户名 |
| password|  String | 是 | 密码 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| name|   String|  用户名称|
| avatar|   String|  用户头像|
| roles|  数组 |  用户角色，**0管理员 1研发助理 2商务 3研发 4生产PMC 5生产工程 6作业员**|

#### 获取已登录用户信息

- **请求URL**
> [auth/cur](#)

- **请求方式** 
>**GET**

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| name|   String|  用户名称|
| avatar|   String|  用户头像|
| roles|  数组 |  用户角色，**0管理员 1研发助理 2商务 3研发 4生产PMC 5生产工程 6作业员**|


#### 登出

- **请求URL**
> [auth/logout](#)

- **请求方式** 
>**POST**

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取验证码（手机登陆有效）

- **请求URL**
> [auth/captcha](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| phone|  String | 是 | 手机号 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 重置密码

- **请求URL**
> [auth/reset_password](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| phone|  String | 是 | 手机号 |
| new_password|  String | 是 | 新密码 |
| code|  String | 是 | 验证码 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改密码

- **请求URL**
> [auth/password](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| old_password|  String | 是 | 旧用户密码 |
| new_password|  String | 是 | 新用户密码 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取用户

- **请求URL**
> [backend/user](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 用户id |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|   String|  用户id|
| name|   String|  用户名称|
| avatar|   String|  用户头像|
| roles|  数组 |  用户角色，**0管理员 1研发助理 2商务 3研发 4生产PMC 5生产工程 6作业员**|


#### 新增用户

- **请求URL**
> [backend/user](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| username|  String | 是 | 登陆名称 |
| password|  String | 是 | 密码 |
| roles|  数组 | 是 | 用户角色，**0管理员 1研发助理 2商务 3研发 4生产PMC 5生产工程 6作业员**|

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改用户

- **请求URL**
> [backend/user](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 用户id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| banned|  Integer | 否 | 是否被ban **0正常 1屏蔽** |
| name|  String | 否 | 用户名称 |
| roles|  数组 | 否 | 用户角色，**0管理员 1研发助理 2商务 3研发 4生产PMC 5生产工程 6作业员**|

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取物料

- **请求URL**
> [backend/materiel](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 物料id |
| part_no|  String | 否 | 料号 |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|   Integer|  物料id|
| part_no|   String|  料号|
| name|   String|  名称|
| desc|  String |  描述 |


#### 新增物料

- **请求URL**
> [backend/materiel](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| part_no|  String | 是 | 料号 |
| name|  String | 是 | 名称 |
| desc|  String | 是 | 名称 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改物料

- **请求URL**
> [backend/materiel](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 物料id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| part_no|  String | 否 | 料号 |
| name|  String | 否 | 名称 |
| desc|  String | 否 | 名称 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除物料

- **请求URL**
> [backend/materiel](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 物料id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取订单

- **请求URL**
> [backend/order](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 订单id |
| order_no|  String | 否 | 订单号 |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| order_id|  Integer |  订单id|
| order_no|   String|  订单号|
| materiel_id|   Integer|  物料id|
| part_no|  String |  料号 |
| start_addr|  String |  开始地址 |
| end_addr|  String |  结束地址 |
| fw_name1|  String |  固件名称1 |
| fw_version1|  String |  固件版本1 |
| fw_name2|  String |  固件名称12|
| fw_version2|  String |  固件版本2 |


#### 新增订单

- **请求URL**
> [backend/order](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| order_no|  String | 是 | 订单号 |
| materiel_id|  Integer | 是 | 物料id |
| part_no|  String | 是 | 料号 |
| start_addr|  String | 是 | 开始地址 |
| end_addr|  String | 是 | 结束地址 |
| fw_name1|  String | 是 | 固件名称1 |
| fw_version1|  String | 是 | 固件版本1 |
| fw_name2|  String | 否 | 固件名称2 |
| fw_version2|  String | 否 | 固件版本2 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改订单

- **请求URL**
> [backend/order](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 物料id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| order_no|  String | 否 | 订单号 |
| materiel_id|  Integer | 否 | 物料id |
| part_no|  String | 否 | 料号 |
| start_addr|  String | 否 | 开始地址 |
| end_addr|  String | 否 | 结束地址 |
| fw_name1|  String | 否 | 固件名称1 |
| fw_version1|  String | 否 | 固件版本1 |
| fw_name2|  String | 否 | 固件名称2 |
| fw_version2|  String | 否 | 固件版本2 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除订单

- **请求URL**
> [backend/order](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 订单id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取工序

- **请求URL**
> [backend/process](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 工序id |
| cate|  Integer | 否 | 类型 |
| is_ref|  Integer | 否 | 是否是参考工序 **1是 0否** |
| is_stand|  Integer | 否 | 是否是标准工序 **1是 0否** |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|  Integer |  工序id|
| work_order|   String|  工站|
| cate|   Integer|  类型|
| name|  String |  名称 |
| work_part_no|  String |  料号 |
| is_ref|  Integer |  是否是参考工序 **1是 0否**  |
| is_stand|  Integer |  是否是标准工序 **1是 0否** |


#### 新增工序

- **请求URL**
> [backend/process](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| work_order|  String | 是 | 工站 |
| cate|  Integer | 是 | 类型 |
| name|  String | 是 | 名称 |
| work_part_no|  String | 是 | 料号 |
| is_ref|  Integer | 是 | 是否是参考工序 **1是 0否** |
| is_stand|  Integer | 是 | 是否是标准工序 **1是 0否** |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改工序

- **请求URL**
> [backend/process](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 工序id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| work_order|  String | 否 | 工站 |
| cate|  Integer | 否 | 类型 |
| name|  String | 否 | 名称 |
| work_part_no|  String | 否 | 料号 |
| is_ref|  Integer | 否 | 是否是参考工序 **1是 0否** |
| is_stand|  Integer | 否 | 是否是标准工序 **1是 0否** |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除工序

- **请求URL**
> [backend/process](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 工序id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取产品工序

- **请求URL**
> [backend/product_process](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 产品工序id |
| materiel_id|  Integer | 否 | 物料id |
| part_no|  String | 否 | 料号 |
| cate|  Integer | 否 | 类型 |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|  Integer |  产品工序id|
| materiel_id|   Integer|  物料id|
| part_no|   String|  料号|
| work_order|  String |  工站 |
| cate|  Integer |  类型 |
| name|  String |  名称  |
| work_part_no|  String |  料号 |


#### 新增产品工序

- **请求URL**
> [backend/product_process](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| materiel_id|  Integer | 是 | 物料id |
| part_no|  String | 是 | 料号 |
| work_order|  String | 是 | 工站 |
| cate|  Integer | 是 | 类型 |
| name|  String | 是 | 名称 |
| work_part_no|  String | 是 | 料号 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改产品工序

- **请求URL**
> [backend/product_process](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 产品工序id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| materiel_id|  Integer | 否 | 物料id |
| part_no|  String | 否 | 料号 |
| work_order|  String | 否 | 工站 |
| cate|  Integer | 否 | 类型 |
| name|  String | 否 | 名称 |
| work_part_no|  String | 否 | 料号 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除产品工序

- **请求URL**
> [backend/product_process](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 产品工序id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取任务令

- **请求URL**
> [backend/task_work](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 任务令id |
| cate|  Integer | 否 | 类型 |
| materiel_id|  Integer | 否 | 物料id |
| part_no|  Integer | 否 | 料号 |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|  Integer |  产品工序id|
| work_order|   Integer|  工站|
| cate|  Integer |  类型 |
| name|  String |  名称  |
| materiel_id|   Integer|  物料id|
| part_no|   String|  料号|
| start_addr|  String |  开始地址 |
| end_addr|  String |  结束地址 |
| num|  Integer |  数量 |
| remark|  String |  备注 |


#### 新增任务令

- **请求URL**
> [backend/task_work](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| work_order|  Integer | 是 | 工站 |
| cate|  Integer | 是 | 类型 |
| name|  String | 是 | 名称 |
| materiel_id|  Integer | 是 | 物料id |
| part_no|  String | 是 | 料号 |
| start_addr|  String | 是 | 开始地址 |
| end_addr|  String | 是 | 结束地址 |
| num|  Integer | 是 | 数量 |
| remark|  String | 是 | 备注 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改任务令

- **请求URL**
> [backend/task_work](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 产品工序id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| work_order|  Integer | 否 | 工站 |
| cate|  Integer | 否 | 类型 |
| name|  String | 否 | 名称 |
| materiel_id|  Integer | 否 | 物料id |
| part_no|  String | 否 | 料号 |
| start_addr|  String | 否 | 开始地址 |
| end_addr|  String | 否 | 结束地址 |
| num|  Integer | 否 | 数量 |
| remark|  String | 否 | 备注 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除任务令

- **请求URL**
> [backend/task_work](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 任务令id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取行为

- **请求URL**
> [backend/action](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 任务令id |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|  Integer |  行为id|
| name|   String|  名称|

#### 新增行为

- **请求URL**
> [backend/action](#)

- **请求方式** 
>**POST**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| name|  String | 是 | 名称 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 修改行为

- **请求URL**
> [backend/action](#)

- **请求方式** 
>**PUT**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 行为id |
| update|  键值对 | 是 | 待修改的字段 |

- **update**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| name|  String | 否 | 名称 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 删除行为

- **请求URL**
> [backend/action](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 行为id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|


#### 获取行为日志

- **请求URL**
> [backend/action_log](#)

- **请求方式** 
>**GET**

- **url参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| id|  Integer | 否 | 任务令id |
| user_id|  Integer | 否 | 用户id |
| action_id|  Integer | 否 | 行为id |
| page|  Integer | 否 | 页码 |
| psize|  Integer | 否 | 页大小 |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|
| data|   键值对|  登陆数据|

- **data**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| id|  Integer |  行为日志id|
| user_id|   Integer|  用户id|
| action_id|   Integer|  行为id|
| action|   String|  行为名称|
| input_data|   String|  输入数据，json|
| output_data|   String|  输出数据，json|


#### 删除行为日志

- **请求URL**
> [backend/action_log](#)

- **请求方式** 
>**DELETE**

- **请求参数**
>
 | 请求参数      |     参数类型 |   是否必须   |   参数说明   |
| :-------- | :--------| :------ | :------ |
| obj_id|  Integer | 是 | 行为日志id |

- **返回参数**
> | 返回参数      |     参数类型 |   参数说明   |
| :-------- | :--------| :------ |
| ret|   Integer|  执行结果ret|
| msg|   String|  执行结果消息|