import cocotb

import os
import random

from cocotb import simulator
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Edge, Event, Timer

from cocotb_test.simulator import run

import math
from fxpmath import Fxp

@cocotb.test()
async def cordic(dut):
    div = 2**c_FRACTIONAL_WIDTH

    dut.i_angle.value = Fxp(0, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi + math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi + math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(math.pi + 3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(2*math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()

    dut.i_angle.value = Fxp(0, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi - math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi - math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-math.pi - 3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()
    dut.i_angle.value = Fxp(-2*math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
    await Timer(10, unit='ns')
    print(f'sin({dut.i_angle.value.to_signed()/div} rad) = {dut.o_sin.value.to_signed()/div}')
    print(f'cos({dut.i_angle.value.to_signed()/div} rad) = {dut.o_cos.value.to_signed()/div}')
    print()

    cycles = 5
    res = 100
    for j in range(cycles):
        for i in range(res):
            dut.i_angle.value = Fxp(2*math.pi*i/res, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()
            await Timer(1, unit='ns')

parameters = {}
parameters['c_INTEGER_WIDTH'] = 4
parameters['c_FRACTIONAL_WIDTH'] = 32
parameters['c_PI'] = 0x3243F6A88
parameters['c_CORDIC_FACTOR'] = 0x09B74EDA8


c_INTEGER_WIDTH = parameters['c_INTEGER_WIDTH']
c_FRACTIONAL_WIDTH = parameters['c_FRACTIONAL_WIDTH']
c_PI = parameters['c_PI']
c_CORDIC_FACTOR = parameters['c_CORDIC_FACTOR']

if __name__ == "__main__":
    run(verilog_sources = [
            './../../rtl/cordic.v',
        ],
        toplevel = "cordic",
        module = "cordic_tb",
        parameters = parameters,
        sim_build = "sim_build/",
        timescale = "1ns/1ps",
        force_compile = True,
        seed = int(0),
        waves = 1,
    )