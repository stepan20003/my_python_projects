from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        diference = end - start
        print(f"Spell completed in {diference:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable | str:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def dec(func: Callable) -> Callable:
        @wraps(func)
        def wraper(*args, **kwargs) -> str | Callable:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt"
                          f" {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wraper
    return dec


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and isinstance(name, str) and all(
                char.isalpha() or char.isspace() for char in name):
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast"
    result = fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")
    dec = retry_spell(3)

    @dec
    def seppl() -> None:
        raise ValueError()
    print(seppl())
    print("Waaaaaaagh spelled !")
    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("HelloWorld"))
    print(MageGuild.validate_mage_name("$"))
    x = MageGuild()
    print(f"{x.cast_spell('Lightning', power = 15)}")
    print(f"{x.cast_spell('Lightning', power = 1)}")
