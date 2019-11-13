# coding: utf-8
import sys
import pymysql
import redis

open_id = sys.argv[1]

table_num = sum(map(lambda x: ord(x), open_id)) % 10

new_duba_test = pymysql.connect(
    "10.47.20.228",
    "newduba_test_pro",
    "9dw7mqpuaxx4kvbw0vee9k67r2ghd8j7",
    "new_duba_test",
    3306,
)

r = redis.StrictRedis('10.47.30.207', password='07#YuKZCzT44(lcZ')

cursor = new_duba_test.cursor()
# 用户信息
cursor.execute('update new_duba_user set is_vip=0,vip_type=0,has_tryout=0,end_time=0 where open_id=%s', open_id)
cursor.execute('update new_duba_user_extend_info set vip_starttime="1970-01-01 00:00:00",succ_order_count=0,\
    succ_conti_count=0,succ_deduc_count=0,succ_sign_count=0,last_order_id="",last_order_pay_type=0,\
    last_open_id_type=0 where open_id=%s', open_id)
r.delete('new_duba_user_%s' % open_id)
r.delete('new_duba_user_extend_info_%s' % open_id)
r.delete('pure_duba_sess__user_%s' % open_id)
# 订单支付
cursor.execute('delete from new_duba_order where open_id=%s', open_id)
cursor.execute('delete from new_duba_continuous where open_id=%s', open_id)
cursor.execute('delete from new_duba_deductions where open_id=%s', open_id)
r.delete('new_duba_continuous_%s' % open_id)
r.delete('new_duba_continuous_code_%s' % open_id)
# 权限相关
cursor.execute('delete from new_duba_user_permission where open_id=%s', open_id)
cursor.execute('delete from new_duba_permission_record_%d where open_id=%s' %(table_num,open_id))
r.delete('new_duba_user_permission_%s' % open_id)
# 账号绑定记录
cursor.execute('delete from new_duba_user_bind where open_id=%s', open_id)
cursor.execute('delete from new_duba_user_bind_tourist where open_id=%s', open_id)
r.delete('user_svrid_%s' % open_id)
r.delete('ijinshan_bind_info_%s' % open_id)
# 1对1服务
cursor.execute('delete from new_duba_121srv_order where open_id=%s', open_id)
cursor.execute('delete from new_duba_121srv_user_order_stat where open_id=%s', open_id)
cursor.execute('delete from new_duba_box_121srv_order where open_id=%s', open_id)
cursor.execute('delete from new_duba_box_121srv_user_order_stat where open_id=%s', open_id)
# 有赞积分商城
cursor.execute('delete from new_duba_youzan_promocode_record where open_id=%s', open_id)

cursor.close()
new_duba_test.commit()
new_duba_test.close()



print("ok, i'am fine")
