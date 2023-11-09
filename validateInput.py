{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOA05qfZNhW1fZ55y3bi7nI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JonathanFerreiraDeLima/Automatize-Tarefas/blob/main/validateInput.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TONtLF9k2dmh",
        "outputId": "92498494-fe5b-49c1-ef70-06817766b8b8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter your age:\n",
            "trinta\n",
            "Please enter a number for your age.\n",
            "Enter your age:\n",
            "28\n",
            "Select a new password (letters and numbers only):\n",
            "John14@\n",
            "Passwords can only have letters and numbers.\n",
            "Select a new password (letters and numbers only):\n",
            "John14\n"
          ]
        }
      ],
      "source": [
        "while True:\n",
        "  print('Enter your age:')\n",
        "  age = input()\n",
        "  if age.isdecimal():\n",
        "    break\n",
        "  print('Please enter a number for your age.')\n",
        "\n",
        "while True:\n",
        "  print('Select a new password (letters and numbers only):')\n",
        "  password = input()\n",
        "  if password.isalnum():\n",
        "    break\n",
        "  print('Passwords can only have letters and numbers.')"
      ]
    }
  ]
}