import cocotb

import os
import random

from cocotb import simulator
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Edge, Event, Timer

from cocotb_test.simulator import run

import math
from fxpmath import Fxp

async def await_s_axis(s_clk, s_axis_tdata, s_axis_tvalid, s_axis_tready, data):
    await RisingEdge(s_clk)
    s_axis_tdata.value = data
    s_axis_tvalid.value = 1
    done = False
    while (not done):
        await RisingEdge(s_clk)
        if (s_axis_tready.value):
            done = True
            s_axis_tvalid.value = 0

# function for passing in signals that you want to be monitored upon assertion of tvalid?
async def await_m_axis(m_clk, m_axis_tvalid, m_axis_tready, *signals):
    div = 2**c_FRACTIONAL_WIDTH
    while (1):
        await RisingEdge(m_clk)
        if (m_axis_tvalid.value):
            m_axis_tready.value = 1
            for signal in signals:
                print(signal)
                print(f'{signal=}: {signal.value.to_signed()/div}')
            print()
            await RisingEdge(m_clk)
            m_axis_tready.value = 0

@cocotb.test()
async def axis_cordic(dut):

    dut.i_rst.value = 0
    dut.i_clk.value = 0

    await Timer(500, unit='ns')

    cocotb.start_soon(Clock(dut.i_clk, 10, unit="ns").start())
    cocotb.start_soon(await_m_axis(dut.i_clk, dut.m_axis_tvalid, dut.m_axis_tready, 
                                   dut.s_axis_angle_tdata_reg,
                                   dut.m_axis_cos_tdata,
                                   dut.m_axis_sin_tdata,
                                   dut.r_current_angle))

    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(0, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi + math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi + math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(math.pi + 3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(2*math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())

    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(0, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi - math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi - math.pi/2, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-math.pi - 3*math.pi/4, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())
    await await_s_axis(dut.i_clk, dut.s_axis_angle_tdata, dut.s_axis_tvalid, dut.s_axis_tready, Fxp(-2*math.pi, dtype=f'S{c_INTEGER_WIDTH}.{c_FRACTIONAL_WIDTH}').bin())



    await Timer(500, unit='ns')
    


parameters = {}
parameters['c_INTEGER_WIDTH'] = 4
parameters['c_FRACTIONAL_WIDTH'] = 16
parameters['c_PI'] = 0x3243F


c_INTEGER_WIDTH = parameters['c_INTEGER_WIDTH']
c_FRACTIONAL_WIDTH = parameters['c_FRACTIONAL_WIDTH']
c_PI = parameters['c_PI']

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