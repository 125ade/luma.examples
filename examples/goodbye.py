#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 Richard Hull and contributors
# See LICENSE.rst for details.

import time
from pathlib import Path
from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont

def display_message(device, message):
    with canvas(device) as draw:
        font = ImageFont.truetype(str(Path(__file__).resolve().parent.joinpath("fonts", "DejaVuSansMono.ttf")), 20)
        width, height = draw.textsize(message, font=font)
        draw.text(
            ((device.width - width) // 2, (device.height - height) // 2),
            message,
            font=font,
            fill="white"
        )

device = get_device()
display_message(device, "goodbye")

# Keep the message on the screen for 10 seconds
time.sleep(10)
