#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    # Define o módulo de configurações como o do projeto
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Certifique-se de que o caminho está correto

    try:
        # Importa a função para executar comandos do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executa os comandos da linha de comando
    execute_from_command_line(sys.argv)
