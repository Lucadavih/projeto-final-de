import yaml


def load_configs():
    """
    Carrega arquivo de configuração YAML.
    """
    with open("assets/config.yml", "r") as file:
        configs = yaml.safe_load(file)

    return configs


# variável esperada pelo app.py
configs = load_configs()
