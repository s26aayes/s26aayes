import os
from pathlib import Path


def check_conda_env_is_activated(name):
    """Check that a specific conda environment is activated.

    Args:
        name (str): Name of conda environment.

    """
    conda_prefix = os.environ.get("CONDA_PREFIX", None)

    if conda_prefix is None:
        raise AssertionError(
            "No conda environment is activated. Please run the code using an activated "
            "conda environment.",
        )

    env_name = Path(conda_prefix).name
    if name not in env_name:
        msg = f"The conda enviroment is called {env_name}, but should be called 'epp'."
        raise AssertionError(
            msg,
        )

    print(
        f"You have successfully run this code in the '{name}' conda environment. Great "
        "job!",
    )


check_conda_env_is_activated(name="epp")
