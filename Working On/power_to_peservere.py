# Runtime error
import math
for t in range(int(input())):
    diameter, motor_revoltuions, amount_power, speed, available_capcity, voltage_requirement, distance = map(int, input().split())
    circumference = math.pi*diameter
    if distance == 0:
        print("Success 1.0000")
    elif circumference == 0:
        print("Fail")
    elif available_capcity == 0:
        print("Fail")
    elif speed == 0:
        print("Fail")
    elif voltage_requirement == 0:
        circumference_m = circumference/100
        rotations_wheel = distance/circumference_m
        rotations_motor = rotations_wheel*motor_revoltuions
        minutes = rotations_motor/speed
        print("Success "+str(round(minutes,4)))
    else:
        circumference_m = circumference/100
        rotations_wheel = distance/circumference_m
        rotations_motor = rotations_wheel*motor_revoltuions
        minutes = rotations_motor/speed
        total_watts = rotations_motor*amount_power
        total_amps = total_watts/voltage_requirement
        total_energy = minutes*total_amps
        amp_hours = total_energy/60
        if amp_hours > available_capcity:
            print("Fail")
        else:
            print("Success "+str(round(minutes,4)))