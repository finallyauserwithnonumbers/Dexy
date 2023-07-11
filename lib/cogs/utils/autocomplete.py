from discord.app_commands import Choice
from discord.ext.commands import Cog
from discord import Interaction
import ujson

with open(
    "lib/cogs/pokedexdata/pokemon_stuff_english_only.json", encoding="utf-8"
) as hmm:
    pokedex_dict: dict = ujson.load(hmm)
    id_dict = {}
    for k, v in pokedex_dict.items():
        if id_dict.get(str(v["num"]), None) is None:
            id_dict[str(v["num"])] = (k, v["name"])
    pokemon_names_disp = [v["name"] for v in pokedex_dict.values()]
def pokemon_autocomplete(func):
    async def inner(interaction:Interaction,current:str):
        return [
            Choice(name=pokemon, value=pokemon)
            for pokemon in pokemon_names_disp
            if current.lower() in pokemon.lower()
        ][:25]
    return inner