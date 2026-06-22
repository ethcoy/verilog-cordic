module axis_cordic #(
    parameter c_INTEGER_WIDTH = 4,
    parameter c_FRACTIONAL_WIDTH = 16,
    // Fixed-point representation of pi
    parameter c_PI = 'h3243F,
    parameter c_DATA_WIDTH = c_INTEGER_WIDTH + c_FRACTIONAL_WIDTH
) (
    input wire i_rst,
    input wire i_clk,

    /*
     * AXI-stream input
     */
    input wire signed [c_DATA_WIDTH - 1:0] s_axis_angle_tdata,
    input wire s_axis_tvalid,
    output wire s_axis_tready,

    /*
     * AXI-stream output
     */
    output wire signed [c_DATA_WIDTH - 1:0] m_axis_cos_tdata,
    output wire signed [c_DATA_WIDTH - 1:0] m_axis_sin_tdata,
    output wire m_axis_tvalid,
    input wire m_axis_tready
);

reg signed [c_DATA_WIDTH - 1:0] s_axis_angle_tdata_reg = {c_DATA_WIDTH{1'b0}};
reg s_axis_angle_tready_reg = 1'b1;

assign s_axis_tready = s_axis_angle_tready_reg;

reg signed [c_DATA_WIDTH - 1:0] m_axis_cos_tdata_reg = {c_DATA_WIDTH{1'b0}};
reg signed [c_DATA_WIDTH - 1:0] m_axis_sin_tdata_reg = {c_DATA_WIDTH{1'b0}};
reg m_axis_tvalid_reg = 1'b0;

assign m_axis_cos_tdata = m_axis_cos_tdata_reg;
assign m_axis_sin_tdata = m_axis_sin_tdata_reg;
assign m_axis_tvalid = m_axis_tvalid_reg;

// Turn into a function that returns cos, sin, and current angle to allow for recursive computation (i.e., compute 2, 3, 4, etc., value ahead)

localparam c_ITERATION_WIDTH = $clog2(c_FRACTIONAL_WIDTH) + 1'b1;

reg [c_ITERATION_WIDTH - 1:0] r_iterations = {c_ITERATION_WIDTH{1'b0}};

localparam c_STATE_IDLE = 2'd0;
localparam c_STATE_COMPUTE = 2'd1;
localparam c_STATE_WAIT = 2'd2;

reg [1:0] r_state = c_STATE_IDLE;

function signed [(c_INTEGER_WIDTH + c_FRACTIONAL_WIDTH)*2 - 1:0] fixed_mult (input signed [c_INTEGER_WIDTH + c_FRACTIONAL_WIDTH - 1:0] a, input signed [c_INTEGER_WIDTH + c_FRACTIONAL_WIDTH - 1:0] b);
    fixed_mult = a*b >> c_FRACTIONAL_WIDTH;
endfunction

reg signed [c_DATA_WIDTH - 1:0] r_atan_lut [0:c_FRACTIONAL_WIDTH - 1];

initial begin
        $display("Reading atan LUT...");
        $readmemh("atan_lut.mem", r_atan_lut);
end

reg signed [c_DATA_WIDTH - 1:0] r_pi = c_PI;

reg signed [c_DATA_WIDTH - 1:0] r_current_angle = {c_DATA_WIDTH{1'b0}};
 
always @(posedge i_clk) begin
    case (r_state)
        c_STATE_IDLE: begin
            s_axis_angle_tready_reg <= 1'b1;
            r_iterations <= {c_ITERATION_WIDTH{1'b0}};
            m_axis_cos_tdata_reg <= {c_DATA_WIDTH{1'b0}};
            m_axis_sin_tdata_reg <= {c_DATA_WIDTH{1'b0}};
            if (s_axis_tvalid & s_axis_tready) begin
                s_axis_angle_tdata_reg <= s_axis_angle_tdata;
                s_axis_angle_tready_reg <= 1'b0;
                r_state <= c_STATE_COMPUTE;
                if ($signed({c_DATA_WIDTH{1'b0}}) <= s_axis_angle_tdata && s_axis_angle_tdata <= r_pi) begin
                    m_axis_sin_tdata_reg <= 1'b1 << c_FRACTIONAL_WIDTH;
                    r_current_angle <= r_pi >> 1'b1;
                end else if (r_pi <= s_axis_angle_tdata && s_axis_angle_tdata <= 2*r_pi) begin
                    m_axis_sin_tdata_reg <= {c_INTEGER_WIDTH{1'b1}} << c_FRACTIONAL_WIDTH;
                    r_current_angle <= 3*r_pi >> 1'b1;
                end else if (-r_pi <= s_axis_angle_tdata && s_axis_angle_tdata <= $signed({c_DATA_WIDTH{1'b0}})) begin
                    m_axis_sin_tdata_reg <= {c_INTEGER_WIDTH{1'b1}} << c_FRACTIONAL_WIDTH;
                    r_current_angle <= -(r_pi >> 1'b1);
                end else begin
                    m_axis_sin_tdata_reg <= 1'b1 << c_FRACTIONAL_WIDTH;
                    r_current_angle <= -(3*r_pi >> 1'b1);
                end
            end
        end

        c_STATE_COMPUTE: begin
            r_iterations <= r_iterations + 1'b1;            
            m_axis_cos_tdata_reg <= m_axis_cos_tdata_reg - (m_axis_sin_tdata_reg >>> r_iterations);
            m_axis_sin_tdata_reg <= (m_axis_cos_tdata_reg >>> r_iterations) + m_axis_sin_tdata_reg;
            r_current_angle <= r_current_angle + r_atan_lut[r_iterations];
            if (s_axis_angle_tdata_reg - r_current_angle < $signed({c_DATA_WIDTH{1'b0}})) begin
                m_axis_cos_tdata_reg <= m_axis_cos_tdata_reg + (m_axis_sin_tdata_reg >>> r_iterations);
                m_axis_sin_tdata_reg <= -(m_axis_cos_tdata_reg >>> r_iterations) + m_axis_sin_tdata_reg;;
                r_current_angle <= r_current_angle - r_atan_lut[r_iterations];
            end
                        
            if (r_iterations == c_FRACTIONAL_WIDTH - 1'b1) begin
                m_axis_tvalid_reg <= 1'b1;
                r_state <= c_STATE_WAIT;
            end
        end

        c_STATE_WAIT: begin
            if (m_axis_tready & m_axis_tvalid) begin
                m_axis_tvalid_reg <= 1'b0;
                r_state <= c_STATE_IDLE;
            end

        end

    endcase
end






endmodule