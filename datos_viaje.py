import random

lugares = {
    "Europa": {
        "España": [
            ("Madrid", "Capital cultural, museos y vida nocturna", "Variable"),
            ("Barcelona", "Arquitectura modernista y costa mediterránea", "Húmedo y suave"),
            ("Valencia", "Ciudad de las Artes, playa y paella", "Húmedo y cálido"),
            ("Sevilla", "Flamenco, tapas y arquitectura morisca", "Muy caluroso"),
            ("Zaragoza", "Legado romano, el Pilar y tapas", "Ventoso"),
            ("Málaga", "Costa del Sol, museos Picasso y espetos", "Mediterráneo"),
            ("Murcia", "Huerta de Europa y catedral barroca", "Muy caluroso"),
            ("Palma de Mallorca", "Playas cristalinas y catedral gótica", "Mediterráneo"),
            ("Las Palmas", "Playas y clima primaveral", "Suave"),
            ("Bilbao", "Museo Guggenheim y pintxos", "Oceánico"),
            ("Alicante", "Castillo de Santa Bárbara", "Mediterráneo"),
            ("Córdoba", "Mezquita-Catedral y patios de flores", "Caluroso"),
            ("Valladolid", "Cuna del castellano y buen vino", "Continental"),
            ("Vigo", "Puerto marítimo, marisco y luces", "Oceánico"),
            ("Gijón", "Costa asturiana, sidra", "Oceánico"),
            ("Hospitalet", "Ciudad de contrastes y ferias", "Mediterráneo"),
            ("Vitoria", "Capital verde europea", "Oceánico"),
            ("A Coruña", "Torre de Hércules", "Oceánico"),
            ("Granada", "La Alhambra maravilla nevada", "Continental"),
            ("Elche", "Palmeral Patrimonio de la Humanidad", "Mediterráneo"),
            ("Oviedo", "Prerrománico asturiano", "Oceánico"),
            ("Tenerife", "Carnavales y clima atlántico", "Suave"),
            ("Cartagena", "Teatro romano y puerto", "Mediterráneo"),
            ("Terrassa", "Masia freixa industrial", "Mediterráneo"),
            ("Jerez", "Motos, vino y caballos", "Caluroso"),
            ("Sabadell", "Modernismo e historia textil", "Mediterráneo"),
            ("Móstoles", "Parques y proximidad capitalina", "Variable"),
            ("Alcalá de Henares", "Universidad histórica", "Variable"),
            ("Pamplona", "Sanfermines y murallas", "Continental"),
            ("Almería", "Alcazaba e historias de cine", "Desértico"),
            ("Fuenlabrada", "Vanguardia en el sur de Madrid", "Variable"),
            ("Leganés", "Zonas verdes", "Variable"),
            ("San Sebastián", "Playa de la Concha y estrellas Michelin", "Oceánico"),
            ("Getafe", "Cerro de los Ángeles", "Variable"),
            ("Burgos", "Catedral gótica", "Continental"),
            ("Santander", "Bahía y Palacio Magdalena", "Oceánico"),
            ("Albacete", "Cuchillería y ferias", "Variable"),
            ("Castellón", "El Fadrí y clima naranja", "Mediterráneo"),
            ("Logroño", "Calle Laurel y capital del Rioja", "Continental"),
            ("Badajoz", "Alcazaba y frontera multicultural", "Caluroso"),
            ("Salamanca", "Ciudad dorada y Plaza Mayor", "Continental"),
            ("Huelva", "Lugares colombinos", "Suave"),
            ("Marbella", "Lujo y Puerto Banús", "Mediterráneo"),
            ("Lleida", "Seu Vella y huerta", "Continental"),
            ("Tarragona", "Tarraco romana y Costa Dorada", "Mediterráneo"),
            ("León", "Barrio húmedo y catedral", "Continental"),
            ("Cádiz", "La Tacita de Plata", "Húmedo"),
            ("Jaén", "Capital del Santo Reino", "Caluroso"),
            ("Ourense", "Termas milenarias", "Oceánico"),
            ("Toledo", "Ciudad histórica medieval patrimonio de la humanidad.", "Soleado"),
            ("Cuenca", "Casas colgadas y naturaleza serrana.", "Fresco"),
            ("Santiago de Compostela", "Meta del peregrinaje", "Lluvioso"),
            ("Ibiza", "Playas cristalinas y fiesta", "Mediterráneo"),
            ("Ciudad Real", "Tierra de Don Quijote", "Continental")
        ],
        "Francia": [
            ("París", "Ciudad del amor, arte y moda", "Templado"),
            ("Marsella", "Puerto vital y del mediterráneo", "Mediterráneo"),
            ("Lyon", "Capital gastronómica y cuna del cine", "Continental"),
            ("Toulouse", "La ciudad rosa y aeronaútica", "Suave"),
            ("Niza", "Paseo de los Ingleses", "Mediterráneo"),
            ("Nantes", "Máquinas de la isla", "Oceánico"),
            ("Montpellier", "Ciudad joven", "Mediterráneo"),
            ("Estrasburgo", "Capital europea y encanto alsaciano", "Continental"),
            ("Burdeos", "Cuna de los mejores vinos del mundo", "Oceánico"),
            ("Lille", "Arquitectura flamenca y cerveza", "Fresco"),
            ("Rennes", "Casas entramadas bretonas", "Oceánico"),
            ("Reims", "Capital del champán", "Continental"),
            ("Cannes", "Festival de cine", "Mediterráneo"),
            ("Dijon", "Mostaza y vinos de borgoña", "Continental")
        ],
        "Italia": [
            ("Roma", "La Ciudad Eterna", "Mediterráneo"),
            ("Milán", "Moda, Duomo y la Última Cena", "Continental"),
            ("Nápoles", "Vesubio y pizza", "Mediterráneo"),
            ("Turín", "Elegancia y los Alpes", "Continental"),
            ("Palermo", "Mezcla árabe-normanda", "Mediterráneo"),
            ("Génova", "Puerto histórico", "Mediterráneo"),
            ("Bolonia", "La Docta, Gorda y Roja", "Continental"),
            ("Florencia", "Cuna del Renacimiento", "Mediterráneo"),
            ("Bari", "San Nicolás costa adriática", "Mediterráneo"),
            ("Catania", "Piedra de lava y el Etna", "Mediterráneo"),
            ("Venecia", "Canales románticos", "Húmedo"),
            ("Verona", "Arena romana y Julieta", "Continental"),
            ("Pisa", "La torre inclinada", "Mediterráneo")
        ],
        "Alemania": [
            ("Berlín", "Muro antiguo, vanguardia y techno", "Continental"),
            ("Hamburgo", "Inmenso puerto", "Oceánico"),
            ("Múnich", "Oktoberfest", "Continental"),
            ("Colonia", "La majestuosa catedral", "Templado"),
            ("Fráncfort", "El Manhattan europeo", "Templado"),
            ("Stuttgart", "Coches de lujo", "Templado"),
            ("Düsseldorf", "Moda y Rin", "Templado"),
            ("Leipzig", "Música clásica", "Continental"),
            ("Núremberg", "Castillo e historia", "Continental")
        ],
        "Reino Unido": [
            ("Londres", "Historia, cultura moderna y pubs", "Lluvioso"),
            ("Birmingham", "Canales y pasado industrial", "Templado"),
            ("Mánchester", "Revolución industrial y música", "Lluvioso"),
            ("Glasgow", "Arte victoriano", "Lluvioso"),
            ("Liverpool", "Los Beatles y gloria marinera", "Oceánico"),
            ("Edimburgo", "Castillo medieval", "Fresco"),
            ("Bristol", "Puente y astilleros", "Suave"),
            ("Belfast", "Titanic y astilleros", "Lluvioso"),
            ("Oxford", "Universidad antigua", "Templado"),
            ("Cambridge", "Punting en el río", "Templado")
        ],
        "Países Bajos y Bélgica": [
            ("Ámsterdam", "Canales y museos", "Oceánico"),
            ("Róterdam", "Arquitectura moderna", "Oceánico"),
            ("La Haya", "Corte internacional", "Oceánico"),
            ("Bruselas", "Parlamento, atomium, gofres", "Templado"),
            ("Brujas", "Mágicos canales medievales", "Templado"),
            ("Amberes", "Capital mundial de los diamantes", "Templado")
        ],
        "Resto de Europa": [
            ("Zúrich", "Centro financiero", "Alpino"),
            ("Ginebra", "Diplomacia y lago", "Alpino"),
            ("Berna", "Los osos", "Alpino"),
            ("Atenas", "La Acrópolis", "Mediterráneo"),
            ("Santorini", "Casas blancas y atardeceres", "Mediterráneo"),
            ("Estambul", "El Bósforo y mezquitas", "Templado"),
            ("Praga", "Ciudad de las 100 torres", "Continental"),
            ("Viena", "Capital de la música clásica", "Continental"),
            ("Budapest", "La perla del Danubio", "Continental"),
            ("Varsovia", "Sirena heróica", "Continental"),
            ("Cracovia", "Leyenda del dragón", "Continental"),
            ("Estocolmo", "Belleza sobre catorce islas", "Frío"),
            ("Gotemburgo", "Canales, tranvías azules", "Oceánico"),
            ("Copenhague", "Sirenita y Tivoli", "Fresco"),
            ("Oslo", "Fiordos y vikingos", "Frío"),
            ("Helsinki", "Saunas y plaza blanca", "Frío"),
            ("Reikiavik", "Geotermia y auroras boreales", "Frío"),
            ("Lisboa", "Fado y tranvías antiguos", "Atlántico"),
            ("Oporto", "Bodegas famosas de vino", "Atlántico"),
            ("Dublín", "Pubs celtas", "Lluvioso")
        ]
    },
    "América": {
        "Estados Unidos": [
            ("Nueva York", "La ciudad que nunca duerme", "Variable"),
            ("Los Ángeles", "Hollywood, estrellas y playa", "Soleado"),
            ("Chicago", "Arquitectura y blues", "Ventoso"),
            ("Las Vegas", "El Strip lleno de neón", "Desértico"),
            ("Miami", "Vibra caribeña y Art Deco", "Tropical"),
            ("San Francisco", "Golden Gate y niebla", "Niebla"),
            ("Orlando", "Parques de diversiones", "Tropical"),
            ("Washington D.C.", "Monumentos nacionales", "Variable"),
            ("Boston", "La ruta de la libertad", "Variable"),
            ("Seattle", "Aguja Espacial y café", "Lluvioso"),
            ("Filadelfia", "Campana de la libertad", "Variable"),
            ("San Diego", "Clima inmejorable", "Soleado"),
            ("Dallas", "JFK y negocios", "Continental"),
            ("Austin", "Capital de la música en vivo", "Caluroso"),
            ("Nueva Orleans", "Carnaval y jazz", "Húmedo"),
            ("Atlanta", "Olimpiadas del 96", "Caluroso"),
            ("Denver", "Mile High a ras de montañas", "Montañoso"),
            ("Honolulu", "Waikiki y volcanes aloha", "Tropical")
        ],
        "México y Canadá": [
            ("Ciudad de México", "Mega urbe azteca", "Templado"),
            ("Cancún", "Playas caribeñas y ruinas mayas", "Tropical"),
            ("Guadalajara", "Mariachi y tequila", "Templado"),
            ("Monterrey", "Sultana industrial", "Caluroso"),
            ("Puebla", "Volcanes guardianes y mole", "Templado"),
            ("Mérida", "Esplendor de cenotes", "Tropical"),
            ("Tijuana", "Frontera vibrante", "Desértico"),
            ("Toronto", "Torre CN", "Continental"),
            ("Montreal", "Festival francés", "Continental"),
            ("Vancouver", "Bosques frente al pacífico", "Lluvioso"),
            ("Calgary", "Estampida petrolera", "Frío"),
            ("Quebec", "Chateau Frontenac", "Frío")
        ],
        "Sudamérica": [
            ("Machu Picchu", "Ciudadela inca en los Andes", "Montañoso"),
            ("Río de Janeiro", "Carnaval, Copacabana y Cristo", "Tropical"),
            ("Buenos Aires", "Tango, asado y obelisco", "Templado"),
            ("São Paulo", "Metrópolis financiera y vibrante", "Tropical"),
            ("Lima", "Barranco y ceviche espectacular", "Desértico"),
            ("Bogotá", "Monserrate y oro prehispánico", "Templado"),
            ("Medellín", "Ciudad de la eterna primavera", "Templado"),
            ("Cartagena", "Ciudad murada romántica y pirata", "Tropical"),
            ("Santiago", "Los Andinisimos y teleférico", "Templado"),
            ("Valparaíso", "Cerros de mil colores y puerto", "Oceánico"),
            ("Cusco", "Ombligo del mundo maravilloso", "Montañoso"),
            ("Quito", "Mitad del mundo y el Pichincha", "Montañoso"),
            ("La Paz", "Altísimos teleféricos y el illimani", "Frío"),
            ("Montevideo", "Ramblas costeras y mate rioplatense", "Templado"),
            ("Asunción", "Preciosa madre guaraní", "Caluroso"),
            ("Caracas", "Ávila inmenso esplendor y arepas", "Tropical")
        ]
    },
    "Asia y Resto": {
        "Japón y Corea": [
            ("Tokio", "Tecnología futurista y tradición", "Húmedo"),
            ("Kioto", "Templos, jardines zen y geishas", "Templado"),
            ("Osaka", "Comida callejera y castillo inmenso", "Templado"),
            ("Hiroshima", "Sagrada paz de la torii roja", "Templado"),
            ("Nara", "Gigante bambi y buda enorme milenario", "Templado"),
            ("Seúl", "K-pop, palacios y río brillante", "Continental"),
            ("Busan", "Playas surcoreanas y puente gigante", "Templado")
        ],
        "China y SE Asiático": [
            ("Pekín", "Muralla inmensa ciudad prohibida", "Continental"),
            ("Shanghái", "Torres altísimas de río futurista", "Tropical"),
            ("Hong Kong", "Bahía brillante y metrópolis", "Tropical"),
            ("Bangkok", "Templos dorados, comida y caos", "Tropical"),
            ("Bali", "Playas, templos y espiritualidad", "Tropical"),
            ("Singapur", "Jardines futuristas y hawker", "Tropical"),
            ("Yakarta", "Masivo archipiélago y monumentos", "Tropical"),
            ("Ho Chi Minh", "Motocicletas y pho infinito", "Tropical"),
            ("Kuala Lumpur", "Torres gemelas de brillante plata", "Tropical"),
            ("Manila", "Intramuros histórica y jeepney colorido", "Tropical")
        ],
        "India y Medio Oriente": [
            ("Nueva Delhi", "India grandiosa e imponente loto", "Caluroso"),
            ("Bombay", "Bollywood majestuoso", "Tropical"),
            ("Agra", "Taj Mahal inmensamente romántico", "Caluroso"),
            ("Dubái", "Rascacielos gigante y oro infinito", "Desértico"),
            ("El Cairo", "Las majestuosas pirámides", "Desértico"),
            ("Abu Dabi", "Blanca y enorme mezquita", "Desértico"),
            ("Jerusalén", "Tierra santísima y sagrada", "Mediterráneo"),
            ("Tel Aviv", "Playas brillantes vibrantes inovadoras", "Mediterráneo"),
            ("Amán", "Ciudad milenaria con blanca ciudadela", "Seco")
        ],
        "África y Oceanía": [
            ("Sídney", "Opera House, surf y canguros", "Soleado"),
            ("Melbourne", "Callejones victorianos arte y café", "Templado"),
            ("Auckland", "Ciudad velero inmenso volcánica", "Oceánico"),
            ("Ciudad del Cabo", "Montaña mesa de verde esperanza inmensa", "Mediterráneo"),
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
    ('Festival de Música Indie', 'Música', '30€'),
    ('Maratón de la Ciudad', 'Deporte', '50€'),
    ('Exposición de Arte Moderno', 'Cultura', '15€'),
    ('Feria Gastronómica Internacional', 'Gastronomía', '20€'),
    ('Carnaval Local Anual', 'Fiesta', 'Gratis'),
    ('Taller de Fotografía', 'Arte', '25€'),
    ('Concierto Clásico en la Plaza', 'Música', '10€'),
    ('Encuentro Tecnológico', 'Tecnología', '40€')
]

# Random event titles base for generation
EVENT_TITLES = {
    'Música': ['Concierto Sinfónico', 'Festival de Jazz', 'Recital Acústico', 'Festival Electrónico'],
    'Deporte': ['Maratón Urbano', 'Clásico de Fútbol', 'Torneo de Tenis', 'Ciclismo en Ruta'],
    'Teatro': ['Microteatro: Comedias', 'Musical de Broadway', 'Obra de Teatro Clásico', 'Drama Contemporáneo'],
    'Arte': ['Exposición Fotográfica', 'Feria de Diseño y Arte', 'Muestra de Escultura', 'Taller de Pintura'],
    'Gastronomía': ['Cata de Vinos y Quesos', 'Festival del Camión de Comida', 'Semana del Restaurante', 'Feria de Dulces'],
    'Tecnología': ['Hackathon Anual', 'Feria de Startups', 'Exposición de Robótica', 'Congreso de IA']
}

def generate_events_for_destination(d_name):
    # Base real events for famous cities
    specifics = {
        'Madrid': [
            ('Partido: Real Madrid vs FC Barcelona', 'Deporte', '120€'),
            ('Concierto: Vetusta Morla', 'Música', '45€'),
            ('Feria del Libro', 'Cultura', 'Gratis')
        ],
        'Barcelona': [
            ('Partido: FC Barcelona vs Valencia', 'Deporte', '90€'),
            ('Festival Primavera Sound', 'Música', '180€'),
            ('Exposición Gaudí', 'Cultura', '25€')
        ],
        'París': [
            ('Fashion Week Runway', 'Moda', 'Invitation'),
            ('PSG vs Marsella', 'Deporte', '150€')
        ],
        'Londres': [
            ('Wimbledon Tennis', 'Deporte', '200£'),
            ('Musical: The Phantom of the Opera', 'Teatro', '70£')
        ],
        'Nueva York': [
            ('Broadway Show: Hamilton', 'Teatro', '180$'),
            ('NBA: Knicks vs Lakers', 'Deporte', '250$')
        ],
        'Tokio': [
            ('Torneo de Sumo', 'Deporte', '8000¥'),
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
            precio = f"{random.randint(10, 80)}€"
            events_list.append((f"{title} en {d_name}", tipo, precio))
    
    return events_list
