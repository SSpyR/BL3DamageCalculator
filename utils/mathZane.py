"""
Script to handle Zane related Math calculations

Arguments for mod: [Death Follows Close, Kill Skill Stacks, Active Action Skills, Movement Speed Over Base]

@author Prismatic
"""


def skillsSpec(skills, mods, gear):
    from utils import calcMain
    # Doubled Agent
    synchronicity = skills[0]
    donnybrook = skills[1]
    trick_of_the_light = skills[2]
    double_barrel = skills[3]

    # Hitman
    cold_bore = skills[4]
    violent_momentum = skills[5]
    death_follows_close = skills[6]

    # Under Cover
    confident_competence = skills[7]

    mods[0] = mods[0] + int(death_follows_close)
    normal_hit = [confident_competence, violent_momentum, synchronicity, donnybrook, double_barrel]

    normal = zane_normal_hit(normal_hit, mods) + gear[0]
    v1=0 + gear[1]
    v2=0 + gear[2]
    splash= 0 + gear[3]
    elemental = 0 + gear[4]
    critical = 0 + gear[5] 
    bonus_cryo = (0.06 * int(cold_bore)) + (0.12 * int(trick_of_the_light)) + gear[6]
    
    mults = [normal, v1, v2, splash, elemental, critical, bonus_cryo]

    response, body, crit = calcMain.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = calcMain.calc_bonus_elements(mults)
    if crit_1 != 0: response = response + "\n" + bonus_ele
    
    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {confident_competence, violent_momentum, synchronicity, donnybrook, double_barrel}
skill modifiers {death_follows_close, kill_skill_stacks, active_action_skills, movement_speed_over_base}
"""
def zane_normal_hit(gun_skills, skill_modifiers):
    dfc = 1+0.25*float(skill_modifiers[0])
    return (0.35*float(gun_skills[0]))+(0.16*float(gun_skills[1])*skill_modifiers[3]*dfc)+(0.04*float(gun_skills[1])*dfc)+(0.04*float(gun_skills[2])*skill_modifiers[2])+(0.03*float(gun_skills[3])*dfc*skill_modifiers[1])+(0.25*float(gun_skills[4]))