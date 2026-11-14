extends Node3D
# Art test: loads the Blender-built market, lights it, and saves screenshots.
# Blender (x, y, z) arrives in Godot as (x, z, -y).

const SHOTS := [
	["wide", Vector3(24, 25, 23), Vector3(-1, 0.5, -3), 30.0],
	["market", Vector3(9, 9.5, 12), Vector3(-2.5, 1.0, -1.5), 36.0],
	["capsules", Vector3(13, 8.5, 5), Vector3(1.5, 3.5, -8.5), 42.0],
]
var out_dir := "res://../out"
var cam: Camera3D
var frame := 0
var shot := 0

func _ready() -> void:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("--out="):
			out_dir = a.substr(6)
	var scene: Node3D = load("res://assets/market.glb").instantiate()
	add_child(scene)

	var noise := FastNoiseLite.new()
	noise.noise_type = FastNoiseLite.TYPE_SIMPLEX_SMOOTH
	noise.frequency = 0.012
	noise.fractal_octaves = 4
	var img := noise.get_seamless_image(512, 512)
	img.generate_mipmaps()
	var mat := ShaderMaterial.new()
	mat.shader = load("res://painted.gdshader")
	mat.set_shader_parameter("noise_tex", ImageTexture.create_from_image(img))

	var flame := StandardMaterial3D.new()
	flame.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	flame.albedo_color = Color(1.0, 0.72, 0.36)
	flame.emission_enabled = true
	flame.emission = Color(1.0, 0.6, 0.25)
	flame.emission_energy_multiplier = 6.0
	_dress(scene, mat, flame)
	_light()

	cam = Camera3D.new()
	add_child(cam)
	_aim()

func _dress(n: Node, mat: Material, flame: Material) -> void:
	if n is MeshInstance3D:
		n.material_override = flame if n.name.begins_with("Flames") else mat
		if n.name.begins_with("Flames"):
			n.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	elif n.name.begins_with("Lamp_"):
		var l := OmniLight3D.new()
		l.light_color = Color(1.0, 0.62, 0.30)
		l.light_energy = 5.0
		l.omni_range = 9.0
		l.omni_attenuation = 1.6
		l.shadow_enabled = int(n.name.get_slice("_", 1)) < 8
		n.add_child(l)
	for c in n.get_children():
		_dress(c, mat, flame)

func _light() -> void:
	var sky_mat := ProceduralSkyMaterial.new()
	sky_mat.sky_top_color = Color(0.20, 0.27, 0.42)
	sky_mat.sky_horizon_color = Color(0.86, 0.60, 0.44)
	sky_mat.ground_bottom_color = Color(0.07, 0.10, 0.11)
	sky_mat.ground_horizon_color = Color(0.30, 0.32, 0.33)
	var sky := Sky.new()
	sky.sky_material = sky_mat
	var env := Environment.new()
	env.background_mode = Environment.BG_SKY
	env.sky = sky
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.30, 0.38, 0.60)
	env.ambient_light_energy = 0.75
	env.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	env.tonemap_white = 6.0
	env.ssao_enabled = true
	env.ssao_radius = 1.6
	env.ssao_intensity = 3.0
	env.ssil_enabled = true
	env.glow_enabled = true
	env.glow_intensity = 0.9
	env.glow_bloom = 0.08
	env.glow_hdr_threshold = 1.1
	env.fog_enabled = true
	env.fog_light_color = Color(0.20, 0.27, 0.30)
	env.fog_density = 0.004
	env.fog_height = -1.5
	env.fog_height_density = 0.35
	env.fog_sky_affect = 0.3
	env.adjustment_enabled = true
	env.adjustment_saturation = 1.04
	env.adjustment_contrast = 1.06
	var we := WorldEnvironment.new()
	we.environment = env
	add_child(we)

	var sun := DirectionalLight3D.new()
	sun.light_color = Color(1.0, 0.72, 0.50)
	sun.light_energy = 1.7
	sun.shadow_enabled = true
	sun.light_angular_distance = 1.2
	sun.directional_shadow_max_distance = 110.0
	sun.directional_shadow_blend_splits = true
	add_child(sun)
	sun.look_at_from_position(Vector3(-50, 15, 24), Vector3.ZERO)

	var fill := DirectionalLight3D.new()
	fill.light_color = Color(0.45, 0.58, 0.85)
	fill.light_energy = 0.35
	add_child(fill)
	fill.look_at_from_position(Vector3(40, 30, -25), Vector3.ZERO)

func _aim() -> void:
	var s: Array = SHOTS[shot]
	cam.fov = s[3]
	cam.look_at_from_position(s[1], s[2])
	cam.current = true

func _process(_d: float) -> void:
	frame += 1
	if frame % 20 != 0:
		return
	await RenderingServer.frame_post_draw
	var path := "%s/%s.png" % [out_dir, SHOTS[shot][0]]
	get_viewport().get_texture().get_image().save_png(path)
	print("saved ", path)
	shot += 1
	if shot >= SHOTS.size():
		get_tree().quit()
	else:
		_aim()
