import time
from .src import CustomLog
import sys
import os

exec_file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
current_path = os.path.dirname(__file__)
store_path = '{}/log_file'.format(current_path)
log_name = '{}.log'.format(exec_file_name)

if not os.path.exists(store_path):
    os.makedirs(store_path)

f_log = CustomLog.Logger(exec_file_name,
                         file_name='{}/{}'.format(store_path, log_name),
                         f_level='debug', t_level='warning', when='H', backup_count=480)


def trace_func(func):
    def wrapper(*args, **kwargs):
        f_log.LOGI("{} start".format(func.__name__))
        start_time = time.time()
        ret = func(*args, **kwargs)
        cost = time.time() - start_time
        f_log.LOGI("{} end. cost {}".format(func.__name__, cost))
        # if func.__name__ not in FuncListGauge.keys():
        #     FuncListGauge[func.__name__] = Gauge(f'{func.__name__}_run_cost', 'programme performace')
        # FuncListGauge[func.__name__].set(cost)
        return ret

    return wrapper
