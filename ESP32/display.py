from machine import Pin, mem32
import time

GPIO_OUT_REG = 0x3FF44004

PIN_0 = 26
PIN_1 = 27
PIN_2 = 15
PIN_3 = 17
PIN_4 = 18 
PIN_5 = 19
PIN_6 = 25


led_0 = Pin(PIN_0, Pin.OUT) #arriba
led_1 = Pin(PIN_1, Pin.OUT) #abajo
led_2 = Pin(PIN_2, Pin.OUT) #centro
led_3 = Pin(PIN_3, Pin.OUT) #arriba derecha
led_4 = Pin(PIN_4, Pin.OUT) #arriba izq
led_5 = Pin(PIN_5, Pin.OUT) #abajo derecha 
led_6 = Pin(PIN_6, Pin.OUT) #abajo izq

led_0.value(1)
led_1.value(1)
led_2.value(1)
led_3.value(1)
led_4.value(1)
led_5.value(1)
led_6.value(1)


while True:
    
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_3) | (1<<PIN_4) | (1<<PIN_5) | (1<<PIN_6)
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_3) | (1<<PIN_5)
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_3) | (1<<PIN_6) 
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_3) | (1<<PIN_5) 
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_2) | (1<<PIN_3) | (1<<PIN_4) | (1<<PIN_5) 
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_4) | (1<<PIN_5) 
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_4) | (1<<PIN_5) | (1<<PIN_6)
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_3) | (1<<PIN_5)
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_3) | (1<<PIN_4) | (1<<PIN_5) | (1<<PIN_6) 
    time.sleep(1)
    mem32[GPIO_OUT_REG] = (1<<PIN_0) | (1<<PIN_1) | (1<<PIN_2) | (1<<PIN_3) | (1<<PIN_4) | (1<<PIN_5)
    time.sleep(1)
    