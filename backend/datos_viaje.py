import random

lugares = {
    "Europa": {
        "Espa├▒a": [
            ("Madrid", "Capital cultural, museos y vida nocturna", "Variable"),
            ("Barcelona", "Arquitectura modernista y costa mediterr├ínea", "H├║medo y suave"),
            ("Valencia", "Ciudad de las Artes, playa y paella", "H├║medo y c├ílido"),
            ("Sevilla", "Flamenco, tapas y arquitectura morisca", "Muy caluroso"),
            ("Zaragoza", "Legado romano, el Pilar y tapas", "Ventoso"),
            ("M├ílaga", "Costa del Sol, museos Picasso y espetos", "Mediterr├íneo"),
            ("Murcia", "Huerta de Europa y catedral barroca", "Muy caluroso"),
            ("Palma de Mallorca", "Playas cristalinas y catedral g├│tica", "Mediterr├íneo"),
            ("Las Palmas", "Playas y clima primaveral", "Suave"),
            ("Bilbao", "Museo Guggenheim y pintxos", "Oce├ínico"),
            ("Alicante", "Castillo de Santa B├írbara", "Mediterr├íneo"),
            ("C├│rdoba", "Mezquita-Catedral y patios de flores", "Caluroso"),
            ("Valladolid", "Cuna del castellano y buen vino", "Continental"),
            ("Vigo", "Puerto mar├¡timo, marisco y luces", "Oce├ínico"),
            ("Gij├│n", "Costa asturiana, sidra", "Oce├ínico"),
            ("Hospitalet", "Ciudad de contrastes y ferias", "Mediterr├íneo"),
            ("Vitoria", "Capital verde europea", "Oce├ínico"),
            ("A Coru├▒a", "Torre de H├®rcules", "Oce├ínico"),
            ("Granada", "La Alhambra maravilla nevada", "Continental"),
            ("Elche", "Palmeral Patrimonio de la Humanidad", "Mediterr├íneo"),
            ("Oviedo", "Prerrom├ínico asturiano", "Oce├ínico"),
            ("Tenerife", "Carnavales y clima atl├íntico", "Suave"),
            ("Cartagena", "Teatro romano y puerto", "Mediterr├íneo"),
            ("Terrassa", "Masia freixa industrial", "Mediterr├íneo"),
            ("Jerez", "Motos, vino y caballos", "Caluroso"),
            ("Sabadell", "Modernismo e historia textil", "Mediterr├íneo"),
            ("M├│stoles", "Parques y proximidad capitalina", "Variable"),
            ("Alcal├í de Henares", "Universidad hist├│rica", "Variable"),
            ("Pamplona", "Sanfermines y murallas", "Continental"),
            ("Almer├¡a", "Alcazaba e historias de cine", "Des├®rtico"),
            ("Fuenlabrada", "Vanguardia en el sur de Madrid", "Variable"),
            ("Legan├®s", "Zonas verdes", "Variable"),
            ("San Sebasti├ín", "Playa de la Concha y estrellas Michelin", "Oce├ínico"),
            ("Getafe", "Cerro de los ├üngeles", "Variable"),
            ("Burgos", "Catedral g├│tica", "Continental"),
            ("Santander", "Bah├¡a y Palacio Magdalena", "Oce├ínico"),
            ("Albacete", "Cuchiller├¡a y ferias", "Variable"),
            ("Castell├│n", "El Fadr├¡ y clima naranja", "Mediterr├íneo"),
            ("Logro├▒o", "Calle Laurel y capital del Rioja", "Continental"),
            ("Badajoz", "Alcazaba y frontera multicultural", "Caluroso"),
            ("Salamanca", "Ciudad dorada y Plaza Mayor", "Continental"),
            ("Huelva", "Lugares colombinos", "Suave"),
            ("Marbella", "Lujo y Puerto Ban├║s", "Mediterr├íneo"),
            ("Lleida", "Seu Vella y huerta", "Continental"),
            ("Tarragona", "Tarraco romana y Costa Dorada", "Mediterr├íneo"),
            ("Le├│n", "Barrio h├║medo y catedral", "Continental"),
            ("C├ídiz", "La Tacita de Plata", "H├║medo"),
            ("Ja├®n", "Capital del Santo Reino", "Caluroso"),
            ("Ourense", "Termas milenarias", "Oce├ínico"),
            ("Toledo", "Ciudad hist├│rica medieval patrimonio de la humanidad.", "Soleado"),
            ("Cuenca", "Casas colgadas y naturaleza serrana.", "Fresco"),
            ("Santiago de Compostela", "Meta del peregrinaje", "Lluvioso"),
            ("Ibiza", "Playas cristalinas y fiesta", "Mediterr├íneo"),
            ("Ciudad Real", "Tierra de Don Quijote", "Continental")
        ],
        "Francia": [
            ("Par├¡s", "Ciudad del amor, arte y moda", "Templado"),
            ("Marsella", "Puerto vital y del mediterr├íneo", "Mediterr├íneo"),
            ("Lyon", "Capital gastron├│mica y cuna del cine", "Continental"),
            ("Toulouse", "La ciudad rosa y aerona├║tica", "Suave"),
            ("Niza", "Paseo de los Ingleses", "Mediterr├íneo"),
            ("Nantes", "M├íquinas de la isla", "Oce├ínico"),
            ("Montpellier", "Ciudad joven", "Mediterr├íneo"),
            ("Estrasburgo", "Capital europea y encanto alsaciano", "Continental"),
            ("Burdeos", "Cuna de los mejores vinos del mundo", "Oce├ínico"),
            ("Lille", "Arquitectura flamenca y cerveza", "Fresco"),
            ("Rennes", "Casas entramadas bretonas", "Oce├ínico"),
            ("Reims", "Capital del champ├ín", "Continental"),
            ("Cannes", "Festival de cine", "Mediterr├íneo"),
            ("Dijon", "Mostaza y vinos de borgo├▒a", "Continental")
        ],
        "Italia": [
            ("Roma", "La Ciudad Eterna", "Mediterr├íneo"),
            ("Mil├ín", "Moda, Duomo y la ├Ültima Cena", "Continental"),
            ("N├ípoles", "Vesubio y pizza", "Mediterr├íneo"),
            ("Tur├¡n", "Elegancia y los Alpes", "Continental"),
            ("Palermo", "Mezcla ├írabe-normanda", "Mediterr├íneo"),
            ("G├®nova", "Puerto hist├│rico", "Mediterr├íneo"),
            ("Bolonia", "La Docta, Gorda y Roja", "Continental"),
            ("Florencia", "Cuna del Renacimiento", "Mediterr├íneo"),
            ("Bari", "San Nicol├ís costa adri├ítica", "Mediterr├íneo"),
            ("Catania", "Piedra de lava y el Etna", "Mediterr├íneo"),
            ("Venecia", "Canales rom├ínticos", "H├║medo"),
            ("Verona", "Arena romana y Julieta", "Continental"),
            ("Pisa", "La torre inclinada", "Mediterr├íneo")
        ],
        "Alemania": [
            ("Berl├¡n", "Muro antiguo, vanguardia y techno", "Continental"),
            ("Hamburgo", "Inmenso puerto", "Oce├ínico"),
            ("M├║nich", "Oktoberfest", "Continental"),
            ("Colonia", "La majestuosa catedral", "Templado"),
            ("Fr├íncfort", "El Manhattan europeo", "Templado"),
            ("Stuttgart", "Coches de lujo", "Templado"),
            ("D├╝sseldorf", "Moda y Rin", "Templado"),
            ("Leipzig", "M├║sica cl├ísica", "Continental"),
            ("N├║remberg", "Castillo e historia", "Continental")
        ],
        "Reino Unido": [
            ("Londres", "Historia, cultura moderna y pubs", "Lluvioso"),
            ("Birmingham", "Canales y pasado industrial", "Templado"),
            ("M├ínchester", "Revoluci├│n industrial y m├║sica", "Lluvioso"),
            ("Glasgow", "Arte victoriano", "Lluvioso"),
            ("Liverpool", "Los Beatles y gloria marinera", "Oce├ínico"),
            ("Edimburgo", "Castillo medieval", "Fresco"),
            ("Bristol", "Puente y astilleros", "Suave"),
            ("Belfast", "Titanic y astilleros", "Lluvioso"),
            ("Oxford", "Universidad antigua", "Templado"),
            ("Cambridge", "Punting en el r├¡o", "Templado")
        ],
        "Pa├¡ses Bajos y B├®lgica": [
            ("├ümsterdam", "Canales y museos", "Oce├ínico"),
            ("R├│terdam", "Arquitectura moderna", "Oce├ínico"),
            ("La Haya", "Corte internacional", "Oce├ínico"),
            ("Bruselas", "Parlamento, atomium, gofres", "Templado"),
            ("Brujas", "M├ígicos canales medievales", "Templado"),
            ("Amberes", "Capital mundial de los diamantes", "Templado")
        ],
        "Resto de Europa": [
            ("Z├║rich", "Centro financiero", "Alpino"),
            ("Ginebra", "Diplomacia y lago", "Alpino"),
            ("Berna", "Los osos", "Alpino"),
            ("Atenas", "La Acr├│polis", "Mediterr├íneo"),
            ("Santorini", "Casas blancas y atardeceres", "Mediterr├íneo"),
            ("Estambul", "El B├│sforo y mezquitas", "Templado"),
            ("Praga", "Ciudad de las 100 torres", "Continental"),
            ("Viena", "Capital de la m├║sica cl├ísica", "Continental"),
            ("Budapest", "La perla del Danubio", "Continental"),
            ("Varsovia", "Sirena her├│ica", "Continental"),
            ("Cracovia", "Leyenda del drag├│n", "Continental"),
            ("Estocolmo", "Belleza sobre catorce islas", "Fr├¡o"),
            ("Gotemburgo", "Canales, tranv├¡as azules", "Oce├ínico"),
            ("Copenhague", "Sirenita y Tivoli", "Fresco"),
            ("Oslo", "Fiordos y vikingos", "Fr├¡o"),
            ("Helsinki", "Saunas y plaza blanca", "Fr├¡o"),
            ("Reikiavik", "Geotermia y auroras boreales", "Fr├¡o"),
            ("Lisboa", "Fado y tranv├¡as antiguos", "Atl├íntico"),
            ("Oporto", "Bodegas famosas de vino", "Atl├íntico"),
            ("Dubl├¡n", "Pubs celtas", "Lluvioso")
        ]
    },
    "Am├®rica": {
        "Estados Unidos": [
            ("Nueva York", "La ciudad que nunca duerme", "Variable"),
            ("Los ├üngeles", "Hollywood, estrellas y playa", "Soleado"),
            ("Chicago", "Arquitectura y blues", "Ventoso"),
            ("Las Vegas", "El Strip lleno de ne├│n", "Des├®rtico"),
            ("Miami", "Vibra caribe├▒a y Art Deco", "Tropical"),
            ("San Francisco", "Golden Gate y niebla", "Niebla"),
            ("Orlando", "Parques de diversiones", "Tropical"),
            ("Washington D.C.", "Monumentos nacionales", "Variable"),
            ("Boston", "La ruta de la libertad", "Variable"),
            ("Seattle", "Aguja Espacial y caf├®", "Lluvioso"),
            ("Filadelfia", "Campana de la libertad", "Variable"),
            ("San Diego", "Clima inmejorable", "Soleado"),
            ("Dallas", "JFK y negocios", "Continental"),
            ("Austin", "Capital de la m├║sica en vivo", "Caluroso"),
            ("Nueva Orleans", "Carnaval y jazz", "H├║medo"),
            ("Atlanta", "Olimpiadas del 96", "Caluroso"),
            ("Denver", "Mile High a ras de monta├▒as", "Monta├▒oso"),
            ("Honolulu", "Waikiki y volcanes aloha", "Tropical")
        ],
        "M├®xico y Canad├í": [
            ("Ciudad de M├®xico", "Mega urbe azteca", "Templado"),
            ("Canc├║n", "Playas caribe├▒as y ruinas mayas", "Tropical"),
            ("Guadalajara", "Mariachi y tequila", "Templado"),
            ("Monterrey", "Sultana industrial", "Caluroso"),
            ("Puebla", "Volcanes guardianes y mole", "Templado"),
            ("M├®rida", "Esplendor de cenotes", "Tropical"),
            ("Tijuana", "Frontera vibrante", "Des├®rtico"),
            ("Toronto", "Torre CN", "Continental"),
            ("Montreal", "Festival franc├®s", "Continental"),
            ("Vancouver", "Bosques frente al pac├¡fico", "Lluvioso"),
            ("Calgary", "Estampida petrolera", "Fr├¡o"),
            ("Quebec", "Chateau Frontenac", "Fr├¡o")
        ],
        "Sudam├®rica": [
            ("Machu Picchu", "Ciudadela inca en los Andes", "Monta├▒oso"),
            ("R├¡o de Janeiro", "Carnaval, Copacabana y Cristo", "Tropical"),
            ("Buenos Aires", "Tango, asado y obelisco", "Templado"),
            ("S├úo Paulo", "Metr├│polis financiera y vibrante", "Tropical"),
            ("Lima", "Barranco y ceviche espectacular", "Des├®rtico"),
            ("Bogot├í", "Monserrate y oro prehisp├ínico", "Templado"),
            ("Medell├¡n", "Ciudad de la eterna primavera", "Templado"),
            ("Cartagena", "Ciudad murada rom├íntica y pirata", "Tropical"),
            ("Santiago", "Los Andinisimos y telef├®rico", "Templado"),
            ("Valpara├¡so", "Cerros de mil colores y puerto", "Oce├ínico"),
            ("Cusco", "Ombligo del mundo maravilloso", "Monta├▒oso"),
            ("Quito", "Mitad del mundo y el Pichincha", "Monta├▒oso"),
            ("La Paz", "Alt├¡simos telef├®ricos y el illimani", "Fr├¡o"),
            ("Montevideo", "Ramblas costeras y mate rioplatense", "Templado"),
            ("Asunci├│n", "Preciosa madre guaran├¡", "Caluroso"),
            ("Caracas", "├üvila inmenso esplendor y arepas", "Tropical")
        ]
    },
    "Asia y Resto": {
        "Jap├│n y Corea": [
            ("Tokio", "Tecnolog├¡a futurista y tradici├│n", "H├║medo"),
            ("Kioto", "Templos, jardines zen y geishas", "Templado"),
            ("Osaka", "Comida callejera y castillo inmenso", "Templado"),
            ("Hiroshima", "Sagrada paz de la torii roja", "Templado"),
            ("Nara", "Gigante bambi y buda enorme milenario", "Templado"),
            ("Se├║l", "K-pop, palacios y r├¡o brillante", "Continental"),
            ("Busan", "Playas surcoreanas y puente gigante", "Templado")
        ],
        "China y SE Asi├ítico": [
            ("Pek├¡n", "Muralla inmensa ciudad prohibida", "Continental"),
            ("Shangh├íi", "Torres alt├¡simas de r├¡o futurista", "Tropical"),
            ("Hong Kong", "Bah├¡a brillante y metr├│polis", "Tropical"),
            ("Bangkok", "Templos dorados, comida y caos", "Tropical"),
            ("Bali", "Playas, templos y espiritualidad", "Tropical"),
            ("Singapur", "Jardines futuristas y hawker", "Tropical"),
            ("Yakarta", "Masivo archipi├®lago y monumentos", "Tropical"),
            ("Ho Chi Minh", "Motocicletas y pho infinito", "Tropical"),
            ("Kuala Lumpur", "Torres gemelas de brillante plata", "Tropical"),
            ("Manila", "Intramuros hist├│rica y jeepney colorido", "Tropical")
        ],
        "India y Medio Oriente": [
            ("Nueva Delhi", "India grandiosa e imponente loto", "Caluroso"),
            ("Bombay", "Bollywood majestuoso", "Tropical"),
            ("Agra", "Taj Mahal inmensamente rom├íntico", "Caluroso"),
            ("Dub├íi", "Rascacielos gigante y oro infinito", "Des├®rtico"),
            ("El Cairo", "Las majestuosas pir├ímides", "Des├®rtico"),
            ("Abu Dabi", "Blanca y enorme mezquita", "Des├®rtico"),
            ("Jerusal├®n", "Tierra sant├¡sima y sagrada", "Mediterr├íneo"),
            ("Tel Aviv", "Playas brillantes vibrantes inovadoras", "Mediterr├íneo"),
            ("Am├ín", "Ciudad milenaria con blanca ciudadela", "Seco")
        ],
        "├üfrica y Ocean├¡a": [
            ("S├¡dney", "Opera House, surf y canguros", "Soleado"),
            ("Melbourne", "Callejones victorianos arte y caf├®", "Templado"),
            ("Auckland", "Ciudad velero inmenso volc├ínica", "Oce├ínico"),
            ("Ciudad del Cabo", "Monta├▒a mesa de verde esperanza inmensa", "Mediterr├íneo"),
            ("Nairobi", "Verde capital gigante de intenso safari verde pura africana", "Templado"),
            ("Marrakech", "Colores de inmenso zoco infinito rojo vibrante milenario gran oriental bella", "Tropical")
        ]
    }
}

# Expand destinations
DESTINOS_POOL = []
for region, paises in lugares.items():
    for pais, lista_ciudades in paises.items():
        for ciudad in lista_ciudades:
            DESTINOS_POOL.append((ciudad[0], ciudad[1], ciudad[2], pais, region))

# We also generate generic and city events based on these dynamically
GENERIC_EVENTS = [
    ('Mercado Local Artesanal', 'Cultura', 'Gratis'),
    ('Festival de M├║sica Indie', 'M├║sica', '30Ôé¼'),
    ('Marat├│n de la Ciudad', 'Deporte', '50Ôé¼'),
    ('Exposici├│n de Arte Moderno', 'Cultura', '15Ôé¼'),
    ('Feria Gastron├│mica Internacional', 'Gastronom├¡a', '20Ôé¼'),
    ('Carnaval Local Anual', 'Fiesta', 'Gratis'),
    ('Taller de Fotograf├¡a', 'Arte', '25Ôé¼'),
    ('Concierto Cl├ísico en la Plaza', 'M├║sica', '10Ôé¼'),
    ('Encuentro Tecnol├│gico', 'Tecnolog├¡a', '40Ôé¼')
]

# Random event titles base for generation
EVENT_TITLES = {
    'M├║sica': ['Concierto Sinf├│nico', 'Festival de Jazz', 'Recital Ac├║stico', 'Festival Electr├│nico'],
    'Deporte': ['Marat├│n Urbano', 'Cl├ísico de F├║tbol', 'Torneo de Tenis', 'Ciclismo en Ruta'],
    'Teatro': ['Microteatro: Comedias', 'Musical de Broadway', 'Obra de Teatro Cl├ísico', 'Drama Contempor├íneo'],
    'Arte': ['Exposici├│n Fotogr├ífica', 'Feria de Dise├▒o y Arte', 'Muestra de Escultura', 'Taller de Pintura'],
    'Gastronom├¡a': ['Cata de Vinos y Quesos', 'Festival del Cami├│n de Comida', 'Semana del Restaurante', 'Feria de Dulces'],
    'Tecnolog├¡a': ['Hackathon Anual', 'Feria de Startups', 'Exposici├│n de Rob├│tica', 'Congreso de IA']
}

def generate_events_for_destination(d_name):
    # Base real events for famous cities
    specifics = {
        'Madrid': [
            ('Partido: Real Madrid vs FC Barcelona', 'Deporte', '120Ôé¼'),
            ('Concierto: Vetusta Morla', 'M├║sica', '45Ôé¼'),
            ('Feria del Libro', 'Cultura', 'Gratis')
        ],
        'Barcelona': [
            ('Partido: FC Barcelona vs Valencia', 'Deporte', '90Ôé¼'),
            ('Festival Primavera Sound', 'M├║sica', '180Ôé¼'),
            ('Exposici├│n Gaud├¡', 'Cultura', '25Ôé¼')
        ],
        'Par├¡s': [
            ('Fashion Week Runway', 'Moda', 'Invitation'),
            ('PSG vs Marsella', 'Deporte', '150Ôé¼')
        ],
        'Londres': [
            ('Wimbledon Tennis', 'Deporte', '200┬ú'),
            ('Musical: The Phantom of the Opera', 'Teatro', '70┬ú')
        ],
        'Nueva York': [
            ('Broadway Show: Hamilton', 'Teatro', '180$'),
            ('NBA: Knicks vs Lakers', 'Deporte', '250$')
        ],
        'Tokio': [
            ('Torneo de Sumo', 'Deporte', '8000┬Ñ'),
            ('Festival de los Cerezos', 'Cultura', 'Gratis')
        ]
    }
    
    events_list = specifics.get(d_name, [])
    # Add random generated events to make sure everyone has some
    if not events_list:
        import random
        # Give 4 to 8 events to each city to easily cross 1000 total events
        num_ev = random.randint(4, 8)
        for _ in range(num_ev):
            tipo = random.choice(list(EVENT_TITLES.keys()))
            title = random.choice(EVENT_TITLES[tipo])
            precio = f"{random.randint(10, 80)}Ôé¼"
            events_list.append((f"{title} en {d_name}", tipo, precio))
    
    return events_list
