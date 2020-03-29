'''
character filter was a strategy, has the ability to analysis the fundamental/technical/research features of one stock
'''
import Data
import Feature
# (TODO) more CharacterFilter needed
class CharacterFilter(Strategy):
    # you can either use data.time_interval to set data time interval or set time interval when strategy initialized
    def __init__(self, data, time_interval=[]):
        super(Strategy, self).__init__(data)
        # feature list is extremely important in strategy
        self._data_keys = Feature.fundamental_list[3::] + Feature.technical_list[2::]
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
        pass

    def run(self, run_method=run_character_filter):
        output_features = run_character_filter(self._data)
        return output_features
 
    def stop(self, stop_method=stop_character_filter):
        stop_MA5(self._data)

def run_character_filter(data):
    output_features = []
    return output_features

def stop_character_filter():
    pass

# (TODO) we should implement more characterfilter to see what method has good performance
class MilestoneFilter(CharacterFilter):
    pass
