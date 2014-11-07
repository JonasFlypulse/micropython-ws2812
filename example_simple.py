from ws2812 import WS2812


ring = WS2812(spi_bus=1, led_count=16)

data = [
    (24, 0, 0),
    (0, 24, 0),
    (0, 0, 24),
    (12, 12, 0),
    (0, 12, 12),
    (12, 0, 12),
    (24, 0, 0),
    (21, 3, 0),
    (18, 6, 0),
    (15, 9, 0),
    (12, 12, 0),
    (9, 15, 0),
    (6, 18, 0),
    (3, 21, 0),
    (0, 24, 0),
    (8, 8, 8),
]

ring.show(data)
