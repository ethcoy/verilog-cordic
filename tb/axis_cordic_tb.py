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
async def axis_cordic(dut):

    dut.i_rst.value = 0
    dut.i_clk.value = 0

    await Timer(500, unit='ns')

    cocotb.start_soon(Clock(dut.i_clk, 10, unit="ns").start())

    await Timer(500, unit='ns')

    # for i in range(c_FRACTIONAL_WIDTH):
    #     print(dut.r_atan_lut[i].value)
    
    # print(dut.r_pi.value)

    dut.s_axis_angle_tdata.value = Fxp(math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin()

    print(Fxp(-0.75, dtype=f'S{2}.{2}').bin())

    await RisingEdge(dut.i_clk)
    dut.s_axis_angle_tvalid.value = 1
    await RisingEdge(dut.i_clk)
    await RisingEdge(dut.i_clk)

    div = 2**c_FRACTIONAL_WIDTH

    await Timer(500, unit='ns')


    # print(int(dut.r_y.value.signed_integer)/div)

    # print(Fxp(int(dut.r_y.value.signed_integer), dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}'))
    # print(Fxp(int(dut.r_current_angle.value.signed_integer), dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}'))
    


parameters = {}
parameters['c_INTEGER_WIDTH'] = 4
parameters['c_FRACTIONAL_WIDTH'] = 16

c_INTEGER_WIDTH = parameters['c_INTEGER_WIDTH']
c_FRACTIONAL_WIDTH = parameters['c_FRACTIONAL_WIDTH']

if __name__ == "__main__":
    run(verilog_sources = [
            './../rtl/axis_cordic.v',
        ],
        toplevel = "axis_cordic",
        module = "axis_cordic_tb",
        parameters = parameters,
        sim_build = "sim_build/",
        timescale = "1ns/1ps",
        force_compile = True,
        seed = int(0),
        waves = 1,
    )