#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 Richard Hull and contributors
# See LICENSE.rst for details.

import time
from pathlib import Path
import socket
from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont

def draw_text(draw, margin_x, line_num, text):
    draw.text((margin_x, margin_y_line[line_num]), text, font=font_default, fill="white")

def stats(device):
    with canvas(device) as draw:
        draw_text(draw, 31, 1, "Goodbye")
        draw_text(draw, 41, 2, "from")
        draw_text(draw, 31, 3, f"{socket.gethostname()}")
        draw_text(draw, 31, 4, "& 125ade")

font_size = 12
margin_y_line = [0, 13, 25, 38, 51]

device = get_device()
font_default = ImageFont.truetype(str(Path(__file__).resolve().parent.joinpath("fonts", "DejaVuSansMono.ttf")), font_size)

stats(device)
time.sleep(10)
