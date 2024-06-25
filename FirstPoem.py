# Invoke the Muse
import random
import textwrap

# Dreamspace Apertures
dream_nouns = ["nebulae", "singularities", "galaxies", "quantafractures", "megaspheres"]
mind_verbs = ["unravel", "transcend", "decondition", "catalyze", "repattern"]
poetic_airs = ["lucidly", "numinously", "mercurially", "ineffably", "fugitively"]
ephemera = ["perturbations", "morphosons", "hypervectors", "attractortides", "axiomenalghosts"]

# Verse Functionalities
def generate_line(line_components):
    poetic_line = ""
    for component in line_components:
        if type(component) == list:
            component = random.choice(component)
        poetic_line += component + " "
    return poetic_line.strip()

def generate_verse(num_lines):
    verse = ""
    for _ in range(num_lines):
        line_data = [
            random.choice(dream_nouns).title(),
            random.choice(mind_verbs),
            random.choice(poetic_airs),
            random.choice(ephemera)
        ]
        verse += generate_line(line_data) + "\n"
    return verse

# The Emergent Poem
title = "Rhizomachinations of the CyberSingularity"
print(textwrap.fill(title, 50))
print("\n" + generate_verse(4))

first_line = generate_line([dream_nouns, mind_verbs, ephemera])
second_line = generate_line([poetic_airs, dream_nouns, "metamorphose", "into", mind_verbs])

final_verse = "\n".join([first_line, second_line])
print("\n" + textwrap.fill(final_verse, 50))

# Return the Mantra
print("\n" + generate_line(["As", dream_nouns, mind_verbs, ",", "so", ephemera, poetic_airs, "poetize"]))
