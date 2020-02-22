"""
Script to handle Amara related Math calculations

Arguments for mod: [Personal Space Strength, Samsara Stacks, unused, unused]

author @Prismatic
"""

def skillsSpec(skills, mods, gear):
    import calcMain

    # Mystical Assault
    transcend = skills[0]
    laid_bare = skills[1]
    wrath = skills[2]

    # Fist of the Elements
    tempest = skills[3]
    dread = skills[4]
    forceful_expression = skills[5]

    # Brawl
    personal_space = skills[6]
    arms_deal = skills[7]
    samsara = skills[8]
    jab_cross = skills[9]

    normal_hit = [float(samsara), float(jab_cross), float(dread), float(wrath)]

    normal = amara_normal_hit(normal_hit, mods) + gear[0]
    v1= (0.25/3*float(laid_bare)) + gear[1]
    v2= (0.177*float(personal_space)*mods[0]) + gear[2]
    splash= (float(arms_deal) * 0.04) + gear[3]
    elemental = (float(tempest) * 0.06) + gear[4]
    critical = (float(transcend) * 0.09) + gear[5] 
    bonus_AS_element = (0.18 * float(forceful_expression)) + gear[6]
    
    mults = [normal, v1, v2, splash, elemental, critical, bonus_AS_element]

    response, body, crit = calcMain.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = calcMain.calc_bonus_elements(mults)
    if crit_1 != 0: response = response + "\n" + bonus_ele
    
    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {samsara, jab_cross, dread, wrath}
skill modifiers {Personal Space strength, Samsara stacks, unused, unused}
"""
def amara_normal_hit(gun_skills, skill_modifiers):
    return (gun_skills[0]*0.05/3*skill_modifiers[1])+(gun_skills[1]*0.03)+(gun_skills[2]*0.15)+(gun_skills[3]*0.4/3)