import serial
import uinput

ser = serial.Serial('/dev/ttyUSB0', 9600)

device = uinput.Device([
        uinput.KEY_A,
        uinput.KEY_B,
        uinput.KEY_G,
        uinput.KEY_F,
        uinput.KEY_E,
        uinput.KEY_D,
        uinput.KEY_J,
        uinput.KEY_DOWN,
        uinput.KEY_UP,
        uinput.KEY_LEFT,
        uinput.KEY_RIGHT,
])

print 'Arduino Keyboard - Thomas Rager\n'

def handleKey(inp, key):
    keyName = 'KEY_' + key.upper()

    if inp == 'P' + key:
        device.emit(getattr(uinput, keyName), 1)

    if inp == 'R' + key:
        device.emit(getattr(uinput, keyName), 0)

def handleDirection(inp, direction )
    if inp == Jl:
        device.emit(uinput.KEY_LEFT, 1)
    if inp == Jr:
        device.emit(uinput.KEY_RIGHT, 1)
    if inp == Ju:
        device.emit(uinput.KEY_UP, 1)
    if inp == Jd:
        device.emit(uinput.KEY_DOWN, 1)

    if inp == Jlu:
        device.emit(uinput.KEY_LEFT, 1)
        device.emit(uinput.KEY_UP, 1)
    if inp == Jld:
        device.emit(uinput.KEY_LEFT, 1)
        device.emit(uinput.KEY_DOWN, 1)
    if inp == Jrd:
        device.emit(uinput.KEY_RIGHT, 1)
        device.emit(uinput.KEY_DOWN, 1)
    if inp == Jru:
        device.emit(uinput.KEY_RIGHT, 1)
        device.emit(uinput.KEY_UP, 1)

    if line == 'J0':
        resetDirection()

def resetDirection()
     device.emit(uinput.KEY_DOWN, 0)
     device.emit(uinput.KEY_UP, 0)
     device.emit(uinput.KEY_LEFT, 0)
     device.emit(uinput.KEY_RIGHT, 0)

while True:
    line = ser.readline().rstrip()

    handleKey(line, 'a')
    handleKey(line, 'b')
    handleKey(line, 'c')
    handleKey(line, 'f')
    handleKey(line, 'e')
    handleKey(line, 'g')
    handleKey(line, 'e')
    handleKey(line, 'd')
    handleKey(line, 'j')

    handleDirection(line)



