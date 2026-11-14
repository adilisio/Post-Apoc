extends Node3D
# Art test 2: loads the rigged characters, poses them from their walk cycles, and saves screenshots.
# Characters are built facing Blender -Y, which is Godot +Z.

var out_dir := "res://../out"
var only := ""
var cam: Camera3D
var frame := 0
var shot := 0
var shots: Array = []
var skin_mat: ShaderMaterial
var flame_mat: StandardMaterial3D
var stage: Node3D
var ground: MeshInstance3D
var paint_mat: ShaderMaterial
var gif := false
var movers: Array = []
const GIF_FPS := 15.0
const GIF_FRAMES := 84

func _ready() -> void:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("--out="):
			out_dir = a.substr(6)
		if a.begins_with("--only="):
			only = a.substr(7)
		if a == "--gif":
			gif = true
	var noise := FastNoiseLite.new()
	noise.noise_type = FastNoiseLite.TYPE_SIMPLEX_SMOOTH
	noise.frequency = 0.012
	noise.fractal_octaves = 4
	var img := noise.get_seamless_image(512, 512)
	img.generate_mipmaps()
	var tex := ImageTexture.create_from_image(img)
	skin_mat = ShaderMaterial.new()
	skin_mat.shader = load("res://painted_skin.gdshader")
	skin_mat.set_shader_parameter("noise_tex", tex)
	flame_mat = StandardMaterial3D.new()
	flame_mat.albedo_color = Color(0.0, 0.0, 0.0)
	flame_mat.emission_enabled = true
	flame_mat.emission = Color(1.0, 0.55, 0.18)
	flame_mat.emission_energy_multiplier = 5.0

	paint_mat = ShaderMaterial.new()
	paint_mat.shader = load("res://painted.gdshader")
	paint_mat.set_shader_parameter("noise_tex", tex)
	ground = MeshInstance3D.new()
	var pm := BoxMesh.new()
	pm.size = Vector3(400, 0.4, 400)
	ground.mesh = pm
	ground.position.y = -0.2
	var gm := ShaderMaterial.new()
	gm.shader = load("res://ground.gdshader")
	gm.set_shader_parameter("noise_tex", tex)
	ground.material_override = gm
	add_child(ground)
	_light()
	cam = Camera3D.new()
	add_child(cam)

	# name, builder, camera position, camera target, fov
	shots = [
		["sounder_close", _sounder_close, Vector3(1.9, 1.75, 2.6), Vector3(0, 1.05, 0), 30.0],
		["sounder_walk", _sounder_walk, Vector3(0, 2.6, 9.0), Vector3(0, 0.95, 0), 30.0],
		["sounder_game", _sounder_game, Vector3(7.5, 8.5, 7.5), Vector3(0, 0.8, 0), 30.0],
	]
	if ResourceLoader.exists("res://assets/longshank.glb"):
		shots += [
			["longshank_close", _dog_close, Vector3(2.6, 1.5, 2.2), Vector3(0, 0.75, 0), 30.0],
			["longshank_walk", _dog_walk, Vector3(0, 2.6, 9.0), Vector3(0, 0.8, 0), 30.0],
			["pair_game", _pair_game, Vector3(7.5, 8.5, 7.5), Vector3(0, 0.8, 0), 30.0],
		]
	shots.append(["market_game", _market_game, Vector3(11.5, 10.5, 11.0), Vector3(1.0, 1.0, -0.5), 30.0])
	if gif:
		shots = [["gif", _gif_stage, Vector3(0.6, 2.3, 7.2), Vector3(0.6, 0.95, 0), 30.0]]
	if only != "":
		shots = shots.filter(func(s): return s[0].begins_with(only))
	_setup()

func spawn(path: String, anim: String, t: float, pos: Vector3, yaw: float, light := true) -> Node3D:
	var n: Node3D = load(path).instantiate()
	stage.add_child(n)
	n.position = pos
	n.rotation.y = yaw
	_dress(n)
	var ap: AnimationPlayer = n.find_child("AnimationPlayer", true, false)
	if ap:
		if not ap.has_animation(anim):
			print("ERROR missing animation ", anim, " have ", ap.get_animation_list())
		else:
			ap.play(anim)
			ap.seek(t * ap.get_animation(anim).length, true)
			ap.pause()
	var sk: Skeleton3D = n.find_child("Skeleton3D", true, false)
	if sk and light and sk.find_bone("staff") >= 0:
		var ba := BoneAttachment3D.new()
		sk.add_child(ba)
		ba.bone_name = "staff"
		var l := OmniLight3D.new()
		l.light_color = Color(1.0, 0.62, 0.30)
		l.light_energy = 0.45
		l.omni_range = 5.0
		l.omni_attenuation = 1.5
		l.shadow_enabled = true
		l.position = Vector3(0, 1.15, 0.6)   # bone space: Y runs up the staff
		ba.add_child(l)
	return n

func _dress(n: Node) -> void:
	if n is MeshInstance3D:
		var fl: bool = n.name.begins_with("Flames")
		n.material_override = flame_mat if fl else skin_mat
		if fl:
			n.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	for c in n.get_children():
		_dress(c)

func _sounder_close() -> void:
	spawn("res://assets/sounder.glb", "idle", 0.1, Vector3.ZERO, 0.25)

func _sounder_walk() -> void:
	for i in 6:
		spawn("res://assets/sounder.glb", "walk", i / 6.0, Vector3(-3.6 + i * 1.45, 0, 0), PI / 2, i % 2 == 0)

func _sounder_game() -> void:
	spawn("res://assets/sounder.glb", "walk", 0.15, Vector3(0, 0, 0), 0.6)
	spawn("res://assets/sounder.glb", "idle", 0.3, Vector3(-2.2, 0, -1.5), 2.2)

func _dog_close() -> void:
	spawn("res://assets/longshank.glb", "idle", 0.1, Vector3.ZERO, 0.15)

func _dog_walk() -> void:
	for i in 5:
		spawn("res://assets/longshank.glb", "walk", i / 5.0, Vector3(-4.0 + i * 2.0, 0, 0), PI / 2)

func _pair_game() -> void:
	spawn("res://assets/sounder.glb", "walk", 0.15, Vector3(-1.2, 0, 0.4), 0.9)
	spawn("res://assets/longshank.glb", "walk", 0.2, Vector3(1.6, 0, -0.6), -2.0)
	spawn("res://assets/longshank.glb", "idle", 0.5, Vector3(3.0, 0, -2.4), -1.2)

func _market_game() -> void:
	var m: Node3D = load("res://assets/market.glb").instantiate()
	stage.add_child(m)
	_dress_market(m)
	spawn("res://assets/sounder.glb", "walk", 0.15, Vector3(3.2, 0, 1.2), -0.5)
	spawn("res://assets/sounder.glb", "idle", 0.3, Vector3(-0.8, 0, 2.6), 1.9)

func _dress_market(n: Node) -> void:
	if n is MeshInstance3D:
		var fl: bool = n.name.begins_with("Flames")
		n.material_override = flame_mat if fl else paint_mat
		if fl:
			n.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	elif n.name.begins_with("Lamp_"):
		var l := OmniLight3D.new()
		l.light_color = Color(1.0, 0.62, 0.30)
		l.light_energy = 5.0
		l.omni_range = 9.0
		l.omni_attenuation = 1.6
		n.add_child(l)
	for c in n.get_children():
		_dress_market(c)

func _gif_stage() -> void:
	movers = [
		[spawn("res://assets/sounder.glb", "walk", 0.0, Vector3(0, 0, -0.7), PI / 2), 0.9, -0.7],
		[spawn("res://assets/longshank.glb", "walk", 0.0, Vector3(0, 0, 0.9), PI / 2), 0.846, 0.9],
	]

func _gif_pose(k: int) -> void:
	var t := k / GIF_FPS
	for m in movers:
		var n: Node3D = m[0]
		n.position = Vector3(-1.9 + m[1] * t + (1.3 if m[2] > 0 else 0.0), 0, m[2])
		var ap: AnimationPlayer = n.find_child("AnimationPlayer", true, false)
		ap.seek(fmod(t, ap.get_animation("walk").length), true)

func _setup() -> void:
	if stage:
		stage.free()
	stage = Node3D.new()
	add_child(stage)
	var s: Array = shots[shot]
	s[1].call()
	ground.visible = s[0] != "market_game"
	cam.fov = s[4]
	cam.look_at_from_position(s[2], s[3])
	cam.current = true

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
	env.ssao_radius = 0.6
	env.ssao_intensity = 2.5
	env.glow_enabled = true
	env.glow_intensity = 0.9
	env.glow_bloom = 0.08
	env.glow_hdr_threshold = 0.9
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
	sun.directional_shadow_max_distance = 40.0
	add_child(sun)
	sun.look_at_from_position(Vector3(-30, 15, 24), Vector3.ZERO)
	var fill := DirectionalLight3D.new()
	fill.light_color = Color(0.45, 0.58, 0.85)
	fill.light_energy = 0.35
	add_child(fill)
	fill.look_at_from_position(Vector3(40, 30, -25), Vector3.ZERO)

func _process(_d: float) -> void:
	frame += 1
	if gif:
		if frame < 12:
			return
		var k := frame - 12
		if k > 0:
			await RenderingServer.frame_post_draw
			get_viewport().get_texture().get_image().save_png("%s/gif/%03d.png" % [out_dir, k - 1])
		if k >= GIF_FRAMES:
			get_tree().quit()
			return
		_gif_pose(k)
		return
	if frame % 12 != 0:
		return
	await RenderingServer.frame_post_draw
	var path := "%s/%s.png" % [out_dir, shots[shot][0]]
	get_viewport().get_texture().get_image().save_png(path)
	print("saved ", path)
	shot += 1
	if shot >= shots.size():
		get_tree().quit()
	else:
		_setup()
