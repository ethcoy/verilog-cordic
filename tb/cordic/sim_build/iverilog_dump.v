module iverilog_dump();
initial begin
    $dumpfile("cordic.fst");
    $dumpvars(0, cordic);
end
endmodule
