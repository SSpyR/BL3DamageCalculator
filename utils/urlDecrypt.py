# urlDecrypt.py
# code provided by @Prismatic

def decode(skills, spec):
    spec_end, n, spec_skill = spec.find("-"), 0, spec[1:3]
    
    # skills and the provided web encoding are ordered, therefore we can simultaneosly iterate
    # through both matching skills and extracting values. This was the most efficient system I could
    # think of in 5 minutes.
    for i in range(0, spec_end, 3):
        while n < len(skills) and spec_skill != skills[n]:
            # If the skill from the link does not match the next skill in our list then
            # we iterate the list that is behind.
            if spec_skill < skills[n]: 
                i=i+3
                spec_skill = spec[i+1:i+3]
            else: 
                skills[n] = 0
                n = n+1
        if n == len(skills):break
        skills[n] = eval(spec[i])
        n=n+1
    return skills


""" Amara Skills [Transcend, Laid Bare, Wrath, Tempest, Dread, Forceful Expression, Personal Space, 
Arms Deal, Samsara, Jab Cross] """
def zoneAmaraSpec(spec):
    skills = ["BE", "BI", "BJ", "BQ", "BT", "BZ", "CB", "CD", "CE", "CL"]
    return decode(skills, spec)
    '''
    # Mystical Assault
    transcend = BE
    laid_bare = BI
    wrath = BJ

    # Fist of the Elements
    tempest = BQ
    dread = BT
    forceful_expression = BZ
        
    # Brawl
    personal_space =  CB
    arms_deal = CD
    samsara = CE
    jab_cross = CL
    '''

def skillsAmaraSpec(spec):
    skills = []
    skills.append(spec[18])
    skills.append(spec[22])
    skills.append(spec[23])
    skills.append(spec[30])
    skills.append(spec[33])
    skills.append(spec[39])
    skills.append(spec[1])
    skills.append(spec[3])
    skills.append(spec[4])
    skills.append(spec[11])
    return skills


"""FL4K Skills [Furious Attack, Turn Tail and Run, Fast and Furryous, Hidden Machine, The Power Inside, Interplanetary Stalker, 
Hunter's Eye, Ambush Predator, Big Game, Most Dangerous Game, Galactic Shadow, Grim Harvest, Persistence Hunter, Frenzy, Barbaric Yawp, Pack Tactics] """
def zoneFlakSpec(spec):
    skills = ["CQ", "CV", "CW", "CX", "CZ", "DA", "DD", "DF", "DH", "DI", "DJ", "DK", "DN", "DR", "DU", "DW"]
    return decode(skills, spec)
    '''
    # Stalker
    furious_attack = CQ
    turn_tail_and_run = CV
    fast_and_furryous = CW
    hidden_machine = CX
    the_power_inside = CZ

    # Hunter
    interplanetary_stalker = DA
    hunter's_eye = DD
    ambush_predator = DF
    big_game = DH
    most_dangerous_game = DI
    galactic_shadow = DJ
    grim_harvest = DK
    
    # Master
    persistence_hunter = DN
    frenzy = DR
    barbaric_yawp = DU
    pack_tactics = DW
    '''

def skillsFlakSpec(spec):
    skills = []
    skills.append(spec[3])
    skills.append(spec[8])
    skills.append(spec[9])
    skills.append(spec[10])
    skills.append(spec[12])
    skills.append(spec[26])
    skills.append(spec[29])
    skills.append(spec[31])
    skills.append(spec[33])
    skills.append(spec[34])
    skills.append(spec[35])
    skills.append(spec[36])
    skills.append(spec[14])
    skills.append(spec[18])
    skills.append(spec[21])
    skills.append(spec[23])
    return skills

    
""" Moze Skills [Selfless Vengeance, Armored Infantry, Drowning in Brass, Experimental Munitions, Desperate Measures, Phalanx Doctrine, Tenacious Defence, 
Cloud of Lead, Stoke the Embers, Scorching RPM's, Click, Click, Fire in the Skag Den, Stainless Steel Bear, Short Fuse] """
def zoneMozeSpec(spec):
    skills = ["DZ", "EB", "EC", "EG", "EI", "EJ", "EL", "EM", "EM", "ET", "EX", "EZ", "FE", "FL"]
    return decode(skills, spec)
    '''
    # Shield of Retribution
    selfless_vengeance = DZ
    armored_infantry = EB
    drowning_in_brass = EC
    experimental_munitions = EG
    desperate_measures = EI
    phalanx_doctrine = EJ
    tenacious_defense = EL
    
    # Bottomless Mags
    cloud_of_lead = EM
    stoke_the_embers = EP
    scorching_rpms = ET
    click_click = EX

    # Demolition Woman
    fire_in_the_skag_den = EZ
    stainless_steel_bear = FE
    short_fuse = FL
    '''


def skillsMozeSpec(spec):
    skills = []
    skills.append(spec[26])
    skills.append(spec[28])
    skills.append(spec[29])
    skills.append(spec[33])
    skills.append(spec[35])
    skills.append(spec[36])
    skills.append(spec[38])
    skills.append(spec[0])
    skills.append(spec[3])
    skills.append(spec[7])
    skills.append(spec[11])
    skills.append(spec[13])
    skills.append(spec[18])
    skills.append(spec[25])
    return skills


""" Zane Skills [Synchronicity, Donnybrook, Trick of the Light, Double Barrel, Cold Bore, Violent Momentum, 
Death Follows Close, Confident Competence] """
def zoneZaneSpec(spec):
    skills = ["FM", "FP", "FY", "FZ", "GB", "GC", "GG", "GR"]
    return decode(skills, spec)
    '''
    # Doubled Agent
    synchronicity = FM
    donnybrook = FP
    trick_of_the_light = FY
    double_barrel = FZ

    # Hitman
    cold_bore = GB
    violent_momentum = GC
    death_follows_close = GG
    
    # Under Cover
    confident_competence = GR
    '''   


def skillsZaneSpec(spec):
    skills = []
    skills.append(spec[25])
    skills.append(spec[28])
    skills.append(spec[37])
    skills.append(spec[38])
    skills.append(spec[15])
    skills.append(spec[16])
    skills.append(spec[20])
    skills.append(spec[6])
    return skills