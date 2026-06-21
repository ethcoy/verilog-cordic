module iverilog_dump();
initial begin
    $dumpfile("axis_cordic.fst");
    $dumpvars(0, axis_cordic);
end
endmodule
