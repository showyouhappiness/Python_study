from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QRect
import sys
import datetime
import os
import shutil
import threading
from queue import Queue

import conf
from database_auto_commit import DataBase
from log import f_log


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(730, 250, 500, 210)
        self.setWindowTitle('复制图片')
        self.label1 = QLabel('请输入班次', self)
        self.label1.setGeometry(QRect(70, 10, 160, 30))
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setGeometry(QRect(190, 10, 221, 30))
        self.lineEdit_1.setFont(QFont('Arial', 14))

        self.checkbox1 = QCheckBox('人工废品图', self)
        self.checkbox1.setGeometry(QRect(70, 50, 160, 30))
        self.checkbox2 = QCheckBox('新算法漏检图', self)
        self.checkbox2.setGeometry(QRect(230, 50, 160, 30))
        self.checkbox3 = QCheckBox('新老算法均为pass图', self)
        self.checkbox3.setGeometry(QRect(70, 90, 160, 30))
        self.checkbox4 = QCheckBox('老算法过检图', self)
        self.checkbox4.setGeometry(QRect(230, 90, 160, 30))
        self.checkbox5 = QCheckBox('新算法过检图', self)
        self.checkbox5.setGeometry(QRect(70, 130, 160, 30))

        self.button = QPushButton('确定', self)
        self.button.setGeometry(QRect(130, 170, 160, 30))

        self.button.clicked.connect(self.confirmButtonClicked)

        self.show()


    def confirmButtonClicked(self):  # 确定按钮,点击后执行复制图片操作
        begintime = self.get_datetime(self.lineEdit_1.text()).get('begintime')
        endtime = self.get_datetime(self.lineEdit_1.text()).get('endtime')
        checkboxList = [self.checkbox1.isChecked(), self.checkbox2.isChecked(), self.checkbox3.isChecked(),
                        self.checkbox4.isChecked(), self.checkbox5.isChecked()]
        for i in range(len(checkboxList)):
            if checkboxList[i]:
                if i == 0:
                    threading.Thread(target=get_manual_reject_wheel, args=(
                        db_obj, fdw_schema, begintime, endtime, '人工废品图')).start()
                elif i == 1:
                    threading.Thread(target=get_algo_missed_wheel, args=(
                        db_obj, fdw_schema, cur_schema, begintime, endtime, 'Fail', 'Pass', '新算法漏检图')).start()
                elif i == 2:
                    threading.Thread(target=get_both_algo_passed_wheel, args=(
                        db_obj, fdw_schema, cur_schema, begintime, endtime, '新老算法均为pass图')).start()
                elif i == 3:
                    threading.Thread(target=get_old_algo_passed_wheel, args=(
                        db_obj, fdw_schema, begintime, endtime, '老算法过检图')).start()
                elif i == 4:
                    threading.Thread(target=get_new_algo_passed_wheel, args=(
                        db_obj, fdw_schema, cur_schema, begintime, endtime, '新算法过检图')).start()


    def get_datetime(self, time_now_str, is_duty=True):
        if not time_now_str:
            endtime = datetime.datetime.now()
        else:
            try:
                endtime = datetime.datetime.strptime(time_now_str, '%Y-%m-%d %H:%M:%S')
            except Exception as err:
                f_log.LOGW('err is {}'.format(err))
                f_log.LOGW('时间格式输入有误,请以 "YYYY-mm-dd HH:MM:SS" 格式输入;'
                           '示例: "2021-09-01 08:00:00" ')
                return

        f_log.LOGW("time_now: {}".format(endtime))

        endtime_day = int(endtime.strftime('%d'))
        endtime_hour = int(endtime.strftime('%H'))

        # 以班次统计
        if is_duty:
            if 8 <= endtime_hour < 20:
                endtime = endtime.strftime('%Y-%m-%d') + ' 08:00:00'
            elif endtime_hour >= 20:
                endtime = endtime.strftime('%Y-%m-%d') + ' 20:00:00'
            elif endtime_hour < 8:
                endtime = endtime - datetime.timedelta(days=1)
                endtime = endtime.strftime('%Y-%m-%d') + ' 20:00:00'

            endtime = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
            begintime = endtime - datetime.timedelta(hours=12)

            endtime = datetime.datetime.strftime(endtime, '%Y-%m-%d %H:%M:%S')
            begintime = datetime.datetime.strftime(begintime, '%Y-%m-%d %H:%M:%S')

        # 以天为单位统计
        else:
            # if running after 8 o'clock(contain 8 o'clock), then statistic yesterday
            # if running before 8 o'clock, then statistic the day before yesterday
            if endtime_hour >= 8:
                begintime = endtime - datetime.timedelta(days=1)
            else:
                begintime = endtime - datetime.timedelta(days=2)
                endtime = endtime - datetime.timedelta(days=1)

            begintime = begintime.strftime('%Y-%m-%d') + ' 08:00:00'
            endtime = endtime.strftime('%Y-%m-%d') + ' 08:00:00'

        begintime_day = int(datetime.datetime.strptime(begintime, '%Y-%m-%d %H:%M:%S').strftime('%d'))

        f_log.LOGI('查询范围 == {} 到 {}'.format(begintime, endtime))
        f_log.LOGI('begintime: {}'.format(begintime))
        f_log.LOGI('endtime: {}'.format(endtime))

        f_log.LOGI('begintime_day: {}'.format(begintime_day))
        f_log.LOGI('endtime_day: {}'.format(endtime_day))

        query_datetime_dict = {
            'begintime': begintime,
            'endtime': endtime,
            'begintime_day': begintime_day,
            'endtime_day': endtime_day
        }

        return query_datetime_dict


# 获取轮毂漏检数据
def get_algo_missed_wheel(db_obj, fdw_schema, cur_schema, begintime, endtime, old_result, new_result, algo_missed):
    sql_script = f" SELECT kf.knuckle_id,kf.x_ray_num " \
                 f" FROM {fdw_schema}.knuckle kf " \
                 f" INNER JOIN {cur_schema}.knuckle k " \
                 f" ON kf.knuckle_id = k.knuckle_id " \
                 f" WHERE k.process_datetime >= %(begintime)s " \
                 f" AND k.process_datetime < %(endtime)s " \
                 f" AND kf.review_result = %(old_result)s " \
                 f" AND k.review_result = %(new_result)s " \
                 f" AND kf.valid=1;"
    sql_script_variable = {
        'begintime': begintime,
        'endtime': endtime,
        'old_result': old_result,
        'new_result': new_result
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for i in query_result:
            f_log.LOGW(i)
            get_algo_missed_wheel_image_path(db_obj, fdw_schema, i, algo_missed)


# 通过漏检id获取漏检图片路径
def get_algo_missed_wheel_image_path(db_obj, fdw_schema, result, algo_missed):
    sql_script = f" SELECT kf.image_path" \
                 f" FROM {fdw_schema}.image kf" \
                 f" WHERE kf.knuckle_id = %(knuckle_id)s;"
    sql_script_variable = {
        'knuckle_id': str(result[0])
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for image_path in query_result:
            download_missed_wheel_image(result[1], image_path, algo_missed)


# 获取新算法轮毂过检数据
def get_new_algo_passed_wheel(db_obj, fdw_schema, cur_schema, begintime, endtime, algo_passed):
    sql_script = f" SELECT kf.knuckle_id,kf.x_ray_num " \
                 f" FROM {fdw_schema}.knuckle kf " \
                 f" INNER JOIN {cur_schema}.knuckle k " \
                 f" ON kf.knuckle_id = k.knuckle_id " \
                 f" WHERE k.process_datetime >= %(begintime)s " \
                 f" AND k.process_datetime < %(endtime)s " \
                 f" AND kf.review_result = 'Pass' " \
                 f" AND kf.result = 'Fail' " \
                 f" AND k.result = 'Fail' " \
                 f" AND kf.valid=1;"
    sql_script_variable = {
        'begintime': begintime,
        'endtime': endtime,
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for i in query_result:
            get_algo_passed_wheel_image_path(db_obj, fdw_schema, i, algo_passed)


# 获取老算法轮毂过检数据
def get_old_algo_passed_wheel(db_obj, fdw_schema, begintime, endtime, algo_passed):
    sql_script = f" SELECT kf.knuckle_id,kf.x_ray_num " \
                 f" FROM {fdw_schema}.knuckle kf " \
                 f" WHERE kf.process_datetime >= %(begintime)s " \
                 f" AND kf.process_datetime < %(endtime)s " \
                 f" AND kf.review_result = 'Pass' " \
                 f" AND kf.result = 'Fail' " \
                 f" AND kf.valid=1;"
    sql_script_variable = {
        'begintime': begintime,
        'endtime': endtime,
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for i in query_result:
            get_algo_passed_wheel_image_path(db_obj, fdw_schema, i, algo_passed)

# 获取人工废品图
def get_manual_reject_wheel(db_obj, fdw_schema, begintime, endtime, manual_reject):
    print('get_manual_reject_wheel')
    sql_script = f" SELECT kf.knuckle_id,kf.x_ray_num " \
                 f" FROM {fdw_schema}.knuckle kf " \
                 f" WHERE kf.process_datetime >= %(begintime)s " \
                 f" AND kf.process_datetime < %(endtime)s " \
                 f" AND kf.review_result = 'Fail' " \
                 f" AND kf.valid=1;"
    sql_script_variable = {
        'begintime': begintime,
        'endtime': endtime,
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for i in query_result:
            get_algo_passed_wheel_image_path(db_obj, fdw_schema, i, manual_reject)

# 新老算法均为pass图
def get_both_algo_passed_wheel(db_obj, fdw_schema, cur_schema, begintime, endtime, both_algo_passed):
    sql_script = f" SELECT kf.knuckle_id,kf.x_ray_num " \
                 f" FROM {fdw_schema}.knuckle kf " \
                 f" INNER JOIN {cur_schema}.knuckle k " \
                 f" ON kf.knuckle_id = k.knuckle_id " \
                 f" WHERE k.process_datetime >= %(begintime)s " \
                 f" AND k.process_datetime < %(endtime)s " \
                 f" AND kf.result = 'OK' " \
                 f" AND k.result = 'OK' " \
                 f" AND kf.valid=1;"
    sql_script_variable = {
        'begintime': begintime,
        'endtime': endtime,
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for i in query_result:
            get_algo_passed_wheel_image_path(db_obj, fdw_schema, i, both_algo_passed)

# 通过过检id获取过检图片路径
def get_algo_passed_wheel_image_path(db_obj, fdw_schema, result, algo_passed):
    sql_script = f" SELECT kf.image_path" \
                 f" FROM {fdw_schema}.image kf" \
                 f" WHERE kf.knuckle_id = %(knuckle_id)s ;"
    sql_script_variable = {
        'knuckle_id': str(result[0])
    }
    query_result = db_obj.query(sql_script, sql_script_variable)
    if query_result:
        for image_path in query_result:
            download_missed_wheel_image(result[1], image_path, algo_passed)

# 下载漏检图片
def download_missed_wheel_image(x_ray_num, image_path, algo_result):
    file_dict = conf.file_dict
    image_path = image_path[0]
    f_log.LOGW(f'x_ray_num: {x_ray_num}, old_image_path: {image_path}')
    if str(x_ray_num) in file_dict.keys():
        image_path = image_path.replace(image_path[0], file_dict.get(str(x_ray_num)), 1)  # 替换路径
        result_path = conf.result_path + '\\' + algo_result + '\\' + str(x_ray_num) + '\\' + image_path.split('\\')[-2]
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        try:
            shutil.copy(image_path, result_path)
            f_log.LOGW(f'copy file: {image_path} to {result_path} success')
        except Exception as e:
            f_log.LOGE(f'copy file error: {e}')


if __name__ == '__main__':
    fdw_schema = getattr(conf, 'database').get('fdw_schema')
    cur_schema = 'knuckle'
    # time_now_str = '2023-03-01 08:00:00'
    # begintime = get_datetime(time_now_str).get('begintime')
    # endtime = get_datetime(time_now_str).get('endtime')
    database_error_queue = Queue()

    database_reconnect_queue = Queue()

    database_state_queue_dict = {'error': database_error_queue,
                                 'status': database_reconnect_queue
                                 }

    db_obj = DataBase(queue_dict=database_state_queue_dict)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
