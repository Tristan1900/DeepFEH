from feh_simulator import skill


class Unit(object):
    cnt = 0

    def __init__(self, index=0, team=0,

                 max_hp: int = 40,
                 atk: int = 30,
                 spd: int = 36,
                 defence: int = 25,
                 res: int = 26,
                 movement_type=skill.MovementType.INFANTRY,
                 passive_a=skill.PassiveA.EMPTY,
                 passive_b=skill.PassiveB.EMPTY,
                 passive_c=skill.PassiveC.EMPTY,
                 passive_s=skill.PassiveS.EMPTY,
                 weapon=skill.Weapon.RUBY_SWORD_PLUS,
                 support=skill.Support.EMPTY,
                 special=skill.Special.EMPTY):
        self.id = Unit.cnt
        Unit.cnt += 1

        self.index: int = index
        self.max_hp: int = max_hp
        self.cur_hp: int = self.max_hp

        self.atk: int = atk
        self.spd: int = spd
        self.defence: int = defence
        self.res: int = res

        self.movement_type = movement_type
        self.weapon = weapon
        self.support = support
        self.special = special
        self.passive_a = passive_a
        self.passive_b = passive_b
        self.passive_c = passive_c
        self.passive_s = passive_s

        self.weapon_type = skill.WEAPON_TO_WEAPON_TYPE[self.weapon]
        self.color = skill.WEAPON_TYPE_TO_COLOR[self.weapon_type]
        self.attack_range = skill.WEAPON_TYPE_TO_ATTACK_RANGE[self.weapon_type]
        self.damage_type = skill.WEAPON_TYPE_TO_DAMAGE_TYPE[self.weapon_type]
        self.movement_range = skill.MOVEMENT_TYPE_TO_MOVEMENT_RANGE[self.movement_type]

        self.is_dead: bool = 0
        self.team: int = team
        return

    def get_attributes(self):
        return self.max_hp, self.cur_hp, self.atk, self.spd, self.defence, self.res, self.attack_range, self.movement_range
