# DataDeck — Abstract Card Architecture

Master Python's design patterns with abstract classes, mixins/interfaces, and modular card systems.

---

## 📁 Repository Structure

```text
├── battle.py                  # Test script for Exercise 0
├── capacitor.py               # Test script for Exercise 1
├── tournament.py              # Test script for Exercise 2
├── ex0/
│   ├── __init__.py            # Exposes ONLY factories
│   └── ...                    # Creature abstract class, concrete cards, factories
├── ex1/
│   ├── __init__.py            # Exposes ONLY healing/transform factories
│   └── ...                    # Capabilities + healing/transform creatures
└── ex2/
    ├── __init__.py            # Exposes strategies and/or tournament components
    └── ...                    # BattleStrategy, Normal/Aggressive/Defensive strategies
```

# 🛠️ General Rules & Requirements
* Python: 3.10+
* Standards: flake8 compliant, comprehensive type annotations (mypy ready).
* Restrictions: No eval() / exec(), no external libraries (stdlib only: typing, abc, etc.).
* Exports: Packages (ex0, ex1) must not expose concrete Creature classes directly—only factory classes!

# 📦 Exercise Breakdown
## Exercise 0: Creature Factory (ex0/, battle.py)
* Pattern: Abstract Factory.
* Key Components:
  *  Creature (abstract): attributes name, type; methods describe(), abstract attack().
  *  Concrete creatures: Flameling, Pyrodon, Aquabub, Torragon.
  *  CreatureFactory (abstract): methods create_base(), create_evolved().
  *  Concrete factories: FlameFactory, AquaFactory.
* Test: python3 battle.py

## Exercise 1: Capabilities (ex1/, capacitor.py)
* Pattern: Composition/Mix-in style separate capability interfaces.
* Key Components:
  *  HealCapability (abstract): method heal().
  *  TransformCapability (abstract): methods transform(), revert(), state tracking affecting attack().
  *  Concrete dual-inheritance classes:
     -  Sproutling, Bloomelle + HealingCreatureFactory
     - Shiftling, Morphagon + TransformCreatureFactory
* Test: python3 capacitor.py

## Exercise 2: Abstract Strategy (ex2/, tournament.py)
* Pattern: Strategy Pattern.
* Key Components:
  *  BattleStrategy (abstract): methods act(), is_valid(creature).
  *  Concrete strategies:
     - NormalStrategy: calls attack().
     - AggressiveStrategy: transform $\rightarrow$ attack $\rightarrow$ revert (valid for transform capability).
     - DefensiveStrategy: attack $\rightarrow$ heal (valid for healing capability).
   * Validation + custom exception handling for invalid strategy-creature pairs.
* Test: python3 tournament.py

# 🚀 Quick Start / VerificationBash# Type checking & linting check (recommended)

mypy .
flake8 .

# Run test suites
python3 battle.py
python3 capacitor.py
python3 tournament.py
