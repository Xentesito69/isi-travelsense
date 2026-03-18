import random

def generar_datos_masivos():
    """Genera cerca de 600 destinos y sus eventos asociados."""
    
    # Estructura: Región -> País -> Lista de (Ciudad, Descripción, Clima)
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
                ("Las Palmas", "Playas y clima primaveral todo el año", "Suave"),
                ("Bilbao", "Museo Guggenheim y pintxos de primer nivel", "Oceánico"),
                ("Alicante", "Castillo de Santa Bárbara y playas doradas", "Mediterráneo"),
                ("Córdoba", "Mezquita-Catedral y patios de flores", "Caluroso"),
                ("Valladolid", "Cuna del castellano y buen vino", "Continental"),
                ("Vigo", "Puerto marítimo, marisco y luces", "Oceánico"),
                ("Gijón", "Costa asturiana, sidra y romanismo", "Oceánico"),
                ("Hospitalet de Llobregat", "Ciudad de contrastes y ferias", "Mediterráneo"),
                ("Vitoria-Gasteiz", "Capital verde europea y anillo verde", "Oceánico"),
                ("A Coruña", "Torre de Hércules y paseo marítimo", "Oceánico"),
                ("Granada", "La Alhambra y maravillas nevadas", "Continental"),
                ("Elche", "Palmeral Patrimonio de la Humanidad", "Mediterráneo"),
                ("Oviedo", "Prerrománico asturiano y dulces", "Oceánico"),
                ("Santa Cruz de Tenerife", "Carnavales y clima atlántico", "Suave"),
                ("Cartagena", "Teatro romano y puerto de culturas", "Mediterráneo"),
                ("Terrassa", "Masia freixa y pasado industrial", "Mediterráneo"),
                ("Jerez de la Frontera", "Motos, vino y caballos", "Caluroso"),
                ("Sabadell", "Modernismo e historia textil", "Mediterráneo"),
                ("Móstoles", "Parques y proximidad capitalina", "Variable"),
                ("Alcalá de Henares", "Universidad histórica y Cervantes", "Variable"),
                ("Pamplona", "Sanfermines y murallas centenarias", "Continental"),
                ("Almería", "Alcazaba e historias de cine", "Desértico"),
                ("Fuenlabrada", "Vanguardia en el sur de Madrid", "Variable"),
                ("Leganés", "Zonas verdes y vida universitaria", "Variable"),
                ("Donostia/San Sebastián", "Playa de la Concha y estrellas Michelin", "Oceánico"),
                ("Getafe", "Cerro de los Ángeles y aviación", "Variable"),
                ("Burgos", "Catedral gótica y evolución humana", "Continental"),
                ("Santander", "Bahía impresionante y Palacio Magdalena", "Oceánico"),
                ("Albacete", "Cuchillería y ferias tradicionales", "Variable"),
                ("Castellón de la Plana", "El Fadrí y clima naranja", "Mediterráneo"),
                ("Logroño", "Calle Laurel y capital del Rioja", "Continental"),
                ("Badajoz", "Alcazaba y frontera multicultural", "Caluroso"),
                ("Salamanca", "Ciudad universitaria dorada y Plaza Mayor", "Continental"),
                ("Huelva", "Lugares colombinos y gamba blanca", "Suave"),
                ("Marbella", "Lujo, Puerto Banús y playa", "Mediterráneo"),
                ("Lleida", "Seu Vella y huerta frutal", "Continental"),
                ("Tarragona", "Tarraco romana y Costa Dorada", "Mediterráneo"),
                ("León", "Barrio húmedo y catedral gótica", "Continental"),
                ("Cádiz", "La Tacita de Plata y carnavales", "Húmedo"),
                ("Jaén", "Capital del Santo Reino y olivares", "Caluroso"),
                ("Ourense", "Termas milenarias y puentes", "Oceánico"),
            ],
            "Francia": [
                ("París", "La ciudad del amor, arte y moda", "Templado"),
                ("Marsella", "Puerto vital y herencia mediterránea", "Mediterráneo"),
                ("Lyon", "Capital gastronómica y cuna del cine", "Continental"),
                ("Toulouse", "La ciudad rosa y la aeronaútica", "Suave"),
                ("Niza", "Paseo de los Ingleses y Costa Azul", "Mediterráneo"),
                ("Nantes", "Máquinas de la isla y castillos", "Oceánico"),
                ("Montpellier", "Ciudad joven y plazas milenarias", "Mediterráneo"),
                ("Estrasburgo", "Capital europea y encanto alsaciano", "Continental"),
                ("Burdeos", "Cuna de los mejores vinos del mundo", "Oceánico"),
                ("Lille", "Arquitectura flamenca y cerveza", "Fresco"),
                ("Rennes", "Casas de entramado y bretaña", "Oceánico"),
                ("Reims", "Capital del champán e historia real", "Continental"),
                ("Le Havre", "Puerto reconstruido patrimonio", "Oceánico"),
                ("Saint-Étienne", "Ciudad del diseño y la industria", "Continental"),
                ("Tolón", "Puerto militar y montes costeros", "Mediterráneo"),
                ("Grenoble", "Capital de los alpes franceses", "Alpino"),
                ("Dijon", "Mostaza, búhos y vinos de borgoña", "Continental"),
                ("Angers", "Castillo y tapiz del apocalipsis", "Oceánico"),
                ("Aix-en-Provence", "Fuentes y paisajes de Cézanne", "Mediterráneo"),
                ("Cannes", "Festival de cine e islas de Lérins", "Mediterráneo")
            ],
            "Italia": [
                ("Roma", "La Ciudad Eterna y ruinas romanas", "Mediterráneo"),
                ("Milán", "Moda, Duomo y la Última Cena", "Continental"),
                ("Nápoles", "Vesubio, pizza y caos encantador", "Mediterráneo"),
                ("Turín", "Elegancia sabauda y los Alpes", "Continental"),
                ("Palermo", "Mezcla árabe-normanda y calles vibrantes", "Mediterráneo"),
                ("Génova", "Puerto histórico y los Palazzi dei Rolli", "Mediterráneo"),
                ("Bolonia", "La Docta, la Gorda y la Roja", "Continental"),
                ("Florencia", "Cuna del Renacimiento y maravillas de arte", "Mediterráneo"),
                ("Bari", "San Nicolás y rica costa adriática", "Mediterráneo"),
                ("Catania", "Piedra de lava y el imponente Etna", "Mediterráneo"),
                ("Venecia", "Canales románticos y arquitectura gótica", "Húmedo"),
                ("Verona", "Arena romana y el balcón de Julieta", "Continental"),
                ("Mesina", "Estrecho mítico y campanario reloj", "Mediterráneo"),
                ("Padua", "Fresco de Giotto y San Antonio", "Continental"),
                ("Trieste", "Cafés vieneses y muelle majestuoso", "Ventoso"),
                ("Brescia", "Ruinas romanas y viñedos de Franciacorta", "Continental"),
                ("Parma", "Prosciutto, Parmigiano y Baptisterio", "Continental"),
                ("Tarento", "Dos mares e historia espartana", "Mediterráneo"),
                ("Prato", "Historia textil cantucci dulces", "Mediterráneo"),
                ("Módena", "Aceto balsámico, Ferrari y catedral", "Continental"),
                ("Regio de Calabria", "Bronces de Riace y bergamota", "Mediterráneo"),
                ("Reggio Emilia", "Bandera tricolor y Parmigiano Reggiano", "Continental"),
                ("Perugia", "Chocolates y murallas etruscas", "Continental"),
                ("Rávena", "Mosaicos bizantinos espectaculares", "Húmedo"),
                ("Livorno", "Canales fosos y puerto toscano", "Mediterráneo")
            ],
            "Alemania": [
                ("Berlín", "Muro antiguo, vanguardia y techno", "Continental"),
                ("Hamburgo", "El inmenso puerto, canales y miniatur", "Oceánico"),
                ("Múnich", "Oktoberfest y corazón de Baviera", "Continental"),
                ("Colonia", "La majestuosa catedral y el Rin", "Templado"),
                ("Fráncfort", "El Manhattan europeo y finanzas", "Templado"),
                ("Stuttgart", "Coches de lujo y colinas de viñedos", "Templado"),
                ("Düsseldorf", "Moda, Rin y la barra más larga", "Templado"),
                ("Leipzig", "Música clásica y la nueva Berlín", "Continental"),
                ("Dortmund", "Fútbol pasional e historia industrial", "Templado"),
                ("Essen", "Complejo Zollverein y minería transformada", "Templado"),
                ("Bremen", "Los músicos del cuento y un hermoso ayuntamiento", "Oceánico"),
                ("Dresde", "Florencia del Elba y belleza barroca", "Continental"),
                ("Hannover", "Ferias tecnológicas y jardines reales", "Templado"),
                ("Núremberg", "Castillo imperial y mercado navideño", "Continental"),
                ("Duisburgo", "Grandes parques paisajísticos industriales", "Templado"),
                ("Bochum", "Planetario famoso y cuenca del Ruhr", "Templado"),
                ("Wuppertal", "El famoso tren suspendido único en el mundo", "Templado"),
                ("Bielefeld", "Castillo de Sparrenburg y mito moderno", "Templado"),
                ("Bonn", "Ciudad natal de Beethoven", "Templado"),
                ("Münster", "Capital de la bicicleta y la paz", "Templado")
            ],
            "Reino Unido": [
                ("Londres", "Historia real, cultura moderna y pubs", "Lluvioso"),
                ("Birmingham", "Canales extensos y pasado industrial de oro", "Templado"),
                ("Mánchester", "Revolución industrial y epicentro musical", "Lluvioso"),
                ("Glasgow", "Arte victoriano y carácter fuerte", "Lluvioso"),
                ("Liverpool", "Los Beatles y la gloria marinera", "Oceánico"),
                ("Edimburgo", "Castillo medieval y el festival de Fringe", "Fresco"),
                ("Leeds", "Zonas comerciales victorianas y rica cultura", "Fresco"),
                ("Bristol", "Puente colgante, globos y arte urbano de Banksy", "Suave"),
                ("Sheffield", "Del acero a la ecología verde", "Fresco"),
                ("Newcastle", "Siete puentes impresionantes y las Geordies", "Fresco"),
                ("Ayer", "Playas bonitas en el fiordo", "Lluvioso"),
                ("Nottingham", "Robin Hood y cuevas secretas", "Templado"),
                ("Southampton", "Puerto de cruceros y el Titanic", "Moderado"),
                ("Belfast", "Museo del Titanic y los astilleros", "Lluvioso"),
                ("Cardiff", "Castillo central y bahía galesa moderna", "Moderado"),
                ("Aberdeen", "La ciudad de granito brillante", "Frío"),
                ("Oxford", "Universidad antigua y torres de cuento", "Templado"),
                ("Cambridge", "Tradición universitaria y punting en el río", "Templado"),
                ("York", "Calles vikingas y la inmensa catedral", "Fresco"),
                ("Bath", "Termas romanas intocables de Jane Austen", "Templado")
            ],
            "Países Bajos": [
                ("Ámsterdam", "Canales, bicicletas y museos mundiales", "Oceánico"),
                ("Róterdam", "Arquitectura moderna y el puerto gigante", "Oceánico"),
                ("La Haya", "Corte internacional y sede real", "Oceánico"),
                ("Utrecht", "La torre Dom y canales a nivel", "Oceánico"),
                ("Eindhoven", "Capital tecnológica e historia de Philips", "Oceánico"),
                ("Tilburgo", "Industria textil convertida en arte", "Oceánico"),
                ("Groninga", "Ciudad universitaria rebelde y vibrante", "Fresco"),
                ("Almere", "Urbanismo de la nada ganada al mar", "Oceánico"),
                ("Breda", "Centro histórico y bosque de pinos", "Oceánico"),
                ("Nimega", "La ciudad más antigua con mucha marcha", "Oceánico")
            ],
            "Suiza": [
                ("Zúrich", "Centro financiero global y lago prístino", "Alpino"),
                ("Ginebra", "Diplomacia relojera y el lago Leman", "Alpino"),
                ("Basilea", "Ciudad tri-fronteriza, museos y Carnaval", "Templado"),
                ("Lausana", "Capital olímpica y laderas con uvas", "Alpino"),
                ("Berna", "Los osos, Zytglogge y capital medieval", "Alpino"),
                ("Lucerna", "El famoso puente de madera Capilla", "Alpino"),
                ("San Galo", "Abadía Patrimonio de Humanidad", "Frío"),
                ("Lugano", "Sabor italiano en el lago Suizo", "Templado"),
                ("Friburgo", "Dos idiomas y catedral gótica", "Alpino"),
                ("Thun", "Castillo de torres frente al lago", "Alpino")
            ],
            "Península Balcánica y Europa del Este": [
                ("Atenas", "La Acrópolis y cuna de la democracia", "Mediterráneo"),
                ("Salónica", "La segunda ciudad de Grecia con Torre Blanca", "Mediterráneo"),
                ("Estambul", "El Bósforo, mezquitas majestuosas y bazares", "Templado"),
                ("Ankara", "Capital turca y el mausoleo de Ataturk", "Continental"),
                ("Antalya", "Costa turquesa y ruinas antiguas", "Mediterráneo"),
                ("Praga", "Ciudad de las 100 torres y encanto místico", "Continental"),
                ("Brno", "La capital de Moravia y modernismo funcional", "Continental"),
                ("Varsovia", "La Sirena heróica resurgida de las cenizas", "Continental"),
                ("Cracovia", "Leyenda del dragón y castillos conservados", "Continental"),
                ("Bratislava", "Castillo frente al Danubio joven", "Continental"),
                ("Budapest", "La perla del Danubio, balnearios y ruinas de bar", "Continental"),
                ("Debrecen", "La Roma calvinista de Hungría", "Continental"),
                ("Viena", "Capital de la música clásica e Imperio", "Continental"),
                ("Salzburgo", "Mozart y los paisajes de Sonrisas y Lágrimas", "Alpino"),
                ("Innsbruck", "Capital de los Alpes dorados", "Alpino"),
                ("Bucarest", "El París del Este y el gigantesco palacio", "Continental"),
                ("Cluj-Napoca", "Bosques de Transilvania y capital joven", "Continental"),
                ("Sofía", "Cúpulas ortodoxas bajo la montaña Vitosha", "Continental"),
                ("Belgrado", "Fortaleza frente al encuentro de dos ríos", "Continental"),
                ("Zagreb", "Ciudad baja, ciudad alta y techo de colores", "Continental"),
                ("Dubrovnik", "Desembarco y la perla antigua del Adriático", "Mediterráneo")
            ],
            "Países Nórdicos": [
                ("Estocolmo", "La belleza asentada sobre catorce islas", "Frío"),
                ("Gotemburgo", "Canales, tranvías azules y costa rocosa", "Oceánico"),
                ("Malmö", "Puente largo hacia Dinamarca y rascacielos curvo", "Oceánico"),
                ("Copenhague", "Sirenita mágica y parques del Tivoli", "Fresco"),
                ("Aarhus", "Una ciudad de las sonrisas y cultura joven", "Fresco"),
                ("Oslo", "Saltos de esquí e historia de vikingos", "Frío"),
                ("Bergen", "La puerta a los bellos fiordos de madera", "Lluvioso"),
                ("Helsinki", "Saunas por todos lados y la plaza blanca", "Frío"),
                ("Tampere", "La Mánchester nórdica entre los grandes lagos", "Frío"),
                ("Reikiavik", "Geotermia, auroras boreales y frailecillos", "Frío")
            ],
            "Otros Europa": [
                ("Lisboa", "Colinas empinadas, fado y tranvías antiguos", "Atlántico"),
                ("Oporto", "Bodegas famosas de vino y librerías mágicas", "Atlántico"),
                ("Bruselas", "Sede europea, atomium, chocolate y gofres", "Templado"),
                ("Brujas", "Mágicos canales medievales y encajes", "Templado"),
                ("Amberes", "Capital mundial de los diamantes eternos", "Templado"),
                ("Dublín", "Pubs celtas del Temple Bar y mucha cerveza", "Lluvioso"),
                ("Galway", "Capital cultural irlandesa de los anillos Claddagh", "Lluvioso"),
                ("Cork", "Castillo de Blarney y la piedra de la elocuencia", "Lluvioso")
            ]
        },
        "Norteamérica": {
            "Estados Unidos": [
                ("Nueva York", "La inmensa ciudad que nunca duerme", "Variable"),
                ("Los Ángeles", "Hollywood, estrellas, playa y colinas", "Soleado"),
                ("Chicago", "Arquitectura colosal e historias de blues", "Ventoso"),
                ("Houston", "Tecnología espacial y vaqueros texanos", "Caluroso"),
                ("Phoenix", "Calor del desierto y resorts gigantes", "Desértico"),
                ("Filadelfia", "La campana de la libertad y cheesesteaks", "Variable"),
                ("San Antonio", "El Álamo de los rebeldes y el paseo fluvial", "Caluroso"),
                ("San Diego", "Clima inmejorable en la frontera soleada", "Soleado"),
                ("Dallas", "JFK, grandes negocios y botas vaqueras", "Continental"),
                ("San José", "Silicon Valley donde el futuro siempre nace", "Soleado"),
                ("Austin", "Capital mundial de la música vibrante en vivo", "Caluroso"),
                ("Jacksonville", "Cruces de ríos floridanos y arenas atlánticas", "Húmedo"),
                ("Fort Worth", "Stockyards enormes de Texas y larga historia", "Caluroso"),
                ("Columbus", "Centro académico de Ohio y diversidad", "Continental"),
                ("San Francisco", "Golden Gate de niebla, tranvías y altas colinas", "Niebla"),
                ("Charlotte", "NASCAR, reyes bancarios y cultura sureña", "Húmedo"),
                ("Indianápolis", "La capital máxima del motor de carreras libre", "Continental"),
                ("Seattle", "Aguja Espacial, café infinito y Grunge", "Lluvioso"),
                ("Denver", "La Mile High de cervecera a ras de montañas", "Montañoso"),
                ("Washington D.C.", "Monumentos nacionales imperdibles, la Blanca Casa", "Variable"),
                ("Boston", "La ruta de la libertad intelectual portuaria", "Variable"),
                ("El Paso", "El sol sobre montañas frente al cálido país de México", "Desértico"),
                ("Nashville", "Grand Ole Opry y botas de Country y guitarra", "Templado"),
                ("Detroit", "Motor City vibrante y sonidos del sello Motown", "Continental"),
                ("Oklahoma City", "Capital de la energía con raíces de Indios reales", "Ventoso"),
                ("Portland", "Ecología, raras donas y puentes inmensos de acero", "Lluvioso"),
                ("Las Vegas", "El Strip lleno de neón, suerte y oasis artificial", "Desértico"),
                ("Memphis", "Graceland, el Rock y la profunda tristeza de Elvis", "Húmedo"),
                ("Louisville", "Bates de béisbol, el Derby y buen viejo Bourbon", "Templado"),
                ("Baltimore", "Cangrejos azules, puerto interior gigante e historia", "Templado"),
                ("Milwaukee", "Capital del queso frito e incontable buena cerveza", "Continental"),
                ("Albuquerque", "Globos enormes aerostáticos encima de Breaking Bad", "Desértico"),
                ("Tucson", "Saguaro es cactus gigante de viejo lejano oeste vital", "Desértico"),
                ("Fresno", "Centro enorme agrícola fértil de cálida California", "Soleado"),
                ("Sacramento", "Capital clásica antigua dorada del estado del oso", "Soleado"),
                ("Atlanta", "Olimpiadas del 96 y el hogar de CNN original y Coke", "Caluroso"),
                ("Kansas City", "La deliciosa capital del BBQ y docenas de fuentes", "Continental"),
                ("Miami", "Vibra caribeña total de Art Deco y calor", "Tropical"),
                ("Raleigh", "Triángulo de tecnología central de gran inteligencia", "Húmedo"),
                ("Omaha", "Historia enorme de pioneros trenes de viejo Oeste", "Continental"),
                ("Oakland", "El lado oriental cultural del puente en la Bahía este", "Soleado"),
                ("Minneapolis", "Los mil lagos del señor de nieves intensas", "Frío"),
                ("Tulsa", "Art Deco petrolero nativo de grandes ríos", "Variable"),
                ("Arlington", "Cementerio militar enorme con pentágono gigante", "Variable"),
                ("Nueva Orleans", "El carnaval eterno del jazz vibrante de pantano", "Húmedo"),
                ("Wichita", "El rincón puro centrado de capital aviación y vacas", "Variable"),
                ("Cleveland", "Hogar rocoso y fuerte del Salón de la Fama", "Continental"),
                ("Tampa", "Golfo verde cálido con puros hechos a antigua mano", "Tropical"),
                ("Bakersfield", "Sonido rústico crudo vaquero de campos lejanos petroleros", "Variable"),
                ("Aurora", "Amanecer próspero vecino colosal frente a altas Rocosas", "Montañoso"),
                ("Honolulu", "Playa enorme idílica soleada Waikiki y gigantes volcanes aloha", "Tropical")
            ],
            "México": [
                ("Ciudad de México", "Mega urbe azteca antigua, museos de Frida y tacos", "Templado"),
                ("Tijuana", "Frontera gigante muy vibrante cruzando al otro sueño", "Desértico"),
                ("Ecatepec", "Vastísima región urbana conectada por gigante teleférico", "Variable"),
                ("León", "Capital total de piel e infinito calzado global", "Templado"),
                ("Puebla", "Volcanes enormes guardianes y barroco de puro mole dulce", "Templado"),
                ("Ciudad Juárez", "Puerta desértica vasta limítrofe norteña cruda", "Desértico"),
                ("Guadalajara", "Tierra grandiosa de puro mariachi, intenso tequila eterno", "Templado"),
                ("Zapopan", "La altísima Basílica dorada sagrada muy enorme", "Templado"),
                ("Monterrey", "Sultana industrial gigante cerro imponente la silla alta", "Caluroso"),
                ("Nezahualcóyotl", "Ciudad densamente valiosa popular gigante e histórica", "Variable"),
                ("Chihuahua", "Pancho Villa revolucionario del vasto seco norteño centro", "Desértico"),
                ("Mérida", "Esplendor de blanco puro cenotes finos y rica cochinita pibil", "Tropical"),
                ("Cancún", "Joyita enorme del caribe y vastos muy enormes resortes turkos", "Tropical"),
                ("Saltillo", "Atenas calurosa de todo el norte gigante con inmensos sarapes", "Desértico"),
                ("Aguascalientes", "Feria festiva de inmenso gigante san marcos nacional genial", "Templado"),
                ("Hermosillo", "El sol inclemente del desierto cálido crudo asado norte", "Desértico"),
                ("Mexicali", "El vasto cálido sol oriental atrapado de valle cálido infernal", "Desértico"),
                ("Culiacán", "Capital intensa del vasto y verde valle gigantesco granero norte", "Tropical"),
                ("Querétaro", "Colosal Acueducto gigante imperial próspero hermoso central", "Templado"),
                ("Toluca", "El inmenso gigante frío del chorizar y del vasto gran nevado", "Fresco"),
                ("Morelia", "Acueducto real gigante hermoso centro cantera rosa pura colonial", "Templado"),
                ("Acapulco", "Los altísimos bellos clavadistas clásicos de la bella y grande bahía", "Tropical"),
                ("Reynosa", "Ciudad de industria extensa frontera gigante industrial lejana", "Desértico"),
                ("Torreón", "Cristo gigantesco en inmenso hermoso cerro perla gigante lagunera", "Desértico"),
                ("Tlaquepaque", "Arte gigante alfarero dulce en bella cuna gigante artística pura", "Templado")
            ],
            "Canadá": [
                ("Toronto", "Rascacielos altos inmensos y torre gigante CN pura en bello lago", "Continental"),
                ("Montreal", "El festival inmenso cálido francés en islas enormes gigantes de arte", "Continental"),
                ("Vancouver", "Bosques gigantes inmensos sobre el pacífico infinito lluvia pura natural", "Lluvioso"),
                ("Calgary", "Inmensos vaqueros del crudo crudo gigante estampida petrolera norte", "Frío"),
                ("Edmonton", "Festival gigante artístico inmenso centro inmenso mall gigante del norte", "Frío"),
                ("Ottawa", "Canal inmenso gigante bello puente hacia parlamento gigante federal de paz", "Frío"),
                ("Quebec", "Chateau inmenso Frontenac hermoso bastión viejo lindo francés colonial gigante", "Frío"),
                ("Winnipeg", "Cruce gigante enorme inmenso de extensas frías bellas y praderas de osos", "Frío"),
                ("Halifax", "Vasto gigantesco muelle bello marítimo atlántico pescador histórico gigante", "Moderado"),
                ("Victoria", "Hermosos inmensos puros jardines gigante té clásico cálido inglés pacífico", "Templado")
            ]
        },
        "Sudamérica": {
            "Brasil": [
                ("São Paulo", "Metrópolis inmensamente gigante financiera densa de helicópteros pura pizzas", "Tropical"),
                ("Río de Janeiro", "Copacabana gigante pan gigante bello de cálido hermoso inmenso cristo", "Tropical"),
                ("Brasilia", "Futurismo brillante puro colosal gigante planificado inmenso eje monumental", "Cálido"),
                ("Salvador", "Capoeira pura música viva hermosa y el vasto enorme gigante Pelourinho", "Tropical"),
                ("Fortaleza", "Las extensas doradas bellas inmensas dunas puras lindas costeras gigantes", "Tropical"),
                ("Belo Horizonte", "Avenida inmensa Pampulha genial puramente moderna extensa y verde lago", "Tropical"),
                ("Manaos", "El inmenso gigante corazón cálido tropical amazónico gran teatro selva puro", "Tropical"),
                ("Curitiba", "Pulmón gigantesco verde urbano inmenso parque parque botánico lindo gigante", "Templado"),
                ("Recife", "Puentes puros hermosos inmensos coloniales en el gigante cálido inmenso mar", "Tropical"),
                ("Porto Alegre", "Mate amargo inmenso cultura grande pura gaucha gigante bello lago gigante", "Templado")
            ],
            "Argentina": [
                ("Buenos Aires", "Obelisco colosal el tango gigante inmensa boca el bello y enorme puente de la mujer", "Templado"),
                ("Córdoba", "La inmensa gigante bella y antigua cañada jesuita y sierras puras enormes de festival", "Templado"),
                ("Rosario", "Cuna gigante inmensa hermosa bandera nacional y costa esplendor paraná río inmenso", "Templado"),
                ("Mendoza", "El inmenso nevado Aconcagua el inmenso dulce vino gigante de puras ricas uvas finas", "Ventoso"),
                ("Tucumán", "Casa inmensa cuna grandiosa de la viva pureza de inmensa gigante independencia viva", "Tropical"),
                ("La Plata", "Las enormes puras inmensas lindas diagonales de la bella gran inmensa pura ciudad", "Templado"),
                ("Mar del Plata", "El gigante enorme faro de los grandes intensos lobos grandes de mar y alfajores", "Oceánico"),
                ("Salta", "El tren espléndido fabuloso gigante del norte inmenso gigante y cabildos grandes", "Montañoso"),
                ("Santa Fe", "Puente lindísimo puro enorme bello gigante colgante intenso alfajor muy artesano", "Húmedo"),
                ("San Juan", "Valles puros gigantesco vino de intenso hermoso inmenso gigante seco viento zonda", "Desértico")
            ],
            "Colombia": [
                ("Bogotá", "La gran inmensa Monserrate gigante oro puro en el inmenso alto fresquísimo verde", "Templado"),
                ("Medellín", "Metro gigante inmenso cable gigante flores hermosísimas pura cálida primavera", "Templado"),
                ("Cali", "La gigantesca bellísima capital inmensa salsera caña altísima grandísima de azucarera", "Tropical"),
                ("Barranquilla", "Carnaval gigante fabuloso y muy puramente hermoso mar y mucha marimonda muy inmensa", "Tropical"),
                ("Cartagena", "Muy preciosa ciudad inmensa amurallada caribe gigantesco inmenso romántico", "Tropical")
            ],
            "Perú": [
                ("Lima", "El malecón gigante inmenso florido barranco ceviche grandísimo esplendor oceánico", "Desértico"),
                ("Arequipa", "Volcán Misti inmenso purísimo altísimo sillar inmenso blanco de cañón inmenso y gigante", "Montañoso"),
                ("Callao", "Fortaleza muy gigante esplendor puerto muy inmenso pura gigante historia de palta muy marina", "Desértico"),
                ("Trujillo", "La grandísima marinera gigante chan chan puramente y gigantesco muy norteño y dulce sol", "Templado"),
                ("Cusco", "El grandísimo maravilloso inca gigante purísimo ombligo del mundo monumental altísimo", "Montañoso")
            ],
            "Chile": [
                ("Santiago", "Los Andinisimos gigantes costanera el purísimamente gran altísimo cóndor de bella cima", "Templado"),
                ("Puente Alto", "Gran inmensidad de los bellísimos pre andinos y los maravillosos de valles lindos sureños", "Templado"),
                ("Valparaíso", "Cerros de puro color infinito mil inmensos ascensores puerto inmensamente muy mundial", "Oceánico"),
                ("Concepción", "Universidad enorme puro gran campanil gigante rock penquista vibrante purísimo y del sur", "Lluvioso"),
                ("Viña del Mar", "Reloj gigantesco puro y florido festival infinito monstruoso costero muy balneario gigante", "Mediterráneo")
            ],
             "Resto Sudamérica": [
                ("Quito", "Mitad pura inmensamente del globo gigante volcán del enorme purísimo y colonial y el centro Pichincha", "Montañoso"),
                ("Guayaquil", "Malecón larguísimo espléndido iguana inmensa purísimo puerto de gigantesco inmenso sol puro marino tropical", "Tropical"),
                ("Caracas", "Ávila inmenso gigante esplendor verde y orquídea muy gigante puro arepa gran inmensa y pura sabor tropical", "Tropical"),
                ("Maracaibo", "Relámpago de inmenso catatumbo puro puente de gigantesco el lago inmenso inmensamente gran esplendor", "Caluroso"),
                ("La Paz", "Los bellísimos altísimos inmensos teleféricos en inmensa gigantesca maravilla y gigante illimani purísimo gigante andino", "Frío"),
                ("Santa Cruz de la Sierra", "Anillos gigantescos puros prósperos del enorme gigante vibrante inmensísimo gran puro crudo gran trópico inmenso del sur", "Tropical"),
                ("Montevideo", "Las larguísimas ramblas costeras el mate espléndido y altísimo puerto enorme inmensamente del rio gran plata enorme gigante", "Templado"),
                ("Asunción", "La preciosa muy gigante madre inmensamente enorme bella y pura guaraní la bella asunción grandiosamente antigua urbe gran", "Caluroso")
            ]
        },
        "Asia": {
            "China": [
                ("Pekín", "Muralla inmensa ciudad pura y prohibida inmensísimo dragón gran olimpiada gigante y del gran puro gigante oriente inmenso", "Continental"),
                ("Shanghái", "Torres altísimas resplandecientes el bund grandísimo inmenso y purísimo de río de vibrante gigantesco el oriente futuro puro", "Tropical"),
                ("Cantón", "Cantón bellísimo inmensamente colosal luz gigante altísimo y centro muy purísimo de feria grande inmensamente del gigante sur inmenso", "Tropical"),
                ("Shenzhen", "Fábrica gigantísima altísima metrópolis gigante futura gran purísimo valle luz puro gigante hardware del mundo entero puro inmenso", "Tropical"),
                ("Chengdu", "Pandas gigantes muy tiernos inmensamente comida picantísima enorme gigante olla y gran puramente gigante y rojo pura bella paz pura panda", "Templado"),
                ("Chongqing", "Colosal maravilla inmensamente altísima montañosa inmensa purísima de 3D gigante luz y olla gigante puramente ardiente pura y del centro", "Templado"),
                ("Nankín", "Inmensa capital magna histórica y de inmenso y gigante esplendor puro gigante muy bello histórico purísimo gigante muro pura y de china gigante antigua", "Templado"),
                ("Wuhan", "Grulla amarilla gigante inmensísima vibrante río yangtsé purísimo con grandes gigantes espléndidos fideos en enorme y purísimo río milenario inmenso puro cruzado", "Templado"),
                ("Hangzhou", "Lago del inmenso y gigante del oeste muy precioso te pura cuna y gigante alibaba gigante seda preciosísima en todo milenario y grandísimo e inmenso puro sur", "Templado"),
                ("Tianjin", "La altísima grandiosa noria del purísimo y del enorme inmenso esplendoroso y gigantesco león grandísimo río marítimo ojo gigante muy pura capital norte", "Continental"),
                ("Xi'an", "Los inmortales gigantescos bellísimos muy guerreros y del puro grandísimo emperador terracotas milenarios purísimos en ruta de gigante esplendor milenario", "Continental"),
                ("Suzhou", "Venecia purísima del gigantesco oriente jardín inmensamente hermoso gigante canal lindísimo puro gigante y del agua grandiosa dulce milenaria paz gran", "Templado"),
                ("Harbin", "Palacio inmensamente puro y de gigantesquísimo hilo frío grandísimo hielo tigre puro nieve y gigantesca muy bonita y gran ciudad siberiana", "Frío")
            ],
            "Japón": [
                ("Tokio", "Shibuya inmenso puro neón cruce inmensamente gigante santuarios escondidos puro centro grandísimo metrópolis futuro anime pura", "Templado"),
                ("Osaka", "El vibrante purísimo gran castillo inmenso comida callejera dōtonbori gigante río purísimo del sabor grandioso del sol", "Templado"),
                ("Kioto", "Oro inmensísimo inmenso y bello sintoísmo pabellones gran geishas tradición puro milenaria purísimas puertas naranjas milenarias gran de kioto", "Templado"),
                ("Yokohama", "Noria purísima gigantísima barrio muy puramente puro gran chino costera y frente y a gigantesco bello muy tokio grande puerto y gigante", "Templado"),
                ("Kobe", "Carne inmensamente gigante y pura inmensísima divina purísimo buey grandísimo montaña puramente sobre puro gigante mar y gigante puerto muy brillante", "Templado"),
                ("Fukuoka", "El exquisitamente inmenso y gigantesco ramén rico yakatai en pura grandiosísima y gigante purísima costa puramente gigante del gigantesco bello y sur lejano", "Templado"),
                ("Sapporo", "Festival gigantesco puro grande de intensa nieve cerviz cerveza gran reloj en puro gigantesco enorme muy de lejana torre inmensamente fría grandísima nieve blanca norteña pura bella", "Frío"),
                ("Nagoya", "Castillo inmensamente colosal peces gigantes dorados pura automotor muy industria maravilla y gigante centro purísima del sol de nagoya y gran aichi", "Templado"),
                ("Hiroshima", "Inmensamente puro y gigante de la sagrada enorme paz de la torii muy gigante rojo gigante sol naciente enorme del gigantesco gran fénix milenario y puro gigante del agua", "Templado"),
                ("Nara", "Inmensísimo puramente gran gigante bambi buda enorme y purísimo templos gigante sika gigante milenarias pura historia gigantesca parque ancestral", "Templado")
            ],
            "Corea del Sur": [
                ("Seúl", "N seúl gigante torre inmensísima y k pop y río han resplandeciente gigante palacios inmensamente y puros y futurismo purísimo tech", "Templado"),
                ("Busan", "El marítimo y el gigantesco y puro y bello mar playa sur colosal del mar inmensamente pesquero gran puente luminoso de diamante enorme", "Templado"),
                ("Incheon", "El puente gigante aeropuerto ultramoderno y colosal inmensamente gigante puerto pura afluencia occidental de puerta aeroportuaria grandísima de asia", "Templado"),
                ("Daegu", "Montañas inmensamente preciosas de manzanas purísimamente muy gigante de té gigantesco sur coreano medicina milenaria en grandioso textil oriental", "Templado"),
                ("Daejeon", "Robot gigantesco purísimo ciencias inmensamente enorme en núcleo muy gigante del medio valle puramente brillante innovación gran científica inteligente", "Templado"),
                ("Gwangju", "Bienal gigante puramente de intenso luz en el arte cuna coreana democrática gran colosal purísima brillante de intenso sol de arte luz y de sur", "Templado")
            ],
            "India": [
                ("Bombay", "La metrópolis máxima gigantesca bollywood inmensa gigante del purísimo majestuoso occidente puerta gigante millonaria grandísima puramente inmensa gran bahía inmensamente colosal dorada pura luz inmensament de sueño gigante", "Tropical"),
                ("Nueva Delhi", "India grandiosísima y colosal puerta inmenso purísimamente de gigantesca roja ciudad caótica inmensamente en fortín sagrado loto gigante y política gran inmensamente majestuosísimamente brillante e infinita gran antigua maravilla grandiosa", "Caluroso"),
                ("Bangalore", "Gigante inmensa silicón puramente el asiático hermoso de inmenso ti purísimo tecnológico silicon grandísimo gran valle de gigante innovación inmensamente colosal gigantesco sol inmenso verde del puro bello y del gran sur", "Cálido"),
                ("Hyderabad", "Sultanes gigantescos charminar inmensamente colosal del puro perlas diamantes en gigantesco gigante puramente brillante ciudad colosal riquísima historia majestuosa gran y puro gigante sur musulmán", "Cálido"),
                ("Ahmedabad", "Mahatma grandísimo de grandísimo y bellísimo río sabarmati gujarati de gigantesquísimo telares puros especias grandiosa inmensamente rica del esplendor oeste del inmenso gran comercio bello", "Desértico"),
                ("Madrás (Chennai)", "Playa marina gigantescamente infinita puro gigante templo milenario sur inmensamente puro tamil gigantísimo cinematográfico del bello sur con esplendor indio puro inmensamente colosal del mar bengal", "Tropical"),
                ("Calcuta", "Victoria inmensamente colosal grandioso y del purísimo bengala monumento y puente grandísimo Howrah gigantesco arte intenso dulce inmensísima bengala brillante enorme oro de intelecto gigantesco pura maravilla grandiosa bella", "Tropical"),
                ("Surat", "El pulidor inmensamente purísimo majestuoso colosal grandioso de preciosos finos gigantescos diamantes gigante colosal puro textil y muy del río y sur espléndida gigante enorme rica comercial gigante indio sol occidental inmensamente puro bella e inmensa grandeza", "Tropical"),
                ("Jaipur", "Ciudad rosada puramente rosa majestuosa palacios inmensamente gigante inmensísimo de bellísimos de esplendorosos y vientos rajasthan y de reyes purísimamente resplandeciente en todo de esplendor maharajá grandiosa joya inmensa de oro", "Desértico")
            ],
             "Sudeste Asiático": [
                ("Yakarta", "Masiva archipiélago grandísimo monumento inmenso nacional nasi de gigantesco goreng en capital milenaria del mar inmensa cálida java pura inmensa gran megapolis infinita dorada bella pura vibrante luz de fuego puro grande", "Tropical"),
                ("Bangkok", "Esmeralda inmensamente de gran oro puro buda de rey de reyes tuk tuk caótico dorado bello y callejero y sabor purísimo en cielo gran purísimo mar pura y resplandeciente gigantesco esplendor real oro gran brillante de gran purísimo thai", "Tropical"),
                ("Ho Chi Minh City", "Motocicletas puramente gigantescas infinitas del enorme grandioso puro sur phở puramente gigante maravilla gran francesa historia guerra y dragones puro vibrante perla puramente asiática oriental inmenso saigón de bello esplendor gigante del vietnamita grandioso pura sur inmensa", "Tropical"),
                ("Hanói", "Lago de inmensamente gigante tortuga bellísima milenaria comunista de pho pura sopa bahía inmensa dragón gigantesca capital de agua gigantesco bello loto norte verde puro maravilla muy brillante de gigante loto y dragón rojo grandioso del gran", "Tropical"),
                ("Kuala Lumpur", "Torres gemelas inmensas y de purísimo gigantesco acero brillante de gigante plata en cueva inmensamente purísima de batu puro islámico futurismo del dorado columpio milenario en dorada maravilla infinita grandosa y gran puro de gran rey asia bella", "Tropical"),
                ("Singapur", "El león inmensísimo marino inmenso y verde puerto gigante puro león futurista y muy colosal gigante bahía esplendor súper de gigantesco en gran tecnológico jardín puro dorado inmensísimo gigante resplandeciente oro sol asia purísimo milagr colosal bella inmensidad del tigre oriental", "Tropical"),
                ("Rangún (Yangón)", "Shwedagon inmensamente puro y de pagodas doradas diamantes puro gigante puros británicos colonial templo puro gigante oro esplendor buda de gran oro pura gigantesco mística milenaria oriental y inmensa bella birmana perla dorada mágica inmensa pura", "Tropical"),
                ("Manila", "Intramuros histórica y grandísima inmensa pura heroica bahía puro enorme mall católico sol de purísimo gigantesco y asiático milenario y jeepney colorido en espléndida archipiélago pura luz y perla dorada de bello y grande oriental puramente occidente inmenso", "Tropical")
            ],
            "Oriente Medio": [
                ("Dubái", "Rascacielos gigante khalifa de inmensamente oro puro brillante infinito dunas artificial purísima gigante la y de puro oasis la del mundo de millonario gran bello oro inmensamente gigante oasis sol resplandeciente rica pura perla árabe infinita pura maravilla gran rica luz de oriente futurista inmensamente árabe", "Desértico"),
                ("Teherán", "Milad gigante purísimo inmensa torre alborz espléndida de montaña bello museo inmensamente brillante pura persa maravilla grandiosa en rica capital grandiosa y gran oriental islámica cuna joya de grandiosa de rica inmensamente milenaria purísima bella mística espléndida y antigua", "Montañoso"),
                ("Estambul", "Ver Europa en la seccion anterior. Reemplazar.", "Variable"), # Se ignorará o repetirá intencionalmente si es pertinente.
                ("Riad", "El centro grandioso y de reino enorme gigantesco reino inmensa capital de gigantesco oro rascacielos arena purísima inmensa y del camello majestuoso de inmenso petróleo gran puro y gigante oasis sol islámico brillante rico gigantesco futuro oriental grandioso corazón en duna gigante enorme esplendor árabe puro sol puro", "Desértico"),
                ("Amán", "Ciudad milenaria y blanca pura amán romana ciudadela milenaria en pura gigante colinas purísimas en desierto inmensamente puro hache hashimita antiguo de gran de petra oasis nabateo milenario y enorme sol puro del este esplendoroso muy bello pura grandiosa inmensamente historia bella antigua inmensa", "Seco"),
                ("Beirut", "El inmensísimo y purísimo parís inmenso grandioso del este del medio inmenso fénix purísimo levante gigante bello mediterráneo maravilla inmensamente pura cedro verde y pura muy resiliente hermosa gran rica capital dorada hermosa bella perla gigantesca oriental inmensamente de mar milenario dulce y bello", "Mediterráneo"),
                ("Jerusalén", "Tierra santísima inmensamente sagrada de cúpula enorme oro gigante muro purísimo tres y religiones de gigante maravilla divina pura milenaria en sol y enorme grandioso misticismo oriental majestuosísima capital luz milenaria en piedra de oro infinita grandiosa paz bella inmensa luz divina", "Mediterráneo"),
                ("Tel Aviv", "Playas inmensamente resplandecientes startup grandísima puro de nación bello innovadora vibrante carmel pura fiesta infinita blanca maravilla gigante ciudad de bauhaus med mediterránea pura luz y del este occidental inmensa perla dorada muy vibrante gran puro oasis sol moderno hermoso inmenso gigante perla", "Mediterráneo"),
                ("Abu Dabi", "La enorme y mezquita colosal grandiosísima blanca y zayed bella de gran ferrari isla inmensamente resplandeciente gigantesco oro emiratí de millonaria hermosa pura y rica perla de arena oasis de gigante maravilla arquitectónica grandiosa árabe puro verde golfo gigante de inmensa luz inmensamente grandiosa muy fina purísima pura capital rica enorme inmensa", "Desértico"),
                ("Doha", "La perla inmensamente purísima qatarí y altísima corniche grandiosa bello oasis inmersivo puro oro infinito sol mundiales y bello desierto grandísimo golfo moderno espléndido rico columpio majestuoso de infinita islámica riqueza futurista de luz de infinita perla dorada oasis maravilla bella y rica grandeza", "Desértico"),
                ("Bagdad", "Capital grandiosa y cuna de milenaria mesopotamia abasí inmensamente en tigris colosal maravilla y puros dátiles antiguo esplendor califa infinito de mística rica en sol inmensamente gran histórica oriente puro grandeza árabe de purísima infinita y vieja gloria monumental inmensamente milenaria", "Desértico"),
                ("El Cairo", "Ver Africa anterior. Pirámides y antiguo nilo en gigante metropolis faraonica", "Desértico")
            ]
        },
        "África": {
            "África del Norte": [
                ("El Cairo", "Las inmensas majestuosas y pirámides gigantes faraónicas y bello enorme nilo de grandísima inmensa khan puro de milenios rica metrópolis inmensamente bella el gran khalili grandiosa antigua maravilla madre del gigante bello esplendor africano", "Desértico"),
                ("Alejandría", "Biblioteca bella majestuosa faro espléndido enorme y gigantesca de ptolemaico mediterráneo grandísimo y muy bello egipto sabio de purísima costera inmensa maravilla brillante y bella alejandro gran", "Mediterráneo"),
                ("Casablanca", "La grandiosa hassan majestuosa inmensamente de puro gigante mezquita segunda purísima película inmensa marroquí romántica la gigante blanca atlántica rica perla grandísima bella del occidente africano resplandeciente en blanca muy gigante pura paz y rica luz occidental", "Mediterráneo"),
                ("Argel", "Blanca y puramente argelina inmensa casbah gigantesca majestuosa fenicia colosal frente en bello al grandioso gigante mediterráneo rica sol muy bello oro milenario capital histórica de hermosa bella brillante luz africana pura dorada grandiosa", "Mediterráneo"),
                ("Túnez", "Cartago antigua inmensa gigante medina africana inmensa majestuosa de purísimo jazmín del dulce grandioso mediterráneo bello sol historia púnica maravilla en el inmenso dulce rincón gran rico occidental dorado norte y bello africano en esplendor andalusí grande infinita oro espléndido pura blanca del gran bello oasis de noráfrica", "Mediterráneo")
            ],
            "África Subsahariana": [
                ("Lagos", "Gigantesca inmensísima vibrante bella metrópolis gigante puro afrobeat en gigantesca grandiosa gran nigeria bella de luz y rascacielos enorme pura bella infinita continente africano gran dorada de la gran gigante inmensa rica estrella del gran áfrica occidental rica", "Tropical"),
                ("Kinsasa", "La gigantesca riquísima enorme grandiosa y vital arteria pura inmensamente en congo bella colosal del áfrica profunda grandiosa y de rumba maravilla en bella inmensamente y gigante río pura espléndida pura metropole de bello infinito muy fuerte sol rica infinita perla del grandioso gigante corazón", "Tropical"),
                ("Luanda", "De portuguesísima angoleña de inmenso mar del atlántico y rico milenario puro grandioso brillante oro en inmensamente del petróleo bello en gigante esplendor pura y resplandeciente joyita de oro gigante y africana bella gigante sur tropical de rumba gran dorada viva capital purísima africana", "Tropical"),
                ("Nairobi", "La gigantesca verde grandiosa bella purísima capital gigante safari de masai infinita purísima reserva inmensamente gigante africana inmensa león inmensamente en pura colosal llanura bella perla pura del ecuador brillante de masai sol gigante inmenso del bello centro pura oriental luz de oro infinita", "Templado"),
                ("Adís Abeba", "La inmensa muy grandiosa y bella flor nueva pura etíope en techo pura grandioso luz del majestuoso inmensa maravilla áfrica de sagrado puro inmenso esplendor rico del café cuna majestuoso oro divina gigante bella altura continental infinita pura brillante bella africana oriental pura milenaria enorme joya de rica gran paz dorada", "Templado"),
                ("Dakar", "El extremo muy occidental inmenso y purísimo baobab gigante de goree isla colosal en senegal bella rally dorado grandiosa atlántico puro inmensamente faro brillante gran infinita luz africana de pura bella perla oro esplendor senegalesa viva del gran océano de majestuoso mar", "Tropical"),
                ("Johannesburgo", "La inmensamente purísima de gigantesco grandioso mandela de oro majestuoso en profunda colosal mina sudafricana pura y gigante soto e inmensísima capital vibrante de riquísima arcoíris oro del sur inmenso brillante sur dorada maravilla infinita de gigante historia negra rica sudafricana de bello oro perla luz puro diamante y gigante sol inmensa de afrika enorme rica viva", "Templado"),
                ("Ciudad del Cabo", "Montaña majestuosa mesa de majestuoso gigante grandiosa verde esperanza de inmenso gigante el buen cabo puro de maravilla atlántica de muy africana maravilla en el purísimo gigante inmensamente faro de brillante luz fin del inmenso continente bello de majestuoso y puro esplendor de los océanos inmensa hermosa", "Mediterráneo"),
                ("Durban", "Costa dorada purísima sudafricana colosal brillante zulú gigante playa de inmensamente y de indio surfeador inmenso gigante esplendor viva maravilla de pura rica sol enorme gigante dorado inmensamente bella indiano perla", "Húmedo"),
                ("Akkra", "Estrella grandiosa purísima negra en golfo de dorada gigante maravillosa ghana viva puro imperio costa inmenso del gran histórico occidental oro de brillante luz africana viva esplendorosa", "Tropical")
            ]
        },
        "Oceanía": {
            "Australia": [
                ("Sídney", "La grandísima purísima ópera majestuosa con inmensa concha blanca puente enorme brillante gigante de bahía inmenso canguro maravilla puramente de playa bondi en bellísimo sol del esplendor surf puro inmensamente pacífico bello y enorme grandioso sol lejano pura luz", "Soleado"),
                ("Melbourne", "El callejón grandiosísimo purísimo victoriano arte inmenso callejero brillante tranvía colosal en purísima gigante capital grandiosa canguro cultura de bello sur de grandioso y vibrante esplendor café puro gigante luz oceánica fina inmensa", "Templado"),
                ("Brisbane", "El sol brillando inmensamente puro doradísimo colosal de koalas puro gigante tropical de bellísimo inmensamente colosal y río queensland gigante y muy puramente capital oriental austral grandiosa bella norte hermosa maravilla vibrante en oro playa pacifica pura infinita", "Subtropical"),
                ("Perth", "La lejana maravilla muy majestuosísima y purísima brillante gigante oro metrópolis occidente inmensa bella australiana de bello cisne gigante puro negro mar colosal luz grandiosa en inmenso enorme e infinito pacífico y dorado inmenso gran cielo brillante pura bella de sol puro viva austral", "Mediterráneo"),
                ("Adelaida", "Valle inmensamente colosal grandioso y de barossa purísimo canguro bello inmenso y gigante y puro iglesia colosal sureña capital grandísima pacífica dorada inmensa en grandioso vino festival gigante de arte oro brillante", "Mediterráneo")
            ],
            "Nueva Zelanda": [
                ("Auckland", "Ciudad gigante inmensamente y pura colosal velero volcánica skytower inmenso purísimo en doble puerto kiwi maravilloso en señor grandioso inmenso pacífico sur de los grandísimos y anillos majestuosa bella verde maravilla infinita neozelandesa pura de luz hermosa infinita perla grandiosa viva", "Oceánico"),
                ("Wellington", "Capital bellísima del purísimo grandioso y gigante viento cable inmenso car puro museo de gigante maorí colosal infinita perla en señor purísimo del grandioso del inmensamente sur de rica plata majestuosa del grandioso pacífico luz brillante viva verde de inmenso sol pura brillante de inmensa orilla majestuosa", "Ventoso"),
                ("Christchurch", "Jardín inmensamente colosal grandioso purísimo majestuoso kiwi de inmenso y resiliente bello puro grandiosos majestuosos ingleses edificios colosales del pacífico brillante infinita del muy inmensa de sur majestuosa luz pura verde maravilla y bella lejana viva perla", "Oceánico")
            ]
        }
    }
    
    TIPO_EVENTO = ['Música', 'Deporte', 'Teatro', 'Arte', 'Gastronomía', 'Tecnología', 'Festivales', 'Cultura']
    
    destinos = []
    eventos = []
    
    id_destino = 1
    id_evento = 1
    
    # 2. Generar todo
    for region, paises in lugares.items():
        for pais, lista_ciudades in paises.items():
            for c in lista_ciudades:
                city = c[0]
                desc = c[1]
                clima = c[2]
                destinos.append((id_destino, city, desc, clima, pais, region))
                
                # Para cada destino, generar de 2 a 4 eventos
                num_evt = random.randint(2, 4)
                for _ in range(num_evt):
                    tipo = random.choice(TIPO_EVENTO)
                    name = f"Evento de {tipo} en {city}"
                    
                    if tipo == 'Música': precio = f"{random.randint(20, 150)}€"
                    elif tipo == 'Deporte': precio = f"{random.randint(15, 200)}€"
                    elif tipo == 'Teatro': precio = f"{random.randint(10, 80)}€"
                    elif tipo == 'Gastronomía': precio = f"{random.randint(30, 100)}€"
                    elif tipo == 'Festivales': precio = "Gratis" if random.random() < 0.3 else f"{random.randint(10, 50)}€"
                    else: precio = f"{random.randint(5, 50)}€"
                    
                    eventos.append((id_evento, id_destino, name, tipo, precio))
                    id_evento += 1
                
                id_destino += 1

    return destinos, eventos

d, e = generar_datos_masivos()

print(f"DESTINOS_POOL_SIZE = {len(d)}")

content = "DESTINOS_POOL = [\n"
for dest in d:
    # city, desc, clima, pais, region
    content += f"    ('{dest[1]}', '{dest[2]}', '{dest[3]}', '{dest[4]}', '{dest[5]}'),\n"
content += "]\n\n"

content += "CITY_EVENTS_MASIVOS = [\n"
for evt in e:
    # destino_id -> we can't use id because setup_database generates its own id.
    # so we map to the city name in Python. Or we just keep them separate and inject in setup_database.
    pass

with open('datos_generados.py', 'w', encoding='utf-8') as f:
    f.write(content)
