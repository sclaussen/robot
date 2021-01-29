import dynamixel_sdk as sdk

TORQUE_ENABLE = 24
GOAL_POSITION = 30
PRESENT_POSITION = 36
MOVING_SPEED = 32

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

def set_torque(tty, protocol, device, value):
    result, error = protocol.write1ByteTxRx(tty, device, TORQUE_ENABLE, value)
    verify_response(result, error)

def goto(tty, protocol, device, goal):
    result, error = protocol.write2ByteTxRx(tty, device, GOAL_POSITION, goal)
    verify_response(result, error)
    while True:
        position, result, error = protocol.read2ByteTxRx(tty, device, PRESENT_POSITION)
        verify_response(result, error)
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (device, goal, position))
        if not abs(goal - position) > 20:
            break

# Open TTY
tty = open_tty('/dev/tty.usbserial-FT3WFGSI', 1000000)
protocol = sdk.PacketHandler(1.0)
set_torque(tty, protocol, 1, 1)
goto(tty, protocol, 1, 1023)
set_torque(tty, protocol, 1, 0)
tty.closePort()
