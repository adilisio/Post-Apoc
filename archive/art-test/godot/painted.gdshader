shader_type spatial;
// Vertex colour carries the paint. Two scales of world-space noise break it up like brushwork.
uniform sampler2D noise_tex : filter_linear_mipmap, repeat_enable;
uniform float brush = 0.30;
varying vec3 wpos;
varying vec3 wnrm;

void vertex() {
	wpos = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	wnrm = normalize(mat3(MODEL_MATRIX) * NORMAL);
}

float tri(float s) {
	vec3 n = abs(wnrm);
	n /= (n.x + n.y + n.z);
	return texture(noise_tex, wpos.zy * s).r * n.x + texture(noise_tex, wpos.xz * s).r * n.y + texture(noise_tex, wpos.xy * s).r * n.z;
}

void fragment() {
	float a = tri(0.11);
	float b = tri(0.47);
	float t = (a * 0.6 + b * 0.4 - 0.5) * 2.0;
	vec3 c = COLOR.rgb * (1.0 + brush * t);
	// cool the darks, warm the lights a touch: painted, not photographed
	c = mix(c * vec3(0.92, 0.97, 1.06), c * vec3(1.05, 1.0, 0.94), smoothstep(-0.4, 0.5, t));
	ALBEDO = c;
	ROUGHNESS = 0.95;
	SPECULAR = 0.08;
}
