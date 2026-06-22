module cordic #(
    parameter c_INTEGER_WIDTH = 4,
    parameter c_FRACTIONAL_WIDTH = 16,
    // Fixed-point representation of pi
    parameter c_PI = 'h3243F,
    parameter c_DATA_WIDTH = c_INTEGER_WIDTH + c_FRACTIONAL_WIDTH
) (
    input wire signed [c_DATA_WIDTH - 1:0] i_angle,
    
    output wire signed [c_DATA_WIDTH - 1:0] o_sin,
    output wire signed [c_DATA_WIDTH - 1:0] o_cos
);

reg signed [c_DATA_WIDTH - 1:0] r_sin [0:c_FRACTIONAL_WIDTH];
reg signed [c_DATA_WIDTH - 1:0] r_cos [0:c_FRACTIONAL_WIDTH];

assign o_sin = r_sin[c_FRACTIONAL_WIDTH - 1];
assign o_cos = r_cos[c_FRACTIONAL_WIDTH - 1];

reg signed [c_DATA_WIDTH - 1:0] r_atan_lut [0:c_FRACTIONAL_WIDTH];

initial begin
        r_cos[0] <= {c_DATA_WIDTH{1'b0}};

        $display("Reading atan LUT...");
        $readmemh("atan_lut.mem", r_atan_lut);
end

reg signed [c_DATA_WIDTH - 1:0] r_pi = c_PI;

reg signed [c_DATA_WIDTH - 1:0] r_current_angle [0:c_FRACTIONAL_WIDTH];

integer i;

reg [c_DATA_WIDTH - 1:0] r_angle = {c_DATA_WIDTH{1'b0}};

always @(*) begin
    if ($signed({c_DATA_WIDTH{1'b0}}) <= i_angle && i_angle <= r_pi) begin
        r_sin[0] = 1'b1 << c_FRACTIONAL_WIDTH;
        r_current_angle[0] = r_pi >> 1'b1;
    end else if (r_pi <= i_angle && i_angle <= 2*r_pi) begin
        r_sin[0] = {c_INTEGER_WIDTH{1'b1}} << c_FRACTIONAL_WIDTH;
        r_current_angle[0] = 3*r_pi >> 1'b1;
    end else if (-r_pi <= i_angle && i_angle <= $signed({c_DATA_WIDTH{1'b0}})) begin
        r_sin[0] = {c_INTEGER_WIDTH{1'b1}} << c_FRACTIONAL_WIDTH;
        r_current_angle[0] = -(r_pi >> 1'b1);
    end else begin
        r_sin[0] = 1'b1 << c_FRACTIONAL_WIDTH;
        r_current_angle[0] = -(3*r_pi >> 1'b1);
    end

    for (i = 0; i < c_FRACTIONAL_WIDTH; i = i + 1) begin
        r_cos[i + 1] = r_cos[i] - (r_sin[i] >>> i);
        r_sin[i + 1] = (r_cos[i] >>> i) + r_sin[i];
        r_current_angle[i + 1] = r_current_angle[i] + r_atan_lut[i];
        if (i_angle - r_current_angle[i] < $signed({c_DATA_WIDTH{1'b0}})) begin
            r_cos[i + 1] = r_cos[i] + (r_sin[i] >>> i);
            r_sin[i + 1] = -(r_cos[i] >>> i) + r_sin[i];
            r_current_angle[i + 1] = r_current_angle[i] - r_atan_lut[i];
        end
    end
end

endmodule