shader_type spatial;
render_mode cull_disabled;
// As painted.gdshader, but the brush noise rides the rest-pose UVs so it does not swim on moving characters.
uniform sampler2D noise_tex : filter_linear_mipmap, repeat_enable;
uniform float brush = 0.22;

void fragment() {
	float a = texture(noise_tex, UV * 0.9).r;
	float b = texture(noise_tex, UV * 3.7).r;
	float t = (a * 0.6 + b * 0.4 - 0.5) * 2.0;
	vec3 c = COLOR.rgb * (1.0 + brush * t);
	c = mix(c * vec3(0.92, 0.97, 1.06), c * vec3(1.05, 1.0, 0.94), smoothstep(-0.4, 0.5, t));
	ALBEDO = c;
	ROUGHNESS = 0.9;
	SPECULAR = 0.1;
	if (!FRONT_FACING) {
		NORMAL = -NORMAL;
		ALBEDO *= 0.6;
	}
}
