# coding=utf-8
import logging
import threading
from logging import handlers
from queue import Queue

import requests
import json


class _Formatter(logging.Formatter):
    TAG = "crf"

    def format(self, record):
        record.app_tag = self.TAG
        return super(_Formatter, self).format(record)

    def set_tag(self, tag):
        self.TAG = tag


class CustomHandler(logging.Handler):
    queue = Queue()
    msg_thread = None

    def emit(self, record):
        log_entry = self.format(record)
        self.queue.put(log_entry)

    def thread_queue(self, url):
        while True:
            try:
                msg = self.queue.get()
                self.queue.task_done()

                if msg == "exit":
                    break

                requests.post(url,
                              json.dumps(msg),
                              headers={"Content-type": "application/json", 'Connection': 'close'},
                              timeout=0.1)
            except Exception:
                pass

    def start_thread_queue(self, url):
        if self.msg_thread is None:
            self.msg_thread = threading.Thread(target=self.thread_queue,
                                               daemon=True,
                                               name="http log",
                                               args=(url, ))
            self.msg_thread.start()

    def stop_thread_queue(self):
        self.queue.put("exit")


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self,
                 module_name,
                 file_name='main.log',
                 f_level='info',
                 t_level='error',
                 when='MIDNIGHT',
                 backup_count=10,
                 fmt='[%(app_tag)s]%(asctime)s %(process)d %(thread)6d - %(levelname)s - %(name)8s - %(filename)s %(funcName)s %(lineno)d - %(threadName)s: %(message)s'):

        self.logger = logging.getLogger(module_name)
        self.format_str = _Formatter(fmt)
        self.logger.setLevel(self.level_relations.get('debug'))
        self.f_level = f_level
        """往屏幕终端上输出"""
        sh = logging.StreamHandler()
        sh.setFormatter(self.format_str)
        sh.setLevel(self.level_relations.get(t_level))

        th = handlers.TimedRotatingFileHandler(filename=file_name,
                                               when=when,
                                               backupCount=backup_count,
                                               encoding='utf-8')

        """
        往文件里写入指定间隔时间自动生成文件的处理器
        实例化TimedRotatingFileHandler
        interval是时间间隔，
        backupCount是备份文件的个数，如果超过这个个数，就会自动删除，
        when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        """
        th.setFormatter(self.format_str)
        th.setLevel(self.level_relations.get(self.f_level))

        "把对象加到logger里"
        self.logger.addHandler(sh)
        self.logger.addHandler(th)

        self.web_handler = None

        self.LOGD = self.logger.debug
        self.LOGI = self.logger.info
        self.LOGW = self.logger.warning
        self.LOGC = self.logger.critical
        self.LOGE = self.logger.error

    def http_handler_add(self, url):
        self.web_handler = CustomHandler()

        self.web_handler.setFormatter(self.format_str)
        self.web_handler.setLevel(self.level_relations.get(self.f_level))
        self.web_handler.start_thread_queue(url)
        self.logger.addHandler(self.web_handler)

    # def LOGD(self, msg, *args, **kwargs):
    #     self.logger.debug(msg, *args, **kwargs)
    #
    # def LOGI(self, msg, *args, **kwargs):
    #     self.logger.info(msg, *args, **kwargs)
    #
    # def LOGW(self, msg, *args, **kwargs):
    #     self.logger.warning(msg, *args, **kwargs)
    #
    # def LOGC(self, msg, *args, **kwargs):
    #     self.logger.critical(msg, *args, **kwargs)
    #
    # def LOGE(self, msg, *args, **kwargs):
    #     self.logger.error(msg, *args, **kwargs)


if __name__ == '__main__':
    log = Logger('all', f_level='debug', t_level='error')
    log.LOGD('debug')
    log.LOGI('info')
    log.LOGW('警告 ')
    log.LOGE('报错')
    log.LOGC('严重')
    Logger('error', f_level='error').LOGE('error')