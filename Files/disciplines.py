def getdiscipline(discipline):
    if discipline == "dominate1":
       part1="""The vampire locks eyes with the subject and speaks
    a one-word command, which the subject must be obey
    instantly. The order must be clear and straightforward:
    run, agree, fall, yawn, jump, laugh, surrender, stop,
    scream, follow. If the command is at all confusing or
    ambiguous, the subject may respond slowly or perform
    the task poorly. The subject cannot be ordered to do
    something directly harmful to herself, so a command
    like “die” is ineffective.

    The command may be included in a sentence, thereby
    concealing the power’s use from others. This effort
    at subtlety still requires the Kindred to make eye
    contact at the proper moment and stress the key word
    slightly. An alert bystander — or even the victim —
    may notice the emphasis. Still, unless she’s conversant
    with supernatural powers, the individual is likely to
    attribute the utterance and the subsequent action to
    bizarre coincidence.

    System: The player rolls Manipulation + Intimidation
    (difficulty equals the target’s current Willpower
    points). More successes force the subject to act with
    greater vigor or for a longer duration (continue running
    for a number of turns, go off on a laughing jag,
    scream uncontrollably)."""
       part2="""Remember, too, that being commanded to against
    one’s Nature confounds the use of this power. Being
    told to “sleep!” in a dangerous situation or “attack!”
    in police custody may not have the desired effect, or
    indeed, any effect at all."""
       return part1,part2 
    elif discipline == "dominate2":
        part1="""With this power, a vampire can verbally implant a
    false thought or hypnotic suggestion in the subject’s
    subconscious mind. Both Kindred and target must be
    free from distraction, since Mesmerize requires intense
    concentration and precise wording to be effective. The
    vampire may activate the imposed thought immediately
    or establish a stimulus that will trigger it later. The
    victim must be able to understand the vampire, though
    the two need to maintain eye contact only as long as it
    takes to implant the idea.

    Mesmerize allows for anything from simple, precise
    directives (handing over an item) to complex, highly
    involved ones (taking notes of someone’s habits and
    relaying that information at an appointed time). It is
    not useful for planting illusions or false memories (such
    as seeing a rabbit or believing yourself to be on fire). A
    subject can have only one suggestion implanted at any
    time."""
        part2="""System: The player rolls Manipulation + Leadership
    (difficulty equal to the target’s current Willpower
    points). The number of successes determines how well
    the suggestion takes hold in the victim’s subconscious.
    If the vampire scores one or two successes, the subject
    cannot be forced to do anything that seems strange to
    her (she might walk outside, but is unlikely to steal a
    car). At three or four successes, the command is effective
    unless following it endangers the subject. At five
    successes or greater, the vampire can implant nearly
    any sort of command.

    No matter how strong the Kindred’s will, his command
    cannot force the subject to harm herself directly
    or defy her innate Nature. So, while a vampire who
    scored five successes could make a 98-pound weakling
    attack a 300-pound bouncer, he could not make the
    mortal shoot herself in the head.

    If a vampire tries to Mesmerize a subject before the
    target fulfills a previously implanted directive, compare
    the successes rolled to those gained during the implanting
    of the first suggestion. Whichever roll had the
    greater number of successes is the command that now
    governs in the target’s behavior; the other suggestion is
    wiped clean. If the successes rolled are equal, the newer
    command supplants the old one."""
        return part1,part2 
    elif discipline == "dominate3":
        part1="""After capturing the subject’s gaze, the vampire delves
    into the subject’s memories, stealing or re-creating
    them at his whim. The Forgetful Mind does not allow
    for telepathic contact; the Kindred operates much like
    a hypnotist, asking directed questions and drawing out
    answers from the subject. The degree of memory alteration
    depends on what the vampire desires. He may alter
    the subject’s mind only slightly (quite effective for
    eliminating memories of the victim meeting or even
    being fed upon by the vampire) or utterly undo the victim’s
    memories of her past.

    The degree of detail used has a direct bearing on how
    strongly the new memories take hold, since the victim’s
    subconscious mind resists the alteration. A simplistic
    or incomplete false memory (“You went to the
    movies last night”) crumbles much more quickly than
    does one with more attention to detail (“You thought
    about texting your girlfriend while you were in line at
    the new movie theater, but you knew you’d have to
    turn your phone off once you got inside. You liked the
    movie well enough, but the plot seemed weak. You
    were tired after it ended, so you went home, watched a
    little late-night television, and went to bed.”)."""
        part2="""Even in its simplest applications, The Forgetful Mind
    requires tremendous skill and finesse. It’s a relatively
    simple matter to rifle through a victim’s psyche and rip
    out the memories of the previous night without knowing
    what the subject did that evening. Doing so leaves
    a gap in the victim’s mind, however — a hole that can
    give rise to further problems down the road. The Kindred
    may describe new memories, but these recollections
    seldom have the same degree of realism that the
    subject’s original thoughts held.

    As such, this power isn’t always completely effective.
    The victim may remember being bitten, but believe it
    to be an animal attack. Greater memories may return
    in pieces as dreams, or through sensory triggers like
    a familiar odor or spoken phrase. Even so, months or
    years may pass before the subject regains enough of her
    lost memories to make sense of the fragments.

    A vampire can also sense when a subject’s memories
    were altered through use of this power, and even restore
    them, as a hypnotist draws forth suppressed thoughts.
    System: The player states what sorts of alteration he
    wants to perform, then rolls Wits + Subterfuge (difficulty
    equal to the target’s current Willpower points).
    Any success pacifies the victim for the amount of time
    it takes the vampire to perform the verbal alteration,
    provided the vampire does not act aggressively toward
    her. The table below indicates the degree of modification
    possible to the subject’s memory. If the successes
    rolled don’t allow for the extent of change the character
    desired, the Storyteller reduces the resulting impact
    on the victim’s mind."""
        part3="""Successes Result
    1 success May remove a single memory;
    lasts one day.
    2 successes May remove, but not alter, memory
    permanently.
    3 successes May make slight changes to memory.
    4 successes May alter or remove entire scene
    from subject’s memory.
    5 successes May reconstruct entire periods of
    subject’s life.

    To restore removed memories or sense false ones
    in a subject, the character’s Dominate rating must be
    equal to or higher than that of the vampire who made
    the alteration. In that situation, the player must make
    a Wits + Empathy roll (difficulty equal to the original
    vampire’s permanent Willpower rating) and score
    more successes than his predecessor did. However, the
    Kindred cannot use The Forgetful Mind to restore his
    own memories if they were stolen in such a way."""
        return part1,part2,part3 
    elif discipline == "dominate4":
        part1 = """Through sustained manipulation, the vampire can
    make a subject more pliant to the Kindred’s will. Over
    time, the victim becomes increasingly susceptible to
    the vampire’s influence while simultaneously growing
    more resistant to the corrupting efforts of other Kindred.
    Gaining complete control over a subject’s mind
    is no small task, taking weeks or even months to accomplish.
    Kindred often fill their retainers’ heads with subtle
    whispers and veiled urges, thereby ensuring these mortals’
    loyalty. Yet vampires must pay a high price for
    the minds they ensnare. Servants Dominated in this
    way lose much of their passion and individuality. They
    follow the vampire’s orders quite literally, seldom taking
    initiative or showing any imagination. In the end,
    such retainers become like automatons or the walking
    dead."""
        part2 = """System: The player rolls Charisma + Leadership (difficulty
    equal to the target’s current Willpower points)
    once per scene. Conditioning is an extended action, for
    which the Storyteller secretly determines the number
    of successes required. It typically requires between five
    and 10 times the subject’s Self-Control/Instinct rating.
    Targets with more empathic Natures may require
    a lower number of successes, while those with willful
    Natures require a higher total. Only through roleplaying
    may a character discern whether his subject is conditioned
    successfully.
    A target may become more tractable even before
    becoming fully conditioned. Once the vampire accumulates
    half the required number of successes, the Storyteller
    may apply a lower difficulty to the vampire’s
    subsequent uses of Dominate. After being conditioned,
    the target falls so far under the vampire’s influence that
    the Kindred need not make eye contact or even be
    present to retain absolute control. The subject does exactly
    as she is told (including taking actions that would
    injure herself), as long as her master can communicate
    with her verbally. No command roll is necessary unless
    the subject is totally isolated from the vampire’s
    presence (in a different room, over the phone). Even
    if a command roll fails, the target will still likely carry
    out part of the orders given, simply because her master
    wishes it."""
        part3 = """After the subject is fully conditioned, other Kindred
    find her more difficult to Dominate. Such conditioning
    raises others’ difficulties by two (to a maximum of 10).
    It is possible, though difficult, to shake Conditioning.
    The subject must be separated entirely from the
    vampire to whom she was in thrall. This period of
    separation varies depending on the individual, but
    the Storyteller may set it at six months, less a number
    of weeks equal to the subject’s permanent Willpower
    rating (so a person with 5 Willpower must stay away
    from the vampire for just under five months). The
    subject regains her personality slowly during this time,
    though she may still lapse into brief spells of listlessness,
    despair, or even anger. If the vampire encounters
    the target before that time passes, a single successful
    Charisma + Leadership roll (difficulty of the target’s
    current Willpower points) on the part of the vampire
    completely reasserts the dominance.
    If the subject makes it through the time period without
    intervention by her master, the target regains her
    former individuality. Even so, the vampire may reestablish
    conditioning more easily than the first time,
    since the subject is now predisposed to falling under
    the Kindred’s mental control. New attempts require
    half the total number of successes than the last bout of
    conditioning did (which means the subject reaches the
    threshold for reduced difficulties sooner, as well)."""
        return part1,part2,part3
    elif discipline =="dominate5":
        part1 = """At this level of Dominate, the force of the Kindred’s
    psyche is such that it can utterly supplant the mind of
    a mortal subject. Speaking isn’t required, but the vampire
    must capture the victim’s gaze. During the psychic
    struggle, the contestants’ eyes are locked on one another.
    Once the Kindred overwhelms the subject’s mind,
    the vampire moves his consciousness into the victim’s
    body and controls it as easily as he uses his own. The
    mortal falls into a mental fugue while under possession.
    She is aware of events only in a distorted, dreamlike
    fashion. In turn, the vampire’s mind focuses entirely
    on controlling his mortal subject. His own body lies
    in a torpid state, defenseless against any actions made
    toward it.

    Vampires cannot possess one another in this fashion,
    as even the weakest Kindred’s mind is strong enough
    to resist such straightforward mental dominance. Only
    through a blood bond can one vampire control another
    to this degree. Supernatural creatures also cannot be
    possessed in this way, although ghouls that have drunk
    from the vampire using Possession can."""
        part2 = """System: The vampire must completely strip away the
    target’s Willpower prior to possessing her. The player
    spends a Willpower point, then rolls Charisma + Intimidation,
    while the subject rolls his Willpower in a
    resisted action (difficulty 7 for each). For each success
    the vampire obtains over the victim’s total, the target
    loses a point of temporary Willpower. Only if the attacker
    botches can the subject escape her fate, since
    this makes the target immune to any further Dominate
    attempts by that vampire for the rest of the story.
    Once the target loses all her temporary Willpower,
    her mind is open. The vampire rolls Manipulation +
    Intimidation (difficulty 7) to determine how fully he
    assumes control of the mortal shell. Similar to the Animalism
    power Subsume the Spirit, multiple successes
    allow the character to utilize some mental Disciplines,
    noted on the chart below. (Vampires possessing ghouls
    can use the physical Disciplines the ghoul possesses,
    but not the mental ones.)

    1 success: Cannot use Disciplines
    2 successes: Can use Auspex and other sensory
    powers
    3 successes: Can also use Presence and other
    powers of emotional manipulation
    4 successes: Can also use Dementation,
    Dominate, and other powers
    of mental manipulation
    5 successes: Can also use Chimerstry,
    Necromancy, Thaumaturgy, and other mystical powers"""
        part3 = """The character may travel as far from his body as he is
    physically able while possessing the mortal. The vampire
    may also venture out during the day in the mortal
    form. However, the vampire’s own body must be awake
    to do so, requiring a successful roll to remain awake
    (see p. 262). If the vampire leaves the mortal shell (by
    choice, if his body falls asleep, through supernatural expulsion,
    after sustaining significant injury, etc.), his consciousness
    returns to his physical form in an instant.
    Once freed from possession, the mortal regains mental
    control of herself. This can happen in an instant, or
    the victim may lie comatose for days while her psyche
    copes with the violation.

    The vampire experiences everything the mortal body
    feels during possession, from pleasure to pain. In fact,
    any damage the victim’s body sustains is also applied
    to the character’s body (though the Kindred may soak
    as normal). If the mortal dies before the vampire’s soul
    can flee from the body, the character’s body falls into
    torpor. Presumably this is in sympathetic response to
    the massive trauma of death, though some Kindred believe
    that the vampire’s soul is cast adrift during this
    time and must find its way back to the body.

    The Kindred can remain in the mortal’s body even if
    his own torpid form is destroyed, though such a pathetic
    creature is not likely to exist for long. At each sunrise,
    the vampire must roll Courage (difficulty 8) or be expelled
    from the body. If forced from the mortal body, the
    vampire tumbles into the astral plane, his soul permanently
    lost in the spirit world. A vampire trapped in a
    mortal body may not be “re-Embraced.” If the Embrace
    occurs to such a creature, he simply meets Final Death."""
        return part1, part2, part3

    elif discipline == "quietus1":
        part1 = """Many Assamites claim never to have heard their
    targets’ death screams. Silence of Death imbues the
    vampire with a mystical silence that radiates from her
    body, muting all noise within a certain vicinity. No
    sound occurs inside this zone, though sounds originating
    outside the area of effect may be heard by anyone
    in it. Rumors abound of certain skilled Assamite viziers
    who have the ability to silence a location rather than a
    circumference that follows them, but no proof of this
    has been forthcoming.

    System: This power (which costs one blood point to
    activate) maintains a 20-foot (6-meter) radius of utter
    stillness around the Kindred for one hour."""
        return part1
    elif discipline == "quietus2":
        part1 = """By changing the properties of her blood, a vampire
    may create powerful venom that strips her prey of his resilience.
    This power is greatly feared by other Kindred,
    and all manner of hideous tales concerning methods of
    delivery circulate among trembling coteries. Kindred
    with Quietus are known to deliver the poison by coating
    their weapons with it, blighting their opponents
    with a touch, or spitting it like a cobra. An apocryphal
    account speaks of a proud Prince who discovered an
    Assamite plotting her exsanguination and began to
    diablerize her would-be assassin. Halfway through the
    act, she learned that she had ingested a dire quantity of
    tainted blood and was then unable to resist the weakened
    hashashiyyin’s renewed attack."""
        part2 = """System: To convert a bit of her blood to poison, the
    Kindred’s player spends at least one blood point and
    rolls Willpower (difficulty 6). If this roll is successful,
    and the vampire successfully hits (but not necessarily
    damages) her opponent, the target loses a number of
    Stamina points equal to the number of blood points
    converted into poison — vampires attempting to drink
    the blood of the Kindred with Scorpion’s Touch are
    automatically considered to be “successfully hit.”
    The victim may resist the poison with a Stamina +
    Fortitude roll (difficulty 6); successes achieved on the
    resistance roll subtract from the vampire’s successes.
    The maximum number of blood points a Kindred may
    convert at any one time is equal to her Stamina. The
    number of successes
    
    success One: turn
    2 successes: One hour
    3 successes: One day
    4 successes: One month
    5 successes: Permanently (though Stamina may
    be bought back up with experience)"""
        part3 = """If a mortal’s Stamina falls to zero through use of Scorpion’s
        Touch, she becomes terminally ill and loses any
        immunity to diseases, her body succumbing to sickness
        within the year unless she somehow manages to increase
        her Stamina again. If a Kindred’s Stamina falls
        to zero, the vampire enters torpor and remains that way
        until one of her Stamina points returns. If a Kindred is
        permanently reduced to zero Stamina, she may recover
        from torpor only through mystical means.

        To afflict someone with the poison, the Cainite must
        touch her target’s flesh or hit him with something that
        carries the venom. Many Assamites lubricate their
        weapons with the excretion, while others pool the toxin
        in their hands (or fleck their lips with the poison,
        for a “kiss of death”) and press it to their opponents.
        Weapons so envenomed must be of the melee variety
        — arrows, sling stones, bullets, thrown weapons, and
        the like cannot carry enough of the stuff to do damage,
        or it drips off in flight. Players whose vampires wish to
        spit at their targets must make a Stamina + Athletics
        roll (difficulty 6). No more than two blood points’
        worth of poison may be expectorated, and a Kindred
        may spit a distance of 10 feet (3 meters) for each point
        of Strength (and Potence) the character possesses.
        Vampires with Quietus are immune to their own poison,
        but not the blood-venom of other Kindred with
        this power."""
        return part1,part2,part3
    elif discipline == "quietus3":
        part1 = """This terrible power allows a vampire to drown her
    target in his own blood. By concentrating, the Kindred
    bursts her target’s blood vessels and fills his lungs with
    vitae that strangles him from within. The blood actually
    constricts the target’s body from the inside as it
    floods through his system; thus, it works even on unbreathing
    Kindred. Until the target collapses in agony
    or death throes, this power has no visible effect, and
    many Kindred like it because it leaves no trace of their
    presence.

    System: The vampire must touch her target prior
    to using Dagon’s Call. Within an hour thereafter, the
    vampire may issue the call, though she need not be in
    the presence or even in the line of sight of her target."""

        part2 = """Invoking the power costs one Willpower point.
    The Kindred’s player makes a contested Stamina roll
    against the target’s Stamina; the difficulty of each roll
    is equal to the opponent’s permanent Willpower rating.
    The number of successes the vampire using Dagon’s
    Call achieves is the amount of lethal damage, in
    health levels, the victim suffers. For an additional point
    of Willpower spent in the next turn, the vampire may
    continue using Dagon’s Call by engaging in another
    contested Stamina roll. So long as the Kindred’s player
    continues to spend Willpower, the character may continue
    rending her opponent from within."""
        return part1,part2
    elif discipline == "quietus4":
        part1 = """The penultimate use of blood as a weapon (short of
    diablerie itself), Baal’s Caress allows the Kindred to
    transmute her blood into a virulent ichor that destroys
    any living or undead flesh it touches. In nights of yore,
    when Assamites led the charges of Saracen legions, the
    Assassins were often seen licking their blades, slicing
    open their tongues and lubricating their weapons with
    this foul secretion.

    Baal’s Caress may be used to augment any bladed
    weapon; everything from poisoned knives and swords
    to tainted fingernails and claws has been reported."""
        part2 = """
        System: Baal’s Caress does not increase the damage
    done by a given weapon, but that weapon inflicts aggravated
    damage rather than normal. No roll is necessary
    to activate this power, but one blood point is
    consumed per hit. For example, if a Cainite poisons his
    knife and strikes his opponent (even if he inflicts no
    damage), one blood point’s worth of lubrication disappears.
    For this reason, many vampires choose to coat their weapons with a significant quantity of blood. If
    the vampire misses, no tainted blood is consumed."""
        return part1,part2
    elif discipline == "quietus5":
        part1 = """A refinement of Baal’s Caress, Taste of Death allows
    the Cainite to spit caustic blood at her target. The
    blood coughed forth with this power burns flesh and
    corrodes bone; some vampires have been reported to
    vomit voluminous streams of vitae that reduce their
    targets to heaps of sludge."""
        part2 = """System: The vampire may spit up to 10 feet (3 meters)
    for each dot of Strength and Potence he possesses.
    Hitting the target requires a Stamina + Athletics roll
    (difficulty 6). Each blood point spewed at the target
    inflicts two dice of aggravated damage, and there is no
    limit (other than the vampire’s capacity and per-turn
    expenditure maximum) to the quantity of blood with
    which a target may be deluged."""
        return part1,part2

    elif discipline == "obfuscate1":
        part1 = """At this level, the vampire must rely on nearby shadows
    and cover to assist in hiding his presence. He steps
    into an out-of-the-way, shadowed place and eases himself
    from normal sight. The vampire remains unnoticed
    as long as he stays silent, still, under some degree of
    cover (such as a curtain, bush, door frame, lamppost,
    or alley), and out of direct lighting. The immortal’s
    concealment vanishes if he moves, attacks, or falls under
    direct light. Furthermore, the vampire’s deception
    cannot stand up to concentrated observation without
    fading.

    System: No roll is required as long as the character
    fulfills the criteria described above. So long as he remains
    quiet and motionless, virtually no one but another
    Kindred with a high enough Auspex rating will
    see him."""
        return part1
    elif discipline == "obfuscate2":
        part1 = """With experience, the vampire can move around
    without being seen. Shadows seem to shift to cover
    him, and people automatically avert their gazes as he
    passes by. Others move unconsciously to avoid contact
    with the cloaked creature; those with weak wills may
    even scurry away from the area in unacknowledged
    fear. The vampire remains ignored indefinitely unless
    someone deliberately seeks him out or he inadvertently
    reveals himself.

    Since the vampire fully retains his physical substance,
    he must be careful to avoid contact with anything
    that may disclose his presence (knocking over a
    vase, bumping into someone). Even a whispered word
    or the scuffing of a shoe against the floor can be enough
    to disrupt the power."""
        part2 = """System: No roll is necessary to use this power unless
    the character speaks, attacks, or otherwise draws attention
    to himself. The Storyteller should call for a Wits +
    Stealth roll under any circumstances that might cause
    the character to reveal himself. The difficulty of the
    roll depends on the situation; stepping on a squeaky
    floorboard might be a 5, while walking through a pool
    of water may require a 9. Other acts may require a certain
    number of successes; speaking quietly without giving
    away one’s position, for instance, demands at least
    three successes. Upon success, the vampire, all her
    clothing, and objects that could fit into a pocket are
    concealed.

    Some things are beyond the power of Unseen Presence
    to conceal. Although the character is cloaked
    from view while he smashes through a window, yells
    out, or throws someone across the room, the vampire
    becomes visible to all in the aftermath. Bystanders snap
    out of the subtle fugue in which Obfuscate put them.
    Worse still, each viewer can make a Wits + Awareness
    roll (difficulty 7); if successful, the mental haze clears
    completely, so those individuals recall every move the
    character made up until then as if he had been visible
    the entire time."""
        return part1,part2
    elif discipline == "obfuscate3":
        part1= """The vampire can influence the perception of others,
    causing them to see a face different from his. Although
    the Kindred’s physical form does not change, any observer
    who cannot sense the truth sees whomever the
    vampire wishes her to see.

    The vampire must have a firm idea of the visage he
    wishes to project. The primary decision is whether to
    create an imaginary face or to superimpose the features
    of another person. Manufactured features are often
    more difficult to compose in believable proportions,
    but such a disguise is easier to maintain than having to
    impersonate someone else. Of course, things get simpler
    if the Kindred borrows the face but doesn’t bother
    with the personality."""
        part2 = """with the personality.
    System: The player rolls Manipulation + Performance
    (difficulty 7) to determine how well the disguise
    works. If the character tries to impersonate someone,
    he must get a good look at the subject before putting
    on the mask. The Storyteller may raise the difficulty if
    the character catches only a glimpse. The chart below
    lists the degrees of success in manufacturing another
    appearance. Vampires wishing to mask themselves as
    a person more attractive than they are must pay additional
    blood points equal to the difference between
    the vampire’s Appearance rating and the Appearance
    of the mask (which means that younger vampires may
    need to take longer in order to spend the blood necessary).

    Successes Result
    1 success: The vampire retains the same height
    and build, with a few slight
    alterations to his basic features.
    Nosferatu can appear as normal,
    albeit ugly, mortals.

    2 successes: He looks unlike himself; people don’t
    easily recognize him or agree about
    his appearance.

    3 successes: He looks the way he wants to appear.

    4 successes: Complete transformation, including
    gestures, mannerisms, appearance,
    and voice.

    5 successes: Profound alteration (appear as the
    opposite sex, a vastly different age,
    or an extreme change of size)."""
        part3 = """Actually posing as someone else carries its own problems.
    The character should know at least basic information
    about the individual; especially difficult deceptions
    (fooling a lover or close friend) require at least
    some familiarity with the target in order to succeed."""
        return part1,part2,part3
    elif discipline =="obfuscate4":
        part1 = """This potent expression of Obfuscate enables the
    vampire to disappear from plain view. So profound is
    this vanishing that the immortal can fade away even if
    he stands directly in front of someone.

    While the disappearance itself is quietly subtle, its
    impact on those who see it is anything but. Most kine
    panic and flee in the aftermath. Especially weak-willed
    individuals wipe the memory of the Kindred from their
    minds. Although vampires are not shaken so easily,
    even Kindred may be momentarily surprised by a sudden
    vanishing.

    System: The player rolls Charisma + Stealth; the
    difficulty equals the target’s Wits + Alertness (use the
    highest total in the group if the character disappears
    in front of a crowd). With three or fewer successes,
    the character fades but does not vanish, becoming an
    indistinct, ghostlike figure. With more than three, he
    disappears completely. If the player scores more successes
    than an observer’s Willpower rating, that person
    forgets that the vampire was there in the first place."""
        part2 = """Tracking the character accurately while he appears
    ghostlike requires a Perception + Alertness roll (difficulty
    8). A successful roll means the individual can
    interact normally with the vampire (although the
    Kindred looks like a profoundly disturbing ghostly
    shape). A failed roll results in a +2 difficulty modifier
    (maximum 10) when attempting to act upon, or
    interact with, the vampire. The Storyteller may call
    for new observation checks if the vampire moves to an
    environment in which he’s difficult to see (heads into
    shadows, crosses behind an obstacle, proceeds through
    a crowd). When fully invisible, the vampire is handled
    as described under Unseen Presence, above.

    A person subject to the vanishing makes a Wits +
    Courage roll (mortals at difficulty 9, vampires at difficulty
    5). A successful roll means the individual reacts
    immediately (although after the vampire performs his
    action for that turn); failure means the person stands
    uncomprehending for two turns while her mind tries to
    make sense of what she just experienced."""
        return part1,part2
    elif discipline=="obfuscate5":
        part1 = """At this degree of power, the vampire may extend
    his concealing abilities to cover an area. The immortal
    may use any Obfuscate power upon those nearby as
    well as upon himself, if he wishes.

    Any protected person who compromises the cloak
    exposes himself to view. Further, if the one who invokes
    the power gives himself away, the cloak falls
    from everyone. This power is particularly useful if the
    vampire needs to bring his retinue through a secure location
    without drawing the notice of others.

    System: The character may conceal one extra individual
    for each dot of Stealth he possesses. He may bestow
    any single Obfuscate power at a given time to the
    group. While the power applies to everyone under the
    character’s cloak, his player need only make a single
    roll. Each individual must follow the requirements described
    under the relevant Obfuscate power to remain
    under its effect; any person who fails to do so loses the
    cloak’s protection, but doesn’t expose the others. Only
    if the vampire himself errs does the power drop for everyone."""
        return part1

    elif discipline=="obtenebration1":
        part1 = """This power grants the vampire limited control over
    shadows and other ambient darkness. Though the vampire
    cannot truly “create” darkness, she can overlap and
    stretch existing shadows, creating patches of gloom.
    This power also allows Kindred to separate shadows
    from their casting bodies and even shape darkness into
    the shadows of things that are not there.

    Once a Kindred takes control of darkness or shadow,
    it gains a mystical tangibility. By varying accounts cold
    or hellishly hot and cloying, the darkness may be used
    to aggravate or even smother victims. Certain callous
    Lasombra claim to have choked mortals to death with
    their own shadows."""
        part2 = """System: This power requires no roll, but a blood
    point must be spent to activate it. Shadow Play lasts for
    one scene and requires no active concentration. Kindred
    cloaking themselves in shadow gain an extra die
    in their Stealth dice pools and add one to the difficulties
    of ranged weapon attacks against them. Vampires
    who use the darkness to make themselves more terrifying
    add one die to Intimidation dice pools. Opponents
    plagued by flapping shadows and strangling darkness
    subtract one die from all Stamina dice pools (including
    soak). Mortals, ghouls, and other air-breathers reduced
    to zero Stamina by strangling shadows begin to
    asphyxiate; vampires lose all appropriate dice but are
    otherwise unaffected. Only one target or subject may
    be affected by this power at any given time, though
    some modicum of concealment is offered to a relatively
    motionless group."""
        part3 = """The unnatural appearance of this power proves extremely
    disconcerting to mortals and animals (and, at
    the Storyteller’s discretion, Kindred who have never
    seen it before). Whenever this power is invoked within
    a mortal’s vicinity, that individual must make a Courage
    roll (difficulty 8) or suffer a one-die penalty to all
    dice pools for the remainder of the scene, due to fear of
    the monstrous shadows."""
        return part1,part2,part3 
    elif discipline =="obtenebration2":
        part1= """The vampire can create a cloud of inky blackness.
    The cloud completely obscures light and even sound
    to some extent. Those who have been trapped within
    it (and survived) describe the cloud as viscous and unnerving.
    This physical manifestation lends credence to
    those Lasombra who claim that their darkness is something
    other than mere shadow.

    The tenebrous cloud may even move, if the creating
    Kindred wishes, though this requires complete concentration.
    System: The player rolls Manipulation + Occult
    (difficulty 7). Success on the roll generates darkness
    roughly 10 feet (three meters) in diameter, though
    the amorphous cloud constantly shifts and undulates,
    sometimes even extending shadowy tendrils. Each
    additional success doubles the diameter of the cloud
    (though the vampire may voluntarily reduce the area
    she wishes to cover). The cloud may be invoked at
    a distance of up to 50 yards/meters, though creating
    darkness outside the vampire’s line of sight adds two
    to the difficulty of the roll and requires a blood point’s
    expenditure."""
        part2= """The tarry mass actually extinguishes light sources it
    engulfs (with the exception of fire), and muffles sounds
    until they are indistinguishable. Those within the
    cloud lose all sense of sight and feel as though they’ve
    been immersed in pitch. Sound also warps and distorts
    within the cloud, making it nearly impossible to accomplish
    anything (+2 difficulty, as per Blind Fighting
    on p. 274). Even those possessed of Heightened
    Senses, Eyes of the Beast, Tongue of the Asp, and similar
    powers suffer the penalty for blindness due to the
    unnatural darkness. Additionally, being surrounded by
    the Shroud of Night reduces Stamina-based dice pools
    by two dice, as the murk smothers and agitates the victims.
    This effect is not cumulative with Shadow Play,
    although targets asphyxiate as per Shadow Play if they
    reach 0 Stamina; more than one unfortunate mortal
    has “drowned” in darkness.

    Mortals and animals surrounded by the Shroud
    of Night must make Courage rolls per Shadow Play,
    above, or panic and flee."""
        return part1, part2
    elif discipline == "obtenebration3":
        part1= """Refining his control over darkness, the Kindred can
    create prehensile tentacles that emerge from patches of
    dim lighting. These tentacles may grasp, restrain, and
    constrict foes.

    System: The player spends a blood point and makes
    a simple (never extended) Manipulation + Occult roll
    (difficulty 7); each success enables the creation of a
    single tentacle. Each tentacle is six feet (two meters)
    long and possesses Strength and Dexterity ratings equal
    to the invoking vampire’s Obtenebration Trait — Potence
    and Celerity dots are added to these Strength and
    Dexterity ratings, respectively. If the vampire chooses,
    she may spend a blood point either to increase a single
    tentacle’s Strength or Dexterity by one or to extend its
    length by another six feet or two meters. Each tentacle
    has four health levels, is affected by fire and sunlight
    as if it were a vampire, and soaks bashing and lethal
    damage using the vampire’s Stamina + Fortitude. Aggravated
    damage may not be soaked."""
        part2 = """Tentacles may constrict foes, inflicting (Strength +1)
    lethal damage per turn. Breaking the grasp of a tentacle
    requires the victim to win a resisted Strength roll
    against the tentacle (difficulty 6 for each). However,
    tentacles cannot be used for any kind of manipulation,
    such as typing or driving.
    All tentacles need not emanate from the same source
    — so long as there are multiple patches of suitable
    darkness, there are sources for the Arms of the Abyss.
    Controlling the tentacles does not require complete
    concentration; if the Kindred is not incapacitated or
    in torpor, she may control tentacles while carrying out
    other actions."""
        return part1,part2
    elif discipline == "obtenebration4":
        part1 = """The Cainite calls upon his inner darkness and infuses
    himself with it, becoming a monstrous hybrid of
    matter and shadow. His body becomes mottled with
    spots of tenebrous shade, and wispy tentacles extrude
    from his torso and abdomen. Though still humanoid,
    the vampire takes on an almost demonic appearance,
    as the darkness within him bubbles to the surface.

    System: The player spends two blood points and
    makes a Manipulation + Courage roll (difficulty 7) —
    vampires of lower Generation may have to take two
    turns to make the transition. Failure indicates the vampire
    cannot undergo the Black Metamorphosis (though
    he spends the blood points nonetheless). A botch inflicts
    two unsoakable health levels of lethal damage on
    the vampire as darkness ravages his undead body."""
        part2 = """While under the effects of the Black Metamorphosis,
    the vampire possesses four tentacles similar to those
    evoked via Arms of the Abyss (though their Strength
    and Dexterity ratings are equal to the vampire’s own
    Attributes, including dice from Celerity and Potence).
    These tentacles, combined with the bands of darkness
    all over the Kindred’s body, subtract two dice from the
    Stamina and soak dice pools of opponents physically
    touched in combat, for as long as the vampire remains
    in contact with the victim. This is not cumulative
    with other powers in Obtenebration, although targets
    can asphyxiate at Stamina 0, as per Shadow Play. The
    vampire may make an additional attack without penalty
    by using the tentacles (for a total of two attacks,
    not one additional attack per tentacle). Additionally,
    the vampire can sense his surroundings fully even in
    pitch darkness."""
        part3= """The vampire’s head and extremities sometimes appear
    to fade away into nothingness, while at other
    times they seem swathed in otherworldly darkness.
    This, combined with the wriggling tentacles writhing
    from his body, creates an unsettling sight. Mortals, animals,
    and other creatures not accustomed to this sort
    of display must make Courage rolls (difficulty 8) or succumb
    to a panic that amounts to Rötschreck (though
    it is inspired by the darkness rather than fire). Many
    Kindred cultivate this devilish aspect, and the Black
    Metamorphosis adds three dice to the invoking Kindred’s
    Intimidation dice pools."""
        return part1,part2,part3
    elif discipline == "obtenebration5":
        part1= """At this level, the Kindred’s mastery of darkness is so
    extensive that she may physically become it. Upon activation
    of this power, the vampire becomes an inky,
    amoeboid patch of shadow. Vampires in this form are
    practically invulnerable and may slither through cracks
    and crevices. In addition, the shadow-vampire gains
    the ability to see in natural darkness."""
        part2= """System: The transformation costs three blood points
    (which may need to occur over three turns, depending
    on the vampire’s Generation). The vampire is immune
    to physical attacks while in the tenebrous form
    (though she still takes aggravated damage from fire and
    sunlight), but may not herself physically attack. She
    may, however, envelop and ooze over others, affecting
    them in the same manner as a Shroud of Night,
    in addition to using mental Disciplines. Vampires in
    Tenebrous Form may even slither up walls and across
    ceilings or “drip” darkness upward — they have no
    mass and are thus unaffected by gravity. Rötschreck
    difficulties from fire and sunlight do increase by one for
    vampires in this form, as the light is even more painful
    to their shadowy bodies.

    Mortals (and others not used to such displays) who
    witness the vampire transform into unholy shadow require
    Courage rolls (difficulty 8) in order to avoid the debilitating
    terror described under Black Metamorphosis."""
        return part1,part2

    elif discipline=="auspexclash":
        part1="""Auspex gives the vampire uncanny sensory abilities.
    She starts with the capacity to heighten her natural
    senses significantly, but as she grows in power, she can
    perceive psychic auras and read the thoughts of another
    being. Auspex can also pierce through mental illusions
    such as those created by Obfuscate — see the sidebar
    “Seeing the Unseen” on p. 142 for more."""
        part2="""However, a vampire with Auspex needs to be careful.
    Her increased sensory sensitivity can cause her to be
    drawn in by beautiful things or stunned by loud noises
    or pungent smells. Sudden or dynamic events can
    disorient an Auspex-using character unless her player
    makes a Willpower roll to block them out (difficulty of
    at least 4, although the more potent the source of distraction,
    the higher the difficulty). Failure overwhelms
    the character’s senses, making her oblivious to her surroundings
    for a turn or two. While the Malkavians and
    Toreador are more prone to these kinds of distractions,
    the Tremere and Tzimisce aren’t immune.
    Dots in Perception are very useful for using Auspex
    powers, as more successes help the character gain more
    sensory information."""
        part3="""• Obfuscate: When a vampire tries to use her
    heightened perceptions to notice a Kindred
    hidden with Obfuscate, she detects the subject’s
    presence if her Auspex rating is higher
    than his Obfuscate, and she succeeds at a
    Perception + Awareness roll (difficulty equals
    7 minus the number of dots by which her
    Auspex exceeds his Obfuscate). Conversely,
    if the target’s Obfuscate outranks her Auspex,
    he remains undiscovered. If the two ratings
    are equal, both characters make a resisted roll
    of Perception + Awareness (Auspex user)
    against Manipulation + Subterfuge (Obfuscate
    user). The difficulty for both rolls is 7, and the
    character with the most successes wins."""
        part4="""• Chimerstry: Likewise, vampires with
    Auspex may seek to penetrate illusions created
    with Chimerstry. The Auspex-wielder
    must actively seek to pierce the illusion (i.e.,
    the player must tell the Storyteller that his
    character is trying to detect an illusion).
    The Auspex-user and Chimerstry-wielder
    then compare relative ratings, per Obfuscate,
    above. The process is otherwise identical to
    piercing Obfuscate."""
        return part1,part2,part3,part4

    elif discipline == "auspex1":
        part1= """This power increases the acuity of all of the vampire’s
    senses, effectively doubling the clarity and range
    of sight, hearing, and smell. While her senses of taste
    and touch extend no farther than normal, they likewise
    become far more distinct; the vampire could taste
    the hint of liquor in a victim’s blood or feel the give of
    the board concealing a hollow space in the floor. The
    Kindred may magnify her senses at will, sustaining this
    heightened focus for as long as she desires. At the Storyteller’s
    option, this may make hunting easier."""
        part2= """Occasionally, this talent provides extrasensory or
    even precognitive insights. These brief, unfocused
    glimpses may be odd premonitions, flashes of empathy,
    or eerie feelings of foreboding. The vampire has no
    control over these perceptions, but with practice can
    learn to interpret them with a fair degree of accuracy.
    Expanded senses come at a price, however. Bright
    lights, loud noises and strong smells present a hazard
    while the vampire uses this power. In addition to the
    possibility for distraction, an especially sudden or potent
    stimulus (like the glare of a spotlight or a clap of
    thunder) can blind or deafen the Kindred for an hour
    or more."""
        part3= """System: It takes a reflexive action to activate this
    ability, but no roll or other cost is required. In certain
    circumstances, dice rolls associated with using the
    character’s sense (such as Perception + Alertness) decrease
    in difficulty by a number equal to the character’s
    Auspex rating when the power is engaged."""
        part4= """The Storyteller may also use this power to see if the
    character perceives a threat. In this case, the Storyteller
    privately rolls the character’s unmodified Auspex
    rating, applying whatever difficulty he feels best suits
    the circumstances. For example, sensing that a pistol is
    pointed at the back of the character’s head may require
    a roll of difficulty 5, while the sudden realization that
    a rival for Primogen is planning her assassination may
    require a 9. Note that even this “precognition” comes
    only as a result of interpreting details the Kindred is
    able to notice. It’s not an all-purpose insight or miraculous
    revelation.

    At the character’s discretion, she may selectively
    heighten one specific sense, rather than leaving them
    all on. In these cases, the difficulty to perceive stimuli
    using that sense drops by one, but the difficulty to
    avoid distraction or temporary bedazzlement increases
    by one."""
        part5= """This power does not let characters see in pitch darkness,
    as does Eyes of the Beast (p. 199), but it does reduce
    difficulty penalties to act in such darkness from
    +2 to +1, and the character may make ranged attacks
    in pitch darkness if she can hear, smell, or otherwise
    detect her foe."""
        return part1,part2,part3,part4,part5
    elif discipline =="auspex2":
        part1="""Using this power, the vampire can perceive the psychic
    “auras” that radiate from mortals and supernatural
    beings alike. These halos comprise a shifting series of
    colors that take practice to discern with clarity. Even
    the simplest individual has many shifting hues within
    his aura; strong emotions predominate, while momentary
    impressions or deep secrets flash through in streaks
    and swirls.

    The colors change in sympathy with the subject’s
    emotional state, blending into new tones in a constantly
    dancing pattern. The stronger the emotions
    involved, the more intense the hues become. A skilled
    vampire can learn much from her subject by reading
    the nuances of color and brilliance in the aura’s flow."""
        part2="""Aside from perceiving emotional states, vampires use
    Aura Perception to detect supernatural beings. The
    colors in Kindred auras, while intense, are quite pale;
    mage halos often flare and crackle with arcane power;
    the race of shapeshifters has strikingly bright, almost
    frantic, auras; ghosts have weak auras that flicker fitfully
    like a dying flame; and faerie creatures’ radiance is
    shot through with capricious rainbow hues.

    System: After the character stares at the subject for
    at least a few seconds, the player rolls Perception + Empathy
    (difficulty 8); each success indicates how much
    of the subject’s aura the character sees and understands
    (see the table below). A failure indicates that the play
    of colors and patterns yields no prevailing impression.
    A botch indicates a false or erroneous interpretation.
    The Storyteller may wish to make this roll, thus keeping
    the player in the dark as to the veracity of the character’s
    interpretation."""
        part3="""Successes Result
    1 success Can distinguish only the shade (pale
    or bright).
    2 successes Can distinguish the main color.
    3 successes Can recognize the color patterns.
    4 successes Can detect subtle shifts.
    5 successes Can identify mixtures of color and
    pattern.
    The Aura Colors chart offers some example ideas
    of common colors and the emotions they reflect that
    Storytellers can use. Note that it is nearly impossible
    to determine with certainty if a particular character is
    lying or not with this power – vampires are inherently
    deceitful by nature, but even mortals might react with
    anxiety to questions while still being truthful. It is,
    however, helpful in determine the target’s emotional
    state, which might lead the vampire to decide that a
    particular target is suspicious."""
        part4="""A character may choose to perform a very cursory
    aura scan of a large area like a nightclub’s dance floor
    or the audience in a gallery. In this case, the player
    decides which characteristic of auras she’s looking for,
    and that’s the only information she’s able to glean if
    the roll is successful. (At the Storyteller’s discretion,
    on this general scan roll, more successes on the roll
    may more quickly yield what the character seeks.) For
    example, the player may specify, “Who’s the most nervous
    person in attendance?” or “Are there any vampirically
    pale auras among the CEO’s entourage?” Thereafter,
    the player may narrow down her scrutiny of a
    single individual, with an additional roll as normal.

    The character may focus in on a particular subject’s
    aura only once per scene with any degree of clarity.
    Any subsequent attempts that result in failure should
    be considered botches. It is very easy for the character
    to imagine seeing what she wants to see when judging
    someone’s intentions. After 24 hours, the character
    may try again at no penalty."""
        part5="""It is possible, though difficult, to sense the aura of a
    being who is otherwise invisible to normal sight. Refer
    to “Seeing the Unseen,” p. 142, for more information."""
        return part1,part2,part3,part4,part5 
    elif discipline=="auspex3":
        part1="""When someone handles an object for any length
    of time, he leaves a psychic impression on the item.
    A vampire with this level of Auspex can “read” these
    sensations, learning who handled the object, when he
    last held it, and what was done with it recently. (For 
    these purposes, a corpse counts as an “object” and can
    be read accordingly.) These visions are seldom clear
    and detailed, registering more like a kind of “psychic
    snapshot.” Still, the Kindred can learn much even
    from such a glimpse. Although most visions concern
    the last person to handle the item, a long-time owner
    leaves a stronger impression than someone who held
    the object briefly."""
        part2="""Gleaning information from the spiritual residue requires
    the vampire to hold the object and enter a shallow
    trance. She is only marginally aware of her surroundings
    while using The Spirit’s Touch, but a loud
    noise or jarring physical sensation breaks the trance
    instantly.

    System: The player rolls Perception + Empathy. The
    difficulty is determined by the age of the impressions
    and the mental and spiritual strength of the person or
    event that left them. Sensing information from a pistol
    used for a murder hours ago may require a 4, while
    learning who owned a bloodstained puppet fashioned a
    century ago might be a 9."""
        part3="""The greater the individual’s emotional connection
    to the object, the stronger the impression he leaves
    on it — and the more information the Kindred can
    glean from it. Events involving strong emotions (a giftgiving,
    a torture, a long family history) likewise leave
    stronger impressions than short or casual contact do.
    Assume that each success offers one piece of information,
    as per the chart below."""
        part4="""Botch The character is overwhelmed by
    psychic impressions for the next 30
    minutes and unable to act.

    Failure No information of value.

    1 success Very basic information: the last
    owner’s gender or hair color,
    for instance.

    2 successes A second piece of basic information.

    3 successes More useful information about the
    last owner, such as age and state of
    mind the last time he used the item.
    4 successes The person’s name.

    5+ successes A wealth of information: nearly
    anything you want to know about the
    person’s relationship with that object
    is available."""
        part5="""At the Storyteller’s discretion, some impressions
    on objects may be so strong — a knife plunged into
    Caesar’s breast, the tip of the Spear of Destiny, a fang
    pulled from the maw of Dracula — that any use of this
    power may be deemed a success."""
        return part1,part2,part3,part4,part5
    elif discipline=="auspex4":
        part1="""The vampire projects a portion of her consciousness
    into a nearby mortal’s mind, creating a mental link
    through which she can communicate wordlessly or
    even read the target’s deepest thoughts. The Kindred
    “hears” in her own mind the thoughts plucked from a
    subject as if they were spoken to her.

    This is one of the most potent vampiric abilities,
    since, given time, a Kindred can learn virtually anything
    from a subject without him ever knowing. The
    Tremere and Tzimisce in particular find this power especially
    useful in gleaning secrets from others, or for
    directing their mortal followers with silent precision.

    System: The player rolls Intelligence + Subterfuge
    (difficulty of the subject’s current Willpower points).
    Projecting thoughts into the target’s mind requires one
    success. The subject recognizes that the thoughts come
    from somewhere other than his own consciousness,
    though he cannot discern their actual origin without a
    successful Perception + Awareness roll (difficulty equal
    to the vampire’s Manipulation + Subterfuge)."""
        part2="""To read minds, one success must be rolled for each
    item of information plucked or each layer of thought
    pierced. Deep secrets or buried memories are harder to
    obtain than surface emotions or unspoken comments,
    requiring five or more successes to access.

    Reading thoughts with Telepathy does not commonly
    work upon the undead mind. A character may
    expend a Willpower point to make the effort, making
    the roll normally afterward. Likewise, it is equally
    difficult to read the thoughts of other supernatural
    creatures. However, the character may project her
    thoughts without expending a Willpower point. These
    thoughts, however, are still obviously intrusions into
    the target’s mind, but the character may attempt to disguise
    her mental “voice” with a roll of Manipulation +
    Subterfuge (difficulty equals the target’s Perception +
    Awareness) so the target doesn’t recognize her as the
    “speaker.”"""
        part3="""Storytellers are encouraged to describe thoughts as
    flowing streams of impressions and images, rather than
    as a sequence of prose (powers such as Telepathic Communication
    are of more use for that). Instead of making
    flat statements like “He’s planning on killing his former
    lover’s new boyfriend,” say “You see a fleeting series
    of visions: A couple kissing passionately in a doorway,
    then the man walking alone at night; you suddenly see
    your hands, knuckles white, wrapped around a steering
    wheel, with a figure crossing the street ahead; your
    heart, mortal now and hammering with panic as you
    hear the engine rev wildly; and above all, a blazing anger
    coupled with emotional agony and a panicked fear
    of loss.” Such descriptions not only add to the story, but
    they also force the player to interpret for herself what
    her character gleans. After all, understanding minds —
    especially highly emotional or deranged minds — is a
    difficult and often puzzling task."""
        return part1,part2,part3 
    elif discipline=="auspex5":
        part1="""The Kindred with this awesome ability projects her
    senses out of her physical shell, stepping from her body
    as an entity of pure thought. The vampire’s astral form
    is immune to physical damage or fatigue, and can “fly”
    with blinding speed anywhere across the earth — or
    even underground — so long as she remains below the
    moon’s orbit.

    The Kindred’s material form lies in a torpid state
    while her astral self is active, and the vampire isn’t
    aware of anything that befalls her body until she returns
    to it. An ephemeral silver cord connects the Kindred’s
    psyche to her body. If this cord is severed, her consciousness
    becomes stranded in the astral plane (the realm of
    ghosts, spirits, and shades). Attempting to return to the
    vampire’s physical shell is a long and terrifying ordeal,
    especially since there is no guarantee that she will accomplish
    the journey successfully. This significant danger
    keeps many Kindred from leaving their bodies for
    long, but those who dare can learn much."""
        part2="""System: Journeying in astral form requires the player
to expend a point of Willpower and make a Perception
+ Awareness roll. Difficulty varies depending on the distance
and complexity of the intended trip; 5 is within
sight, 7 is nearby or to a familiar location, and 9 reflects a
trip far from familiar territory (a first journey from North
America to the Far East; trying to shortcut through the
earth). The greater the number of successes rolled, the
more focused the character’s astral presence is, and the
easier it is for her to reach her desired destination.

Failure means the character is unable to separate
her consciousness from her body, while a botch can
have nasty consequences — flinging her astral form to
a random destination on Earth or in the spirit realm,
arriving in a place where the sun is active (necessitating
a frenzy roll, although the sunlight doesn’t do any
damage), or hurtling toward the desired destination so
forcefully that the silver cord snaps.

The player may spend a point of Willpower to activate
this power, and an additional point of Willpower to
gain the success necessary to perform the jaunt. This is
an exception to the normal rule where a player may not
spend more than a single point of Willpower per turn."""
        part3="""Each scene in Psychic Projection requires another
    point of Willpower and a new roll. Failure indicates
    that the vampire has lost her way and must retrace the
    path of her silver cord. A botch at this stage means the
    cord snaps, stranding the character’s psychic form in
    the mysterious astral plane.

    An astral form may travel at great speeds (the Storyteller
    can use roughly 1000 miles per hour or 1500
    kilometers per hour as a general guide) and carries no
    clothing or material objects of any kind. Some artifacts
    are said to exist in the spirit world, and the character
    can try to use one of these tools if she finds one. The
    character cannot bring such relics to the physical world
    when she returns to her body, however.

    Interaction with the physical world is impossible
    while using Psychic Projection. At best, the character
    may spend a Willpower point to manifest as a ghostlike
    shape. This apparition lasts one turn before fading
    away; while she can’t affect anything physically during
    this time, the character can speak. Despite lacking
    physical substance, an astral character can use Auspex
    normally. At the Storyteller’s discretion, such a character
    may employ some or all Animalism, Dementation,
    Dominate, Necromancy, Obtenebration, Presence,
    Thaumaturgy, and similar non-corporeal powers
    she has, though this typically requires a minimum of
    three successes on the initial Psychic Projection roll."""
        part4="""If two astral shapes encounter one another, they
interact as if they were solid. They may talk, touch,
and even fight as if both were in the material world.
Since they have no physical bodies, astral characters
seeking to interact “physically” substitute Mental and
Social Traits for Physical ones (Wits replaces Dexterity,
Manipulation supplants Strength, and Intelligence
replaces Stamina). Due to the lack of a material form,
the only real way to damage another psychic entity is
to cut its silver cord. When fighting this way, consider
Willpower points to be health levels; when a combatant
loses all of her Willpower, the cord is severed.

Although an astrally projected character remains in
the reflection of the mortal world, she may venture further
into the spirit realms, especially if she becomes
lost. Other beings with particular sensitivity to psychic
activity, such as ghosts, werewolves, and even some
magi, travel the astral plane as well, and can interact
with a vampire’s psychic presence normally (although
the astrally projected character is not considered a
“ghost” for powers such as Necromancy). The observing
character notices the astrally projecting vampire
with a Perception + Awareness roll (difficulty 8), requiring
more successes than the Psychic Projection
activation roll. Even those who do notice you won’t
be able to identify you; you are merely an immaterial
shade hovering in the general area. Storytellers are encouraged
to make trips into the spirit world as bizarre,
mysterious, and dreamlike as possible. The world beyond
is a vivid and fantastic place, where the true nature
of things is stronger and often strikingly different
from their earthly appearances."""
        return part1,part2,part3,part4

    elif discipline=="chimerstry1":
        part1="""The vampire may conjure a minor, static mirage that
    confounds one sense. For instance, he may evoke a sulfurous
    stench, the appearance of stigmata, or the shatter
    of broken glass. Note that though tactile illusions
    can be felt, they have no real substance; an invisible
    but tactile wall cannot confine anyone, and invisible
    razor-wire causes no real damage. Similarly, the vampire
    must know the characteristics of what he’s creating.
    While it’s easy enough to estimate what a knife
    wound might look like, falsifying a person’s voice or a
    photograph of a childhood home requires knowledge
    of the details.

    System: The player spends a point of Willpower
    for the vampire to create this illusion. The volume of
    smells, ambient lighting, smoke clouds, and the like
    are limited to roughly 20 cubic feet (half a cubic meter)
    per dot the vampire has in Chimerstry. The illusion
    lasts until the vampire leaves its vicinity (such as
    stepping out of the room) or until another person sees
    through it somehow. The Cainite may also end the illusion
    at any time with no effort."""
        return part1
    elif discipline=="chimerstry2":
        part1="""The Cainite can now create illusions that appeal to
    all the senses, though they remain static. For example,
    the vampire could make a filthy cellar appear as an opulent
    ballroom, though she could not create a glittering
    chandelier or a score of graceful dancers. Again, the
    illusion has no solid presence, though it’s easy enough
    to fool an enraptured visitor with suggestions of what
    she might expect. A bucket of brackish water is as cool
    as chilled champagne, after all.

    System: The player spends a Willpower point and a
    blood point to create the illusion. These static images
    remain until dispelled, in much the same way that an
    Ignis Fatuus illusion does."""
        return part1
    elif discipline=="chimerstry3":
        part1="""Not really a power unto itself, Apparition allows a
    vampire to give motion to an illusion created with Ignis
    Fatuus or Fata Morgana. Thus, the Cainite could
    create the illusion of a living being, running water,
    fluttering drapes, or a roaring fire.

    System: The creator spends one blood point to make
    the illusion move in one significant way, or in any
    number of subtle ways. For example, the vampire could
    create the illusion of a lurking mugger lurching at her
    victim, or she could create the illusion of a desolate
    street, down which a chill wind blows trash while a
    streetlamp flickers and hums. Taking complicated actions
    besides maintaining the illusion — that is, anything
    that would require a dice roll — first requires success
    on a Willpower roll, resulting in the dissolution of
    the false construct if the roll fails.

    Once the creator stops concentrating on the illusion,
    it can continue in simple, repetitive motions – roughly
    speaking, anything that can be described in a simple
    sentence, such as a guard walking back and forth in
    front of a steel door. After that, the vampire cannot
    regain control over the illusion – she can either allow
    it to continue moving as ordered, or let it fade as described
    under Ignis Fatuus."""
        return part1
    elif discipline=="chimerstry4":
        part1="""This power, also used in conjunction with Ignis
    Fatuus or Fata Morgana, allows a mirage to persist even
    when the vampire cannot see it. In this way, Ravnos
    often cloak their temporary havens in false trappings of
    luxury, or ward off trespassers with illusory guard dogs.
    System: The vampire need only spend a blood point,
    and the illusion becomes permanent until dissolved
    (including “programmed” illusions like those created
    by Apparition)."""
        return part1
    elif discipline=="chimerstry5":
        part1="""Rather than create simple illusions, the vampire
    can now project hallucinations directly into a victim’s
    mind. The target of these illusions believes completely
    that the images are real; a hallucinatory fire can burn
    him, an imaginary noose can strangle him, and an illusory
    wall can block him. This power affects only one
    person at a time; though others can see the illusion, it
    doesn’t impact them in the same way. Other people
    can try to convince the victim that his terrors are not
    real, but he won’t believe them. Note that targets with
    enough dots in Auspex can still attempt to roll for Seeing
    the Unseen (p. 142).

    System: A Horrid Realty illusion costs two Willpower
    points to set in motion and lasts for an entire
    scene (though its effects may last longer; see below).
    If the vampire is trying to injure his victim, his player
    must roll Manipulation + Subterfuge (difficulty of the
    victim’s Perception + Self-Control/Instinct). Each
    success inflicts one health level of lethal damage on
    the victim that cannot be soaked — the Cainite assaults
    the victim’s mind and perceptions, not his body.
    If the player wishes to inflict less damage or change it
    to bashing, he may announce a maximum amount of
    damage before rolling the dice. Secondary effects (such
    as frenzy rolls for illusory fire) may also occur."""
        part2="""The victim heals all his damage instantaneously if
    he can be convinced that the damage he took was illusory,
    but convincing him may take some doing, such
    as with at least two successes on a Charisma + Empathy
    roll (difficulty equal to the Manipulation + Subterfuge
    of the Cainite using Horrid Reality). The target must
    be convinced of the attack’s illusory nature within 24
    hours of its taking place, or it becomes too well established
    in his memory, and he will have to heal the damage
    using blood (if a vampire) or over time (if mortal).

    This power cannot actually kill its victims (though a
    target with a heart condition may well die from fright).
    A victim “killed” by an illusory attack loses consciousness
    or enters torpor."""
        return part1,part2

    elif discipline=="dementation1":
        part1="""The vampire stirs his victim’s emotions, either
    heightening them to a fevered pitch or blunting them
    until the target is completely desensitized. The Cainite
    may not choose which emotion is affected; she may
    only amplify or dull emotions already present in the
    target. In this way, a vampire can inflame mild irritation
    into quivering rage or atrophy true love into casual
    interest.

    System: The character talks to her victim, and
    the vampire’s player rolls Charisma + Empathy (difficulty
    equals the victim’s Humanity or Path rating).
    The number of successes determines the duration of
    the altered state of feeling. Effects of this power might
    include one- or two-point additions or subtractions
    to difficulties of frenzy rolls, Virtue rolls, rolls to resist
    Presence powers, etc."""
        part2="""1 success One turn
    2 successes One hour
    3 successes One night
    4 successes One week
    5 successes One month
    6+ successes Three months"""
        return part1,part2
    elif discipline=="dementation2":
        part1="""The vampire manipulates the sensory centers of his
    victim’s brain, flooding the victim’s senses with visions,
    sounds, scents, or feelings that aren’t really there. The
    images, regardless of the sense to which they appeal,
    are only fleeting “glimpses,” barely perceptible to the
    victim. The vampire using Dementation cannot control
    what the victim perceives, but may choose which
    sense is affected.

    The “haunting” effects occur mainly when the victim
    is alone, and mostly at night. They may take the
    form of the subject’s repressed fears, guilty memories,
    or anything else that the Storyteller finds dramatically
    appropriate. The effects are never pleasant or unobtrusive,
    however. The Storyteller should let her imagination
    run wild when describing these sensory impressions;
    the victim may well feel as if she is going mad, or
    as if the world is.

    System: After the vampire speaks to the victim, the
    player spends a blood point and rolls Manipulation +
    Subterfuge (difficulty of his victim’s Perception + Self-
    Control/Instinct). The number of successes determines
    the length of the sensory “visitations.” The precise effects
    are up to the Storyteller, though particularly eerie
    or harrowing apparitions can certainly reduce dice
    pools for a turn or two after the manifestation."""
        part2="""1 success One night
    2 successes Two nights
    3 successes One week
    4 successes One month
    5 successes Three months
    6+ successes One year"""
        return part1,part2
    elif discipline=="dementation3":
        part1="""This peculiar power allows the vampire to take advantage
    of the fleeting clarity hidden in insanity. She
    may scrutinize the “patterns” of a person’s soul, the
    convolutions of a vampire’s inner nature, or even random
    events in nature itself. The Kindred with this
    power can discern the most well-hidden psychoses, or
    gain insight into a person’s true self. Malkavians with
    this power often have (or claim to have) knowledge of
    the moves and countermoves of the great Jyhad, or the
    patterns of fate.

    System: This power allows a vampire to determine a
    person’s true Nature, among other things. The vampire
    concentrates for a turn, then her player rolls Perception
    + Occult. The difficulty depends on the intricacy of the
    pattern. Discerning the Nature of a stranger would be
    difficulty 9, a casual acquaintance would be an 8, and
    an established ally a 6. The vampire could also read
    the message locked in a coded missive (difficulty 7), or
    even see the doings of an invisible hand in such events
    as the pattern of falling leaves (difficulty 6). Almost
    anything might contain some hidden insight, no matter
    how trivial or meaningless. The patterns are present
    in most things, but are often so intricate they can
    keep a vampire spellbound for hours while she tries to
    understand their message."""
        part2="""This is a potent power, subject to adjudication. Storytellers,
    this power is an effective way to introduce
    plot threads for a chronicle, reveal an overlooked clue,
    foreshadow important events, or communicate critical
    information a player seeks. Important to its use, though,
    is delivering the information properly. Secrets revealed
    via Eyes of Chaos are never simple facts; they’re tantalizing
    symbols adrift in a sea of madness. Describe the
    results of this power in terms of allegory: “The man
    before you appears as a crude marionette, with garish
    features painted in bright stage makeup, and strings
    vanishing up into the night sky.” Avoid stating plainly,
    “You learn that this ghoul is the minion of a powerful
    Methuselah.”"""
        return part1,part2
    elif discipline=="dementation4":
        part1="""By merely addressing his victims aloud, the Kindred
    can drive targets into fits of blind rage or fear, forcing
    them to abandon reason and higher thought. Victims
    are plagued by hallucinations of their subconscious demons,
    and try to flee or destroy their hidden shames.
    Tragedy almost always follows in the wake of this power’s
    use, though offending Malkavians often claim that
    they were merely encouraging people to act “according
    to their natures.” Unfortunately for the vampire concerned,
    he runs a very real risk of falling prey to his
    own voice’s power.

    System: The player spends a blood point and makes
    a Manipulation + Empathy roll (difficulty 7). One target
    is affected per success, although all potential victims
    must be listening to the vampire’s voice.
    Affected victims fly immediately into frenzy or a
    blind fear like Rötschreck. Kindred or other creatures
    capable of frenzy, such as Lupines, may make a frenzy
    check or Rötschreck test (Storyteller’s choice as to how
    they are affected) at +2 difficulty to resist the power.
    Mortals are automatically affected and don’t remember
    their actions while berserk. The frenzy or fear lasts for
    a scene, though vampires and Lupines may test as usual
    to snap out of it."""
        part2="""The vampire using Voice of Madness must also test
    for frenzy or Rötschreck upon invoking this power,
    though his difficulty to resist is one lower than normal.
    If the initial roll to invoke this power is a failure,
    however, the roll to resist the frenzy is one higher than
    normal. If the roll to invoke this power is a botch, the
    frenzy or Rötschreck response is automatic."""
        return part1,part2
    elif discipline=="dementation5":
        part1="""The vampire coaxes the madness from the deepest
    recesses of her target’s mind, focusing it into an overwhelming
    wave of insanity. This power has driven
    countless victims, vampire and mortal alike, to unfortunate
    ends.

    System: The Kindred must gain her target’s undivided
    attention for at least one full turn to enact this
    power. The player spends a blood point and rolls Manipulation
    + Intimidation (difficulty of her victim’s
    current Willpower points). If the roll is successful, the
    victim is afflicted with five derangements of the Storyteller’s
    choice (see p. 290). The number of successes
    determines the duration.
    Successes Result
    1 success One turn
    2 successes One night
    3 successes One week
    4 successes One month
    5+ successes One year"""
        part2="""On a botch… well, the Storyteller can decide what
    a vampire inflicts upon herself by attempting to incite
    the primal hells lurking within the darkest recesses of
    a victim’s mind.

    The victim (or the target of a botch) can spend a
    number of Willpower points equal to the successes
    rolled to end the duration prematurely. The Storyteller
    decides when such Willpower points can be spent (such
    as after a therapy session or after a friend has managed
    to prove a particular delusion to be false)."""
        return part1,part2

    elif discipline=="presence1":
        part1="""Those near the vampire suddenly desire to be closer
    to her and become receptive to her point of view. Awe
    is extremely useful for mass communication. It matters
    little what is said — the hearts of those affected lean
    toward the vampire’s opinion. The weak want to agree
    with her; even if the strong-willed resist, they soon
    find themselves outnumbered. Awe can turn a chancy
    deliberation into a certain resolution in the vampire’s
    favor almost before her opponents know that the tide
    has turned.

    Despite the intensity of this attraction, those so smitten
    do not lose their sense of self-preservation. Danger
    breaks the spell of fascination, as does leaving the area.
    Those subject to Awe will remember how they felt in
    the vampire’s presence, however. This will influence
    their reactions should they ever encounter her again."""
        part2="""System: The player spends a blood point and rolls
    Charisma + Performance (difficulty 7). The number of
    successes rolled determines how many people are affected,
    as noted on the chart below. If there are more
    people present than the character can influence, Awe
    affects those with lower Willpower ratings first. The
    power stays in effect for the remainder of the scene or
    until the character chooses to drop it.

    Successes Result
    1 success One person
    2 successes Two people
    3 successes Six people
    4 successes 20 people
    5 successes Everyone in the vampire’s immediate
    vicinity (an entire auditorium, a mob)

    Those affected can use Willpower points to overcome
    the effect, but must continue spending Willpower every
    scene for as long as they remain in the same area as
    the vampire. As soon as an individual spends a number
    of Willpower points equal to the successes rolled, he
    shakes off the Awe completely and remains unaffected
    for the rest of the night."""
        return part1,part2
    elif discipline=="presence2":
        part1="""While all Kindred can frighten others by physically
    revealing their true vampiric natures — baring claws
    and fangs, glaring with malevolence, hissing loudly with
    malice — this power focuses these elements to insanely
    terrifying levels. Dread Gaze engenders unbearable terror
    in its victim, stupefying him into madness, immobility,
    or reckless flight. Even the most stalwart individual
    will fall back from the vampire’s horrific visage.

    System: The player rolls Charisma + Intimidation
    (difficulty equal to the victim’s Wits + Courage). SucVAMPIRE
    cess indicates the victim is cowed, while failure means
    the target is startled but not terrified by the sight. Three
    or more successes means he runs away in abject fear;
    victims who have nowhere to run claw at the walls,
    hoping to dig a way out rather than face the vampire.
    Moreover, each success subtracts one from the target’s
    action dice pools next turn."""
        part2="""The character may attempt Dread Gaze once per turn
    against a single target, though she may also perform it
    as an extended action, adding her successes in order to
    subjugate the target completely. Once the target loses
    enough dice that he cannot perform any action, he’s so
    shaken and terrified that he curls up on the ground and
    weeps. Failure during the extended action means the
    attempt falters. The character loses all her collected
    successes and can start over next turn, while the victim
    may act normally again.

    A botch at any time indicates the target is not at all
    impressed — perhaps even finding the vampire’s antics
    comical — and remains immune to any further uses of
    Presence by the character for the rest of the story."""
        return part1,part2
    elif discipline=="presence3":
        part1="""This power bends others’ emotions, making them
    the vampire’s willing servants. Due to what these individuals
    see as true and enduring devotion, they heed
    the vampire’s every desire. Since this is done willingly,
    instead of having their wills sapped, these servants retain
    their creativity and individuality.

    While these obedient minions are more personable
    and spirited than the mind-slaves created by Dominate,
    they’re also somewhat unpredictable. Further,
    since Entrancement is of a temporary duration, dealing
    with a lapsed servant can be troublesome. A wise Kindred
    either disposes of those she Entrances after they
    serve their usefulness, or binds them more securely by a
    blood bond (made much easier by the minion’s willingness
    to serve).

    System: The player spends a blood point and rolls
    Appearance + Empathy (difficulty equal to the target’s
    current Willpower points); the number of successes
    determines how long the subject is Entranced, as per
    the chart below. (Subjects can still spend Willpower to
    temporarily resist, like any other Presence power.) The
    Storyteller may wish to make the roll instead, since the
    character is never certain of the strength of her hold
    on the victim. The vampire may try to keep the subject
    under her thrall, but can do so only after the initial
    Entrancement wears off. Attempting this power while
    Entrancement is already in operation has no effect."""
        part2="""Successes Result
    Botch Subject cannot be entranced
    for the rest of the story.
    Failure Subject cannot be entranced
    for the rest of the night.
    1 success One hour
    2 successes One day
    3 successes One week
    4 successes One month
    5 successes One year"""
        return part1,part2 
    elif discipline=="presence4":
        part1="""This impressive power enables the vampire to call to
    herself any person whom she has ever met. This call
    can go to anyone, mortal or supernatural, across any
    distance within the physical world. The subject of the
    Summons comes as fast as he is able, possibly without
    even knowing why. He knows intuitively how to find
    his Summoner — even if the vampire moves to a new
    location, the subject redirects his own course as soon
    as he can. After all, he’s coming to the vampire herself,
    not to some predetermined site.

    Although this power allows the vampire to call someone
    across a staggering distance, it is most useful when
    used locally. Even if the desired person books the next
    available flight, getting to Kyoto from Milwaukee can
    still take far longer than the vampire needs. Obviously,
    the individual’s financial resources are a factor; if he
    doesn’t have the money to travel quickly, it will take
    him a far greater time to get there.

    The subject thinks mainly of reaching the vampire,
    but does not neglect his own well-being. This is less
    of a consideration if he only has to cross a room, unless
    he must get through a gang of gun-wielding punks
    to do so. The individual retains his survival instincts,
    and while he won’t shirk physical violence to reach
    the vampire’s side, he won’t subject himself to suicidal
    situations."""
        part2="""The Summoning dissipates at dawn. Unless the subject
    is trained to continue toward the vampire after the
    first call, the immortal must Summon each night until
    the target arrives. Still, as long as the vampire is willing
    and able, she is assured to greet her desired subject
    some night — as long as nothing happens to him along
    the way, of course.

    System: The player spends a blood point and rolls
    Charisma + Subterfuge. The base difficulty is 5; this in196
    creases to difficulty 7 if the subject was met only briefly.
    If the character used Presence successfully on the target
    in the past, this difficulty drops to 4, but if the attempt
    was unsuccessful, the difficulty rises to 8.
    The number of successes indicates the subject’s speed
    and attitude in responding:
    Successes Result
    Botch Subject cannot be Summoned by
    that vampire for the rest of the story.
    Failure Subject cannot be Summoned by that
    vampire for the rest of the night.
    1 success Subject approaches slowly
    and hesitantly.
    2 successes Subject approaches reluctantly and
    is easily thwarted by obstacles.
    3 successes Subject approaches with
    reasonable speed.
    4 successes Subject comes with haste,
    overcoming any obstacles in
    his way.
    5 successes Subject rushes to the vampire, doing
    anything to get to her."""
        return part1,part2 
    elif discipline=="presence5":
        part1="""At this stage, the vampire can augment her supernatural
    mien a thousandfold. The attractive become
    paralyzingly beautiful; the homely become hideously
    twisted. Majesty inspires universal respect, devotion,
    fear — or all those emotions at once — in those
    around the vampire. The weak scramble to obey her
    every whim, and even the most dauntless find it almost
    impossible to deny her.

    People affected find the vampire so formidable that
    they dare not risk her displeasure. Raising their voices
    to her is difficult; raising a hand against her is unthinkable.
    Those few who shake off the vampire’s potent
    mystique enough to oppose her are shouted down by
    the many under her thrall, before the immortal need
    even respond.

    Under Majesty’s influence, hearts break, power trembles,
    and the bold shake. Wise Kindred use this power
    with caution against mortal and immortal alike. While
    Majesty can cow influential politicians and venerable Primogen,
    the vampire must be careful that doing so doesn’t
    come back to haunt her. After all, a dignitary brought
    low before others loses his usefulness quickly, while a humiliated
    Kindred has centuries to plan revenge."""
        part2="""System: No roll is required on the part of the vampire,
    but she must spend a Willpower point. A subject
    must make a Courage roll (difficulty equal to the vampire’s
    Charisma + Intimidation, to a maximum of 10) if
    he wishes to be rude or simply contrary to the vampire.
    Success allows the individual to act normally for the
    moment, although he feels the weight of the vampire’s
    displeasure crushing down on him. A subject who fails
    the roll aborts his intended action and even goes to
    absurd lengths to humble himself before the vampire,
    no matter who else is watching. The effects of Majesty
    last for one scene."""
        return part1,part2

    elif discipline=="protean1":
        part1="""The vampire sees perfectly well in pitch darkness,
    not requiring a light source to notice details in even
    the darkest basement or cave. The vampire’s Beast is
    evident in his red glowing eyes, a sight sure to disturb
    most mortals.

    System: The character must declare his desire to call
    forth the Eyes. No roll is necessary, but the change requires
    a full turn to complete. While manifesting the
    Eyes, the character suffers a +1 difficulty to all Social
    rolls with mortals unless he takes steps to shield his
    eyes (sunglasses are the simplest solution). (A vampire
    without this power who is immersed in total darkness
    suffers blind-fighting penalties as per p. 274.)"""
        return part1
    elif discipline=="protean2":
        part1="""The vampire’s nails transform into long, bestial claws.
    These talons are wickedly sharp, able to rend flesh with
    ease and even carve stone and metal with little trouble.
    The Beast is prominent in the claws as well, making
    them fearsome weapons against other immortals. It’s
    rumored that some Gangrel have modified this power
    to change their vampiric fangs into vicious tusks.
    System: The claws grow automatically in response to
    the character’s desire, and can grow from both hands
    and feet. The transformation requires the expenditure
    of a blood point, takes a single turn to complete, and
    lasts for a scene.

    The character attacks normally in combat, but the
    claws inflict Strength + 1 aggravated damage. Other
    supernaturals cannot normally soak this damage, although
    a power such as Fortitude may be used. Additionally,
    the difficulties of all climbing rolls are reduced
    by two."""
        return part1
    elif discipline=="protean3":
        part1="""One of the most prized powers within Protean,
Earth Meld enables the vampire to become one with
the earth. The immortal literally sinks into the bare
ground, transmuting his substance to bond with the
earth.

Though a vampire can immerse himself fully into the
ground, he cannot move around within it. Further, it
is impossible to meld into earth through another substance.
Wood slats, blacktop, even artificial turf blocks
Earth Meld’s effectiveness — then again, it’s a relatively
simple matter for a vampire at this level of power
to grow claws and rip apart enough of the flooring to
expose the raw soil beneath.

By interring himself in the ground, the vampire gains
full protection from daylight when outdoors. It is also
the method of choice for those Kindred who wish to
sleep away the centuries; these vampires lock themselves
in the earth’s embrace, gaining strength and
power as they rest. Superstitious and paranoid Kindred
whisper that thousands of Ancients sleep within the
ground and will awaken when Gehenna arrives."""
        part2="""While so interred, the vampire is in a transitional
state between flesh and earth. His physical presence
exists between the physical world and the astral plane.
As such, the vampire is difficult to sense, even through
supernatural means. However, a disruption to the soil
that the immortal occupies, or to his presence on the
astral realm, returns him immediately to the physical
world (and to full wakefulness), showering dirt outward
as his body displaces the soil.

System: No roll is necessary, although the character
must spend a blood point. Sinking into the earth is
automatic and takes a turn to complete. The character
falls into a state one step above torpor during this time,
sensing his surroundings only distantly. The player
must make a Humanity or Path roll (difficulty 6) for
the character to rouse himself in response to danger
prior to his desired time of emergence.
Since the character is in an in-between state, any attempts
to locate him (catching his scent, scanning for
his aura, traveling astrally, and so on) are made at +2
difficulty. Astral individuals cannot affect the vampire
directly, instead meeting with a kind of spongy resistance
as their hands pass through him. Similarly, digging
in the material world encounters incredibly hardpacked
earth, virtually as dense as stone.

Attempts at violence upon the submerged vampire
from either side return him to his physical nature, expelling
the soil with which he bonded in a blinding
spray (all Perception-based rolls are at +2 difficulty for
the turn). The character himself subtracts two from
his initiative for the first turn after his restoration, due
to momentary disorientation. Once expelled from the
earth, the vampire may act normally."""
        return part1,part2 
    elif discipline=="protean4":
        part1="""This endows the vampire with the legendary ability
    to transform into a wolf or bat. A Kindred changed
    in this way is a particularly imposing representative
    of the animal kingdom. Indeed, he is far superior to
    normal animals, even ones possessed by Subsume the
    Spirit. He retains his own psyche and temperament,
    but can still call upon the abilities of the beast form
    — increased senses for the wolf and flight for the bat.
    Gangrel are reputed to change to other animal forms
    better suited to their environment — jackals in Africa,
    dholes in Asia, and even enormous rats in urban environments
    — a feat that other Clans learning Protean
    cannot seem to duplicate.

    System: The character spends one blood point to assume
    the desired shape. The transformation requires
    three turns to complete (spending additional blood
    points reduces the time of transformation by one turn
    per point spent, to a minimum of one). The vampire
    remains in his beast form until the next dawn, unless
    he wishes to change back sooner.
    While in the animal’s shape, the vampire can use any
    Discipline he possesses except Necromancy, Serpentis,
    Thaumaturgy, or Vicissitude (as well as any others
    the Storyteller deems unavailable). Furthermore, each
    form gives the character the abilities of that creature.
    In wolf form, the vampire’s teeth and claws inflict
    Strength + 1 aggravated damage, he can run at double
    speed, and the difficulties of all Perception rolls are reduced
    by two. In bat form, the vampire’s Strength is reduced
    to 1, but he can fly at speeds of up to 20 miles per
    hour, difficulties for all hearing-based Perception rolls
    are reduced by three, and attacks made against him are
    at +2 difficulty due to his small size.
    The Storyteller may allow Gangrel to assume a different
    animal shape, but should establish the natural
    abilities it grants the character."""
        return part1 
    elif discipline =="protean5":
        part1="""This truly unsettling power enables the vampire to
turn into mist. His physical shape disperses into a hazy
cloud, but one still subject entirely to the immortal’s
will. He floats at a brisk pace and may slip under doors,
through screens, down pipes, and through other tiny
openings. Although strong winds can blow the vampire
from his chosen course, even hurricane-force winds
cannot disperse his mist shape.
Some Kindred feel that this power is an expression of
the vampire’s ultimate control over the material world,
while others believe that it is the immortal’s soul made
manifest (damned though it may be).

System: No roll is required, although a blood point
must be spent. The transformation takes three turns to
complete, although the character may reduce this time
by one turn for each additional blood point spent (to
a minimum of one turn). Strong winds may buffet the
character, although Disciplines such as Potence may
be used to resist them. Vampires in Mist Form can perceive
their surroundings normally, although they cannot
use powers that require eye contact.

The vampire is immune to all mundane physical attacks
while in mist form, although supernatural attacks
affect him normally. Also, the vampire takes one fewer
die of damage from fire and sunlight. The character may
not attack others physically while in this state — this
includes encountering another vampire in mist form.
He may use Disciplines that do not require physical
substance, however."""
        return part1

    elif discipline=="serpentis1":
        part1="""This power grants the vampire the legendary hypnotic
    gaze of the serpent. The Kindred’s eyes become
    gold with large black irises, and mortals in the character’s
    vicinity find themselves strangely attracted to
    him. A mortal who meets the vampire’s beguiling gaze
    is immobilized. Until the character takes his eyes off
    his victim, the person is frozen in place.

    System: No roll is required, but this power can be
    avoided if the mortal takes care not to look into the
    vampire’s eyes. Vampires and other supernatural creatures
    can also be affected by this power if the Cainite’s
    player succeeds on a Willpower roll (difficulty 9). If attacked
    or otherwise harmed, supernatural creatures can
    spend a point of Willpower to break the spell.

    Note: This is different than normal eye contact detailed
    on p. 152. The target must be able to see the
    vampire’s eyes for Eyes of the Serpent to work."""
        return part1 
    elif discipline=="serpentis2":
        part1="""The vampire may lengthen her tongue at will, splitting
    it into a fork like that of a serpent. The tongue
    may reach 18 inches or half a meter, and makes a terrifyingly
    effective weapon in close combat.

    System: The lash of the tongue’s razor fork causes aggravated
    wounds (difficulty 6, Strength damage). If the
    Kindred wounds her enemy, she may drink blood from
    the target on the next turn as though she had sunk her
    fangs into the victim’s neck. Horrifying though it is, the
    tongue’s caress is very like the Kiss, and strikes mortal
    victims helpless with fear and ecstasy. Additionally,
    the tongue is highly sensitive to vibrations, enabling
    the vampire to function effectively in the darkness the
    Clan prefers. By flicking his tongue in and out of his
    mouth, the vampire can halve any penalties relating to
    darkness (p. 274)."""
        return part1 
    elif discipline=="serpentis3":
        part1="""By calling upon her Blood, the vampire may transform
    her skin into a mottled, scaly hide. A vampire in
    this form becomes more supple and flexible.

    System: The vampire spends one blood point and
    one Willpower point. Her skin becomes scaly and
    mottled; this, combined with the character’s increased
    flexibility, reduces soak difficulties to 5. The vampire
    may use her Stamina to soak aggravated damage from
    claws and fangs, but not from fire, sunlight, or other supernatural
    energies. The vampire’s mouth widens and
    fangs lengthen, enabling her bite to inflict an extra die
    of damage. Finally, the vampire may slip through any
    opening wide enough to fit her head through.
    The vampire’s Appearance drops to 1, and she is obviously
    inhuman if observed with any degree of care,
    though casual passersby might not notice, if the vampire
    is in darkness or wearing heavy clothing."""
        return part1 
    elif discipline=="serpentis4":
        part1="""The Cainite may change his form into that of a huge
    black cobra. The serpent weighs as much as the vampire’s
    human form, stretches over 10 feet or three meters
    long, and is about 20 inches (50 cm) around. The
    Form of the Cobra grants several advantages, including
    a venomous bite, the ability to slither through small
    spaces, and a greatly enhanced sense of smell. The
    character may use any Disciplines while in this form
    save those that require hands (such as Feral Claws).

    System: The vampire spends one blood point; the
    change is automatic, but takes three turns. Clothing
    and small personal possessions transform with the vampire.
    The vampire remains in serpent form until the
    next dawn, unless he desires to change back sooner.
    The Storyteller may allow the Setite bonus dice on all
    Perception rolls related to smell, but the difficulties for
    all hearing rolls are increased by two. The cobra’s bite
    inflicts damage equal to the vampire’s, but the vampire
    does not need to grapple his victim; furthermore, the
    poison delivered is fatal to mortals."""
        return part1 
    elif discipline=="serpentis5":
        part1="""A Kindred with mastery of Serpentis may pull her
    heart from her body. She can even use this ability on
    other Cainites, although this requires several hours of
    gruesome surgery. This power can only be invoked during
    a new moon. If performed under any other moon,
    the rite fails. Upon removing her heart, the vampire
    places it in a small clay urn, and then carefully hides or
    buries the urn. While her heart is hidden, she cannot
    be staked by any wood that pierces her breast. Moreover,
    because the heart is the seat of emotion, the difficulties
    of all her rolls to resist frenzy are two lower
    while this power is in effect.

    Cainites are careful to keep their hearts safe from
    danger. If someone seizes her heart, the vampire is
    completely at that person’s mercy. The heart can be
    destroyed only by casting it into a fire or exposing it to
    sunlight. If this happens, the Kindred dies where she
    stands, boiling away into a blistering heap of ash and
    blackened bone. Plunging a wooden stake into an exposed
    heart drives the vampire into instant torpor.

    A vampire may carry her heart with her, or have
    several false hearts buried in different places. A smart
    Kindred often avoids her heart’s hiding place, to deter
    discovery. Those wise in Setite lore whisper that the
    corrupt elders of the Clan often hold their underlings’
    hearts as yet another method of control."""
        part2="""System: This power requires no roll. Those who witness
    a vampire pull his heart from his breast (or cut
    the heart from another vampire) must make Courage
    rolls. Failure indicates anything from strong uneasiness
    to complete revulsion, possibly even Rötschreck."""
        return part1,part2

    elif discipline=="vicissitude1":
        part1="""A vampire with this power may alter her own bodily
    parameters: height, build, voice, facial features, and
    skin tone, among other things. Such changes are cosmetic
    and minor in scope — no more than a foot (30
    cm) of height gained or lost, for example. She must
    physically mold the alteration, literally shaping her
    flesh into the desired result.

    System: The player must spend a blood point for
    each body part to be changed, then roll Intelligence +
    Medicine (difficulty 6). To duplicate another person or
    voice requires a Perception + Medicine roll (difficulty
    8), and five successes are required for a flawless copy;
    fewer successes leave minute (or not-so-minute) flaws.
    Increasing one’s Appearance Trait has a difficulty of 9,
    and the vampire must spend an additional blood point
    for each dot of Appearance increased beyond their natural
    total. A botch permanently reduces the Attribute
    by one."""
        return part1 
    elif discipline=="vicissitude2":
        part1="""This power is similar to Malleable Visage, above, but
    allows the vampire to perform drastic, grotesque alterations
    on other creatures. Tzimisce often use this power
    to transform their servitors into monstrous guards, the
    better to frighten foes. Only flesh (skin, muscle, fat,
    and cartilage, but not bone) may be transformed.
    System: After spending a blood point, the vampire
    must grapple the intended victim. The player of
    the Flescrafting vampire makes a successful Dexterity
    + Medicine roll (difficulty variable: 5 for a crude
    yank-and-tuck, up to 9 for precise transformations). A
    vampire who wishes to increase another’s Appearance
    Trait does so as described under Malleable Visage; reducing
    the Attribute is considerably easier (difficulty
    5), though truly inspired disfigurement may dictate a
    higher difficulty. In either case, each success increases
    or reduces the Attribute by one.

    A vampire may use this power to move clumps of
    skin, fat, and muscle tissue, thus providing additional
    padding where needed. For each success scored on a
    Dexterity + Medicine roll (difficulty 8), the vampire
    may increase the subject’s soak dice pool by one, at the
    expense of either a point of Strength or a health level
    (vampire’s choice)."""
        return part1 
    elif discipline=="vicissitude3":
        part1="""This terrible power allows a vampire to manipulate
    bone in the same manner that flesh is shaped. In conjunction
    with Fleshcraft, above, this power enables a
    Vicissitude practitioner to deform a victim (or herself)
    beyond recognition. This power should be used in conjunction
    with the flesh-shaping arts, unless the vampire
    wants to inflict injury on the victim (see below).

    System: The vampire’s player must spend a blood
    point and make a Strength + Medicine roll (difficulties
    as above). Bonecraft may be used without the fleshshaping
    arts, as an offensive weapon. Each success
    scored on the Strength + Medicine roll (difficulty 7)
    inflicts one health level of lethal damage on the victim,
    as his bones rip, puncture, and slice their way out
    of his skin.

    The vampire may utilize this power (on herself or
    others) to form spikes or talons of bone, either on the
    knuckles as an offensive weapon or all over the body
    as defensive “quills.” If bone spikes are used, the vampire
    or victim takes one health level of lethal damage
    (the vampire’s comes from having the very sharp bone
    pierce through his skin — this weaponry doesn’t come
    cheaply). In the case of quills, the subject takes a number
    of health levels equal to five minus the number of
    successes (a botch kills the subject or sends the vampire
    into torpor). These health levels may be healed normally.
    Knuckle spikes inflict Strength +1 lethal damage.
    Defensive quills inflict a hand-to-hand attacker’s
    Strength in lethal damage unless the attacker scores
    three or more successes on the attack roll (in which
    case the attacker takes no damage); the defender still
    takes damage normally. Quills also enable the vampire
    or altered subject to add two to all damage inflicted via
    holds, clinches, or tackles"""
        part2="""A vampire who scores five or more successes on the
    Strength + Medicine roll may cause a rival vampire’s
    rib cage to curve inward and pierce the heart. While
    this does not send a vampire into torpor, it does cause
    the affected vampire to lose half his blood points, as
    the seat of his vitae ruptures in a shower of gore."""
        return part1,part2 
    elif discipline=="vicissitude4":
        part1="""Kindred use this power to become hideous and deadly
    monsters. The vampire’s stature increases to a full
    eight feet (two and a half meters), the skin becomes a
    sickly greenish-gray or grayish-black chitin, the arms
    become apelike and ropy with ragged black nails, and
    the face warps into something out of a nightmare. A
    row of spines sprouts from the vertebrae, and the external
    carapace exudes a foul-smelling grease.

    System: The Horrid Form costs two blood points to
    awaken. All Physical Attributes increase by three, but
    all Social Attributes drop to zero, except when dealing
    with others also in Horrid Form. However, a vampire
    in Horrid Form who is trying to intimidate someone
    may substitute Strength for a Social Attribute. Damage
    inflicted in brawling combat increases by one due
    to the jagged ridges and bony knobs creasing the creature’s
    hands."""
        return part1 
    elif discipline=="vicissitude5":
        part1="""A vampire with this power can physically transform
    all or part of her body into sentient vitae. This blood
    is in all respects identical to the vampire’s normal vitae;
    she can use it to nourish herself or others, create
    ghouls, or establish blood bonds. If all this blood is imbibed
    or otherwise destroyed, the vampire meets Final
    Death.

    System: The vampire may transform all or part of
    herself as she deems fit. Each leg can turn into two
    blood points worth of vitae, as can the torso; each arm,
    the head, and the abdomen convert to one blood point
    each. The blood can be reconverted to the body part,
    provided it is in contact with the vampire. If the blood
    has been utilized or destroyed, the vampire must spend
    a number of blood points equal to what was originally
    created to regrow the missing body part.

    A vampire entirely in this form may not be staked,
    cut, bludgeoned, or pierced, but can be burned or exposed
    to the sun. The vampire may ooze along, drip up
    walls, and flow through the narrowest cracks, as though
    she were in Tenebrous Form (p. 190).

    Mental Disciplines may be used, provided no eye
    contact or vocal utterance is necessary, although the
    vampire can perceive her surroundings just fine (but
    the perceptions are always centered on the largest pool
    of blood). If a vampire in this form “washes” over a
    mortal or animal, that mortal must make a Courage
    roll (difficulty 8) or fly into a panic."""
        return part1 
    elif discipline=="vicissitude6":
        part1="""Similar to Horrid Form, the Chiropteran Marauder
    is a terrifying, bipedal bat, bearing a wickedly fanged
    maw and veined, leathery wings. This power confers all
    of the benefits of the Horrid Form, in addition to a few
    others. The mere sight of the marauder is enough to
    make mortals or weak-willed vampires flee in horror.

    System: The vampire gains all the effects of the Horrid
    Form. Further, the Marauder’s fluted wings allow
    flight at 25 mph (40 kph), during which the vampire
    may carry, but not manipulate, objects no larger than
    it can hold in its hands. If the player chooses to, she
    may make a Strength + Medicine roll (difficulty 6) to
    extend bony claws at the ends of the vampire’s wings.
    These claws inflict Strength +2 aggravated damage.
    Also, the vampire subtracts two from all hearing-based
    Perception rolls (though he adds one to vision- based
    Wits and Perception rolls). Assuming the mantle of
    the Chiropteran Marauder costs three blood points."""
        return part1 

        



