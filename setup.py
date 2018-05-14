from cx_Freeze import setup, Executable

setup(
    name = "game",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable('test2.py')]
)