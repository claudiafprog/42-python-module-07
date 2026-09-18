#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    try:
        num_opponents = len(opponents)
        for i in range(num_opponents):
            for j in range(i + 1, num_opponents):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()
                print("* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print("now fight!")
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
                print()
    except InvalidStrategyError as e:
        print(f"{e}\n")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal_strategy),
        (heal_factory, defensive_strategy)
    ])
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive_strategy),
        (heal_factory, defensive_strategy)
    ])
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal_strategy),
        (heal_factory, defensive_strategy),
        (trans_factory, aggressive_strategy)
    ])


if __name__ == "__main__":
    main()
