# math.py
# base code provided by @Prismatic

# Clean up code to catch and explain exceptions/errors
# Implement Official Website Trees


import urlDecrypt as url
import mathMoze as Moze
import mathZane as Zane
import mathAmara as Amara
import mathFL4K as FL4K



"""
gear {Normal hit, v1, v2, Splash, elemental, crit, bonus element}
"""
def unpack(link, mods, gear, author="Testing"):
    toReturn=""
    
    if "bl3zone.com" in link:
        index = link.find("planner/")+11
        if "A" == link[index-1]:
            skills = url.zoneAmaraSpec(link[index:len(link)+1])
            toReturn = Amara.skillsSpec(skills, mods, gear)
        elif "B" == link[index-1]:
            skills = url.zoneFlakSpec(link[index:len(link)+1])
            toReturn = FL4K.skillsSpec(skills, mods, gear)
        elif "C" == link[index-1]:
            skills = url.zoneMozeSpec(link[index:len(link)+1])
            toReturn = Moze.skillsSpec(skills, mods, gear)
        elif "D" == link[index-1]:
            skills = url.zoneZaneSpec(link[index:len(link)+1])
            toReturn = Zane.skillsSpec(skills, mods, gear)
    
    elif "bl3skills" in link:
        index = link.find("#")+1
        if "gunner" in link:
            skills = url.skillsMozeSpec(link[index:len(link)+1])
            toReturn = Moze.skillsSpec(skills, mods, gear)
        elif "operative" in link:
            skills = url.skillsZaneSpec(link[index:len(link)+1])
            toReturn = Zane.skillsSpec(skills, mods, gear)
        elif "siren" in link:
            skills = url.skillsAmaraSpec(link[index:len(link)+1])
            toReturn = Amara.skillsSpec(skills, mods, gear)
        elif "beastmaster" in link:
            skills = url.skillsFlakSpec(link[index:len(link)+1])
            toReturn = FL4K.skillsSpec(skills, mods, gear)
    
    print(str(author) + "\n\n" + toReturn)
    return toReturn


"""
mults {Normal hit, v1, v2, Splash, elemental, crit, bonus element}
"""
def calc_bonus_elements(mults, experimental_munitions=0):
    bonus_element = mults[6] * (1+mults[0]) * (1+mults[1]) * (1+mults[2]) * (1+mults[4])
    str_bonus_element = "Bonus Element Damage: " + str(round(bonus_element,2))

    crit_bonus_element = (bonus_element+experimental_munitions) * 2 * (1+mults[5])
    str_crit_bonus_element = "Critical Bonus Element Damage: " + str(round(crit_bonus_element,2))
    return str_bonus_element + "\n" + str_crit_bonus_element, bonus_element, crit_bonus_element


"""
mults is expected to be a list of modifiers
{Gun Damage, V1, V2, Splash, Elemental, Critical, Bonus Element}
"""
def calc_Damage(mults):
    damage = (1+mults[0]) * (1+mults[1]) * (1+mults[2]) * (1+mults[3]) * (1+mults[4])
    body = "Damage: " + str(round(damage,2))

    crit_damage = damage * 2 * (1+mults[5])
    crit = "Critical Hit Damage: " + str(round(crit_damage,2))
    return body + "\n" + crit, damage, crit_damage

