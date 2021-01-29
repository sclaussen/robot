import dynamixel_sdk as sdk

ID = 3
TORQUE_ENABLE = 24
GOAL_POSITION = 30
PRESENT_POSITION = 36
MOVING_SPEED = 32

tty = None
protocol = None

def open_tty(name, baudrate):
    tty = sdk.PortHandler(name)
    tty.openPort()
    tty.setBaudRate(baudrate)
    return tty

def verify_response(result, error):
    if result != sdk.COMM_SUCCESS:
        print("%s" % protocol.getTxRxResult(result))
    elif error != 0:
        print("%s" % protocol.getRxPacketError(error))

def set_torque(device_id, value):
    result, error = protocol.write1ByteTxRx(tty, device_id, TORQUE_ENABLE, value)
    verify_response(result, error)

def set_position(device_id, goal):
    result, error = protocol.write2ByteTxRx(tty, device_id, GOAL_POSITION, goal)
    verify_response(result, error)
    while True:
        position = get_position(device_id)
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (device_id, goal, position))
        if not abs(goal - position) > 20:
            break

def get_position(device_id):
    position, result, error = protocol.read2ByteTxRx(tty, device_id, PRESENT_POSITION)
    verify_response(result, error)
    return position

def set_id(device_id, new_device_id):
    result, error = protocol.write1ByteTxRx(tty, device_id, ID, new_device_id)
    verify_response(result, error)


# Open TTY
tty = open_tty('/dev/tty.usbserial-FT3WFGSI', 1000000)
protocol = sdk.PacketHandler(1.0)

set_position(1, 1000)
print(get_position(1))
# set_id(5, 1)
# print(get_position(5))

tty.closePort()
