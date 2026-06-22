module iverilog_dump();
initial begin
    $dumpfile("axis_cordic_iterative.fst");
    $dumpvars(0, axis_cordic_iterative);
end
endmodule
