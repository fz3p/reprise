from cx_Freeze import setup, Executable

setup(
    name="toolbox_csv",
    version="0.1",
    description="stat on csv",
    executables=[Executable("windows.py")]
)