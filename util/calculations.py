'''
Calculations for solar racing telemetry system
'''

def calculate_voltage(s_value):
    voltage =  (s_value / 32767.0) * 6.144
    return voltage

def calculate_state_of_charge(v_res):
    battery_level = (v_res / 38.7)*100
    return battery_level

def calculate_power(s1_plus, s1_minus):
    power = ((s1_plus - s1_minus) / 0.001) * s1_minus
    return power