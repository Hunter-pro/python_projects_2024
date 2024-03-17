from re import T
import pandas
from sqlalchemy import column

class Data:
    def __init__(self) -> None:
        self.data = pandas.read_csv('./guess_the_state/50_states.csv')
        self.states = self.data.state.to_list()
        self.x_cor = self.data.x.to_list()
        self.y_cor = self.data.y.to_list()
        self.cord_dict = {}
        self.missedstates = self.states
        for i in range(len(self.states)):
            for i in range(len(self.states)):
                self.cord_dict[self.states[i]] = (self.x_cor[i],self.y_cor[i])
    
    def check_state(self,name):
        if name in self.states:
            self.missedstates = self.states.remove(name)
            return True
        return False
    
    def create_missed(self):
        missed_df = pandas.DataFrame(self.missedstates,columns=['states'])
        missed_df.to_csv('./guess_the_state/missed_states.csv')
    
