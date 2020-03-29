"""
strategy means how to use the input and output data, include strategy run/stop 
"""
import Data
import numpy as np
import pandas as pd
class Strategy:
    def __init__(self, data):
        # data should be data class object carrying necessary info
        self._data = data
        self._data_keys = []
        self._time_internal = []

    def init():
        raise NotImplementedError
    def run():
        raise NotImplementedError
    def stop():
        raise NotImplementedError

    # we should make sure that subclass strategy feature list equal to input data feature list
    def check_data_valid(subclass_list, data_list):
        subclass_list = subclass_list.sort()
        data_list = data_list.sort()
        return subclass_list == data_list

# (TODO) implement specific run/stop method by different strategies
# MA5Strategy is just an example
def run_MA5(data):
    print("strategy is MA5")
    output_features = pd.DataFrame() 
    return output_features

def stop_MA5(data):
    print("strategy MA5 stoped")

""" 
Usage of strategy class
when initializing a strategy, you should set the data attribute including time_interval and
>>>> mysql_data = MysqlData()
>>>> mysql_data.init()
should set the atttribute that strategy used
>>>> mysql_data.data_keys = ["MA5"]
>>>> mysql_data.time_interval = ["20200119", "20200201"]
>>>> mysql_data.fetch()
MA5Strategy will check whether the data keys is valid for this strategy
>>>> MA5 = MA5Strategy(mysql_data)

"""
# (TODO) more strategies needed
class MA5Strategy(Strategy):
    # you can either use data.time_interval to set data time interval or set time interval when strategy initialized
    def __init__(self, data, time_interval=[]):
        super(MA5Strategy, self).__init__(data)
        # feature list is extremely important in strategy
        self._data_keys = ["MA5"]
        # class keys should stay no difference with data keys while time interval can change
        self._time_interval = time_interval

        data_keys_ready = check_data_valid(self._subclass_keys, self._data.data_keys)
        time_interval_ready = check_data_valid(self._subclass_time_interval, self._data.time_interval)

        self._data.data_ready = data_keys_ready and time_interval_ready

        if not self._data.data_ready:
            # data keys are used different with time interval, but both should stay the same
            self._data.fetch(data_keys=strategy_features, time_interval=time_interval)

    def init(self):
        print("init strategy!")

    def run(self, run_method=run_MA5):
        output_features = run_MA5(self._data)
        return output_features
 
    def stop(self, stop_method=stop_MA5):
        stop_MA5(self._data)

