from enum import Enum


class Expansion(Enum):
    NONE = ''
    ORGANIZER = 'organizer'
    GAME = 'game'


class MatchType(Enum):
    ALL = 'all'
    UPCOMING = 'upcoming'
    ONGOING = 'ongoing'
    PAST = 'past'


class Region(Enum):
    EU = 'EU'
    US = 'US'
    SEA = 'SEA'
    OCEANIA = 'Oceania'
    SA = 'SA'


class Country(Enum):
    AFGHANISTAN = 'AF'
    ALAND_ISLANDS = 'AX'
    ALBANIA = 'AL'
    ALGERIA = 'DZ'
    AMERICAN_SAMOA = 'AS'
    ANDORRA = 'AD'
    ANGOLA = 'AO'
    ANGUILLA = 'AI'
    ANTARCTICA = 'AQ'
    ANTIGUA_AND_BARBUDA = 'AG'
    ARGENTINA = 'AR'
    ARMENIA = 'AM'
    ARUBA = 'AW'
    AUSTRALIA = 'AU'
    AUSTRIA = 'AT'
    AZERBAIJAN = 'AZ'
    BAHAMAS = 'BS'
    BAHRAIN = 'BH'
    BANGLADESH = 'BD'
    BARBADOS = 'BB'
    BELARUS = 'BY'
    BELGIUM = 'BE'
    BELIZE = 'BZ'
    BENIN = 'BJ'
    BERMUDA = 'BM'
    BHUTAN = 'BT'
    BOLIVIA = 'BO'
    BONAIRE = 'BQ'
    BOSNIA_AND_HERZEGOVINA = 'BA'
    BOTSWANA = 'BW'
    BOUVET_ISLAND = 'BV'
    BRAZIL = 'BR'
    BRITISH_INDIAN_OCEAN_TERRITORY = 'IO'
    BRUNEI_DARUSSALAM = 'BN'
    BULGARIA = 'BG'
    BURKINA_FASO = 'BF'
    BURUNDI = 'BI'
    CAMBODIA = 'KH'
    CAMEROON = 'CM'
    CANADA = 'CA'
    CABO_VERDE = 'CV'
    CAYMAN_ISLANDS = 'KY'
    CENTRAL_AFRICAN_REPUBLIC = 'CF'
    CHAD = 'TD'
    CHILE = 'CL'
    CHINA = 'CN'
    CHRISTMAS_ISLAND = 'CX'
    COCOS_ISLANDS = 'CC'
    COLOMBIA = 'CO'
    COMOROS = 'KM'
    CONGO = 'CG'
    DEMOCRATIC_REPUBLIC_OF_THE_CONGO = 'CD'
    COOK_ISLANDS = 'CK'
    COSTA_RICA = 'CR'
    COTE_D_IVOIRE = 'CI'
    CROATIA = 'HR'
    CUBA = 'CU'
    CURACAO = 'CW'
    CYPRUS = 'CY'
    CZECH_REPUBLIC = 'CZ'
    DENMARK = 'DK'
    DJIBOUTI = 'DJ'
    DOMINICA = 'DM'
    DOMINICAN_REPUBLIC = 'DO'
    ECUADOR = 'EC'
    EGYPT = 'EG'
    EL_SALVADOR = 'SV'
    EQUATORIAL_GUINEA = 'GQ'
    ERITREA = 'ER'
    ESTONIA = 'EE'
    ETHIOPIA = 'ET'
    FALKLAND_ISLANDS = 'FK'
    FAROE_ISLANDS = 'FO'
    FIJI = 'FJ'
    FINLAND = 'FI'
    FRANCE = 'FR'
    FRENCH_GUIANA = 'GF'
    FRENCH_POLYNESIA = 'PF'
    FRENCH_SOUTHERN_TERRITORIES = 'TF'
    GABON = 'GA'
    GAMBIA = 'GM'
    GEORGIA = 'GE'
    GERMANY = 'DE'
    GHANA = 'GH'
    GIBRALTAR = 'GI'
    GREECE = 'GR'
    GREENLAND = 'GL'
    GRENADA = 'GD'
    GUADELOUPE = 'GP'
    GUAM = 'GU'
    GUATEMALA = 'GT'
    GUERNSEY = 'GG'
    GUINEA = 'GN'
    GUINEA_BISSAU = 'GW'
    GUYANA = 'GY'
    HAITI = 'HT'
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HM'
    HOLY_SEE = 'VA'
    HONDURAS = 'HN'
    HONG_KONG = 'HK'
    HUNGARY = 'HU'
    ICELAND = 'IS'
    INDIA = 'IN'
    INDONESIA = 'ID'
    IRAN = 'IR'
    IRAQ = 'IQ'
    IRELAND = 'IE'
    ISLE_OF_MAN = 'IM'
    ISRAEL = 'IL'
    ITALY = 'IT'
    JAMAICA = 'JM'
    JAPAN = 'JP'
    JERSEY = 'JE'
    JORDAN = 'JO'
    KAZAKHSTAN = 'KZ'
    KENYA = 'KE'
    KIRIBATI = 'KI'
    DEMOCRATIC_PEOPLES_REPUBLIC_OF_KOREA = 'KP'
    REPUBLIC_OF_KOREA = 'KR'
    KUWAIT = 'KW'
    KYRGYZSTAN = 'KG'
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LA'
    LATVIA = 'LV'
    LEBANON = 'LB'
    LESOTHO = 'LS'
    LIBERIA = 'LR'
    LIBYA = 'LY'
    LIECHTENSTEIN = 'LI'
    LITHUANIA = 'LT'
    LUXEMBOURG = 'LU'
    MACAO = 'MO'
    MACEDONIA = 'MK'
    MADAGASCAR = 'MG'
    MALAWI = 'MW'
    MALAYSIA = 'MY'
    MALDIVES = 'MV'
    MALI = 'ML'
    MALTA = 'MT'
    MARSHALL_ISLANDS = 'MH'
    MARTINIQUE = 'MQ'
    MAURITANIA = 'MR'
    MAURITIUS = 'MU'
    MAYOTTE = 'YT'
    MEXICO = 'MX'
    MICRONESIA = 'FM'
    MOLDOVA = 'MD'
    MONACO = 'MC'
    MONGOLIA = 'MN'
    MONTENEGRO = 'ME'
    MONTSERRAT = 'MS'
    MOROCCO = 'MA'
    MOZAMBIQUE = 'MZ'
    MYANMAR = 'MM'
    NAMIBIA = 'NA'
    NAURU = 'NR'
    NEPAL = 'NP'
    NETHERLANDS = 'NL'
    NEW_CALEDONIA = 'NC'
    NEW_ZEALAND = 'NZ'
    NICARAGUA = 'NI'
    NIGER = 'NE'
    NIGERIA = 'NG'
    NIUE = 'NU'
    NORFOLK_ISLAND = 'NF'
    NORTHERN_MARIANA_ISLANDS = 'MP'
    NORWAY = 'NO'
    OMAN = 'OM'
    PAKISTAN = 'PK'
    PALAU = 'PW'
    STATE_OF_PALESTINE = 'PS'
    PANAMA = 'PA'
    PAPUA_NEW_GUINEA = 'PG'
    PARAGUAY = 'PY'
    PERU = 'PE'
    PHILIPPINES = 'PH'
    PITCAIRN = 'PN'
    POLAND = 'PL'
    PORTUGAL = 'PT'
    PUERTO_RICO = 'PR'
    QATAR = 'QA'
    REUNION = 'RE'
    ROMANIA = 'RO'
    RUSSIAN_FEDERATION = 'RU'
    RWANDA = 'RW'
    SAINT_BARTHELEMY = 'BL'
    SAINT_HELENA_ASCENSION_AND_TRISTAN_DA_CUNHA = 'SH'
    SAINT_KITTS_AND_NEVIS = 'KN'
    SAINT_LUCIA = 'LC'
    SAINT_MARTIN_FENCH = 'MF'
    SAINT_PIERRE_AND_MIQUELON = 'PM'
    SAINT_VINCENT_AND_THE_GRENADINES = 'VC'
    SAMOA = 'WS'
    SAN_MARINO = 'SM'
    SAO_TOME_AND_PRINCIPE = 'ST'
    SAUDI_ARABIA = 'SA'
    SENEGAL = 'SN'
    SERBIA = 'RS'
    SEYCHELLES = 'SC'
    SIERRA_LEONE = 'SL'
    SINGAPORE = 'SG'
    SINT_MAARTEN_DUTCH = 'SX'
    SLOVAKIA = 'SK'
    SLOVENIA = 'SI'
    SOLOMON_ISLANDS = 'SB'
    SOMALIA = 'SO'
    SOUTH_AFRICA = 'ZA'
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'GS'
    SOUTH_SUDAN = 'SS'
    SPAIN = 'ES'
    SRI_LANKA = 'LK'
    SUDAN = 'SD'
    SURINAME = 'SR'
    SVALBARD_AND_JAN_MAYEN = 'SJ'
    SWAZILAND = 'SZ'
    SWEDEN = 'SE'
    SWITZERLAND = 'CH'
    SYRIAN_ARAB_REPUBLIC = 'SY'
    TAIWAN = 'TW'
    TAJIKISTAN = 'TJ'
    TANZANIA = 'TZ'
    THAILAND = 'TH'
    TIMOR_LESTE = 'TL'
    TOGO = 'TG'
    TOKELAU = 'TK'
    TONGA = 'TO'
    TRINIDAD_AND_TOBAGO = 'TT'
    TUNISIA = 'TN'
    TURKEY = 'TR'
    TURKMENISTAN = 'TM'
    TURKS_AND_CAICOS_ISLANDS = 'TC'
    TUVALU = 'TV'
    UGANDA = 'UG'
    UKRAINE = 'UA'
    UNITED_ARAB_EMIRATES = 'AE'
    UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND = 'GB'
    UNITED_STATES_OF_AMERICA = 'US'
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UM'
    URUGUAY = 'UY'
    UZBEKISTAN = 'UZ'
    VANUATU = 'VU'
    VENEZUELA = 'VE'
    VIET_NAM = 'VN'
    VIRGIN_ISLANDS_BRITISH = 'VG'
    VIRGIN_ISLANDS_US = 'VI'
    WALLIS_AND_FUTUNA = 'WF'
    WESTERN_SAHARA = 'EH'
    YEMEN = 'YE'
    ZAMBIA = 'ZM'
    ZIMBABWE = 'ZW'


class Game(Enum):
    RL_XBOX_PC = 'rl_XBOX_PC'
    WOT_XBOX = 'wot_xbox'
    WOT_NA = 'wot_NA'
    WOT_RU = 'wot_RU'
    WOT_EU = 'wot_EU'
    SMITE_XBOX = 'smite_xbox'
    SMITE = 'smite'
    DIRTY_BOMB = 'dirtybomb'
    NHL_20_XBOX = 'nhl_20_xbox'
    NHL_19_XBOX = 'nhl_19_XBOX'
    NHL_18_XBOX = 'nhl_18_XBOX'
    NHL_20_PS4 = 'nhl_20_ps4'
    NHL_19_PS4 = 'nhl_19_PS4'
    NHL_18_PS4 = 'nhl_18_PS4'
    NHL_19 = 'nhl_19'
    NHL_20 = 'nhl_20_parent'
    APEX = 'apex'
    MINION_MASTERS = 'minion_masters'
    HALO_3 = 'halo_3'
    HALO_5_XBOX = 'halo_5'
    HALO_INFINITE = 'halo_infinite'
    HALO_MCC = 'halo_mcc'
    RAINBOW6S_PS4 = 'gs_rainbow_6_ps4'
    RAINBOW6S_XBOX = 'gs_rainbow_6_xbox'
    RAINBOW6S_PC = 'gs_rainbow_6'
    RAINBOW6S = 'rainbow_6'
    WARFACE_EU = 'warface_eu'
    WARFACE_NA = 'warface_na'
    WARFACE_ALPHA = 'warface_alpha'
    WARFACE_PARENT = 'warface_parent'
    WARFACE = 'warface'
    BRAWL_STARS_AUTO = 'brawl_stars_auto'
    BRAWL_STARS = 'brawl_stars'
    OVERWATCH_EU = 'overwatch_EU'
    OVERWATCH_US = 'overwatch_US'
    OVERWATCH_KR = 'overwatch_KR'
    OVERWATCH = 'overwatch'
    CLASH_ROYALE_AUTO = 'clash_royale_auto'
    CLASH_ROYALE = 'clash_royale'
    DESTINY_2_XBOX = 'destiny2_xbox'
    DESTINY_2_PS4 = 'destiny2_ps4'
    DESTINY_2_PC = 'destiny2'
    DESTINY_2 = 'destiny2_parent'
    LOL_TR = 'lol_TR'
    LOL_EUN = 'lol_EUN'
    LOL_EUW = 'lol_EUW'
    LOL_OCE = 'lol_OCE'
    LOL_BR = 'lol_BR'
    LOL_LAN = 'lol_LAN'
    LOL_LAS = 'lol_LAS'
    LOL_NA = 'lol_NA'
    LOL = 'Wild'
    LOL_PARENT = 'lol_parent'
    KRUNKER = 'krunker'
    RING_OF_ELYSIUM = 'ring_of_elysium'
    TF2 = 'tf2'
    CS_DZ = 'csdz'
    VALORANT = 'valorant'
    DOTA_2 = 'dota2'
    TEMPERIA = 'temperia'
    HS_BATTLEGROUNDS = 'hearthstone-battlegrounds'
    FIFA22 = 'fifa22'
    FIFA20 = 'fifa20'
    WOW = 'wow'
    QUAKE_CHAMPIONS = 'quake_champions'
    TRACKMANIA = 'trackmania'
    PUBG = 'pubg'
    NEW_STATE_MOBILE = 'newstate'
    RIFT = 'wildrift'
    HEARTHSTONE = 'hearthstone'
    FALLGUYS = 'fallguys'
    TEAMFIGHT_TACTICS = 'teamfight_tactics'
    PUBG_MOBILE = 'pubgmobile'
    ROCKET_LEAGUE = 'rocket_league'
    CS_GO = 'csgo'
