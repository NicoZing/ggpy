from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy

CRAYON_COLORS = {
    "red": "#ed0a3f",
    "maroon": "#c32148",
    "scarlet": "#fd0e35",
    "brick red": "#c62d42",
    "english vermilion": "#cc474b",
    "madder lake": "#cc3336",
    "permanent geranium lake": "#e12c2c",
    "maximum red": "#d92121",
    "indian red": "#b94e48",
    "orange-red": "#ff5349",
    "sunset orange": "#fe4c40",
    "bittersweet": "#fe6f5e",
    "dark venetian red": "#b33b24",
    "venetian red": "#cc553d",
    "light venetian red": "#e6735c",
    "vivid tangerine": "#ff9980",
    "middle red": "#e58e73",
    "burnt orange": "#ff7f49",
    "red-orange": "#ff681f",
    "orange": "#ff8833",
    "macaroni and cheese": "#ffb97b",
    "middle yellow red": "#ecb176",
    "mango tango": "#e77200",
    "yellow-orange": "#ffae42",
    "maximum yellow red": "#f2ba49",
    "banana mania": "#fbe7b2",
    "maize": "#f2c649",
    "orange-yellow": "#f8d568",
    "goldenrod": "#fcd667",
    "dandelion": "#fed85d",
    "yellow": "#fbe870",
    "green-yellow": "#f1e788",
    "middle yellow": "#ffeb00",
    "olive green": "#b5b35c",
    "spring green": "#ecebbd",
    "maximum yellow": "#fafa37",
    "canary": "#ffff99",
    "lemon yellow": "#ffff9f",
    "maximum green yellow": "#d9e650",
    "middle green yellow": "#acbf60",
    "inchworm": "#afe313",
    "light chrome green": "#bee64b",
    "yellow-green": "#c5e17a",
    "maximum green": "#5e8c31",
    "asparagus": "#7ba05b",
    "granny smith apple": "#9de093",
    "fern": "#63b76c",
    "middle green": "#4d8c57",
    "green": "#3aa655",
    "medium chrome green": "#6ca67c",
    "forest green": "#5fa777",
    "sea green": "#93dfb8",
    "shamrock": "#33cc99",
    "mountain meadow": "#1ab385",
    "jungle green": "#29ab87",
    "caribbean green": "#00cc99",
    "tropical rain forest": "#00755e",
    "middle blue green": "#8dd9cc",
    "pine green": "#01786f",
    "maximum blue green": "#30bfbf",
    "robin's egg blue": "#00cccc",
    "teal blue": "#008080",
    "light blue": "#8fd8d8",
    "aquamarine": "#95e0e8",
    "turquoise blue": "#6cdae7",
    "outer space": "#2d383a",
    "sky blue": "#76d7ea",
    "middle blue": "#7ed4e6",
    "blue-green": "#0095b7",
    "pacific blue": "#009dc4",
    "cerulean": "#02a4d3",
    "maximum blue": "#47abcc",
    "blue1": "#4997d0",
    "cerulean blue": "#339acc",
    "cornflower": "#93ccea",
    "green-blue": "#2887c8",
    "midnight blue": "#00468c",
    "navy blue": "#0066cc",
    "denim": "#1560bd",
    "blue3": "#0066ff",
    "cadet blue": "#a9b2c3",
    "periwinkle": "#c3cde6",
    "blue2": "#4570e6",
    "wild blue yonder": "#7a89b8",
    "indigo": "#4f69c6",
    "manatee": "#8d90a1",
    "cobalt blue": "#8c90c8",
    "celestial blue": "#7070cc",
    "blue bell": "#9999cc",
    "maximum blue purple": "#acace6",
    "violet-blue": "#766ec8",
    "blue-violet": "#6456b7",
    "ultramarine blue": "#3f26bf",
    "middle blue purple": "#8b72be",
    "purple heart": "#652dc1",
    "royal purple": "#6b3fa0",
    "violet2": "#8359a3",
    "medium violet": "#8f47b3",
    "wisteria": "#c9a0dc",
    "lavender1": "#bf8fcc",
    "vivid violet": "#803790",
    "maximum purple": "#733380",
    "purple mountains' majesty": "#d6aedd",
    "fuchsia": "#c154c1",
    "pink flamingo": "#fc74fd",
    "violet1": "#732e6c",
    "brilliant rose": "#e667ce",
    "orchid": "#e29cd2",
    "plum": "#8e3179",
    "medium rose": "#d96cbe",
    "thistle": "#ebb0d7",
    "mulberry": "#c8509b",
    "red-violet": "#bb3385",
    "middle purple": "#d982b5",
    "maximum red purple": "#a63a79",
    "jazzberry jam": "#a50b5e",
    "eggplant": "#614051",
    "magenta": "#f653a6",
    "cerise": "#da3287",
    "wild strawberry": "#ff3399",
    "lavender2": "#fbaed2",
    "cotton candy": "#ffb7d5",
    "carnation pink": "#ffa6c9",
    "violet-red": "#f7468a",
    "razzmatazz": "#e30b5c",
    "pig pink": "#fdd7e4",
    "carmine": "#e62e6b",
    "blush": "#db5079",
    "tickle me pink": "#fc80a5",
    "mauvelous": "#f091a9",
    "salmon": "#ff91a4",
    "middle red purple": "#a55353",
    "mahogany": "#ca3435",
    "melon": "#febaad",
    "pink sherbert": "#f7a38e",
    "burnt sienna": "#e97451",
    "brown": "#af593e",
    "sepia": "#9e5b40",
    "fuzzy wuzzy": "#87421f",
    "beaver": "#926f5b",
    "tumbleweed": "#dea681",
    "raw sienna": "#d27d46",
    "van dyke brown": "#664228",
    "tan": "#d99a6c",
    "desert sand": "#edc9af",
    "peach": "#ffcba4",
    "burnt umber": "#805533",
    "apricot": "#fdd5b1",
    "almond": "#eed9c4",
    "raw umber": "#665233",
    "shadow": "#837050",
    "raw sienna1": "#e6bc5c",
    "timberwolf": "#d9d6cf",
    "gold1": "#92926e",
    "gold2": "#e6be8a",
    "silver": "#c9c0bb",
    "copper": "#da8a67",
    "antique brass": "#c88a65",
    "black": "#000000",
    "charcoal gray": "#736a62",
    "gray": "#8b8680",
    "blue-gray": "#c8c8cd",
    "radical red": "#ff355e",
    "wild watermelon": "#fd5b78",
    "outrageous orange": "#ff6037",
    "atomic tangerine": "#ff9966",
    "neon carrot": "#ff9933",
    "sunglow": "#ffcc33",
    "laser lemon": "#ffff66",
    "unmellow yellow": "#ffff66",
    "electric lime": "#ccff00",
    "screamin' green": "#66ff66",
    "magic mint": "#aaf0d1",
    "blizzard blue": "#50bfe6",
    "shocking pink": "#ff6eff",
    "razzle dazzle rose": "#ee34d2",
    "hot magenta": "#ff00cc",
    "purple pizzazz": "#ff00cc",
    "sizzling red": "#ff3855",
    "red salsa": "#fd3a4a",
    "tart orange": "#fb4d46",
    "orange soda": "#fa5b3d",
    "bright yellow": "#ffaa1d",
    "yellow sunshine": "#fff700",
    "slimy green": "#299617",
    "green lizard": "#a7f432",
    "denim blue": "#2243b6",
    "blue jeans": "#5dadec",
    "plump purple": "#5946b2",
    "purple plum": "#9c51b6",
    "sweet brown": "#a83731",
    "brown sugar": "#af6e4d",
    "eerie black": "#1b1b1b",
    "black shadows": "#bfafb2",
    "fiery rose": "#ff5470",
    "sizzling sunrise": "#ffdb00",
    "heat wave": "#ff7a00",
    "lemon glacier": "#fdff00",
    "spring frost": "#87ff2a",
    "absolute zero": "#0048ba",
    "winter sky": "#ff007c",
    "frostbite": "#e936a7",
    "alloy orange": "#c46210",
    "b'dazzled blue": "#2e5894",
    "big dip o' ruby": "#9c2542",
    "bittersweet shimmer": "#bf4f51",
    "blast off bronze": "#a57164",
    "cyber grape": "#58427c",
    "deep space sparkle": "#4a646c",
    "gold fusion": "#85754e",
    "illuminating emerald": "#319177",
    "metallic seaweed": "#0a7e8c",
    "metallic sunburst": "#9c7c38",
    "razzmic berry": "#8d4e85",
    "sheen green": "#8fd400",
    "shimmering blush": "#d98695",
    "sonic silver": "#757575",
    "steel blue": "#0081ab",
    "aztec gold": "#c39953",
    "burnished brown": "#a17a74",
    "cerulean frost": "#6d9bc3",
    "cinnamon satin": "#cd607e",
    "copper penny": "#ad6f69",
    "cosmic cobalt": "#2e2d88",
    "glossy grape": "#ab92b3",
    "granite gray": "#676767",
    "green sheen": "#6eaea1",
    "lilac luster": "#ae98aa",
    "misty moss": "#bbb477",
    "mystic maroon": "#ad4379",
    "pearly purple": "#b768a2",
    "pewter blue": "#8ba8b7",
    "polished pine": "#5da493",
    "quick silver": "#a6a6a6",
    "rose dust": "#9e5e6f",
    "rusty red": "#da2c43",
    "shadow blue": "#778ba5",
    "shiny shamrock": "#5fa778",
    "steel teal": "#5f8a8b",
    "sugar plum": "#914e75",
    "twilight lavender": "#8a496b",
    "wintergreen dream": "#56887d",
    "baby powder": "#fefefa",
    "banana": "#ffd12a",
    "blueberry": "#4f86f7",
    "bubble gum": "#ffd3f8",
    "cedar chest": "#c95a49",
    "cherry": "#da2647",
    "chocolate": "#bd8260",
    "coconut": "#fefefe",
    "daffodil": "#ffff31",
    "eucalyptus": "#44d7a8",
    "fresh air": "#a6e7ff",
    "grape": "#6f2da8",
    "jelly bean": "#da614e",
    "leather jacket": "#253529",
    "lemon": "#ffff38",
    "licorice": "#1a1110",
    "lilac": "#db91ef",
    "lime": "#b2f302",
    "lumber": "#ffe4cd",
    "new car": "#214fc6",
    "orange": "#ff8866",
    "peach": "#ffd0b9",
    "pine": "#45a27d",
    "rose": "#ff5050",
    "shampoo": "#ffcff1",
    "smoke": "#738276",
    "soap": "#cec8ef",
    "strawberry": "#fc5a8d",
    "tulip": "#ff878d",
    "amethyst": "#64609a",
    "citrine": "#933709",
    "emerald": "#14a989",
    "jade": "#469a84",
    "jasper": "#d05340",
    "lapis lazuli": "#436cb9",
    "malachite": "#469496",
    "moonstone": "#3aa8c1",
    "onyx": "#353839",
    "peridot": "#abad48",
    "pink pearl": "#b07080",
    "rose quartz": "#bd559c",
    "ruby": "#aa4069",
    "sapphire": "#2d5da1",
    "smokey topaz": "#832a0d",
    "tiger's eye": "#b56917",
    "baseball mitt": "#e97451",
    "bubble bath": "#fc80a5",
    "earthworm": "#c62d42",
    "flower shop": "#c9a0dc",
    "fresh air": "#76d7ea",
    "grandma's perfume": "#ff8833",
    "koala tree": "#29ab87",
    "pet shop": "#af593e",
    "pine tree": "#01786f",
    "saw dust": "#ffcba4",
    "sharpening pencils": "#fcd667",
    "smell the roses": "#ed0a3f",
    "sunny day": "#fbe870",
    "wash the dog": "#fed85d",
    "alien armpit": "#84de02",
    "big foot feet": "#e88e5a",
    "booger buster": "#dde26a",
    "dingy dungeon": "#c53151",
    "gargoyle gas": "#ffdf46",
    "giant's club": "#b05c52",
    "magic potion": "#ff4466",
    "mummy's tomb": "#828e84",
    "ogre odor": "#fd5240",
    "pixie powder": "#391285",
    "princess perfume": "#ff85cf",
    "sasquatch socks": "#ff4681",
    "sea serpent": "#4bc7cf",
    "smashed pumpkin": "#ff6d3a",
    "sunburnt cyclops": "#ff404c",
    "winter wizard": "#a0e6f"
}


class scale_color_crayon(scale):
    """
    Examples
    --------
    >>> from ggplot import *
    >>> import pandas as pd
    >>> df = pd.DataFrame(dict(x=range(3), y=range(3), crayon=['sunset orange', 'inchworm', 'cadet blue']))
    >>> p = ggplot(aes(x='x', y='y', color='crayon'), data=df)
    >>> p += geom_point(size=250)
    >>> print(p + scale_color_crayon())
    """
    VALID_SCALES = []

    def __radd__(self, gg):
        colors = sorted(gg.data[gg._aes['color']].unique())
        gg.manual_color_list = []
        for color in colors:
            new_color = CRAYON_COLORS.get(color.lower())
            if not new_color:
                raise Exception("Color not found: %s" % color)
            gg.manual_color_list.append(new_color)
        return gg
