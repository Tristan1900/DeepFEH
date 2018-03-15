from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    COLORLESS = auto()

class MovementType(Enum):
    INFANTRY = auto()
    ARMORED = auto()
    CAVALRY = auto()
    FLYING = auto()

class DamageType(Enum):
    PHYSICAL = auto()
    MAGICAL = auto()

class WeaponType(Enum):
    RED_SWORD = auto()
    BLUE_LANCE = auto()
    GREEN_AXE = auto()
    COLORLESS_DAGGER = auto()
    COLORLESS_BOW = auto()
    RED_TOME = auto()
    RED_BREATH = auto()
    BLUE_TOME = auto()
    BLUE_BREATH = auto()
    GREEN_TOME = auto()
    GREEN_BREATH = auto()
    COLORLESS_STAFF = auto()


class PassiveA(Enum):
    EMPTY = auto()
    TRIANGLE_ADEPT_1 = auto()
    TRIANGLE_ADEPT_2 = auto()
    TRIANGLE_ADEPT_3 = auto()


class PassiveB(Enum):
    EMPTY = auto()


class PassiveC(Enum):
    EMPTY = auto()


class PassiveS(Enum):
    EMPTY = auto()


class Special(Enum):
    EMPTY = auto()


class Support(Enum):
    EMPTY = auto()


class Weapon(Enum):
    EMPTY = auto()

    RUBY_SWORD_PLUS = auto()
    RAUTHRRAVEN_PLUS = auto()

    EMERALD_AXE_PLUS = auto()
    GRONNRAVEN_PLUS = auto()

    SAPPHIRE_LANCE_PLUS = auto()
    BLARRAVEN_PLUS = auto()


WEAPON_TO_WEAPON_TYPE = {
    Weapon.EMPTY: WeaponType.COLORLESS_STAFF,
    Weapon.RUBY_SWORD_PLUS: WeaponType.RED_SWORD,
    Weapon.RAUTHRRAVEN_PLUS: WeaponType.RED_TOME,
    Weapon.EMERALD_AXE_PLUS: WeaponType.GREEN_AXE,
    Weapon.GRONNRAVEN_PLUS: WeaponType.GREEN_TOME,
    Weapon.SAPPHIRE_LANCE_PLUS: WeaponType.BLUE_LANCE,
    Weapon.BLARRAVEN_PLUS: WeaponType.GREEN_TOME
}

WEAPON_TYPE_TO_COLOR = {
    WeaponType.RED_SWORD: Color.RED,
    WeaponType.RED_TOME: Color.RED,
    WeaponType.RED_BREATH: Color.RED,
    WeaponType.GREEN_AXE: Color.GREEN,
    WeaponType.GREEN_TOME: Color.GREEN,
    WeaponType.GREEN_BREATH: Color.GREEN,
    WeaponType.BLUE_LANCE: Color.BLUE,
    WeaponType.BLUE_TOME: Color.BLUE,
    WeaponType.BLUE_BREATH: Color.BLUE,
    WeaponType.COLORLESS_BOW: Color.COLORLESS,
    WeaponType.COLORLESS_DAGGER: Color.COLORLESS,
    WeaponType.COLORLESS_STAFF: Color.COLORLESS
}

WEAPON_TYPE_TO_DAMAGE_TYPE = {
    WeaponType.RED_SWORD: DamageType.PHYSICAL,
    WeaponType.GREEN_AXE: DamageType.PHYSICAL,
    WeaponType.BLUE_LANCE: DamageType.PHYSICAL,
    WeaponType.RED_TOME: DamageType.MAGICAL,
    WeaponType.GREEN_TOME: DamageType.MAGICAL,
    WeaponType.BLUE_TOME: DamageType.MAGICAL,
    WeaponType.RED_BREATH: DamageType.MAGICAL,
    WeaponType.GREEN_BREATH: DamageType.MAGICAL,
    WeaponType.BLUE_BREATH: DamageType.MAGICAL,
    WeaponType.COLORLESS_BOW: DamageType.PHYSICAL,
    WeaponType.COLORLESS_DAGGER: DamageType.PHYSICAL,
    WeaponType.COLORLESS_STAFF: DamageType.MAGICAL
}

WEAPON_TYPE_TO_ATTACK_RANGE = {
    WeaponType.RED_SWORD: 1,
    WeaponType.GREEN_AXE: 1,
    WeaponType.BLUE_LANCE: 1,
    WeaponType.RED_TOME: 2,
    WeaponType.GREEN_TOME: 2,
    WeaponType.BLUE_TOME: 2,
    WeaponType.RED_BREATH: 1,
    WeaponType.GREEN_BREATH: 1,
    WeaponType.BLUE_BREATH: 1,
    WeaponType.COLORLESS_BOW: 2,
    WeaponType.COLORLESS_DAGGER: 2,
    WeaponType.COLORLESS_STAFF: 2
}

MOVEMENT_TYPE_TO_MOVEMENT_RANGE = {
    MovementType.INFANTRY: 2,
    MovementType.CAVALRY: 3,
    MovementType.ARMORED: 1,
    MovementType.FLYING: 2
}