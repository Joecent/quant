"""
Data responsible of the input data and data fetch, pre-processing and persist

"""
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
def check_data_format(data_format):
    # only support data fetch from mysql/csv/online
    default_data_format = ["mysql", "csv", "online"]
    return data_format if data_format in default_data_format else None

# abstract class Data, support fetch from one data format and persist into another
class Data:
    def __init__(self, data_format):
        self._data_format = check_data_format(data_format)
        if self._data_format == None:
            print("data_format not supported, please check!")
            exit(-1)
        # initialize an empty pandas data frame
        self._data = pd.DataFrame()
        # to decide whether we should fetch data from other format
        self._data_ready = False
        # when data keys not set, all data will be fetched
        self._data_keys = []
        # when not set, all data will be fetched
        self._time_interval = []
       
    @property
    def data(self):
        return self._data
    # data can be fetched or just assign from existed pandas data frame
    @data.setter
    def data(self, value):
        self._data = value
    @property
    def data_ready(self):
        return self._data_ready
    @data_ready.setter
    def data_ready(self, value):
        self._data_ready = value
    @property
    def time_interval(self):
        return self._time_interval
    @time_interval.setter
    def time_interval(self, value):
        self._time_interval=value
    @property
    def data_keys(self):
        return self._data_keys
    @data_keys.setter
    def data_keys(self, value):
        self._data_keys=value
'''
    def fetch(self, fetch_method=fetch_data_from_mysql, data_keys=[]):
        raise NotImplementedError
    def process(self):
        raise NotImplementedError
    def persist(self):
        raise NotImplementedError
'''
# (TODO) implement the init/fetch/process/persist method by data format
def init_mysql():
    #print("init data from mysql")
    engine = create_engine('mysql+pymysql://Joe:sjjgtjytz@localhost:3306/quant')
    
    return engine
def fetch_data_from_mysql(data, data_keys, time_interval):
    print("fetch data from mysql")

def process_data(data):
    print("process data from mysql")

def persist_data_into_mysql(data):
    # when data exist and has no difference, then return out
    data_exist = check_data_existance(data)
    if data_exist:
        print("data has already exist and stay no difference, exit")
    else:
        print("persist data into mysql")

def check_data_existance(data):
    print("check data existance when persist data")
    return '333'
"""
Usage of data class:
init the class
>>>> mysql_data = MysqlData()
>>>> mysql_data.init()
fetch data from other format(like from mysql data base) to numpy/pandas arrray
>>>> data = mysql_data.fetch(fetch_data_from_mysql)
directly get the data when you ensure you just fetched data
>>>> data = mysql_data.data
set the numpy/pandas array data
>>>> mysql_data.data = valid_data
write numpy/pandas array to formated data(eg. data base)
>>>> mysql_data.persist(persist_data_into_mysql)
or just use default persist method
>>>> mysql_data.persist()
"""
class MysqlData(Data):
    def __init__(self):
        super(MysqlData, self).__init__("mysql")

    # different data format need different init method
    def init(self, init_method=init_mysql):
        self._init_method = init_method
        if self._init_method != None:
            if not self._init_method():
                print("init failed from {}".format(self._data_format))
                exit(-1)
        
    # data keys to specific the data feature name so only fetch these features
    # eg. data_keys = ["MACD", "OPEN", "MA5"] or data_keys = ["600010"] (stock id)
    # when set empty, all data will be fetched into numpy/pandas array
    def fetch(self, fetch_method=fetch_data_from_mysql, data_keys=[], time_interval=[]):
        # support change data_keys, time_interval  when fetch data
        if len(data_keys) != 0:
            self._data_keys = data_keys
        if len(time_interval) != 0:
            self._time_interval = time_interval

        self._data = fetch_method(self._data, self._data_keys, self._time_interval)
        self._data_ready = True
        return self._data
    def fetch_mysql(self):
        engine = init_mysql()
        sql_query = 'select * from user where id=1;'
        df_read = pd.read_sql_query(sql_query, engine)
        #test = {"id":"333"}
        test = df_read.to_json(orient='records')
        #data4 = init_mysql()
        return test
    def process(self, process_method=process_data):
        self._data = process_method(self._data)

    def persist(self, persist_method=persist_data_into_mysql):
        persist_method(self._data)

# (TODO) subclass like csv and online data format should also be implemented 


