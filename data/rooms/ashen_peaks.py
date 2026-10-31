"""The Ashen Peaks and the Lair of Pyraxis (37-52)."""
from data.rooms.common import R

ROOMS = {
    "meltwater_gorge": R(
        "The Meltwater Gorge", "Ashen Peaks",
        "Above the glacier, ice and fire meet. Meltwater pours in roaring falls down walls of black "
        "rock and vanishes hissing into vents of red heat, filling the gorge with scalding fog. Shapes "
        "of living steam twist through the murk, and the air is too hot to breathe deeply.",
        {"s": "frost_throne", "n": "smoking_scree"},
        spawns=[("steam_wraith", 3)], level=(37, 38)),
    "smoking_scree": R(
        "The Smoking Scree", "Ashen Peaks",
        "A slope of loose black stone climbs toward the burning heights, every rock warm to the touch "
        "and fumes leaking from the cracks between them. Lean hounds with ember eyes hunt among the "
        "boulders, and a hulking shape glows dull red where it squats beside a vent.",
        {"s": "meltwater_gorge", "n": "ashen_waste"},
        spawns=[("cinder_hound", 2), ("lava_troll", 1)], level=(39, 40)),
    "ashen_waste": R(
        "The Ashen Waste", "Ashen Peaks",
        "A blasted landscape of grey ash and black rock stretches beneath a sky the colour of a bruise. "
        "Rivers of lava glow in the distance, and pillars of living flame dance on the plain. To the "
        "east, the plain is ablaze from edge to edge.",
        {"s": "smoking_scree", "n": "cinder_road", "e": "burning_fields"},
        spawns=[("fire_elemental", 3), ("salamander", 1)], level=(41, 42)),
    "burning_fields": R(
        "The Burning Fields", "Ashen Peaks",
        "Fires that have burned for a hundred years flicker across a plain of cinders, never "
        "spreading and never dying. Great red lizards wallow in the hottest beds of coals, and black "
        "hounds trot between the flames as if they were cool spring grass.",
        {"w": "ashen_waste", "n": "drake_roost"},
        spawns=[("salamander", 2), ("cinder_hound", 1)], level=(41, 43)),
    "cinder_road": R(
        "The Cinder Road", "Ashen Peaks",
        "A road of fused black glass climbs the flank of a smoking volcano. Grey drakes bask on the warm "
        "rocks, and ruined statues of dragon-worshippers line the way.",
        {"s": "ashen_waste", "n": "obsidian_halls", "e": "drake_roost"},
        spawns=[("ash_drake", 2), ("salamander", 2)], level=(42, 44)),
    "drake_roost": R(
        "The Drake Roost", "Ashen Peaks",
        "Ledges of black rock step up the volcano's flank like the tiers of a vast nest, each one "
        "scorched and littered with cracked eggshells the size of shields. Ash drakes coil on every "
        "ledge, raising their heads one by one to watch you climb.",
        {"w": "cinder_road", "s": "burning_fields", "n": "cult_forge"},
        spawns=[("ash_drake", 3)], level=(44, 45)),
    "obsidian_halls": R(
        "The Obsidian Halls", "Ashen Peaks",
        "Halls of polished black glass, carved into the heart of the volcano by the dragon cult. "
        "Scaled guards stand at attention, and great golems of obsidian grind along the corridors. "
        "The ring of hammers and a red glow come from a forge to the east.",
        {"s": "cinder_road", "d": "molten_depths", "e": "cult_forge"},
        spawns=[("dragonkin_guard", 3), ("obsidian_golem", 1)], level=(45, 46)),
    "cult_forge": R(
        "The Forge of the Dragon Cult", "Ashen Peaks",
        "A great forge is built over a vent of living magma, where the cult hammers out blades and "
        "golems in the image of their dragon god. Robed flamecallers chant over the anvils, and a "
        "half-finished golem of black glass stands chained to the wall, its eyes beginning to glow.",
        {"w": "obsidian_halls", "s": "drake_roost"},
        spawns=[("cult_flamecaller", 2), ("obsidian_golem", 1)], level=(46, 47)),
    "molten_depths": R(
        "The Molten Depths", "Ashen Peaks",
        "A cavern of roaring heat where lakes of magma churn and spit. Demons of fire stalk the shores, "
        "and something colossal wades through the molten rock. A vast tunnel to the north glows "
        "with a terrible red light.",
        {"u": "obsidian_halls", "n": "dragon_lair"},
        spawns=[("flame_demon", 2), ("magma_titan", 1)], level=(48, 50)),
    "dragon_lair": R(
        "The Lair of Pyraxis", "Ashen Peaks",
        "A cavern so vast its ceiling is lost in smoke. A mountain of gold, gems and the bones of "
        "heroes fills the floor, and coiled upon it is a dragon older than kingdoms. One golden eye "
        "opens. 'Ahh,' rumbles a voice like an avalanche. 'A morsel that believes itself a legend.'",
        {"s": "molten_depths"},
        spawns=[("pyraxis", 1)], level=(52, 52)),
}
