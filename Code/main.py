from machine import Pin, I2C
import sh1106
import time

#PIN CONFIG

# I2C OLED Display pins (D4 = SDA, D5 = SCL)
i2c = I2C(0, scl=Pin(23), sda=Pin(22), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3C)

# Status Indicator LED (D6 net)
led = Pin(16, Pin.OUT)

# Cherry MX Keyswitches (D0, D1, D2, D3 nets)
# Configured as PULL_UP because the switch routes to GND when pressed.
key1 = Pin(0, Pin.IN, Pin.PULL_UP)   # D0/A0
key2 = Pin(1, Pin.IN, Pin.PULL_UP)   # D1/A1
key3 = Pin(2, Pin.IN, Pin.PULL_UP)   # D2/A2
key4 = Pin(21, Pin.IN, Pin.PULL_UP)  # D3

#START

display.fill(0)
display.text("HACK CLUB PCB", 12, 10, 1)
display.text("Firmware v1.0", 12, 30, 1)
display.show()
time.sleep(1.5)

#MAIN

while True:
    display.fill(0)
    
    # Text headers
    display.text("--- COUNTER ---", 0, 0, 1)
    
    # Read switches (0 means pressed because of PULL_UP layout configuration)
    k1_pressed = (key1.value() == 0)
    k2_pressed = (key2.value() == 0)
    k3_pressed = (key3.value() == 0)
    k4_pressed = (key4.value() == 0)
    
    # Visual grid indicator updates
    display.text(f"KEY 1: {'[X]' if k1_pressed else '[ ]'}", 0, 20, 1)
    display.text(f"KEY 2: {'[X]' if k2_pressed else '[ ]'}", 0, 35, 1)
    display.text(f"KEY 3: {'[X]' if k3_pressed else '[ ]'}", 64, 20, 1)
    display.text(f"KEY 4: {'[X]' if k4_pressed else '[ ]'}", 64, 35, 1)
    
    # Master LED action: Turn ON if any key is actively being pressed down
    if k1_pressed or k2_pressed or k3_pressed or k4_pressed:
        led.value(1)
        display.text("LED Status: ON", 0, 52, 1)
    else:
        led.value(0)
        display.text("LED Status: OFF", 0, 52, 1)
        
    # Render loop changes to the physical SH1106 screen
    display.show()
    
    # Short sleep interval to prevent screen flicker
    time.sleep(0.05)
