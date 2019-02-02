import pandas
import json

'''
DATA
'''
def cull_data():
    data = pandas.read_csv('./CAN_Test_DATA.csv', index_col=0)
    data.drop([ 'equipment_type', 'can_id', 'can_unit' ], axis=1)
    data.drop(df.index[0])
    data.to_csv('./data.csv')

def get_data():
    data = pandas.read_csv('./data.csv', index_col=0)
    return data

def get_state():
    with open('./state.json', 'r') as f:
        state = json.load(f)
    return state

state = get_state()


'''
ALERTS
'''
def moisture_alert(data):
    for pt in data:
        if pt > 25.0 and state['moisture'] == "good":
            state['moisture'] = "alert"
            print('Moisture Alert: ' + str(pt))
        elif pt <= 25.0 and state['moisture'] == "alert":
            state['moisture'] = "good"
            print('Moisture Fixed: ' + str(pt))
        else:
            print(pt)

def grain_loss_alert(data):
    for pt in data:
        if pt > 2.0 and state['grain_loss'] == "good":
            state['grain_loss'] = "alert"
            print('Grain Loss Alert: ' + str(pt))
        elif pt <= 2.0 and state['grain_loss'] == "alert":
            state['grain_loss'] = "good"
            print('Grain Loss Fixed: ' + str(pt))
        else:
            print(pt)

def fuel_efficiency_alert(data):
    for pt in data:
        if pt <= .0000120292 and state['fuel_efficiency'] != "good":
            state['fuel_efficiency'] = "good"
            print('Fuel Efficiency Fixed: ' + str(pt))
        elif pt <= .000016298 and state['fuel_efficiency'] != "warning":
            state['fuel_efficiency'] = "warning"
            print('Fuel Efficiency Warning: ' + str(pt))
        elif pt > .000016298and state['fuel_efficiency'] != "alert":
            state['fuel_efficiency'] = "alert"
            print('Fuel Efficiency Alert: ' + str(pt))
        else:
            print(pt)

'''
MAIN
'''
# cull_data()
data = get_data()
moisture_alert(data.loc[data['can_name'] == 'MOISTURE']['can_value'])
grain_loss_alert(data.loc[data['can_name'] == 'GRAIN_LOSS_Shoe']['can_value'])
fuel_efficiency_alert(data.loc[data['can_name'] == 'FUEL_RATE']['can_value'])
