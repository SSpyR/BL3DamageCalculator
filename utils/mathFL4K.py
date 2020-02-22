"""
Script to handle FL4K related Math calculations

Arguments for mod: [Big Game, Furious Attack Stacks, Interplanetary Stalker Stacks, Full Health or Not]

@author SSpyR
"""


def skillsSpec(skills, mods, gear):
    import calcMain
    # Stalker
    furious_attack = skills[0]
    turn_tail_and_run = skills[1]
    fast_and_furryous = skills[2]
    hidden_machine = skills[3]
    the_power_inside = skills[4]

    # Hunter
    interplanetary_stalker = skills[5]
    hunters_eye = skills[6]
    ambush_predator = skills[7]
    big_game = skills[8]
    most_dangerous_game = skills[9]
    galactic_shadow = skills[10]
    grim_harvest = skills[11]

    # Master
    persistence_hunter = skills[12]
    frenzy = skills[13]
    barbaric_yawp = skills[14]
    pack_tactics = skills[15]

    mods[0] = mods[0] + eval(big_game)
    if mods[3] == 1:
        mods[3]=0.50
    else:
        mods[3]=0.25
    bg = 1+0.10*float(mods[0])
    normal_hit = [float(furious_attack), float(turn_tail_and_run), float(fast_and_furryous), float(most_dangerous_game), float(grim_harvest)]

    normal = fl4k_normal_hit(normal_hit, mods) + gear[0]
    v1=((0.08*float(frenzy)*bg)+(0.05*float(pack_tactics))+(0.02*float(interplanetary_stalker)*mods[2]*bg)+(mods[3]*float(the_power_inside))) + gear[1]
    v2=(0.06*float(hidden_machine)) + gear[2]
    splash=0 + gear[3]
    elemental=0 + gear[4]
    critical=((0.03*float(hunters_eye)*bg)+(0.04*float(ambush_predator))+(0.033*float(most_dangerous_game)*bg)+(0.15*float(galactic_shadow))) + gear[5]
    bonus_element=0 + gear[6]

    mults[normal, v1, v2, splash, elemental, critical, bonus_element]

    response, body, crit = calcMain.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = calcMain.calc_bonus_elements(mults)
    if crit_1 != 0: response = response + "\n" + bonus_ele

    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {furious_attack, turn_tail_and_run, fast_and_furryous, most_dangerous_game, grim_harvest}
skill modifiers {Big Game, Furious Attack Stacks, Interplanetary Stalker Stacks, Full Health or Not}
"""
def fl4k_normal_hit(gun_skills, skill_modifiers):
    bg = 1+0.10*float(skill_modifiers[0])
    return (gun_skills[0]*0.04*skill_modifiers[1]*bg)+(gun_skills[1]*0.083)+(gun_skills[2]*0.08*bg)+(gun_skills[3]*0.03)