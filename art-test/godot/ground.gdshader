shader_type spatial;
// Plain worn deck for the character stage: one colour, broken up by world-space noise.
uniform sampler2D noise_tex : filter_linear_mipmap, repeat_enable;
varying vec3 wpos;

void vertex() {
	wpos = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
}

void fragment() {
	float a = texture(noise_tex, wpos.xz * 0.11).r;
	float b = texture(noise_tex, wpos.xz * 0.53).r;
	float t = (a * 0.6 + b * 0.4 - 0.5) * 2.0;
	ALBEDO = vec3(0.20, 0.20, 0.185) * (1.0 + 0.35 * t);
	ROUGHNESS = 1.0;
	SPECULAR = 0.05;
}
