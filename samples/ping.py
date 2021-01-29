import dynamixel_sdk as sdk


def ping(device, device_id):
    tty = sdk.PortHandler('/dev/tty.usbserial-FT3WFGSI')
    tty.openPort()
    tty.setBaudRate(1000000)
    model, result, error = device.ping(tty, device_id)
    if result != sdk.COMM_SUCCESS:
        print("%s" % ax12a.getTxRxResult(result))
    elif error != 0:
        print("%s" % ax12a.getRxPacketError(error))
    else:
        return model
    tty.closePort()


ax12a = sdk.PacketHandler(1.0)
model = ping(ax12a, 1)
print("Model: %d" % model)
