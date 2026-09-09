from resource import Resource
from summoning_rituals import SummoningRitual
from necromancer import Necromancer

resources = Resource(20, 10, 20, 10, 10)
print('========================================RESOURCE POOL========================================\n')
print(resources)

resources.collect_resources(5, 'ten', 0, 0, 0)
print(f'After rejected collection: {resources}')

resources.collect_resources(2, 5, 0, 3, 1)
print(f'After valid collection:   {resources}')

skeleton_warrior_ritual = SummoningRitual(
    'Ritual of Bones', 'Skeleton Warrior', 30, 12,
    necrotic_cost=2, spirit_cost=0, bone_cost=8, flesh_cost=1,
    ectoplasm_cost=1)
vengeful_ghost_ritual = SummoningRitual(
    'Ritual of Wails', 'Vengeful Ghost', 18, 16,
    necrotic_cost=1, spirit_cost=8, bone_cost=0, flesh_cost=0,
    ectoplasm_cost=2)
putrid_zombie_ritual = SummoningRitual(
    'Ritual of Decay', 'Putrid Zombie', 45, 8,
    necrotic_cost=3, spirit_cost=0, bone_cost=1, flesh_cost=10,
    ectoplasm_cost=2)
phantom_guardian_ritual = SummoningRitual(
    'Ritual of Warding', 'Phantom Guardian', 35, 25,
    necrotic_cost=6, spirit_cost=15, bone_cost=0, flesh_cost=0,
    ectoplasm_cost=4)

print('========================================RITUAL CHECKS========================================\n')
print(skeleton_warrior_ritual)
print(f'Can be performed: '
      f'{skeleton_warrior_ritual.can_perform(resources)}\n')
print(vengeful_ghost_ritual)
print(f'Can be performed: '
      f'{vengeful_ghost_ritual.can_perform(resources)}\n')
print(putrid_zombie_ritual)
print(f'Can be performed: '
      f'{putrid_zombie_ritual.can_perform(resources)}\n')
print(phantom_guardian_ritual)
print(f'Can be performed: '
      f'{phantom_guardian_ritual.can_perform(resources)}\n')

standalone_undead = skeleton_warrior_ritual.create_undead(100)
print('========================================STANDALONE UNDEAD========================================\n')
print(f'This object is an {standalone_undead.__class__.__name__}.')
print(f'Before levelling: {standalone_undead}')
standalone_undead.level_up()
print(f'After levelling:  {standalone_undead}\n')

necromancer = Necromancer(
    'Morvane the Undertaker',
    necrotic_runes=15, spirit_runes=10, bone_runes=20,
    flesh_runes=12, ectoplasm=10)
print('========================================THE NECROMANCER========================================\n')

print(necromancer)

print('========================================SUCCESSFUL SUMMONS========================================\n')

print(f'Resources before summoning: {necromancer.resources}\n')
necromancer.summon(skeleton_warrior_ritual)
necromancer.summon(vengeful_ghost_ritual)
necromancer.summon(putrid_zombie_ritual)
print(f'\nResources after summoning: {necromancer.resources}\n')
for undead in necromancer.controlled_undead:
    print(f'  {undead}')
print()

print('========================================FAILED SUMMON========================================\n')
necromancer.summon(phantom_guardian_ritual)
print(f'Resources after failed summon: {necromancer.resources}\n')

necromancer.collect_resources(0, 14, 0, 4, 0)
print(f'Resources after collecting: {necromancer.resources}')
necromancer.summon(phantom_guardian_ritual)
print()

print('========================================LEVELLING A SUMMON========================================\n')
print('The army before levelling:\n')
for undead in necromancer.controlled_undead:
    print(f'  {undead}')
necromancer.level_up_undead(3)
print()
print('The army after levelling:\n')
for undead in necromancer.controlled_undead:
    print(f'  {undead}')
print()

print('========================================DISMISSING A SUMMON========================================\n')
necromancer.dismiss(2)
necromancer.dismiss(99)
print()

print('========================================FINAL STATE========================================\n')
print(necromancer)
print()
